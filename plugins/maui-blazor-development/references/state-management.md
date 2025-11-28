# State Management

## Dependency Injection Patterns

### Service Lifetimes

| Lifetime | Scope | Use Case |
|----------|-------|----------|
| `Singleton` | App lifetime | Settings, device services, app state |
| `Scoped` | Per BlazorWebView | User session, page state |
| `Transient` | Per request | Stateless helpers, factories |

### Registration Patterns

```csharp
// MauiProgram.cs
public static MauiApp CreateMauiApp()
{
    var builder = MauiApp.CreateBuilder();

    // Singletons - app-wide shared state
    builder.Services.AddSingleton<ISettingsService, SettingsService>();
    builder.Services.AddSingleton<IAppState, AppState>();

    // Platform services as singletons
    builder.Services.AddSingleton(Connectivity.Current);
    builder.Services.AddSingleton(Geolocation.Default);
    builder.Services.AddSingleton(Preferences.Default);

    // Scoped - per BlazorWebView instance
    builder.Services.AddScoped<IUserSession, UserSession>();

    // Transient - new instance each time
    builder.Services.AddTransient<IDataValidator, DataValidator>();

    // HttpClient with typed client
    builder.Services.AddHttpClient<IApiClient, ApiClient>(client =>
    {
        client.BaseAddress = new Uri("https://api.example.com");
    });

    return builder.Build();
}
```

### Extension Methods for Clean Registration

```csharp
public static class ServiceCollectionExtensions
{
    public static IServiceCollection AddAppServices(this IServiceCollection services)
    {
        services.AddSingleton<ISettingsService, SettingsService>();
        services.AddSingleton<IAuthService, AuthService>();
        services.AddScoped<IDataService, DataService>();
        return services;
    }

    public static IServiceCollection AddViewModels(this IServiceCollection services)
    {
        services.AddTransient<MainViewModel>();
        services.AddTransient<SettingsViewModel>();
        services.AddTransient<ProfileViewModel>();
        return services;
    }
}

// Usage
builder.Services.AddAppServices().AddViewModels();
```

## MVVM with CommunityToolkit.Mvvm

### Installation

```xml
<PackageReference Include="CommunityToolkit.Mvvm" Version="8.*" />
```

### Observable ViewModel

```csharp
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;

public partial class MainViewModel : ObservableObject
{
    private readonly IDataService _dataService;

    [ObservableProperty]
    private string _title = "Home";

    [ObservableProperty]
    [NotifyPropertyChangedFor(nameof(FullName))]
    private string _firstName = "";

    [ObservableProperty]
    [NotifyPropertyChangedFor(nameof(FullName))]
    private string _lastName = "";

    [ObservableProperty]
    [NotifyCanExecuteChangedFor(nameof(SaveCommand))]
    private bool _isValid;

    public string FullName => $"{FirstName} {LastName}";

    public MainViewModel(IDataService dataService)
    {
        _dataService = dataService;
    }

    [RelayCommand]
    private async Task LoadDataAsync()
    {
        var data = await _dataService.GetDataAsync();
        Title = data.Title;
    }

    [RelayCommand(CanExecute = nameof(CanSave))]
    private async Task SaveAsync()
    {
        await _dataService.SaveAsync(new Data { Title = Title });
    }

    private bool CanSave() => IsValid;
}
```

### ViewModel in Blazor Component

```razor
@inject MainViewModel ViewModel
@implements IDisposable

<h1>@ViewModel.Title</h1>

<input @bind="ViewModel.FirstName" />
<input @bind="ViewModel.LastName" />
<p>Full Name: @ViewModel.FullName</p>

<button @onclick="ViewModel.LoadDataCommand.ExecuteAsync"
        disabled="@ViewModel.LoadDataCommand.IsRunning">
    @(ViewModel.LoadDataCommand.IsRunning ? "Loading..." : "Load")
</button>

@code {
    protected override void OnInitialized()
    {
        ViewModel.PropertyChanged += OnViewModelChanged;
    }

    private void OnViewModelChanged(object? sender, PropertyChangedEventArgs e)
    {
        InvokeAsync(StateHasChanged);
    }

    public void Dispose()
    {
        ViewModel.PropertyChanged -= OnViewModelChanged;
    }
}
```

## Component State Patterns

### Local State

```razor
@code {
    private List<Item> items = new();
    private bool isLoading = true;
    private string? errorMessage;

    protected override async Task OnInitializedAsync()
    {
        try
        {
            items = await DataService.GetItemsAsync();
        }
        catch (Exception ex)
        {
            errorMessage = ex.Message;
        }
        finally
        {
            isLoading = false;
        }
    }
}
```

### Cascading State

```razor
@* AppState.razor - State provider *@
<CascadingValue Value="this">
    @ChildContent
</CascadingValue>

@code {
    [Parameter] public RenderFragment? ChildContent { get; set; }

    public User? CurrentUser { get; private set; }
    public bool IsDarkMode { get; private set; }

    public event Action? OnChange;

    public void SetUser(User user)
    {
        CurrentUser = user;
        NotifyStateChanged();
    }

    public void ToggleDarkMode()
    {
        IsDarkMode = !IsDarkMode;
        NotifyStateChanged();
    }

    private void NotifyStateChanged() => OnChange?.Invoke();
}

@* Usage in child component *@
@code {
    [CascadingParameter] public AppState AppState { get; set; } = default!;

    protected override void OnInitialized()
    {
        AppState.OnChange += StateHasChanged;
    }
}
```

### State Container Service

```csharp
public class AppStateService
{
    public User? CurrentUser { get; private set; }
    public bool IsAuthenticated => CurrentUser is not null;

    public event Action? OnChange;

    public void SetUser(User? user)
    {
        CurrentUser = user;
        NotifyStateChanged();
    }

    public void ClearUser()
    {
        CurrentUser = null;
        NotifyStateChanged();
    }

    private void NotifyStateChanged() => OnChange?.Invoke();
}

// Registration
builder.Services.AddSingleton<AppStateService>();

// In component
@inject AppStateService AppState
@implements IDisposable

@code {
    protected override void OnInitialized()
    {
        AppState.OnChange += HandleStateChange;
    }

    private async void HandleStateChange()
    {
        await InvokeAsync(StateHasChanged);
    }

    public void Dispose()
    {
        AppState.OnChange -= HandleStateChange;
    }
}
```

## Persistent State

### Preferences (Simple Key-Value)

```csharp
public class SettingsService : ISettingsService
{
    private readonly IPreferences _preferences;

    public SettingsService(IPreferences preferences)
    {
        _preferences = preferences;
    }

    public bool IsDarkMode
    {
        get => _preferences.Get("dark_mode", false);
        set => _preferences.Set("dark_mode", value);
    }

    public string? UserId
    {
        get => _preferences.Get<string?>("user_id", null);
        set => _preferences.Set("user_id", value);
    }

    public void ClearAll() => _preferences.Clear();
}
```

### Secure Storage (Sensitive Data)

```csharp
public class AuthTokenService
{
    private const string TokenKey = "auth_token";
    private const string RefreshTokenKey = "refresh_token";

    public async Task SaveTokensAsync(string token, string refreshToken)
    {
        await SecureStorage.Default.SetAsync(TokenKey, token);
        await SecureStorage.Default.SetAsync(RefreshTokenKey, refreshToken);
    }

    public async Task<(string? Token, string? RefreshToken)> GetTokensAsync()
    {
        var token = await SecureStorage.Default.GetAsync(TokenKey);
        var refresh = await SecureStorage.Default.GetAsync(RefreshTokenKey);
        return (token, refresh);
    }

    public void ClearTokens()
    {
        SecureStorage.Default.Remove(TokenKey);
        SecureStorage.Default.Remove(RefreshTokenKey);
    }
}
```

### File-Based State

```csharp
public class JsonStateService<T> where T : class, new()
{
    private readonly string _filePath;
    private readonly JsonSerializerOptions _options = new()
    {
        WriteIndented = true
    };

    public JsonStateService(string fileName)
    {
        _filePath = Path.Combine(FileSystem.AppDataDirectory, fileName);
    }

    public async Task<T> LoadAsync()
    {
        if (!File.Exists(_filePath))
            return new T();

        var json = await File.ReadAllTextAsync(_filePath);
        return JsonSerializer.Deserialize<T>(json, _options) ?? new T();
    }

    public async Task SaveAsync(T state)
    {
        var json = JsonSerializer.Serialize(state, _options);
        await File.WriteAllTextAsync(_filePath, json);
    }
}
```

## INotifyPropertyChanged Base Class

```csharp
public abstract class ObservableBase : INotifyPropertyChanged
{
    public event PropertyChangedEventHandler? PropertyChanged;

    protected virtual void OnPropertyChanged([CallerMemberName] string? propertyName = null)
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }

    protected bool SetProperty<T>(ref T field, T value, [CallerMemberName] string? propertyName = null)
    {
        if (EqualityComparer<T>.Default.Equals(field, value))
            return false;

        field = value;
        OnPropertyChanged(propertyName);
        return true;
    }
}

// Usage
public class UserSettings : ObservableBase
{
    private bool _isDarkMode;
    public bool IsDarkMode
    {
        get => _isDarkMode;
        set => SetProperty(ref _isDarkMode, value);
    }

    private string _language = "en";
    public string Language
    {
        get => _language;
        set => SetProperty(ref _language, value);
    }
}
```

## State Management Decision Guide

| Scenario | Recommended Approach |
|----------|---------------------|
| Simple UI state | Component `@code` block |
| Cross-component state | Cascading parameters or state service |
| Complex business logic | MVVM with ViewModel |
| User preferences | IPreferences service |
| Authentication tokens | SecureStorage |
| Offline data | SQLite or file-based storage |
| Real-time updates | State service with events |
