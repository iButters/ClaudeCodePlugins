# Blazor Component Patterns

## Component Lifecycle

```
┌─────────────────────────────────────────────────────────────┐
│                    Component Created                         │
└─────────────────────┬───────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  SetParametersAsync (parameters received from parent)        │
└─────────────────────┬───────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  OnInitialized / OnInitializedAsync (first render only)     │
└─────────────────────┬───────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  OnParametersSet / OnParametersSetAsync                      │
└─────────────────────┬───────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  ShouldRender (returns bool, default true)                   │
└─────────────────────┬───────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  BuildRenderTree (render UI)                                 │
└─────────────────────┬───────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  OnAfterRender / OnAfterRenderAsync                          │
└─────────────────────────────────────────────────────────────┘
```

### Lifecycle Methods

```csharp
@code {
    [Parameter] public int ItemId { get; set; }

    private Item? item;
    private bool isLoading = true;

    // Called ONCE on first render
    protected override async Task OnInitializedAsync()
    {
        // Initial data load
        await LoadItemAsync(ItemId);
    }

    // Called on EVERY parameter change (including initial)
    protected override async Task OnParametersSetAsync()
    {
        // React to parameter changes
        if (ItemId != item?.Id)
        {
            await LoadItemAsync(ItemId);
        }
    }

    // Called AFTER render completes
    protected override void OnAfterRender(bool firstRender)
    {
        if (firstRender)
        {
            // Safe to use JS interop here
        }
    }

    // Control re-rendering (performance optimization)
    protected override bool ShouldRender()
    {
        return !isLoading; // Don't render while loading
    }

    private async Task LoadItemAsync(int id)
    {
        isLoading = true;
        item = await DataService.GetItemAsync(id);
        isLoading = false;
    }
}
```

## RenderFragment Patterns

### Child Content

```razor
@* Card.razor *@
<div class="card">
    <div class="card-header">@Title</div>
    <div class="card-body">
        @ChildContent
    </div>
</div>

@code {
    [Parameter] public string Title { get; set; } = "";
    [Parameter] public RenderFragment? ChildContent { get; set; }
}

@* Usage *@
<Card Title="Welcome">
    <p>This is the card content.</p>
    <button>Click me</button>
</Card>
```

### Named RenderFragments

```razor
@* Layout.razor *@
<div class="layout">
    <header>@Header</header>
    <main>@Body</main>
    <footer>@Footer</footer>
</div>

@code {
    [Parameter] public RenderFragment? Header { get; set; }
    [Parameter] public RenderFragment? Body { get; set; }
    [Parameter] public RenderFragment? Footer { get; set; }
}

@* Usage *@
<Layout>
    <Header><h1>My App</h1></Header>
    <Body><p>Main content here</p></Body>
    <Footer><small>Copyright 2024</small></Footer>
</Layout>
```

### Templated Components

```razor
@* ListView.razor *@
@typeparam TItem

<ul class="list">
    @foreach (var item in Items)
    {
        <li>@ItemTemplate(item)</li>
    }
</ul>

@code {
    [Parameter] public IEnumerable<TItem> Items { get; set; } = [];
    [Parameter] public RenderFragment<TItem> ItemTemplate { get; set; } = default!;
}

@* Usage *@
<ListView Items="products" Context="product">
    <ItemTemplate>
        <span>@product.Name - @product.Price.ToString("C")</span>
    </ItemTemplate>
</ListView>
```

## EventCallback Patterns

### Basic EventCallback

```razor
@* Child.razor *@
<button @onclick="OnButtonClick">@Text</button>

@code {
    [Parameter] public string Text { get; set; } = "Click";
    [Parameter] public EventCallback OnClick { get; set; }

    private async Task OnButtonClick()
    {
        await OnClick.InvokeAsync();
    }
}

@* Parent.razor *@
<Child Text="Save" OnClick="HandleSave" />

@code {
    private void HandleSave()
    {
        // Handle click - StateHasChanged called automatically
    }
}
```

### EventCallback with Value

```razor
@* Counter.razor *@
<div>
    <span>@Count</span>
    <button @onclick="Increment">+</button>
</div>

@code {
    [Parameter] public int Count { get; set; }
    [Parameter] public EventCallback<int> CountChanged { get; set; }

    private async Task Increment()
    {
        await CountChanged.InvokeAsync(Count + 1);
    }
}

@* Parent.razor - Two-way binding *@
<Counter @bind-Count="currentCount" />
<p>Count: @currentCount</p>

@code {
    private int currentCount = 0;
}
```

## Cascading Parameters

### Cascading Value Provider

```razor
@* App.razor or Layout *@
<CascadingValue Value="@theme" Name="AppTheme">
    <CascadingValue Value="@user">
        @Body
    </CascadingValue>
</CascadingValue>

@code {
    private Theme theme = new() { IsDark = false };
    private User? user;
}
```

### Consuming Cascading Values

```razor
@* ChildComponent.razor *@
<div class="@(Theme.IsDark ? "dark" : "light")">
    @if (User is not null)
    {
        <span>Welcome, @User.Name</span>
    }
</div>

@code {
    [CascadingParameter(Name = "AppTheme")]
    public Theme Theme { get; set; } = default!;

    [CascadingParameter]
    public User? User { get; set; }
}
```

## Data Binding

### One-Way Binding

```razor
<p>@message</p>
<input value="@inputValue" />

@code {
    private string message = "Hello";
    private string inputValue = "";
}
```

### Two-Way Binding

```razor
@* Native HTML elements *@
<input @bind="name" />
<input @bind="name" @bind:event="oninput" />
<input @bind="date" @bind:format="yyyy-MM-dd" />

@* Component binding *@
<MyInput @bind-Value="email" />

@code {
    private string name = "";
    private DateTime date = DateTime.Now;
    private string email = "";
}
```

### Binding to Component Parameters

```razor
@* TextInput.razor *@
<input value="@Value" @oninput="OnInput" />

@code {
    [Parameter] public string Value { get; set; } = "";
    [Parameter] public EventCallback<string> ValueChanged { get; set; }

    private async Task OnInput(ChangeEventArgs e)
    {
        await ValueChanged.InvokeAsync(e.Value?.ToString());
    }
}
```

## StateHasChanged Usage

### When to Call StateHasChanged

```csharp
// NOT needed after:
// - Event handlers (@onclick, @onchange, etc.)
// - Parameter changes
// - Lifecycle methods completing

// REQUIRED for:
// - Timer callbacks
// - External event handlers
// - Background task completion
// - Service event subscriptions

@implements IDisposable

@code {
    private System.Timers.Timer? timer;

    protected override void OnInitialized()
    {
        timer = new System.Timers.Timer(1000);
        timer.Elapsed += async (s, e) =>
        {
            // Must use InvokeAsync from non-UI thread
            await InvokeAsync(() =>
            {
                UpdateUI();
                StateHasChanged();
            });
        };
        timer.Start();
    }

    public void Dispose() => timer?.Dispose();
}
```

## Performance Optimization

### ShouldRender Override

```csharp
@code {
    private string lastValue = "";

    [Parameter] public string Value { get; set; } = "";

    protected override bool ShouldRender()
    {
        if (Value == lastValue) return false;
        lastValue = Value;
        return true;
    }
}
```

### @key for List Rendering

```razor
@* Preserve component state during list changes *@
@foreach (var item in items)
{
    <ItemComponent @key="item.Id" Item="item" />
}
```

### Virtualization

```razor
@* For large lists *@
<Virtualize Items="allItems" Context="item">
    <ItemTemplate>
        <div>@item.Name</div>
    </ItemTemplate>
    <Placeholder>
        <div>Loading...</div>
    </Placeholder>
</Virtualize>
```
