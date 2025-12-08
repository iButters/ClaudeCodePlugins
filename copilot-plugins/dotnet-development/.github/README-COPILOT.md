# .NET Development - GitHub Copilot Chat Edition

Expert guidance for modern .NET development with Domain-Driven Design, SOLID principles, ASP.NET Core APIs, and testing best practices.

## 📋 Overview

This is the GitHub Copilot Chat version of the .NET Development plugin. It provides comprehensive guidance for building enterprise-grade .NET applications using:
- Domain-Driven Design (DDD) tactical patterns
- SOLID principles
- Clean Architecture
- ASP.NET Core REST APIs
- Entity Framework Core
- Modern C# features (12+)
- Comprehensive testing strategies

## 🚀 Installation

### Copy to Your .NET Repository

```bash
cp -r .github /path/to/your/dotnet/project/
```

The instructions automatically activate when working with:
- C# files (`.cs`)
- Project files (`.csproj`, `.sln`)
- ASP.NET Core applications
- Domain-Driven Design implementations

## 💡 Features

### Automatic Context Activation

When you open C# files or .NET projects, GitHub Copilot automatically applies these expert guidelines:

**No commands needed!** Just start coding or ask questions like:
- "How should I structure this aggregate?"
- "Review my domain model for SOLID principles"
- "Design a REST API controller for this service"
- "Generate tests for this domain logic"

### Expert Capabilities

- ✅ Design aggregate roots, entities, and value objects
- ✅ Implement clean architecture with proper layer separation
- ✅ Create RESTful APIs (Controllers and Minimal APIs)
- ✅ Apply SOLID principles for maintainability
- ✅ Write comprehensive unit and integration tests
- ✅ Configure Entity Framework Core correctly
- ✅ Implement domain events and event handlers
- ✅ Review code for security and performance

## 🏗️ Architecture Patterns

### Domain-Driven Design (DDD)

The system guides you to implement:

**Ubiquitous Language**: Consistent business terminology across code

**Bounded Contexts**: Clear service boundaries

**Aggregates**: Transactional consistency boundaries
```csharp
public class Order : AggregateRoot
{
    public Guid Id { get; private set; }
    public Guid CustomerId { get; private set; }
    private readonly List<OrderLine> _lines = [];
    
    public static Order Create(Guid customerId) { /* ... */ }
    public void AddLine(Product product, int quantity) { /* ... */ }
}
```

**Domain Events**: Capture business-significant occurrences
```csharp
public record OrderCreatedEvent(Guid OrderId, Guid CustomerId) : IDomainEvent;
```

**Rich Domain Models**: Business logic in domain, not services

### SOLID Principles

| Principle | Application in .NET |
|-----------|---------------------|
| **Single Responsibility** | Each class has one job |
| **Open/Closed** | Use interfaces and inheritance |
| **Liskov Substitution** | Interfaces fulfill contracts |
| **Interface Segregation** | Small, focused interfaces |
| **Dependency Inversion** | Depend on abstractions (IRepository, not Repository) |

### Clean Architecture Layers

```
Domain Layer (Core)
├── Entities & Aggregates
├── Value Objects
├── Domain Events
└── Interfaces (IRepository)

Application Layer
├── Commands & Queries (CQRS)
├── Command Handlers
├── DTOs & Validators
└── Application Services

Infrastructure Layer
├── DbContext & Repositories
├── External Services
└── API Clients
```

## 🔧 Implementation Workflow

When implementing features, the system guides you through:

### 1. Analysis Phase
- Identify domain concepts (aggregates, entities, value objects)
- Determine affected layer (Domain, Application, Infrastructure)
- Map SOLID principles to design
- Assess security requirements

### 2. Architecture Review
- Check aggregate boundaries for consistency
- Apply Single Responsibility Principle
- Enforce Dependency Inversion (dependencies point inward)
- Validate domain encapsulation

### 3. Implementation
- Use modern C# features (primary constructors, collection expressions, pattern matching)
- Implement async/await correctly with CancellationToken
- Apply constructor injection
- Validate at boundaries
- Encapsulate business rules in domain

### 4. Testing
- Use `MethodName_Condition_ExpectedResult` naming
- Structure with Arrange-Act-Assert (AAA)
- Test domain invariants
- Verify domain events

## 📝 Code Examples

### Aggregate Root with Domain Events

```csharp
public class Order : AggregateRoot
{
    public Guid Id { get; private set; }
    public OrderStatus Status { get; private set; }
    private readonly List<OrderLine> _lines = [];
    
    public static Order Create(Guid customerId)
    {
        var order = new Order
        {
            Id = Guid.NewGuid(),
            Status = OrderStatus.Draft
        };
        
        order.AddDomainEvent(new OrderCreatedEvent(order.Id, customerId));
        return order;
    }
    
    public void AddLine(Product product, int quantity)
    {
        if (Status != OrderStatus.Draft)
            throw new DomainException("Cannot modify submitted order");
        
        if (quantity <= 0)
            throw new DomainException("Quantity must be positive");
        
        _lines.Add(new OrderLine(Id, product, quantity));
        AddDomainEvent(new OrderLineAddedEvent(Id));
    }
}
```

### Value Objects

```csharp
public record Money(decimal Amount, Currency Currency)
{
    public static Money Zero(Currency currency) => new(0, currency);
    
    public Money Add(Money other)
    {
        if (Currency != other.Currency)
            throw new DomainException("Cannot add different currencies");
        
        return new Money(Amount + other.Amount, Currency);
    }
}
```

### REST API Controller

```csharp
[ApiController]
[Route("api/[controller]")]
public class OrdersController(IMediator mediator) : ControllerBase
{
    [HttpPost]
    [ProducesResponseType(StatusCodes.Status201Created)]
    public async Task<ActionResult<Guid>> CreateOrder(
        [FromBody] CreateOrderRequest request,
        CancellationToken ct)
    {
        var command = new CreateOrderCommand(request.CustomerId, request.Lines);
        var orderId = await mediator.Send(command, ct);
        
        return CreatedAtAction(nameof(GetOrder), new { id = orderId }, orderId);
    }
}
```

### Minimal API

```csharp
app.MapPost("/api/orders", async (
    CreateOrderRequest request,
    IMediator mediator,
    CancellationToken ct) =>
{
    var command = new CreateOrderCommand(request.CustomerId, request.Lines);
    var orderId = await mediator.Send(command, ct);
    
    return Results.Created($"/api/orders/{orderId}", orderId);
})
.Produces<Guid>(StatusCodes.Status201Created)
.WithTags("Orders");
```

### Unit Tests

```csharp
public class OrderTests
{
    [Fact]
    public void AddLine_WithValidQuantity_AddsLineToOrder()
    {
        // Arrange
        var order = Order.Create(Guid.NewGuid());
        var product = CreateTestProduct();
        
        // Act
        order.AddLine(product, 2);
        
        // Assert
        Assert.Single(order.Lines);
        Assert.Contains(order.Lines, l => l.Quantity == 2);
    }
    
    [Fact]
    public void AddLine_WithZeroQuantity_ThrowsDomainException()
    {
        // Arrange
        var order = Order.Create(Guid.NewGuid());
        
        // Act & Assert
        var ex = Assert.Throws<DomainException>(() => 
            order.AddLine(CreateTestProduct(), 0));
        Assert.Equal("Quantity must be positive", ex.Message);
    }
}
```

## 🎯 Usage Scenarios

### Scenario 1: Designing a New Domain Model

**You**: "I need to design an aggregate for managing customer subscriptions. Each subscription has a plan, billing cycle, and payment history."

**Copilot** (with this guidance): Will suggest:
- Subscription as aggregate root
- Plan as value object or reference by ID
- BillingCycle as value object
- Payment as entity within aggregate
- Domain events for subscription created, renewed, cancelled
- Proper encapsulation of business rules

### Scenario 2: Reviewing Existing Code

**You**: "Review this service class for SOLID principles violations"

**Copilot**: Will analyze against:
- Single Responsibility (does it do too much?)
- Dependency Inversion (depends on interfaces?)
- Interface Segregation (interfaces too large?)
- Domain logic placement (in service vs. domain?)

### Scenario 3: Creating REST API

**You**: "Generate a REST controller for user management"

**Copilot**: Will create:
- Proper HTTP verbs and status codes
- Async methods with CancellationToken
- ProducesResponseType attributes
- Proper routing
- CQRS pattern with MediatR

### Scenario 4: Writing Tests

**You**: "Generate tests for this aggregate"

**Copilot**: Will create:
- Tests following naming convention
- AAA structure (Arrange-Act-Assert)
- Domain invariant tests
- Event verification tests
- Edge case coverage

## 🚫 Anti-Patterns Avoided

The system helps you avoid:

### ❌ Anemic Domain Model
Business logic in services instead of domain objects

### ✅ Rich Domain Model
Business logic encapsulated in aggregates

### ❌ Domain Logic in Controllers
Controllers containing business rules

### ✅ Thin Controllers
Controllers orchestrating via commands/queries

### ❌ Crossing Aggregate Boundaries
Direct navigation between aggregates

### ✅ References by ID
Aggregates reference others by ID only

## 🔒 Security & Performance

Automatically applied best practices:

**Security**:
- Input validation at API boundaries
- Authorization with [Authorize] attributes
- Parameterized queries (EF Core)
- HTTPS enforcement
- CORS policies

**Performance**:
- Async/await for I/O operations
- AsNoTracking() for read-only queries
- Pagination for large datasets
- Proper use of IMemoryCache
- Connection pooling

## 🧪 Testing Strategy

Comprehensive testing guidance:

**Unit Tests**:
- Domain logic (aggregates, entities, value objects)
- Business rule validation
- Domain event generation
- Fast, isolated, no dependencies

**Integration Tests**:
- API endpoints
- Database operations
- Complete workflows
- WebApplicationFactory for testing

**Test Naming**: `MethodName_Condition_ExpectedResult`

**Test Structure**: Arrange-Act-Assert (AAA)

## 🆕 Modern C# Features

The system promotes use of:

- **Primary Constructors**: Simplified dependency injection
- **Collection Expressions**: `[]` syntax
- **Pattern Matching**: Switch expressions
- **File-Scoped Namespaces**: Cleaner code
- **Required Members**: Required properties
- **Records**: Immutable value objects
- **Init-only Properties**: Immutable DTOs

## 📁 File Structure

```
.github/
├── copilot-instructions.md          # Main .NET development guidance
└── README-COPILOT.md               # This file
```

## 🆚 Differences from Claude Code Version

| Feature | Claude Code | GitHub Copilot Chat |
|---------|-------------|---------------------|
| **Activation** | Plugin installation | Copy `.github` directory |
| **Context** | Explicit skill reference | Automatic for .cs files |
| **Commands** | Slash commands | Natural language |
| **Tools** | Read, Write, Edit tools | Chat interface |
| **Integration** | Claude Code IDE | VS Code, Visual Studio |

## 🚦 Getting Started

1. **Copy files**:
   ```bash
   cp -r .github /path/to/your/dotnet/project/
   ```

2. **Start coding** - Open any `.cs` file and the guidance activates automatically

3. **Ask questions**:
   ```
   How should I structure this order aggregate?
   Review my repository implementation
   Generate tests for this domain model
   Design a REST API for this feature
   ```

4. **Iterate** - Copilot applies DDD and SOLID principles to suggestions

## 💡 Pro Tips

1. **Mention patterns explicitly**: "Design this using DDD aggregate pattern"
2. **Request specific layers**: "Create an application service for this"
3. **Ask for reviews**: "Review this for SOLID principle violations"
4. **Generate tests**: "Generate unit tests using xUnit and FluentAssertions"
5. **Reference architecture**: "Follow clean architecture for this feature"

## 🐛 Troubleshooting

**Copilot suggestions feel generic**:
- Mention "using DDD patterns" or "following SOLID principles"
- Reference specific patterns: "aggregate root", "value object", "domain event"

**Not enough context**:
- Describe the domain: "for an e-commerce order system"
- Mention constraints: "must maintain transactional consistency"

**Want specific patterns**:
- Be explicit: "use the repository pattern with Unit of Work"
- Reference layers: "in the application layer using CQRS"

## 📄 License

MIT License - Same as the original Claude Code plugin

## 🤝 Contributing

Improvements welcome! This conversion maintains the same principles and patterns as the original plugin.

---

**Build Better .NET Applications with DDD and SOLID! 🏗️**
