# Platform Integration

## Device Information

### DeviceInfo API

```csharp
// Access device information
var model = DeviceInfo.Current.Model;           // "iPhone 15 Pro"
var manufacturer = DeviceInfo.Current.Manufacturer; // "Apple"
var name = DeviceInfo.Current.Name;             // User's device name
var version = DeviceInfo.Current.VersionString; // "17.0"
var platform = DeviceInfo.Current.Platform;     // iOS, Android, WinUI, macOS
var idiom = DeviceInfo.Current.Idiom;           // Phone, Tablet, Desktop, Watch
var deviceType = DeviceInfo.Current.DeviceType; // Physical, Virtual

// In Blazor component
@inject IDeviceInfo DeviceInfo

@if (DeviceInfo.Idiom == DeviceIdiom.Phone)
{
    <MobileLayout />
}
```

### Platform Checks

```csharp
// Runtime checks
if (DeviceInfo.Current.Platform == DevicePlatform.Android) { }
if (DeviceInfo.Current.Platform == DevicePlatform.iOS) { }
if (DeviceInfo.Current.Platform == DevicePlatform.WinUI) { }
if (DeviceInfo.Current.Platform == DevicePlatform.MacCatalyst) { }

// Compile-time checks (in .cs files)
#if ANDROID
    // Android-only code
#elif IOS
    // iOS-only code
#elif MACCATALYST
    // macOS-only code
#elif WINDOWS
    // Windows-only code
#endif
```

## Permissions

### Requesting Permissions

```csharp
public async Task<bool> RequestCameraPermissionAsync()
{
    var status = await Permissions.CheckStatusAsync<Permissions.Camera>();

    if (status == PermissionStatus.Granted)
        return true;

    if (status == PermissionStatus.Denied && DeviceInfo.Platform == DevicePlatform.iOS)
    {
        // iOS: Permission permanently denied, open settings
        return false;
    }

    status = await Permissions.RequestAsync<Permissions.Camera>();
    return status == PermissionStatus.Granted;
}
```

### Common Permissions

| Permission | Description |
|------------|-------------|
| `Permissions.Camera` | Camera access |
| `Permissions.Microphone` | Microphone access |
| `Permissions.LocationWhenInUse` | Location while app is active |
| `Permissions.LocationAlways` | Background location |
| `Permissions.Photos` | Photo library |
| `Permissions.StorageRead` | Read external storage (Android) |
| `Permissions.StorageWrite` | Write external storage (Android) |
| `Permissions.Notifications` | Push notifications |

### Permission Service Pattern

```csharp
public interface IPermissionService
{
    Task<bool> RequestCameraAsync();
    Task<bool> RequestLocationAsync();
}

public class PermissionService : IPermissionService
{
    public async Task<bool> RequestCameraAsync()
    {
        var status = await Permissions.RequestAsync<Permissions.Camera>();
        return status == PermissionStatus.Granted;
    }

    public async Task<bool> RequestLocationAsync()
    {
        var status = await Permissions.RequestAsync<Permissions.LocationWhenInUse>();
        return status == PermissionStatus.Granted;
    }
}

// Register in MauiProgram.cs
builder.Services.AddSingleton<IPermissionService, PermissionService>();
```

## Sensors & Device Features

### Geolocation

```csharp
public async Task<Location?> GetCurrentLocationAsync()
{
    try
    {
        var request = new GeolocationRequest(GeolocationAccuracy.Medium, TimeSpan.FromSeconds(10));
        var location = await Geolocation.Default.GetLocationAsync(request);
        return location;
    }
    catch (FeatureNotSupportedException)
    {
        // Not supported on device
        return null;
    }
    catch (PermissionException)
    {
        // Permission not granted
        return null;
    }
}
```

### Accelerometer

```csharp
@implements IDisposable

@code {
    private Vector3? acceleration;

    protected override void OnInitialized()
    {
        if (Accelerometer.Default.IsSupported)
        {
            Accelerometer.Default.ReadingChanged += OnReadingChanged;
            Accelerometer.Default.Start(SensorSpeed.UI);
        }
    }

    private void OnReadingChanged(object? sender, AccelerometerChangedEventArgs e)
    {
        acceleration = new Vector3(e.Reading.Acceleration.X,
                                   e.Reading.Acceleration.Y,
                                   e.Reading.Acceleration.Z);
        InvokeAsync(StateHasChanged);
    }

    public void Dispose()
    {
        if (Accelerometer.Default.IsSupported)
        {
            Accelerometer.Default.Stop();
            Accelerometer.Default.ReadingChanged -= OnReadingChanged;
        }
    }
}
```

### Connectivity

```csharp
// Check connectivity
var current = Connectivity.Current.NetworkAccess;
bool isConnected = current == NetworkAccess.Internet;

// Monitor changes
Connectivity.Current.ConnectivityChanged += (s, e) =>
{
    var access = e.NetworkAccess;
    var profiles = e.ConnectionProfiles; // WiFi, Cellular, etc.
};

// Connection profiles
var profiles = Connectivity.Current.ConnectionProfiles;
bool hasWifi = profiles.Contains(ConnectionProfile.WiFi);
```

### Battery

```csharp
var level = Battery.Default.ChargeLevel;      // 0.0 to 1.0
var state = Battery.Default.State;            // Charging, Discharging, Full, etc.
var source = Battery.Default.PowerSource;     // Battery, AC, USB

// Monitor changes
Battery.Default.BatteryInfoChanged += (s, e) =>
{
    var level = e.ChargeLevel;
    var state = e.State;
};
```

## Secure Storage

```csharp
// Store securely
await SecureStorage.Default.SetAsync("auth_token", token);

// Retrieve
var token = await SecureStorage.Default.GetAsync("auth_token");

// Remove
SecureStorage.Default.Remove("auth_token");

// Remove all
SecureStorage.Default.RemoveAll();
```

## File Picker

```csharp
public async Task<FileResult?> PickFileAsync()
{
    var result = await FilePicker.Default.PickAsync(new PickOptions
    {
        PickerTitle = "Select a file",
        FileTypes = new FilePickerFileType(new Dictionary<DevicePlatform, IEnumerable<string>>
        {
            { DevicePlatform.iOS, new[] { "public.json", "public.plain-text" } },
            { DevicePlatform.Android, new[] { "application/json", "text/plain" } },
            { DevicePlatform.WinUI, new[] { ".json", ".txt" } },
        })
    });

    return result;
}

// Pick multiple files
var results = await FilePicker.Default.PickMultipleAsync();
```

## MainThread Dispatcher

```csharp
// Execute on UI thread from background
MainThread.BeginInvokeOnMainThread(() =>
{
    // UI update code
    label.Text = "Updated!";
});

// Async version
await MainThread.InvokeOnMainThreadAsync(async () =>
{
    await DoSomethingAsync();
});

// Check if on main thread
if (MainThread.IsMainThread)
{
    // Already on main thread
}
```

## Platform-Specific Services

### Interface Abstraction Pattern

```csharp
// Shared interface
public interface INativeAlert
{
    Task ShowAlertAsync(string title, string message);
}

// Android implementation
#if ANDROID
public class AndroidNativeAlert : INativeAlert
{
    public Task ShowAlertAsync(string title, string message)
    {
        var context = Platform.CurrentActivity;
        new Android.App.AlertDialog.Builder(context)
            .SetTitle(title)
            .SetMessage(message)
            .SetPositiveButton("OK", (s, e) => { })
            .Show();
        return Task.CompletedTask;
    }
}
#endif

// iOS implementation
#if IOS
public class iOSNativeAlert : INativeAlert
{
    public Task ShowAlertAsync(string title, string message)
    {
        var alert = UIKit.UIAlertController.Create(title, message,
            UIKit.UIAlertControllerStyle.Alert);
        alert.AddAction(UIKit.UIAlertAction.Create("OK",
            UIKit.UIAlertActionStyle.Default, null));

        var vc = Platform.GetCurrentUIViewController();
        vc?.PresentViewController(alert, true, null);
        return Task.CompletedTask;
    }
}
#endif

// Registration
#if ANDROID
builder.Services.AddSingleton<INativeAlert, AndroidNativeAlert>();
#elif IOS
builder.Services.AddSingleton<INativeAlert, iOSNativeAlert>();
#endif
```

## App Lifecycle Events

```csharp
// In App.xaml.cs
public partial class App : Application
{
    protected override Window CreateWindow(IActivationState? activationState)
    {
        var window = base.CreateWindow(activationState);

        window.Created += (s, e) => { /* Window created */ };
        window.Activated += (s, e) => { /* App resumed */ };
        window.Deactivated += (s, e) => { /* App backgrounded */ };
        window.Stopped += (s, e) => { /* App stopped */ };
        window.Resumed += (s, e) => { /* App resumed from background */ };
        window.Destroying += (s, e) => { /* Window closing */ };

        return window;
    }
}
```
