# Testing Patterns Reference

Comprehensive testing patterns for .NET applications.

## Table of Contents

1. [Test Naming Convention](#test-naming-convention)
2. [Test Categories](#test-categories)
3. [Domain Tests](#domain-tests)
4. [Application Layer Tests](#application-layer-tests)
5. [Integration Tests](#integration-tests)
6. [Mocking Strategies](#mocking-strategies)
7. [Coverage Requirements](#coverage-requirements)

## Test Naming Convention

Use the pattern: `MethodName_Condition_ExpectedResult`

```csharp
// Good examples
public void CalculateTotal_WithValidItems_ReturnsSumOfPrices()
public void AddLine_WithZeroQuantity_ThrowsDomainException()
public void Submit_WhenOrderIsEmpty_ThrowsDomainException()
public void GetById_WhenOrderExists_ReturnsOrder()
public void GetById_WhenOrderNotFound_ReturnsNull()

// Bad examples (avoid these)
public void TestCalculateTotal()           // No condition or expected result
public void ItShouldReturnCorrectTotal()   // BDD style, inconsistent
public void Calculate_Total_Test()         // Unclear, uses underscores wrong
```

## Test Categories

### Unit Tests

Test isolated domain logic without external dependencies.

```csharp
public class OrderTests
{
    [Fact]
    public void AddLine_WithValidProduct_IncreasesLineCount()
    {
        var order = Order.Create(Guid.NewGuid());
        var product = CreateTestProduct(price: 100m);
        
        order.AddLine(product, quantity: 2);
        
        Assert.Single(order.Lines);
        Assert.Equal(200m, order.Total.Amount);
    }
    
    [Fact]
    public void AddLine_WithZeroQuantity_ThrowsDomainException()
    {
        var order = Order.Create(Guid.NewGuid());
        var product = CreateTestProduct();
        
        var exception = Assert.Throws<DomainException>(() => 
            order.AddLine(product, quantity: 0));
        
        Assert.Equal("Quantity must be positive", exception.Message);
    }
    
    [Theory]
    [InlineData(0)]
    [InlineData(-1)]
    [InlineData(-100)]
    public void AddLine_WithInvalidQuantity_ThrowsDomainException(int quantity)
    {
        var order = Order.Create(Guid.NewGuid());
        var product = CreateTestProduct();
        
        Assert.Throws<DomainException>(() => order.AddLine(product, quantity));
    }
    
    private static ProductSnapshot CreateTestProduct(decimal price = 50m) =>
        new(Guid.NewGuid(), "Test Product", Money.Of(price, Currency.USD));
}
```

### Integration Tests

Test component interactions with real or simulated infrastructure.

```csharp
public class OrderRepositoryTests : IClassFixture<DatabaseFixture>
{
    private readonly AppDbContext _db;
    
    public OrderRepositoryTests(DatabaseFixture fixture) =>
        _db = fixture.CreateContext();
    
    [Fact]
    public async Task SaveAsync_WithNewOrder_PersistsToDatabase()
    {
        var repository = new OrderRepository(_db);
        var order = Order.Create(Guid.NewGuid());
        order.AddLine(CreateTestProduct(), 1);
        
        await repository.SaveAsync(order, CancellationToken.None);
        
        var loaded = await repository.GetByIdAsync(order.Id, CancellationToken.None);
        Assert.NotNull(loaded);
        Assert.Single(loaded.Lines);
    }
    
    [Fact]
    public async Task GetByIdAsync_WhenNotExists_ReturnsNull()
    {
        var repository = new OrderRepository(_db);
        
        var result = await repository.GetByIdAsync(Guid.NewGuid(), CancellationToken.None);
        
        Assert.Null(result);
    }
}

public class DatabaseFixture : IDisposable
{
    private readonly SqliteConnection _connection;
    
    public DatabaseFixture()
    {
        _connection = new SqliteConnection("DataSource=:memory:");
        _connection.Open();
        
        var options = new DbContextOptionsBuilder<AppDbContext>()
            .UseSqlite(_connection)
            .Options;
        
        using var context = new AppDbContext(options);
        context.Database.EnsureCreated();
    }
    
    public AppDbContext CreateContext()
    {
        var options = new DbContextOptionsBuilder<AppDbContext>()
            .UseSqlite(_connection)
            .Options;
        return new AppDbContext(options);
    }
    
    public void Dispose() => _connection.Dispose();
}
```

### API Integration Tests

Test HTTP endpoints end-to-end.

```csharp
public class OrdersApiTests : IClassFixture<WebApplicationFactory<Program>>
{
    private readonly HttpClient _client;
    
    public OrdersApiTests(WebApplicationFactory<Program> factory)
    {
        _client = factory.WithWebHostBuilder(builder =>
        {
            builder.ConfigureServices(services =>
            {
                // Replace real database with in-memory
                services.RemoveAll<DbContextOptions<AppDbContext>>();
                services.AddDbContext<AppDbContext>(options =>
                    options.UseInMemoryDatabase("TestDb"));
            });
        }).CreateClient();
    }
    
    [Fact]
    public async Task CreateOrder_WithValidData_ReturnsCreated()
    {
        var command = new CreateOrderCommand
        {
            CustomerId = Guid.NewGuid(),
            Lines = [new() { ProductId = Guid.NewGuid(), Quantity = 1 }]
        };
        
        var response = await _client.PostAsJsonAsync("/api/orders", command);
        
        Assert.Equal(HttpStatusCode.Created, response.StatusCode);
        Assert.NotNull(response.Headers.Location);
        
        var order = await response.Content.ReadFromJsonAsync<OrderDto>();
        Assert.NotNull(order);
        Assert.NotEqual(Guid.Empty, order.Id);
    }
    
    [Fact]
    public async Task CreateOrder_WithEmptyLines_ReturnsBadRequest()
    {
        var command = new CreateOrderCommand
        {
            CustomerId = Guid.NewGuid(),
            Lines = []
        };
        
        var response = await _client.PostAsJsonAsync("/api/orders", command);
        
        Assert.Equal(HttpStatusCode.BadRequest, response.StatusCode);
        
        var problem = await response.Content.ReadFromJsonAsync<ValidationProblemDetails>();
        Assert.Contains("Lines", problem!.Errors.Keys);
    }
    
    [Fact]
    public async Task GetOrder_WhenNotExists_ReturnsNotFound()
    {
        var response = await _client.GetAsync($"/api/orders/{Guid.NewGuid()}");
        
        Assert.Equal(HttpStatusCode.NotFound, response.StatusCode);
    }
}
```

## Domain Tests

### Value Object Tests

```csharp
public class MoneyTests
{
    [Fact]
    public void Of_WithNegativeAmount_ThrowsDomainException()
    {
        Assert.Throws<DomainException>(() => Money.Of(-1m, Currency.USD));
    }
    
    [Fact]
    public void Add_WithSameCurrency_ReturnsSummedAmount()
    {
        var a = Money.Of(10m, Currency.USD);
        var b = Money.Of(20m, Currency.USD);
        
        var result = a.Add(b);
        
        Assert.Equal(30m, result.Amount);
        Assert.Equal(Currency.USD, result.Currency);
    }
    
    [Fact]
    public void Add_WithDifferentCurrency_ThrowsDomainException()
    {
        var usd = Money.Of(10m, Currency.USD);
        var eur = Money.Of(10m, Currency.EUR);
        
        Assert.Throws<DomainException>(() => usd.Add(eur));
    }
    
    [Theory]
    [InlineData(100, 0.5, 50)]
    [InlineData(99.99, 0.1, 10.00)]
    [InlineData(33.33, 3, 99.99)]
    public void Multiply_WithFactor_ReturnsCorrectlyRoundedResult(
        decimal amount, decimal factor, decimal expected)
    {
        var money = Money.Of(amount, Currency.USD);
        
        var result = money.Multiply(factor);
        
        Assert.Equal(expected, result.Amount);
    }
}
```

### Aggregate Tests

```csharp
public class OrderAggregateTests
{
    [Fact]
    public void Create_WithValidCustomerId_InitializesDraftOrder()
    {
        var customerId = Guid.NewGuid();
        
        var order = Order.Create(customerId);
        
        Assert.NotEqual(Guid.Empty, order.Id);
        Assert.Equal(customerId, order.CustomerId);
        Assert.Equal(OrderStatus.Draft, order.Status);
        Assert.Empty(order.Lines);
        Assert.Single(order.DomainEvents);
        Assert.IsType<OrderCreatedEvent>(order.DomainEvents.First());
    }
    
    [Fact]
    public void Submit_WhenDraftWithLines_ChangesStatusToSubmitted()
    {
        var order = CreateOrderWithLine();
        
        order.Submit();
        
        Assert.Equal(OrderStatus.Submitted, order.Status);
        Assert.Contains(order.DomainEvents, e => e is OrderSubmittedEvent);
    }
    
    [Fact]
    public void Submit_WhenEmpty_ThrowsDomainException()
    {
        var order = Order.Create(Guid.NewGuid());
        
        var exception = Assert.Throws<DomainException>(() => order.Submit());
        
        Assert.Equal("Cannot submit empty order", exception.Message);
    }
    
    [Fact]
    public void Submit_WhenAlreadySubmitted_ThrowsDomainException()
    {
        var order = CreateOrderWithLine();
        order.Submit();
        
        Assert.Throws<DomainException>(() => order.Submit());
    }
    
    private static Order CreateOrderWithLine()
    {
        var order = Order.Create(Guid.NewGuid());
        order.AddLine(new ProductSnapshot(Guid.NewGuid(), "Test", Money.Of(10m, Currency.USD)), 1);
        return order;
    }
}
```

### Domain Event Tests

```csharp
public class OrderEventTests
{
    [Fact]
    public void AddLine_PublishesOrderLineAddedEvent()
    {
        var order = Order.Create(Guid.NewGuid());
        var productId = Guid.NewGuid();
        var product = new ProductSnapshot(productId, "Test", Money.Of(10m, Currency.USD));
        
        order.AddLine(product, quantity: 3);
        
        var evt = order.DomainEvents.OfType<OrderLineAddedEvent>().Single();
        Assert.Equal(order.Id, evt.OrderId);
        Assert.Equal(productId, evt.ProductId);
        Assert.Equal(3, evt.Quantity);
    }
}
```

## Application Layer Tests

```csharp
public class OrderServiceTests
{
    private readonly Mock<IOrderRepository> _orderRepo = new();
    private readonly Mock<IProductRepository> _productRepo = new();
    private readonly Mock<IEventPublisher> _eventPublisher = new();
    
    private OrderService CreateSut() =>
        new(_orderRepo.Object, _productRepo.Object, _eventPublisher.Object);
    
    [Fact]
    public async Task AddLineAsync_WithValidData_AddsLineAndPublishesEvents()
    {
        var orderId = Guid.NewGuid();
        var productId = Guid.NewGuid();
        var order = Order.Create(Guid.NewGuid());
        var product = new Product(productId, "Test", Money.Of(50m, Currency.USD));
        
        _orderRepo.Setup(r => r.GetByIdAsync(orderId, It.IsAny<CancellationToken>()))
            .ReturnsAsync(order);
        _productRepo.Setup(r => r.GetByIdAsync(productId, It.IsAny<CancellationToken>()))
            .ReturnsAsync(product);
        
        var command = new AddLineCommand(productId, Quantity: 2);
        var sut = CreateSut();
        
        var result = await sut.AddLineAsync(orderId, command);
        
        Assert.Single(order.Lines);
        _orderRepo.Verify(r => r.SaveAsync(order, It.IsAny<CancellationToken>()), Times.Once);
        _eventPublisher.Verify(e => e.PublishAsync(
            It.Is<IEnumerable<IDomainEvent>>(events => events.Any()), 
            It.IsAny<CancellationToken>()), Times.Once);
    }
    
    [Fact]
    public async Task AddLineAsync_WhenOrderNotFound_ThrowsNotFoundException()
    {
        _orderRepo.Setup(r => r.GetByIdAsync(It.IsAny<Guid>(), It.IsAny<CancellationToken>()))
            .ReturnsAsync((Order?)null);
        
        var sut = CreateSut();
        
        await Assert.ThrowsAsync<NotFoundException>(() =>
            sut.AddLineAsync(Guid.NewGuid(), new AddLineCommand(Guid.NewGuid(), 1)));
    }
}
```

## Mocking Strategies

### Repository Mocks

```csharp
public static class MockExtensions
{
    public static Mock<IOrderRepository> SetupGetById(
        this Mock<IOrderRepository> mock,
        Guid orderId,
        Order? order)
    {
        mock.Setup(r => r.GetByIdAsync(orderId, It.IsAny<CancellationToken>()))
            .ReturnsAsync(order);
        return mock;
    }
    
    public static Mock<IOrderRepository> SetupSave(this Mock<IOrderRepository> mock)
    {
        mock.Setup(r => r.SaveAsync(It.IsAny<Order>(), It.IsAny<CancellationToken>()))
            .Returns(Task.CompletedTask);
        return mock;
    }
}

// Usage
_orderRepo
    .SetupGetById(orderId, existingOrder)
    .SetupSave();
```

### Test Builders

```csharp
public class OrderBuilder
{
    private Guid _customerId = Guid.NewGuid();
    private OrderStatus _status = OrderStatus.Draft;
    private readonly List<(ProductSnapshot Product, int Quantity)> _lines = [];
    
    public OrderBuilder WithCustomer(Guid customerId)
    {
        _customerId = customerId;
        return this;
    }
    
    public OrderBuilder WithLine(decimal price = 50m, int quantity = 1)
    {
        var product = new ProductSnapshot(
            Guid.NewGuid(),
            "Test Product",
            Money.Of(price, Currency.USD));
        _lines.Add((product, quantity));
        return this;
    }
    
    public OrderBuilder AsSubmitted()
    {
        _status = OrderStatus.Submitted;
        return this;
    }
    
    public Order Build()
    {
        var order = Order.Create(_customerId);
        
        foreach (var (product, quantity) in _lines)
        {
            order.AddLine(product, quantity);
        }
        
        if (_status == OrderStatus.Submitted && _lines.Count > 0)
        {
            order.Submit();
        }
        
        order.ClearDomainEvents();
        return order;
    }
}

// Usage
var order = new OrderBuilder()
    .WithLine(price: 100m, quantity: 2)
    .WithLine(price: 50m, quantity: 1)
    .AsSubmitted()
    .Build();
```

## Coverage Requirements

### Minimum Coverage Targets

| Layer | Minimum Coverage |
|-------|-----------------|
| Domain | 90% |
| Application | 85% |
| Infrastructure | 70% |
| API/Controllers | 80% |

### What to Test

**Always test:**
- Domain invariants and business rules
- State transitions in aggregates
- Value object validation and equality
- Error paths and exceptions
- Edge cases (empty collections, boundary values)

**Consider skipping:**
- Simple property getters/setters
- Framework-generated code
- Trivial mapping methods
- Third-party library behavior

### Running Coverage

```bash
dotnet test --collect:"XPlat Code Coverage"
dotnet tool install -g dotnet-reportgenerator-globaltool
reportgenerator -reports:**/coverage.cobertura.xml -targetdir:coverage-report
```
