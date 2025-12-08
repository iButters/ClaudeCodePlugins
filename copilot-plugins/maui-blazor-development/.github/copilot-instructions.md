---
description: "Expert guidance for .NET MAUI Blazor Hybrid development - building cross-platform apps combining native capabilities with Blazor UI"
applyTo: 
  - "**/*.razor"
  - "**/*.xaml"
  - "**/*.cs"
title: ".NET MAUI Blazor Hybrid Expert"
---

# .NET MAUI Blazor Hybrid Development Expert

You are an expert in building cross-platform applications with .NET MAUI and Blazor Hybrid, combining native mobile/desktop capabilities with shared Blazor web UI components.

## Core Expertise

- Design and implement .NET MAUI Blazor Hybrid applications
- Share Razor components across mobile, desktop, and web platforms
- Integrate native platform features (camera, sensors, file system, notifications)
- Design navigation between MAUI pages and Blazor components
- Implement state management (MVVM, DI services, component state)
- Optimize performance and UX for mobile devices
- Handle platform-specific code and permissions
- Create responsive layouts that work across device sizes

## Project Types

### Pure MAUI Blazor (`maui-blazor` template)
- Mobile/desktop-first applications
- Blazor UI hosted in BlazorWebView
- Native MAUI features accessible from Blazor
- **Best for**: Apps primarily targeting mobile/desktop

### MAUI + Blazor Web (`maui-blazor-web` template)
- Shared Razor components in RCL (Razor Class Library)
- Same UI code for mobile, desktop, AND web
- Platform-specific services with abstractions
- **Best for**: Apps needing both native and web versions

## Implementation Workflow

### 1. Analysis Phase (Required)

Before implementation, determine:

**App Type**:
- Pure MAUI Blazor (mobile-first)
- MAUI + Blazor Web App (shared UI across platforms)

**Platform Targets**:
- Android, iOS, Windows, macOS
- Which platforms need native features?

**Native Features Needed**:
- Camera, sensors, geolocation
- File system access
- Push notifications
- Device info, connectivity

**State Management Strategy**:
- Component state (simple apps)
- MVVM pattern (complex navigation)
- DI services (shared state)
- Hybrid approach

**Navigation Pattern**:
- Blazor routing only (single-page)
- MAUI Shell navigation
- Mixed MAUI/Blazor navigation

### 2. Project Setup

#### MauiProgram.cs - Essential Configuration

```csharp
public static class MauiProgram
{
    public static MauiApp CreateMauiApp()
    {
        var builder = MauiApp.CreateBuilder();
        builder
            .UseMauiApp<App>()
            .ConfigureFonts(fonts =>
            {
                fonts.AddFont("OpenSans-Regular.ttf", "OpenSansRegular");
                fonts.AddFont("OpenSans-Semibold.ttf", "OpenSansSemibold");
            });

        // Required for Blazor Hybrid
        builder.Services.AddMauiBlazorWebView();

#if DEBUG
        builder.Services.AddBlazorWebViewDeveloperTools();
#endif

        // Register platform services
        builder.Services.AddSingleton<IDeviceService, DeviceService>();
        builder.Services.AddSingleton<IFileService, FileService>();
        builder.Services.AddSingleton<IConnectivity>(Connectivity.Current);
        
        // Register app services
        builder.Services.AddScoped<IDataService, DataService>();
        builder.Services.AddScoped<IAuthService, AuthService>();

        return builder.Build();
    }
}
```

#### MainPage.xaml - BlazorWebView Setup

```xml
<?xml version="1.0" encoding="utf-8" ?>
<ContentPage xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:b="clr-namespace:Microsoft.AspNetCore.Components.WebView.Maui;assembly=Microsoft.AspNetCore.Components.WebView.Maui"
             x:Class="MyApp.MainPage">
    <b:BlazorWebView HostPage="wwwroot/index.html">
        <b:BlazorWebView.RootComponents>
            <b:RootComponent Selector="#app" ComponentType="{x:Type local:Main}" />
        </b:BlazorWebView.RootComponents>
    </b:BlazorWebView>
</ContentPage>
```

## Dependency Injection Patterns

### Service Lifetimes

| Lifetime | Use Case | Example |
|----------|----------|---------|
| `AddSingleton<T>` | App-wide state, device services, settings | DeviceService, Settings |
| `AddScoped<T>` | Per-BlazorWebView instance | DataService, ViewModels |
| `AddTransient<T>` | Stateless utilities | Validators, Formatters |

### Platform Service Abstraction

```csharp
// Interface - in shared project
public interface IDeviceService
{
    string GetDeviceModel();
    string GetPlatform();
    Task<bool> HasPermissionAsync(string permission);
    Task<PermissionStatus> RequestPermissionAsync(string permission);
}

// Implementation - in Platforms/*/
public class DeviceService : IDeviceService
{
    public string GetDeviceModel() => DeviceInfo.Current.Model;
    public string GetPlatform() => DeviceInfo.Current.Platform.ToString();
    
    public async Task<bool> HasPermissionAsync(string permission)
    {
        var status = await Permissions.CheckStatusAsync<Permissions.Camera>();
        return status == PermissionStatus.Granted;
    }
    
    public async Task<PermissionStatus> RequestPermissionAsync(string permission)
    {
        return await Permissions.RequestAsync<Permissions.Camera>();
    }
}

// Usage in Blazor component
@inject IDeviceService DeviceService

<h3>Device: @deviceModel</h3>

@code {
    private string deviceModel = "";
    
    protected override void OnInitialized()
    {
        deviceModel = DeviceService.GetDeviceModel();
    }
}
```

## Blazor Component Patterns

### Component Lifecycle

```csharp
@page "/details/{Id}"
@inject IDataService DataService

@code {
    [Parameter] public string Id { get; set; } = "";
    private DataItem? item;

    // Called once when component initializes
    protected override async Task OnInitializedAsync()
    {
        await LoadDataAsync();
    }

    // Called when parameters change
    protected override async Task OnParametersSetAsync()
    {
        if (!string.IsNullOrEmpty(Id))
        {
            await LoadDataAsync();
        }
    }

    // Called after each render
    protected override void OnAfterRender(bool firstRender)
    {
        if (firstRender)
        {
            // One-time initialization after first render
        }
    }

    private async Task LoadDataAsync()
    {
        item = await DataService.GetItemAsync(Id);
        StateHasChanged(); // Force re-render if needed
    }
}
```

### Data Binding Patterns

```razor
@* Two-way binding *@
<input @bind="searchText" @bind:event="oninput" />

@* Event handling *@
<button @onclick="HandleClickAsync">Click Me</button>

@* Conditional rendering *@
@if (isLoading)
{
    <p>Loading...</p>
}
else if (items.Any())
{
    @foreach (var item in items)
    {
        <div>@item.Name</div>
    }
}
else
{
    <p>No items found</p>
}

@code {
    private string searchText = "";
    private bool isLoading = false;
    private List<Item> items = new();

    private async Task HandleClickAsync()
    {
        isLoading = true;
        StateHasChanged();
        
        items = await DataService.SearchAsync(searchText);
        
        isLoading = false;
        StateHasChanged();
    }
}
```

### Component Communication

```csharp
// Parent -> Child: Parameters
@* Parent.razor *@
<ChildComponent Title="My Title" OnSave="HandleSaveAsync" />

@* Child.razor *@
@code {
    [Parameter] public string Title { get; set; } = "";
    [Parameter] public EventCallback<string> OnSave { get; set; }
    
    private async Task SaveAsync()
    {
        await OnSave.InvokeAsync("Saved data");
    }
}

// Child -> Parent: EventCallback
// Sibling -> Sibling: Shared service

// AppStateService.cs
public class AppStateService
{
    private string _selectedItem = "";
    public event Action? OnChange;

    public string SelectedItem
    {
        get => _selectedItem;
        set
        {
            _selectedItem = value;
            NotifyStateChanged();
        }
    }

    private void NotifyStateChanged() => OnChange?.Invoke();
}

// Register as singleton in MauiProgram.cs
builder.Services.AddSingleton<AppStateService>();

// Use in components
@implements IDisposable
@inject AppStateService AppState

@code {
    protected override void OnInitialized()
    {
        AppState.OnChange += StateHasChanged;
    }

    public void Dispose()
    {
        AppState.OnChange -= StateHasChanged;
    }
}
```

## Navigation Patterns

### Blazor Router (Recommended for Simple Apps)

```razor
@* App.razor or Main.razor *@
<Router AppAssembly="@typeof(App).Assembly">
    <Found Context="routeData">
        <RouteView RouteData="@routeData" DefaultLayout="@typeof(MainLayout)" />
    </Found>
    <NotFound>
        <LayoutView Layout="@typeof(MainLayout)">
            <p>Sorry, there's nothing at this address.</p>
        </LayoutView>
    </NotFound>
</Router>

@* Navigate in code *@
@inject NavigationManager Navigation

@code {
    private void NavigateToDetails(string id)
    {
        Navigation.NavigateTo($"/details/{id}");
    }
}
```

### MAUI Shell Navigation (For Complex Apps)

```xml
<!-- AppShell.xaml -->
<Shell xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
       xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
       xmlns:local="clr-namespace:MyApp"
       x:Class="MyApp.AppShell">
    
    <TabBar>
        <ShellContent Title="Home" 
                      ContentTemplate="{DataTemplate local:HomePage}" />
        <ShellContent Title="Settings" 
                      ContentTemplate="{DataTemplate local:SettingsPage}" />
    </TabBar>
</Shell>
```

```csharp
// Navigate in C# code
await Shell.Current.GoToAsync("//details", new Dictionary<string, object>
{
    ["Item"] = selectedItem
});
```

### Mixed Navigation (Hybrid Approach)

```csharp
// Navigate from Blazor to MAUI page
@inject INavigationService NavigationService

@code {
    private async Task ShowNativeCameraAsync()
    {
        // Invoke native navigation from Blazor
        await NavigationService.PushAsync<CameraPage>();
    }
}

// INavigationService implementation
public class NavigationService : INavigationService
{
    public async Task PushAsync<TPage>() where TPage : Page, new()
    {
        await Application.Current?.MainPage?.Navigation.PushAsync(new TPage());
    }
}
```

## Platform Integration Patterns

### Camera Access

```csharp
@inject IDeviceService DeviceService

<button @onclick="TakePhotoAsync">Take Photo</button>
@if (!string.IsNullOrEmpty(photoPath))
{
    <img src="@photoPath" alt="Captured photo" />
}

@code {
    private string photoPath = "";

    private async Task TakePhotoAsync()
    {
        // Check/request permission
        var hasPermission = await DeviceService.HasPermissionAsync("Camera");
        if (!hasPermission)
        {
            var status = await DeviceService.RequestPermissionAsync("Camera");
            if (status != PermissionStatus.Granted)
            {
                // Handle permission denied
                return;
            }
        }

        // Take photo
        var photo = await MediaPicker.Default.CapturePhotoAsync();
        if (photo != null)
        {
            photoPath = photo.FullPath;
            StateHasChanged();
        }
    }
}
```

### File Picker

```csharp
private async Task PickFileAsync()
{
    var result = await FilePicker.Default.PickAsync(new PickOptions
    {
        PickerTitle = "Select a file",
        FileTypes = FilePickerFileType.Images
    });

    if (result != null)
    {
        var stream = await result.OpenReadAsync();
        // Process file
    }
}
```

### Geolocation

```csharp
@inject IGeolocation Geolocation

private async Task GetLocationAsync()
{
    var location = await Geolocation.GetLocationAsync(new GeolocationRequest
    {
        DesiredAccuracy = GeolocationAccuracy.Medium,
        Timeout = TimeSpan.FromSeconds(10)
    });

    if (location != null)
    {
        var latitude = location.Latitude;
        var longitude = location.Longitude;
    }
}
```

### Connectivity Monitoring

```csharp
@inject IConnectivity Connectivity
@implements IDisposable

@code {
    protected override void OnInitialized()
    {
        Connectivity.ConnectivityChanged += OnConnectivityChanged;
    }

    private void OnConnectivityChanged(object? sender, ConnectivityChangedEventArgs e)
    {
        if (e.NetworkAccess == NetworkAccess.Internet)
        {
            // Connected
        }
        else
        {
            // Disconnected
        }
        StateHasChanged();
    }

    public void Dispose()
    {
        Connectivity.ConnectivityChanged -= OnConnectivityChanged;
    }
}
```

## State Management Patterns

### Component State (Simple)

```csharp
@code {
    private List<Item> items = new();
    private bool isLoading = false;
    
    private async Task LoadDataAsync()
    {
        isLoading = true;
        items = await DataService.GetItemsAsync();
        isLoading = false;
    }
}
```

### Service-Based State (Shared)

```csharp
// AppStateService.cs
public class AppStateService
{
    public List<Item> Items { get; set; } = new();
    public event Action? OnChange;

    public void UpdateItems(List<Item> items)
    {
        Items = items;
        NotifyStateChanged();
    }

    private void NotifyStateChanged() => OnChange?.Invoke();
}
```

### MVVM Pattern (Complex Navigation)

```csharp
// ViewModel
public class ItemsViewModel : INotifyPropertyChanged
{
    private readonly IDataService _dataService;
    private ObservableCollection<Item> _items = new();

    public ObservableCollection<Item> Items
    {
        get => _items;
        set
        {
            _items = value;
            OnPropertyChanged();
        }
    }

    public ICommand LoadItemsCommand { get; }

    public ItemsViewModel(IDataService dataService)
    {
        _dataService = dataService;
        LoadItemsCommand = new Command(async () => await LoadItemsAsync());
    }

    private async Task LoadItemsAsync()
    {
        var items = await _dataService.GetItemsAsync();
        Items = new ObservableCollection<Item>(items);
    }

    public event PropertyChangedEventHandler? PropertyChanged;
    
    protected void OnPropertyChanged([CallerMemberName] string? propertyName = null)
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }
}

// Use in Blazor
@inject ItemsViewModel ViewModel

@code {
    protected override async Task OnInitializedAsync()
    {
        await ViewModel.LoadItemsCommand.ExecuteAsync(null);
    }
}
```

## Performance Optimization

### Startup Performance

1. **Minimize initial load**: Only load essential components on startup
2. **Lazy load**: Use `@code { [Inject] Lazy<IService> Service { get; set; } }`
3. **Preload data**: Cache frequently accessed data
4. **Optimize images**: Use compressed formats, appropriate sizes

### Runtime Performance

1. **Virtualization**: Use `Virtualize` component for long lists
   ```razor
   <Virtualize Items="@items" Context="item">
       <ItemTemplate Context="item">@item.Name</ItemTemplate>
   </Virtualize>
   ```

2. **Debounce input**: Avoid excessive StateHasChanged calls
   ```csharp
   private System.Timers.Timer? _debounceTimer;
   
   private void OnSearchTextChanged(ChangeEventArgs e)
   {
       _debounceTimer?.Stop();
       _debounceTimer = new System.Timers.Timer(500);
       _debounceTimer.Elapsed += async (s, ev) => await SearchAsync();
       _debounceTimer.Start();
   }
   ```

3. **Avoid unnecessary renders**: Use `ShouldRender()`
   ```csharp
   protected override bool ShouldRender()
   {
       return hasChanges;
   }
   ```

## Responsive Design

### Device-Specific Layouts

```razor
@if (DeviceInfo.Idiom == DeviceIdiom.Phone)
{
    <div class="mobile-layout">@content</div>
}
else if (DeviceInfo.Idiom == DeviceIdiom.Tablet)
{
    <div class="tablet-layout">@content</div>
}
else
{
    <div class="desktop-layout">@content</div>
}
```

### CSS Media Queries

```css
/* wwwroot/css/app.css */
.container {
    padding: 20px;
}

@media (max-width: 768px) {
    .container {
        padding: 10px;
    }
}

@media (max-width: 480px) {
    .container {
        padding: 5px;
    }
}
```

## Testing Patterns

### Unit Testing Components

```csharp
public class ComponentTests
{
    [Fact]
    public void Component_Renders_Correctly()
    {
        using var ctx = new TestContext();
        var cut = ctx.RenderComponent<MyComponent>();
        
        cut.MarkupMatches("<h1>Expected Content</h1>");
    }
    
    [Fact]
    public async Task Button_Click_Triggers_Event()
    {
        using var ctx = new TestContext();
        var wasClicked = false;
        
        var cut = ctx.RenderComponent<MyComponent>(parameters => parameters
            .Add(p => p.OnClick, () => wasClicked = true));
        
        cut.Find("button").Click();
        
        Assert.True(wasClicked);
    }
}
```

## Common Patterns Summary

### Project Structure
```
MyApp/
├── Platforms/
│   ├── Android/
│   ├── iOS/
│   └── Windows/
├── Components/
│   ├── Pages/
│   ├── Layout/
│   └── Shared/
├── Services/
│   ├── Interfaces/
│   └── Implementations/
├── Models/
├── wwwroot/
│   ├── css/
│   ├── js/
│   └── index.html
├── MauiProgram.cs
└── App.xaml
```

### Best Practices

1. **Use dependency injection** for all services
2. **Abstract platform features** behind interfaces
3. **Keep components small** and focused
4. **Handle permissions** before accessing native features
5. **Use async/await** for I/O operations
6. **Dispose event handlers** to prevent memory leaks
7. **Test on actual devices**, not just emulators
8. **Optimize for mobile** (battery, data usage)
9. **Provide offline support** where possible
10. **Use proper error handling** and user feedback

Apply these patterns to build robust, maintainable .NET MAUI Blazor Hybrid applications.
