# .NET MAUI Blazor Hybrid Development - GitHub Copilot Chat Edition

Expert guidance for building cross-platform apps with .NET MAUI and Blazor Hybrid - combining native mobile/desktop capabilities with shared Blazor web UI.

## 📋 Overview

This is the GitHub Copilot Chat version of the MAUI Blazor Development plugin. It provides comprehensive guidance for:
- .NET MAUI Blazor Hybrid application architecture
- Sharing Razor components across mobile, desktop, and web
- Native platform integration (camera, sensors, file system, notifications)
- Navigation patterns (Blazor routing, MAUI Shell, mixed)
- State management strategies (MVVM, DI services, component state)
- Performance optimization for mobile devices
- Responsive design across device sizes

## 🚀 Installation

### Copy to Your MAUI Project

```bash
cp -r .github /path/to/your/maui/project/
```

The instructions automatically activate when working with:
- Razor files (`.razor`)
- XAML files (`.xaml`)
- C# files (`.cs`) in MAUI projects

## 💡 Features

### Automatic Expert Guidance

When you open MAUI Blazor Hybrid files, GitHub Copilot automatically applies these expert patterns:

**No commands needed!** Just start coding or ask questions like:
- "How do I set up BlazorWebView in MAUI?"
- "Design a service to access the camera from Blazor"
- "Show me navigation patterns for this app"
- "How do I share state between components?"

### Expert Capabilities

- ✅ Design MAUI Blazor Hybrid architecture
- ✅ Integrate native platform features from Blazor
- ✅ Implement navigation (Blazor Router, MAUI Shell, mixed)
- ✅ Manage state across components and platforms
- ✅ Create responsive layouts for all device sizes
- ✅ Optimize performance for mobile devices
- ✅ Handle platform-specific code and permissions
- ✅ Share UI between mobile, desktop, and web

## 🏗️ Project Types

### Pure MAUI Blazor (`maui-blazor` template)
**Best for**: Mobile/desktop-first apps
- Blazor UI hosted in BlazorWebView
- Native MAUI features accessible from Blazor
- Single codebase for mobile and desktop

### MAUI + Blazor Web (`maui-blazor-web` template)
**Best for**: Apps needing both native and web versions
- Shared Razor components in RCL (Razor Class Library)
- Same UI code for mobile, desktop, AND web
- Platform-specific services with abstractions

## 📐 Architecture Patterns

### Project Setup

**MauiProgram.cs** - Essential configuration:
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
            });

        // Required for Blazor Hybrid
        builder.Services.AddMauiBlazorWebView();

#if DEBUG
        builder.Services.AddBlazorWebViewDeveloperTools();
#endif

        // Register platform services
        builder.Services.AddSingleton<IDeviceService, DeviceService>();
        builder.Services.AddScoped<IDataService, DataService>();

        return builder.Build();
    }
}
```

**MainPage.xaml** - BlazorWebView setup:
```xml
<ContentPage xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
             xmlns:b="clr-namespace:Microsoft.AspNetCore.Components.WebView.Maui;assembly=Microsoft.AspNetCore.Components.WebView.Maui">
    <b:BlazorWebView HostPage="wwwroot/index.html">
        <b:BlazorWebView.RootComponents>
            <b:RootComponent Selector="#app" ComponentType="{x:Type local:Main}" />
        </b:BlazorWebView.RootComponents>
    </b:BlazorWebView>
</ContentPage>
```

### Dependency Injection

| Lifetime | Use Case | Example |
|----------|----------|---------|
| `AddSingleton<T>` | App-wide state, device services | DeviceService, Settings |
| `AddScoped<T>` | Per-BlazorWebView instance | DataService, ViewModels |
| `AddTransient<T>` | Stateless utilities | Validators, Formatters |

### Platform Service Abstraction

```csharp
// Interface - shared across platforms
public interface IDeviceService
{
    string GetDeviceModel();
    Task<bool> HasPermissionAsync(string permission);
}

// Implementation - platform-specific
public class DeviceService : IDeviceService
{
    public string GetDeviceModel() => DeviceInfo.Current.Model;
    
    public async Task<bool> HasPermissionAsync(string permission)
    {
        var status = await Permissions.CheckStatusAsync<Permissions.Camera>();
        return status == PermissionStatus.Granted;
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

## 🔄 Navigation Patterns

### Blazor Router (Simple Apps)
```razor
<Router AppAssembly="@typeof(App).Assembly">
    <Found Context="routeData">
        <RouteView RouteData="@routeData" DefaultLayout="@typeof(MainLayout)" />
    </Found>
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

### MAUI Shell Navigation (Complex Apps)
```xml
<Shell xmlns="http://schemas.microsoft.com/dotnet/2021/maui">
    <TabBar>
        <ShellContent Title="Home" ContentTemplate="{DataTemplate local:HomePage}" />
        <ShellContent Title="Settings" ContentTemplate="{DataTemplate local:SettingsPage}" />
    </TabBar>
</Shell>
```

```csharp
// Navigate in C#
await Shell.Current.GoToAsync("//details", new Dictionary<string, object>
{
    ["Item"] = selectedItem
});
```

## 📱 Platform Integration

### Camera Access
```csharp
@inject IDeviceService DeviceService

<button @onclick="TakePhotoAsync">Take Photo</button>

@code {
    private async Task TakePhotoAsync()
    {
        var hasPermission = await DeviceService.HasPermissionAsync("Camera");
        if (!hasPermission)
        {
            var status = await DeviceService.RequestPermissionAsync("Camera");
            if (status != PermissionStatus.Granted)
                return;
        }

        var photo = await MediaPicker.Default.CapturePhotoAsync();
        if (photo != null)
        {
            // Process photo
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

## 🎨 Component Patterns

### Component Lifecycle
```csharp
@page "/details/{Id}"
@inject IDataService DataService

@code {
    [Parameter] public string Id { get; set; } = "";

    protected override async Task OnInitializedAsync()
    {
        // Called once on component initialization
        await LoadDataAsync();
    }

    protected override async Task OnParametersSetAsync()
    {
        // Called when parameters change
        if (!string.IsNullOrEmpty(Id))
        {
            await LoadDataAsync();
        }
    }

    protected override void OnAfterRender(bool firstRender)
    {
        if (firstRender)
        {
            // One-time initialization after first render
        }
    }
}
```

### Data Binding
```razor
@* Two-way binding *@
<input @bind="searchText" @bind:event="oninput" />

@* Event handling *@
<button @onclick="HandleClickAsync">Search</button>

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
```

### Component Communication
```csharp
// Parent -> Child: Parameters
<ChildComponent Title="My Title" OnSave="HandleSaveAsync" />

// Child component
@code {
    [Parameter] public string Title { get; set; } = "";
    [Parameter] public EventCallback<string> OnSave { get; set; }
    
    private async Task SaveAsync()
    {
        await OnSave.InvokeAsync("Saved data");
    }
}

// Sibling -> Sibling: Shared service
public class AppStateService
{
    public event Action? OnChange;
    
    public void UpdateState()
    {
        NotifyStateChanged();
    }
    
    private void NotifyStateChanged() => OnChange?.Invoke();
}
```

## 📊 State Management

### Component State (Simple)
```csharp
@code {
    private List<Item> items = new();
    private bool isLoading = false;
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
        OnChange?.Invoke();
    }
}

// Register as singleton
builder.Services.AddSingleton<AppStateService>();

// Use in components
@inject AppStateService AppState
@implements IDisposable

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

### MVVM Pattern (Complex)
```csharp
public class ItemsViewModel : INotifyPropertyChanged
{
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
        LoadItemsCommand = new Command(async () => await LoadItemsAsync());
    }
}
```

## ⚡ Performance Optimization

### Virtualization for Long Lists
```razor
<Virtualize Items="@items" Context="item">
    <ItemTemplate>
        <div>@item.Name</div>
    </ItemTemplate>
</Virtualize>
```

### Debounce Input
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

### Avoid Unnecessary Renders
```csharp
protected override bool ShouldRender()
{
    return hasChanges;
}
```

## 📱 Responsive Design

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

## 🎯 Usage Scenarios

### Scenario 1: Setting Up a New MAUI Blazor App

**You**: "Create a new MAUI Blazor Hybrid app targeting Android and iOS with camera access"

**Copilot** (with this guidance): Will provide:
- Complete MauiProgram.cs configuration
- MainPage.xaml with BlazorWebView
- IDeviceService interface for camera abstraction
- Platform-specific implementations
- Permission handling
- Example Blazor component using the camera

### Scenario 2: Navigation Between Pages

**You**: "How do I navigate from a Blazor component to another page with parameters?"

**Copilot**: Will suggest:
- Blazor Router for component-to-component navigation
- MAUI Shell for native page navigation
- Parameter passing patterns
- Deep linking setup

### Scenario 3: Sharing State

**You**: "I need to share user authentication state across multiple components"

**Copilot**: Will design:
- AppStateService with event notifications
- Singleton registration in MauiProgram.cs
- Component subscription pattern
- Proper disposal to prevent memory leaks

## 📁 File Structure

```
.github/
├── copilot-instructions.md          # Main MAUI Blazor guidance
└── README-COPILOT.md               # This file
```

## 🆚 Differences from Claude Code Version

| Feature | Claude Code | GitHub Copilot Chat |
|---------|-------------|---------------------|
| **Activation** | Plugin installation | Copy `.github` directory |
| **Context** | Explicit skill reference | Automatic for .razor/.xaml files |
| **Commands** | Slash commands | Natural language |
| **Integration** | Claude Code IDE | VS Code, Visual Studio |

## 🚦 Getting Started

1. **Copy files to your MAUI project**:
   ```bash
   cp -r .github /path/to/your/maui/project/
   ```

2. **Start coding** - Open any `.razor`, `.xaml`, or `.cs` file

3. **Ask questions**:
   ```
   How do I access the camera from a Blazor component?
   Design a navigation pattern for this app
   Show me how to share state between components
   ```

4. **Iterate** - Copilot applies MAUI Blazor best practices

## 💡 Pro Tips

1. **Mention the platform**: "for Android and iOS" or "targeting mobile devices"
2. **Be specific about features**: "using the camera" or "with file picker"
3. **Request patterns**: "using dependency injection" or "with MVVM pattern"
4. **Ask for complete examples**: "show the full MauiProgram.cs setup"
5. **Include context**: "for a cross-platform messaging app"

## 🐛 Troubleshooting

**Copilot suggestions feel generic**:
- Mention "MAUI Blazor Hybrid" explicitly
- Reference specific patterns: "BlazorWebView", "platform service abstraction"

**Need platform-specific code**:
- Specify the platform: "for Android" or "for iOS"
- Mention native features: "using MAUI Essentials"

**Want architecture guidance**:
- Ask explicitly: "What's the best architecture for this?"
- Mention constraints: "targeting mobile and web"

## 📄 License

MIT License - Same as the original Claude Code plugin

---

**Build Amazing Cross-Platform Apps! 📱💻🌐**
