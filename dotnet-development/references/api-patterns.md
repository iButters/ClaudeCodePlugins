# API Patterns Reference

Detailed patterns for REST API development with ASP.NET Core.

## Table of Contents

1. [API Design Principles](#api-design-principles)
2. [Validation](#validation)
3. [Error Handling](#error-handling)
4. [Versioning](#versioning)
5. [Documentation](#documentation)
6. [Authentication & Authorization](#authentication--authorization)
7. [Performance](#performance)

## API Design Principles

### Resource-Oriented URLs

```
GET    /api/orders              # List orders
GET    /api/orders/{id}         # Get specific order
POST   /api/orders              # Create order
PUT    /api/orders/{id}         # Replace order
PATCH  /api/orders/{id}         # Partial update
DELETE /api/orders/{id}         # Delete order

GET    /api/orders/{id}/lines   # List order lines (sub-resource)
POST   /api/orders/{id}/lines   # Add line to order
```

### HTTP Status Codes

| Code | Meaning | When to Use |
|------|---------|-------------|
| 200 | OK | Successful GET, PUT, PATCH |
| 201 | Created | Successful POST (include Location header) |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Validation failure, malformed request |
| 401 | Unauthorized | Missing/invalid authentication |
| 403 | Forbidden | Authenticated but not authorized |
| 404 | Not Found | Resource doesn't exist |
| 409 | Conflict | Business rule violation, concurrency conflict |
| 422 | Unprocessable | Semantically invalid (alternative to 400) |
| 500 | Server Error | Unexpected error |

### Controller vs Minimal API Decision

**Use Controllers when:**
- Large API with many endpoints
- Team familiar with MVC patterns
- Need built-in model binding features
- Complex routing scenarios

**Use Minimal APIs when:**
- Microservices with few endpoints
- Performance-critical paths
- Simple CRUD operations
- Modern, concise codebase preferred

## Validation

### Data Annotations

```csharp
public record CreateOrderCommand
{
    [Required(ErrorMessage = "Customer ID is required")]
    public Guid CustomerId { get; init; }
    
    [Required]
    [MinLength(1, ErrorMessage = "At least one line item required")]
    public List<OrderLineDto> Lines { get; init; } = [];
}

public record OrderLineDto
{
    [Required]
    public Guid ProductId { get; init; }
    
    [Range(1, 10000, ErrorMessage = "Quantity must be between 1 and 10000")]
    public int Quantity { get; init; }
}
```

### FluentValidation

```csharp
public class CreateOrderCommandValidator : AbstractValidator<CreateOrderCommand>
{
    public CreateOrderCommandValidator(IProductRepository products)
    {
        RuleFor(x => x.CustomerId)
            .NotEmpty()
            .WithMessage("Customer ID is required");
        
        RuleFor(x => x.Lines)
            .NotEmpty()
            .WithMessage("At least one line item required");
        
        RuleForEach(x => x.Lines).ChildRules(line =>
        {
            line.RuleFor(l => l.ProductId)
                .NotEmpty()
                .MustAsync(async (id, ct) => await products.ExistsAsync(id, ct))
                .WithMessage("Product not found");
            
            line.RuleFor(l => l.Quantity)
                .InclusiveBetween(1, 10000);
        });
    }
}

// Registration
builder.Services.AddValidatorsFromAssemblyContaining<CreateOrderCommandValidator>();
builder.Services.AddFluentValidationAutoValidation();
```

### Custom Validation Response

```csharp
builder.Services.Configure<ApiBehaviorOptions>(options =>
{
    options.InvalidModelStateResponseFactory = context =>
    {
        var errors = context.ModelState
            .Where(e => e.Value?.Errors.Count > 0)
            .ToDictionary(
                e => e.Key,
                e => e.Value!.Errors.Select(x => x.ErrorMessage).ToArray()
            );
        
        var problem = new ValidationProblemDetails(errors)
        {
            Type = "https://tools.ietf.org/html/rfc7231#section-6.5.1",
            Title = "Validation Failed",
            Status = StatusCodes.Status400BadRequest,
            Instance = context.HttpContext.Request.Path
        };
        
        return new BadRequestObjectResult(problem);
    };
});
```

## Error Handling

### Problem Details (RFC 7807)

```csharp
// Custom exception types
public class NotFoundException(string message) : Exception(message);
public class ConflictException(string message) : Exception(message);
public class ForbiddenException(string message) : Exception(message);

// Global exception handler
public class GlobalExceptionHandler : IExceptionHandler
{
    private readonly ILogger<GlobalExceptionHandler> _logger;
    
    public GlobalExceptionHandler(ILogger<GlobalExceptionHandler> logger) =>
        _logger = logger;
    
    public async ValueTask<bool> TryHandleAsync(
        HttpContext context,
        Exception exception,
        CancellationToken ct)
    {
        _logger.LogError(exception, "Unhandled exception: {Message}", exception.Message);
        
        var problem = exception switch
        {
            NotFoundException e => new ProblemDetails
            {
                Status = StatusCodes.Status404NotFound,
                Title = "Resource Not Found",
                Detail = e.Message,
                Type = "https://tools.ietf.org/html/rfc7231#section-6.5.4"
            },
            ConflictException e => new ProblemDetails
            {
                Status = StatusCodes.Status409Conflict,
                Title = "Conflict",
                Detail = e.Message,
                Type = "https://tools.ietf.org/html/rfc7231#section-6.5.8"
            },
            ForbiddenException e => new ProblemDetails
            {
                Status = StatusCodes.Status403Forbidden,
                Title = "Forbidden",
                Detail = e.Message,
                Type = "https://tools.ietf.org/html/rfc7231#section-6.5.3"
            },
            DomainException e => new ProblemDetails
            {
                Status = StatusCodes.Status400BadRequest,
                Title = "Business Rule Violation",
                Detail = e.Message,
                Type = "https://example.com/problems/business-rule"
            },
            _ => new ProblemDetails
            {
                Status = StatusCodes.Status500InternalServerError,
                Title = "Internal Server Error",
                Type = "https://tools.ietf.org/html/rfc7231#section-6.6.1"
            }
        };
        
        problem.Instance = context.Request.Path;
        problem.Extensions["traceId"] = Activity.Current?.Id ?? context.TraceIdentifier;
        
        context.Response.StatusCode = problem.Status ?? 500;
        await context.Response.WriteAsJsonAsync(problem, ct);
        
        return true;
    }
}

// Registration
builder.Services.AddExceptionHandler<GlobalExceptionHandler>();
builder.Services.AddProblemDetails();

app.UseExceptionHandler();
```

## Versioning

### URL Path Versioning

```csharp
builder.Services.AddApiVersioning(options =>
{
    options.DefaultApiVersion = new ApiVersion(1, 0);
    options.AssumeDefaultVersionWhenUnspecified = true;
    options.ReportApiVersions = true;
    options.ApiVersionReader = new UrlSegmentApiVersionReader();
})
.AddApiExplorer(options =>
{
    options.GroupNameFormat = "'v'VVV";
    options.SubstituteApiVersionInUrl = true;
});

// Controller
[ApiController]
[Route("api/v{version:apiVersion}/orders")]
[ApiVersion("1.0")]
[ApiVersion("2.0")]
public class OrdersController : ControllerBase
{
    [HttpGet("{id}")]
    [MapToApiVersion("1.0")]
    public IActionResult GetV1(Guid id) => Ok(new { Id = id, Version = "1.0" });
    
    [HttpGet("{id}")]
    [MapToApiVersion("2.0")]
    public IActionResult GetV2(Guid id) => Ok(new { OrderId = id, ApiVersion = "2.0" });
}

// Minimal API
var v1 = app.NewVersionedApi()
    .MapGroup("/api/v{version:apiVersion}/orders")
    .HasApiVersion(1.0);

var v2 = app.NewVersionedApi()
    .MapGroup("/api/v{version:apiVersion}/orders")
    .HasApiVersion(2.0);
```

## Documentation

### OpenAPI/Swagger Setup

```csharp
builder.Services.AddOpenApi();

// Or with customization
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen(options =>
{
    options.SwaggerDoc("v1", new OpenApiInfo
    {
        Title = "Orders API",
        Version = "v1",
        Description = "API for managing orders",
        Contact = new OpenApiContact
        {
            Name = "API Support",
            Email = "api@example.com"
        }
    });
    
    // Include XML comments
    var xmlFile = $"{Assembly.GetExecutingAssembly().GetName().Name}.xml";
    var xmlPath = Path.Combine(AppContext.BaseDirectory, xmlFile);
    options.IncludeXmlComments(xmlPath);
    
    // JWT authentication
    options.AddSecurityDefinition("Bearer", new OpenApiSecurityScheme
    {
        Type = SecuritySchemeType.Http,
        Scheme = "bearer",
        BearerFormat = "JWT",
        Description = "Enter JWT token"
    });
    
    options.AddSecurityRequirement(new OpenApiSecurityRequirement
    {
        {
            new OpenApiSecurityScheme
            {
                Reference = new OpenApiReference
                {
                    Type = ReferenceType.SecurityScheme,
                    Id = "Bearer"
                }
            },
            Array.Empty<string>()
        }
    });
});

app.UseSwagger();
app.UseSwaggerUI();
```

### XML Documentation

```csharp
/// <summary>
/// Creates a new order for the specified customer.
/// </summary>
/// <param name="command">The order creation details.</param>
/// <param name="ct">Cancellation token.</param>
/// <returns>The created order.</returns>
/// <response code="201">Order created successfully.</response>
/// <response code="400">Invalid order data.</response>
/// <response code="404">Customer not found.</response>
/// <example>
/// POST /api/orders
/// {
///   "customerId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
///   "lines": [
///     { "productId": "...", "quantity": 2 }
///   ]
/// }
/// </example>
[HttpPost]
[ProducesResponseType<OrderDto>(StatusCodes.Status201Created)]
[ProducesResponseType<ValidationProblemDetails>(StatusCodes.Status400BadRequest)]
[ProducesResponseType<ProblemDetails>(StatusCodes.Status404NotFound)]
public async Task<IActionResult> Create(CreateOrderCommand command, CancellationToken ct)
{
    var order = await _orderService.CreateAsync(command, ct);
    return CreatedAtAction(nameof(Get), new { id = order.Id }, order);
}
```

## Authentication & Authorization

### JWT Bearer Setup

```csharp
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(options =>
    {
        options.Authority = builder.Configuration["Auth:Authority"];
        options.Audience = builder.Configuration["Auth:Audience"];
        options.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true,
            ValidateAudience = true,
            ValidateLifetime = true,
            ValidateIssuerSigningKey = true
        };
    });

builder.Services.AddAuthorization(options =>
{
    options.AddPolicy("OrdersRead", policy =>
        policy.RequireClaim("scope", "orders:read"));
    
    options.AddPolicy("OrdersWrite", policy =>
        policy.RequireClaim("scope", "orders:write"));
    
    options.AddPolicy("AdminOnly", policy =>
        policy.RequireRole("Admin"));
});

app.UseAuthentication();
app.UseAuthorization();
```

### Policy-Based Authorization

```csharp
// Custom requirement
public class OrderOwnerRequirement : IAuthorizationRequirement { }

public class OrderOwnerHandler(IOrderRepository orders) 
    : AuthorizationHandler<OrderOwnerRequirement, Guid>
{
    protected override async Task HandleRequirementAsync(
        AuthorizationHandlerContext context,
        OrderOwnerRequirement requirement,
        Guid orderId)
    {
        var userId = context.User.FindFirstValue(ClaimTypes.NameIdentifier);
        if (userId is null) return;
        
        var order = await orders.GetByIdAsync(orderId);
        if (order?.CustomerId.ToString() == userId)
        {
            context.Succeed(requirement);
        }
    }
}
```

## Performance

### Response Caching

```csharp
builder.Services.AddResponseCaching();
builder.Services.AddOutputCache(options =>
{
    options.AddBasePolicy(policy => policy.Expire(TimeSpan.FromMinutes(5)));
    options.AddPolicy("Products", policy => 
        policy.Expire(TimeSpan.FromHours(1)).Tag("products"));
});

app.UseOutputCache();

// Controller
[HttpGet]
[OutputCache(PolicyName = "Products")]
public async Task<IActionResult> GetProducts() { }

// Minimal API
app.MapGet("/products", async () => { })
   .CacheOutput("Products");

// Cache invalidation
app.MapPost("/products", async (IOutputCacheStore cache) =>
{
    await cache.EvictByTagAsync("products", default);
});
```

### Pagination

```csharp
public record PagedRequest(int Page = 1, int PageSize = 20)
{
    public int Page { get; init; } = Math.Max(1, Page);
    public int PageSize { get; init; } = Math.Clamp(PageSize, 1, 100);
    public int Skip => (Page - 1) * PageSize;
}

public record PagedResponse<T>(
    IReadOnlyList<T> Items,
    int Page,
    int PageSize,
    int TotalCount)
{
    public int TotalPages => (int)Math.Ceiling(TotalCount / (double)PageSize);
    public bool HasPrevious => Page > 1;
    public bool HasNext => Page < TotalPages;
}

// Usage
[HttpGet]
public async Task<ActionResult<PagedResponse<OrderDto>>> GetOrders(
    [FromQuery] PagedRequest request,
    CancellationToken ct)
{
    var totalCount = await _db.Orders.CountAsync(ct);
    
    var items = await _db.Orders
        .OrderByDescending(o => o.CreatedAt)
        .Skip(request.Skip)
        .Take(request.PageSize)
        .Select(o => o.ToDto())
        .ToListAsync(ct);
    
    return new PagedResponse<OrderDto>(items, request.Page, request.PageSize, totalCount);
}
```

### Compression

```csharp
builder.Services.AddResponseCompression(options =>
{
    options.EnableForHttps = true;
    options.Providers.Add<BrotliCompressionProvider>();
    options.Providers.Add<GzipCompressionProvider>();
});

builder.Services.Configure<BrotliCompressionProviderOptions>(options =>
    options.Level = CompressionLevel.Fastest);

app.UseResponseCompression();
```
