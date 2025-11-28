# DDD Patterns Reference

Detailed patterns for Domain-Driven Design implementation in .NET.

## Table of Contents

1. [Aggregate Design](#aggregate-design)
2. [Value Objects](#value-objects)
3. [Domain Events](#domain-events)
4. [Domain Services](#domain-services)
5. [Specifications](#specifications)
6. [Quality Checklist](#quality-checklist)

## Aggregate Design

### Aggregate Root Pattern

```csharp
public abstract class AggregateRoot : Entity
{
    private readonly List<IDomainEvent> _domainEvents = [];
    
    public IReadOnlyCollection<IDomainEvent> DomainEvents => 
        _domainEvents.AsReadOnly();
    
    protected void AddDomainEvent(IDomainEvent domainEvent) =>
        _domainEvents.Add(domainEvent);
    
    public void ClearDomainEvents() => _domainEvents.Clear();
}
```

### Consistency Boundaries

Aggregates define transactional boundaries:

- All changes within an aggregate are atomic
- Reference other aggregates by ID only
- Keep aggregates small and focused
- One aggregate per transaction

**Example: Order Aggregate**

```csharp
public class Order : AggregateRoot
{
    public Guid Id { get; private set; }
    public Guid CustomerId { get; private set; }  // Reference by ID
    public OrderStatus Status { get; private set; }
    public Money Total { get; private set; }
    
    private readonly List<OrderLine> _lines = [];
    public IReadOnlyCollection<OrderLine> Lines => _lines.AsReadOnly();
    
    private Order() { }  // EF Core
    
    public static Order Create(Guid customerId)
    {
        var order = new Order
        {
            Id = Guid.NewGuid(),
            CustomerId = customerId,
            Status = OrderStatus.Draft,
            Total = Money.Zero(Currency.USD)
        };
        
        order.AddDomainEvent(new OrderCreatedEvent(order.Id, customerId));
        return order;
    }
    
    public void AddLine(ProductSnapshot product, int quantity)
    {
        GuardAgainstInvalidState();
        
        if (quantity <= 0)
            throw new DomainException("Quantity must be positive");
        
        var line = new OrderLine(Id, product, quantity);
        _lines.Add(line);
        RecalculateTotal();
        
        AddDomainEvent(new OrderLineAddedEvent(Id, product.Id, quantity));
    }
    
    public void Submit()
    {
        if (Status != OrderStatus.Draft)
            throw new DomainException("Only draft orders can be submitted");
            
        if (_lines.Count == 0)
            throw new DomainException("Cannot submit empty order");
        
        Status = OrderStatus.Submitted;
        AddDomainEvent(new OrderSubmittedEvent(Id, Total));
    }
    
    private void GuardAgainstInvalidState()
    {
        if (Status != OrderStatus.Draft)
            throw new DomainException("Order cannot be modified");
    }
    
    private void RecalculateTotal() =>
        Total = _lines.Aggregate(Money.Zero(Currency.USD), 
            (sum, line) => sum.Add(line.Subtotal));
}
```

## Value Objects

Immutable objects representing domain concepts without identity.

```csharp
public record Money
{
    public decimal Amount { get; }
    public Currency Currency { get; }
    
    private Money(decimal amount, Currency currency)
    {
        if (amount < 0)
            throw new DomainException("Amount cannot be negative");
            
        Amount = amount;
        Currency = currency;
    }
    
    public static Money Zero(Currency currency) => new(0, currency);
    public static Money Of(decimal amount, Currency currency) => new(amount, currency);
    
    public Money Add(Money other)
    {
        EnsureSameCurrency(other);
        return new Money(Amount + other.Amount, Currency);
    }
    
    public Money Subtract(Money other)
    {
        EnsureSameCurrency(other);
        return new Money(Amount - other.Amount, Currency);
    }
    
    public Money Multiply(decimal factor) =>
        new(Math.Round(Amount * factor, 2, MidpointRounding.AwayFromZero), Currency);
    
    private void EnsureSameCurrency(Money other)
    {
        if (Currency != other.Currency)
            throw new DomainException($"Cannot operate on different currencies: {Currency} vs {other.Currency}");
    }
}

public record Address(
    string Street,
    string City,
    string PostalCode,
    string Country)
{
    public static Address Create(string street, string city, string postalCode, string country)
    {
        if (string.IsNullOrWhiteSpace(street))
            throw new DomainException("Street is required");
        if (string.IsNullOrWhiteSpace(city))
            throw new DomainException("City is required");
            
        return new Address(street, city, postalCode, country);
    }
}
```

## Domain Events

Events capture business-significant state changes.

### Event Definition

```csharp
public interface IDomainEvent
{
    Guid EventId { get; }
    DateTimeOffset OccurredAt { get; }
}

public abstract record DomainEvent : IDomainEvent
{
    public Guid EventId { get; } = Guid.NewGuid();
    public DateTimeOffset OccurredAt { get; } = DateTimeOffset.UtcNow;
}

public record OrderSubmittedEvent(Guid OrderId, Money Total) : DomainEvent;

public record OrderLineAddedEvent(
    Guid OrderId, 
    Guid ProductId, 
    int Quantity) : DomainEvent;
```

### Event Handling

```csharp
public interface IDomainEventHandler<in TEvent> where TEvent : IDomainEvent
{
    Task HandleAsync(TEvent domainEvent, CancellationToken ct = default);
}

public class OrderSubmittedHandler(
    INotificationService notifications,
    IInventoryService inventory) : IDomainEventHandler<OrderSubmittedEvent>
{
    public async Task HandleAsync(OrderSubmittedEvent e, CancellationToken ct)
    {
        await notifications.SendOrderConfirmationAsync(e.OrderId, ct);
        await inventory.ReserveStockAsync(e.OrderId, ct);
    }
}
```

### Event Publisher

```csharp
public interface IEventPublisher
{
    Task PublishAsync(IEnumerable<IDomainEvent> events, CancellationToken ct = default);
}

public class MediatREventPublisher(IMediator mediator) : IEventPublisher
{
    public async Task PublishAsync(IEnumerable<IDomainEvent> events, CancellationToken ct)
    {
        foreach (var domainEvent in events)
        {
            await mediator.Publish(domainEvent, ct);
        }
    }
}
```

## Domain Services

Stateless services for operations spanning multiple aggregates.

```csharp
public class TransferService(
    IAccountRepository accounts,
    IEventPublisher events)
{
    public async Task TransferAsync(
        Guid fromAccountId,
        Guid toAccountId,
        Money amount,
        CancellationToken ct = default)
    {
        var fromAccount = await accounts.GetByIdAsync(fromAccountId, ct)
            ?? throw new NotFoundException($"Account {fromAccountId} not found");
            
        var toAccount = await accounts.GetByIdAsync(toAccountId, ct)
            ?? throw new NotFoundException($"Account {toAccountId} not found");
        
        // Domain logic in entities
        fromAccount.Withdraw(amount);
        toAccount.Deposit(amount);
        
        // Persist both (use transaction/saga for real systems)
        await accounts.SaveAsync(fromAccount, ct);
        await accounts.SaveAsync(toAccount, ct);
        
        // Publish events
        var allEvents = fromAccount.DomainEvents.Concat(toAccount.DomainEvents);
        await events.PublishAsync(allEvents, ct);
    }
}
```

## Specifications

Encapsulate complex business rules and queries.

```csharp
public abstract class Specification<T>
{
    public abstract Expression<Func<T, bool>> ToExpression();
    
    public bool IsSatisfiedBy(T entity) =>
        ToExpression().Compile().Invoke(entity);
    
    public Specification<T> And(Specification<T> other) =>
        new AndSpecification<T>(this, other);
        
    public Specification<T> Or(Specification<T> other) =>
        new OrSpecification<T>(this, other);
}

public class OrderReadyForShipmentSpec : Specification<Order>
{
    public override Expression<Func<Order, bool>> ToExpression() =>
        order => order.Status == OrderStatus.Paid 
              && order.Lines.All(l => l.IsInStock);
}

public class HighValueOrderSpec(Money threshold) : Specification<Order>
{
    public override Expression<Func<Order, bool>> ToExpression() =>
        order => order.Total.Amount >= threshold.Amount 
              && order.Total.Currency == threshold.Currency;
}

// Usage in repository
public class OrderRepository(AppDbContext db) : IOrderRepository
{
    public async Task<IReadOnlyList<Order>> FindAsync(
        Specification<Order> spec,
        CancellationToken ct) =>
        await db.Orders
            .Where(spec.ToExpression())
            .ToListAsync(ct);
}
```

## Quality Checklist

Verify before completing any DDD implementation:

### Domain Model Validation

- [ ] Aggregates properly model business concepts
- [ ] Ubiquitous language used consistently
- [ ] Business rules encapsulated in domain objects
- [ ] Domain events capture significant state changes
- [ ] Aggregates referenced by ID, not direct references

### SOLID Compliance

- [ ] Each class has single responsibility
- [ ] New features extend, don't modify existing code
- [ ] Derived types substitutable for base types
- [ ] Interfaces are focused and cohesive
- [ ] High-level modules don't depend on low-level details

### Financial Domain (if applicable)

- [ ] `decimal` used for monetary calculations
- [ ] Currency-aware value objects implemented
- [ ] Proper rounding applied per financial standards
- [ ] Transaction boundaries maintain consistency
- [ ] Audit trail via domain events

### Security & Compliance

- [ ] Authorization at aggregate boundaries
- [ ] PCI-DSS compliance in payment handling
- [ ] LGPD/GDPR in personal data handling
- [ ] Audit events for compliance reporting
