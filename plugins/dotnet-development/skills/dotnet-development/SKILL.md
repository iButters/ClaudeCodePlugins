---
name: dotnet-development
description: |
  Comprehensive .NET development guidelines covering DDD, SOLID principles, ASP.NET Core REST APIs, and C# best practices.
  Use when working with: (1) C# code files (.cs), (2) .NET project files (.csproj, .sln), (3) ASP.NET Core applications,
  (4) Domain-Driven Design implementations, (5) REST API development, (6) Entity Framework Core,
  (7) Unit/integration testing in .NET. Applies to any .NET/C# development task requiring architectural guidance.
---

# .NET Development Skill

Expert guidance for .NET development with Domain-Driven Design, SOLID principles, and modern C# practices.

## Implementation Workflow

Follow this process for any .NET implementation task:

### 1. Analysis Phase (Required)

Before writing code, determine:

- **Domain concepts**: Identify aggregates, entities, value objects involved
- **Layer affected**: Domain / Application / Infrastructure
- **SOLID alignment**: Which principles apply to this change
- **Security considerations**: Authorization, data protection requirements

### 2. Architecture Review (Required)

Validate the approach:

- Aggregate boundaries preserve consistency
- Single Responsibility Principle guides class design
- Dependencies point inward (DIP)
- Domain logic stays in domain layer, not services

### 3. Implementation

Execute with these standards:

- Use latest C# features (currently C# 14)
- Apply `async`/`await` for I/O operations
- Use constructor injection for dependencies
- Validate inputs at application layer boundaries
- Encapsulate business rules in domain objects

### 4. Testing (Required)

Write tests following `MethodName_Condition_ExpectedResult` naming:

```csharp
[Fact]
public void CalculateTotal_WithDiscount_ReturnsReducedAmount()
{
    var order = new Order();
    order.ApplyDiscount(0.1m);
    
    var total = order.CalculateTotal();
    
    Assert.Equal(90m, total);
}
```

## Core Principles

### Domain-Driven Design

| Concept | Purpose |
|---------|---------|
| Ubiquitous Language | Consistent business terminology across code |
| Bounded Contexts | Clear service boundaries |
| Aggregates | Transactional consistency boundaries |
| Domain Events | Capture business-significant occurrences |
| Rich Domain Models | Business logic in domain, not services |

### SOLID Principles

- **SRP**: One reason to change per class
- **OCP**: Open for extension, closed for modification
- **LSP**: Subtypes substitutable for base types
- **ISP**: No forced dependency on unused methods
- **DIP**: Depend on abstractions

### C# Conventions

**Naming:**
- PascalCase: Types, methods, public members, properties
- camelCase: Private fields, local variables
- Prefix interfaces with `I` (e.g., `IUserService`)

**Formatting:**
- File-scoped namespaces
- Newline before opening braces
- Pattern matching and switch expressions preferred
- Use `nameof` over string literals

**Nullability:**
- Enable nullable reference types
- Use `is null` / `is not null` (not `== null`)
- Validate at entry points, trust annotations internally

## Layer Responsibilities

### Domain Layer

```csharp
// Aggregate root with encapsulated business logic
public class Order : AggregateRoot
{
    private readonly List<OrderLine> _lines = [];
    
    public IReadOnlyCollection<OrderLine> Lines => _lines.AsReadOnly();
    
    public void AddLine(Product product, int quantity)
    {
        if (quantity <= 0)
            throw new DomainException("Quantity must be positive");
            
        _lines.Add(new OrderLine(product, quantity));
        AddDomainEvent(new OrderLineAddedEvent(Id, product.Id, quantity));
    }
}
```

### Application Layer

```csharp
// Application service orchestrates domain operations
public class OrderService(
    IOrderRepository orders,
    IProductRepository products,
    IEventPublisher events)
{
    public async Task<OrderDto> AddLineAsync(
        Guid orderId, 
        AddLineCommand command,
        CancellationToken ct = default)
    {
        // Validate input
        ArgumentNullException.ThrowIfNull(command);
        
        var order = await orders.GetByIdAsync(orderId, ct)
            ?? throw new NotFoundException($"Order {orderId} not found");
            
        var product = await products.GetByIdAsync(command.ProductId, ct)
            ?? throw new NotFoundException($"Product {command.ProductId} not found");
        
        // Execute domain logic
        order.AddLine(product, command.Quantity);
        
        // Persist and publish events
        await orders.SaveAsync(order, ct);
        await events.PublishAsync(order.DomainEvents, ct);
        
        return order.ToDto();
    }
}
```

### Infrastructure Layer

```csharp
// Repository implementation
public class OrderRepository(AppDbContext db) : IOrderRepository
{
    public async Task<Order?> GetByIdAsync(Guid id, CancellationToken ct) =>
        await db.Orders
            .Include(o => o.Lines)
            .FirstOrDefaultAsync(o => o.Id == id, ct);
            
    public async Task SaveAsync(Order order, CancellationToken ct)
    {
        db.Orders.Update(order);
        await db.SaveChangesAsync(ct);
    }
}
```

## REST API Patterns

### Controller-Based API

```csharp
[ApiController]
[Route("api/[controller]")]
public class OrdersController(OrderService orderService) : ControllerBase
{
    /// <summary>
    /// Adds a line item to an existing order.
    /// </summary>
    [HttpPost("{orderId:guid}/lines")]
    [ProducesResponseType<OrderDto>(StatusCodes.Status200OK)]
    [ProducesResponseType<ProblemDetails>(StatusCodes.Status404NotFound)]
    public async Task<IActionResult> AddLine(
        Guid orderId,
        AddLineCommand command,
        CancellationToken ct)
    {
        var result = await orderService.AddLineAsync(orderId, command, ct);
        return Ok(result);
    }
}
```

### Minimal API

```csharp
var orders = app.MapGroup("/api/orders")
    .WithTags("Orders")
    .RequireAuthorization();

orders.MapPost("/{orderId:guid}/lines", async (
    Guid orderId,
    AddLineCommand command,
    OrderService service,
    CancellationToken ct) =>
{
    var result = await service.AddLineAsync(orderId, command, ct);
    return Results.Ok(result);
})
.WithName("AddOrderLine")
.Produces<OrderDto>()
.ProducesProblem(StatusCodes.Status404NotFound);
```

## Reference Documentation

For detailed patterns and checklists, see:

- **[DDD Patterns](../../references/ddd-patterns.md)**: Aggregate design, domain events, specifications
- **[API Patterns](../../references/api-patterns.md)**: Validation, error handling, versioning, documentation
- **[Testing Patterns](../../references/testing-patterns.md)**: Test categories, mocking strategies, coverage requirements

## Quick Reference

### Monetary Values

- Use `decimal` for all financial calculations
- Implement currency-aware value objects
- Handle rounding per financial standards
- Maintain precision through calculation chains

### Error Handling

```csharp
// Global exception handler middleware
app.UseExceptionHandler(error => error.Run(async context =>
{
    var exception = context.Features.Get<IExceptionHandlerFeature>()?.Error;
    
    var problem = exception switch
    {
        NotFoundException e => new ProblemDetails
        {
            Status = 404,
            Title = "Not Found",
            Detail = e.Message
        },
        DomainException e => new ProblemDetails
        {
            Status = 400,
            Title = "Business Rule Violation",
            Detail = e.Message
        },
        _ => new ProblemDetails
        {
            Status = 500,
            Title = "Internal Server Error"
        }
    };
    
    context.Response.StatusCode = problem.Status ?? 500;
    await context.Response.WriteAsJsonAsync(problem);
}));
```

### Dependency Injection Setup

```csharp
// Program.cs
builder.Services.AddScoped<IOrderRepository, OrderRepository>();
builder.Services.AddScoped<OrderService>();
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("Default")));
```
