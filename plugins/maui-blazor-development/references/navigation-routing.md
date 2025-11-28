# Navigation & Routing

## Blazor Routing (Within BlazorWebView)

### Page Routing

```razor
@page "/"
@page "/home"

<h1>Home Page</h1>

@page "/items/{id:int}"
@page "/items/{id:int}/{action?}"

@code {
    [Parameter] public int Id { get; set; }
    [Parameter] public string? Action { get; set; }
}
```

### Route Constraints

| Constraint | Example | Matches |
|------------|---------|---------|
| `int` | `{id:int}` | `123`, `-123` |
| `bool` | `{active:bool}` | `true`, `false` |
| `datetime` | `{date:datetime}` | `2024-01-15` |
| `guid` | `{id:guid}` | `CD2C1638-...` |
| `long` | `{id:long}` | `123456789` |
| `float` | `{price:float}` | `1.23` |

### NavigationManager

```csharp
@inject NavigationManager Navigation

@code {
    private void NavigateToDetails(int id)
    {
        // Navigate within Blazor
        Navigation.NavigateTo($"/details/{id}");

        // With force load (full page reload)
        Navigation.NavigateTo("/other", forceLoad: true);

        // Replace history entry
        Navigation.NavigateTo("/new", replace: true);
    }

    // Get current URI
    private void CheckLocation()
    {
        var uri = Navigation.Uri;              // Full URI
        var baseUri = Navigation.BaseUri;      // Base URI
        var relative = Navigation.ToBaseRelativePath(uri);
    }
}
```

### Navigation Events

```csharp
@implements IDisposable
@inject NavigationManager Navigation

@code {
    protected override void OnInitialized()
    {
        Navigation.LocationChanged += HandleLocationChanged;
    }

    private void HandleLocationChanged(object? sender, LocationChangedEventArgs e)
    {
        var newUri = e.Location;
        var isNavIntercepted = e.IsNavigationIntercepted;
    }

    public void Dispose()
    {
        Navigation.LocationChanged -= HandleLocationChanged;
    }
}
```

### Query Parameters

```csharp
@page "/search"
@inject NavigationManager Navigation

@code {
    [SupplyParameterFromQuery]
    public string? Query { get; set; }

    [SupplyParameterFromQuery(Name = "page")]
    public int PageNumber { get; set; } = 1;

    private void Search(string term, int page)
    {
        // Navigate with query params
        Navigation.NavigateTo($"/search?query={term}&page={page}");
    }
}
```

## MAUI Navigation

### NavigationPage Setup

```csharp
// App.xaml.cs
public App()
{
    InitializeComponent();
    MainPage = new NavigationPage(new MainPage());
}
```

### Page Navigation from Blazor

```csharp
@inject IServiceProvider ServiceProvider

@code {
    private async Task NavigateToSettingsPage()
    {
        var settingsPage = ServiceProvider.GetRequiredService<SettingsPage>();
        var mainPage = Application.Current?.MainPage;

        if (mainPage is NavigationPage navPage)
        {
            await navPage.PushAsync(settingsPage);
        }
    }

    private async Task GoBack()
    {
        var mainPage = Application.Current?.MainPage;
        if (mainPage is NavigationPage navPage)
        {
            await navPage.PopAsync();
        }
    }
}
```

### MAUI Content Page with Blazor

```csharp
// Views/SettingsPage.xaml
<?xml version="1.0" encoding="utf-8" ?>
<ContentPage xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             x:Class="MyApp.Views.SettingsPage"
             Title="Settings">

    <StackLayout>
        <Label Text="Settings" FontSize="24" />
        <Button Text="Close" Clicked="OnCloseClicked" />
    </StackLayout>

</ContentPage>

// Views/SettingsPage.xaml.cs
public partial class SettingsPage : ContentPage
{
    public SettingsPage()
    {
        InitializeComponent();
    }

    private async void OnCloseClicked(object sender, EventArgs e)
    {
        await Navigation.PopAsync();
    }
}
```

## Shell Navigation

### Shell Setup

```xml
<!-- AppShell.xaml -->
<Shell xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
       xmlns:views="clr-namespace:MyApp.Views"
       FlyoutBehavior="Disabled">

    <TabBar>
        <ShellContent Title="Home"
                      Icon="home.png"
                      ContentTemplate="{DataTemplate views:MainPage}" />
        <ShellContent Title="Settings"
                      Icon="settings.png"
                      ContentTemplate="{DataTemplate views:SettingsPage}" />
    </TabBar>

</Shell>
```

### Shell Navigation from Blazor

```csharp
@code {
    private async Task NavigateWithShell()
    {
        // Absolute route
        await Shell.Current.GoToAsync("//settings");

        // Relative route
        await Shell.Current.GoToAsync("details");

        // With parameters
        await Shell.Current.GoToAsync($"details?id={itemId}");

        // Go back
        await Shell.Current.GoToAsync("..");
    }
}
```

### Register Routes

```csharp
// In AppShell.xaml.cs or MauiProgram.cs
Routing.RegisterRoute("details", typeof(DetailsPage));
Routing.RegisterRoute("profile/edit", typeof(EditProfilePage));
```

## BlazorWebView StartPath

### Configure Initial Path

```xml
<!-- MainPage.xaml -->
<BlazorWebView HostPage="wwwroot/index.html"
               StartPath="/dashboard">
    <BlazorWebView.RootComponents>
        <RootComponent Selector="#app" ComponentType="{x:Type local:Main}" />
    </BlazorWebView.RootComponents>
</BlazorWebView>
```

```csharp
// Or in code
public MainPage()
{
    InitializeComponent();
    blazorWebView.StartPath = "/dashboard";
}
```

## URL Loading & External Links

### Handle External URLs

```csharp
// MainPage.xaml.cs
public MainPage()
{
    InitializeComponent();
    blazorWebView.UrlLoading += OnUrlLoading;
}

private void OnUrlLoading(object? sender, UrlLoadingEventArgs e)
{
    // Check if external URL
    if (e.Url.Host != "0.0.0.0")
    {
        // Options:
        // - OpenExternally: System browser
        // - OpenInWebView: Stay in BlazorWebView
        // - CancelLoad: Block navigation

        e.UrlLoadingStrategy = UrlLoadingStrategy.OpenExternally;
    }
}
```

### Open External Browser

```csharp
@code {
    private async Task OpenWebsite()
    {
        await Browser.Default.OpenAsync("https://example.com", BrowserLaunchMode.SystemPreferred);
    }

    private async Task OpenInApp()
    {
        await Browser.Default.OpenAsync("https://example.com", BrowserLaunchMode.External);
    }
}
```

## Deep Linking / App Links

### Android Configuration

```xml
<!-- Platforms/Android/AndroidManifest.xml -->
<activity android:name="MainActivity">
    <intent-filter android:autoVerify="true">
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data android:scheme="https"
              android:host="myapp.example.com"
              android:pathPrefix="/open" />
    </intent-filter>
</activity>
```

### iOS Configuration

```xml
<!-- Platforms/iOS/Info.plist -->
<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>myapp</string>
        </array>
    </dict>
</array>
```

### Handle Deep Links

```csharp
// App.xaml.cs
protected override void OnAppLinkRequestReceived(Uri uri)
{
    base.OnAppLinkRequestReceived(uri);

    // Parse URI and navigate
    if (uri.Host == "myapp.example.com")
    {
        var path = uri.AbsolutePath;
        // Navigate to appropriate page
        Shell.Current.GoToAsync(path);
    }
}
```

## Navigation Service Pattern

```csharp
public interface INavigationService
{
    Task NavigateToAsync(string route);
    Task NavigateToAsync(string route, IDictionary<string, object> parameters);
    Task GoBackAsync();
}

public class NavigationService : INavigationService
{
    public async Task NavigateToAsync(string route)
    {
        await Shell.Current.GoToAsync(route);
    }

    public async Task NavigateToAsync(string route, IDictionary<string, object> parameters)
    {
        await Shell.Current.GoToAsync(route, parameters);
    }

    public async Task GoBackAsync()
    {
        await Shell.Current.GoToAsync("..");
    }
}

// Register
builder.Services.AddSingleton<INavigationService, NavigationService>();
```
