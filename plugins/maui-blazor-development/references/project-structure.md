# Project Structure & Setup

## Solution Templates

### MAUI Blazor App (Single Project)

```bash
dotnet new maui-blazor -n MyApp
```

Creates a standalone MAUI Blazor Hybrid app:

```
MyApp/
├── App.xaml(.cs)           # Application entry
├── MauiProgram.cs          # DI & service configuration
├── MainPage.xaml(.cs)      # BlazorWebView host
├── Main.razor              # Root Blazor component
├── Components/
│   └── Pages/              # Razor pages
├── wwwroot/
│   ├── index.html          # Blazor host page
│   ├── css/
│   └── js/
└── Platforms/              # Platform-specific code
    ├── Android/
    ├── iOS/
    ├── MacCatalyst/
    └── Windows/
```

### MAUI Blazor + Web App (Shared UI)

```bash
dotnet new maui-blazor-web -o MyApp -I Server
# Options: Server, WebAssembly, Auto
```

Creates a solution with shared Razor Class Library:

```
MyApp/
├── MyApp.Maui/             # MAUI app
├── MyApp.Web/              # Blazor Web App
├── MyApp.Web.Client/       # (WebAssembly/Auto only)
└── MyApp.Shared/           # Shared RCL
    ├── Components/
    ├── Services/
    └── _Imports.razor
```

## MauiProgram.cs Configuration

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

        // Blazor WebView
        builder.Services.AddMauiBlazorWebView();

#if DEBUG
        builder.Services.AddBlazorWebViewDeveloperTools();
        builder.Logging.AddDebug();
#endif

        // Register services
        RegisterServices(builder.Services);

        return builder.Build();
    }

    private static void RegisterServices(IServiceCollection services)
    {
        // Platform services
        services.AddSingleton<IConnectivity>(Connectivity.Current);
        services.AddSingleton<IGeolocation>(Geolocation.Default);
        services.AddSingleton<IPreferences>(Preferences.Default);

        // App services
        services.AddSingleton<ISettingsService, SettingsService>();
        services.AddScoped<IAuthService, AuthService>();
        services.AddHttpClient<IApiService, ApiService>(client =>
        {
            client.BaseAddress = new Uri("https://api.example.com/");
        });
    }
}
```

## Razor Class Library (RCL) for Sharing

### Creating Shared Components

```csharp
// MyApp.Shared/Services/IFormFactorService.cs
public interface IFormFactorService
{
    string GetFormFactor();
    string GetPlatform();
}

// MyApp.Maui/Services/FormFactorService.cs
public class FormFactorService : IFormFactorService
{
    public string GetFormFactor() =>
        DeviceInfo.Current.Idiom == DeviceIdiom.Phone ? "Mobile" : "Desktop";

    public string GetPlatform() =>
        DeviceInfo.Current.Platform.ToString();
}

// MyApp.Web/Services/FormFactorService.cs
public class FormFactorService : IFormFactorService
{
    public string GetFormFactor() => "Web";
    public string GetPlatform() => "Browser";
}
```

### Conditional Rendering

```razor
@* MyApp.Shared/Components/AdaptiveLayout.razor *@
@inject IFormFactorService FormFactor

@if (FormFactor.GetFormFactor() == "Mobile")
{
    <MobileLayout>@ChildContent</MobileLayout>
}
else
{
    <DesktopLayout>@ChildContent</DesktopLayout>
}

@code {
    [Parameter] public RenderFragment? ChildContent { get; set; }
}
```

## wwwroot Structure

```
wwwroot/
├── index.html              # Host page (required)
├── css/
│   ├── app.css             # App styles
│   └── bootstrap/          # CSS framework
├── js/
│   └── app.js              # Custom JS
└── images/
    └── logo.png
```

### index.html Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My MAUI Blazor App</title>
    <base href="/" />
    <link rel="stylesheet" href="css/bootstrap/bootstrap.min.css" />
    <link rel="stylesheet" href="css/app.css" />
</head>
<body>
    <div id="app">Loading...</div>

    <div id="blazor-error-ui">
        An unhandled error has occurred.
        <a href="" class="reload">Reload</a>
    </div>

    <script src="_framework/blazor.webview.js" autostart="false"></script>
</body>
</html>
```

## Multi-Targeting Configuration

### .csproj Settings

```xml
<Project Sdk="Microsoft.NET.Sdk.Razor">
    <PropertyGroup>
        <TargetFrameworks>net9.0-android;net9.0-ios;net9.0-maccatalyst</TargetFrameworks>
        <TargetFrameworks Condition="$([MSBuild]::IsOSPlatform('windows'))">
            $(TargetFrameworks);net9.0-windows10.0.19041.0
        </TargetFrameworks>
        <OutputType>Exe</OutputType>
        <UseMaui>true</UseMaui>
        <SingleProject>true</SingleProject>
        <EnableDefaultCssItems>false</EnableDefaultCssItems>
    </PropertyGroup>

    <!-- Platform-specific ItemGroups -->
    <ItemGroup Condition="$(TargetFramework.Contains('-android'))">
        <AndroidResource Include="Platforms\Android\Resources\**" />
    </ItemGroup>
</Project>
```

### Platform-Specific Files

```
Platforms/
├── Android/
│   ├── AndroidManifest.xml
│   ├── MainActivity.cs
│   ├── MainApplication.cs
│   └── Resources/
├── iOS/
│   ├── Info.plist
│   ├── AppDelegate.cs
│   └── Program.cs
├── MacCatalyst/
│   ├── Info.plist
│   └── AppDelegate.cs
└── Windows/
    ├── Package.appxmanifest
    └── App.xaml(.cs)
```

## Render Mode Configuration (MAUI + Web)

### InteractiveRenderSettings for RCL

```csharp
// MyApp.Shared/InteractiveRenderSettings.cs
using Microsoft.AspNetCore.Components;
using Microsoft.AspNetCore.Components.Web;

public static class InteractiveRenderSettings
{
    public static IComponentRenderMode? InteractiveServer { get; set; } =
        RenderMode.InteractiveServer;

    public static IComponentRenderMode? InteractiveAuto { get; set; } =
        RenderMode.InteractiveAuto;

    public static IComponentRenderMode? InteractiveWebAssembly { get; set; } =
        RenderMode.InteractiveWebAssembly;

    public static void ConfigureBlazorHybridRenderModes()
    {
        // MAUI apps are always interactive, no render mode needed
        InteractiveServer = null;
        InteractiveAuto = null;
        InteractiveWebAssembly = null;
    }
}

// Call in MauiProgram.cs
InteractiveRenderSettings.ConfigureBlazorHybridRenderModes();
```
