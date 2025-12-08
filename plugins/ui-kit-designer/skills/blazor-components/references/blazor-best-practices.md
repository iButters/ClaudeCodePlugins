# Blazor Component Best Practices Reference

This reference documents all best practices, patterns, and conventions for creating premium Blazor components in a Razor Class Library.

---

## Table of Contents

1. [Project Structure](#project-structure)
2. [Component Architecture](#component-architecture)
3. [File Separation](#file-separation)
4. [Naming Conventions](#naming-conventions)
5. [Parameters & Events](#parameters--events)
6. [CSS Isolation](#css-isolation)
7. [Accessibility](#accessibility)
8. [Performance](#performance)
9. [Testing](#testing)
10. [Documentation](#documentation)

---

## Project Structure

### Atomic Design Organization

```
ProjectName.Components/
├── ProjectName.Components.csproj
├── _Imports.razor                    # Global usings
├── CssBuilder.cs                     # CSS class builder utility
│
├── wwwroot/                          # Static assets
│   └── css/
│       ├── variables.css             # Design tokens
│       └── base.css                  # Reset & base styles
│
├── Components/                       # All components
│   ├── Atoms/                        # Basic building blocks
│   │   ├── Button/
│   │   │   ├── Button.razor          # Markup only
│   │   │   ├── Button.razor.cs       # Logic (CodeBehind)
│   │   │   └── Button.razor.css      # Scoped styles
│   │   ├── Input/
│   │   ├── Badge/
│   │   └── ...
│   │
│   ├── Molecules/                    # Combinations of atoms
│   │   ├── Card/
│   │   ├── ListItem/
│   │   └── ...
│   │
│   ├── Organisms/                    # Complex UI sections
│   │   ├── Header/
│   │   ├── Modal/
│   │   └── ...
│   │
│   └── Templates/                    # Page layouts
│       ├── MainLayout/
│       └── AuthLayout/
│
├── Pages/                            # Full page components
├── Services/                         # Component services
├── Models/                           # Component models/enums
└── Extensions/
    └── ServiceCollectionExtensions.cs
```

### Why This Structure?

1. **Atomic Design** - Predictable component organization
2. **Colocated Files** - Related files in same folder
3. **Clear Separation** - Components, services, models separate
4. **Scalable** - Easy to add new components
5. **Discoverable** - Developers find components quickly

---

## Component Architecture

### Atomic Design Principles

#### Atoms
Smallest building blocks that can't be broken down further.

```
Button, Input, Icon, Badge, Avatar, Checkbox, Radio, Spinner, Skeleton
```

#### Molecules
Combinations of atoms that form functional units.

```
Card = Container + Content slots
SearchBar = Input + Button + Icon
FormField = Label + Input + Error message
ListItem = Avatar + Text + Action
Toggle = Label + Switch atom
```

#### Organisms
Complex components made of molecules and atoms.

```
Header = Logo + NavItems + SearchBar + Avatar
Modal = Overlay + Card + Header + Footer
DataTable = Header row + Data rows + Pagination
Form = Multiple FormFields + Submit button
```

#### Templates
Page-level layout structures.

```
MainLayout = Header + Content slot + BottomNav
AuthLayout = Centered card + Branding
DashboardLayout = Sidebar + Header + Content
```

---

## File Separation

### The Three-File Pattern

Every component should have exactly three files:

```
ComponentName/
├── ComponentName.razor       # Markup only
├── ComponentName.razor.cs    # Logic only
└── ComponentName.razor.css   # Styles only
```

### 1. Markup File (.razor)

Contains ONLY HTML/Razor markup. No @code blocks.

```razor
@namespace ProjectName.Components.Atoms

<button @attributes="AdditionalAttributes"
        class="@CssClass"
        type="@Type"
        disabled="@IsDisabled"
        aria-busy="@IsLoading"
        @onclick="HandleClick">
    @if (IsLoading)
    {
        <Spinner Size="SpinnerSize.Small" />
    }
    else
    {
        @if (Icon is not null)
        {
            <span class="btn__icon">@Icon</span>
        }
        <span class="btn__text">@ChildContent</span>
    }
</button>
```

### 2. CodeBehind File (.razor.cs)

Contains ALL logic, parameters, and methods with XML documentation.

### 3. Scoped CSS File (.razor.css)

Contains ONLY styles for this component using BEM naming.

---

## Naming Conventions

### Files

| Type | Convention | Example |
|------|-----------|---------|
| Component Folder | PascalCase | `Button/`, `TodoItem/` |
| Markup | PascalCase.razor | `Button.razor` |
| CodeBehind | PascalCase.razor.cs | `Button.razor.cs` |
| Scoped CSS | PascalCase.razor.css | `Button.razor.css` |
| Service Interface | IPascalCase | `IThemeService.cs` |
| Service Implementation | PascalCase | `ThemeService.cs` |
| Enum | PascalCase | `ButtonVariant.cs` |

### CSS Classes (BEM)

```css
/* Block */
.card { }

/* Element (double underscore) */
.card__header { }
.card__body { }
.card__footer { }

/* Modifier (double dash) */
.card--elevated { }
.card--clickable { }
.card--highlighted { }

/* Combined */
.card__header--centered { }
```

### C# Code

| Type | Convention | Example |
|------|-----------|---------|
| Class | PascalCase | `Button`, `TodoItem` |
| Interface | IPascalCase | `IThemeService` |
| Parameter | PascalCase | `ButtonVariant` |
| Private field | _camelCase | `_isLoading` |
| Method | PascalCase | `HandleClick` |
| Event | OnPascalCase | `OnClick`, `OnChange` |
| Enum | PascalCase | `ButtonVariant.Primary` |

---

## Parameters & Events

### Parameter Best Practices

```csharp
public partial class Button : ComponentBase
{
    // 1. Group parameters logically with regions
    #region Appearance Parameters

    /// <summary>
    /// Always add XML documentation
    /// </summary>
    [Parameter]
    public ButtonVariant Variant { get; set; } = ButtonVariant.Primary;

    #endregion

    #region Behavior Parameters

    [Parameter]
    public bool IsDisabled { get; set; }

    [Parameter]
    public bool IsLoading { get; set; }

    #endregion

    #region Content Parameters

    [Parameter]
    public RenderFragment? ChildContent { get; set; }

    [Parameter]
    public RenderFragment? Icon { get; set; }

    #endregion

    #region Event Parameters

    [Parameter]
    public EventCallback<MouseEventArgs> OnClick { get; set; }

    #endregion

    // 2. Always capture unmatched values for flexibility
    [Parameter(CaptureUnmatchedValues = true)]
    public Dictionary<string, object>? AdditionalAttributes { get; set; }
}
```

### Two-Way Binding

```csharp
// For two-way binding, provide both Value and ValueChanged
[Parameter]
public string Value { get; set; } = string.Empty;

[Parameter]
public EventCallback<string> ValueChanged { get; set; }

// Use in component:
private async Task HandleInput(ChangeEventArgs e)
{
    Value = e.Value?.ToString() ?? string.Empty;
    await ValueChanged.InvokeAsync(Value);
}
```

### Event Callbacks

```csharp
// Simple event
[Parameter]
public EventCallback OnClick { get; set; }

// Event with data
[Parameter]
public EventCallback<MouseEventArgs> OnClick { get; set; }

// Event with custom data
[Parameter]
public EventCallback<TodoItem> OnItemSelected { get; set; }

// Always check HasDelegate before invoking
private async Task HandleClick(MouseEventArgs args)
{
    if (OnClick.HasDelegate)
    {
        await OnClick.InvokeAsync(args);
    }
}
```

---

## CSS Isolation

### How It Works

Blazor automatically scopes CSS by adding unique attributes:

```html
<!-- Generated HTML -->
<button b-abc123 class="btn btn--primary">Click</button>
```

```css
/* Generated CSS */
.btn[b-abc123] { ... }
```

### Best Practices

1. **Always use scoped CSS for components**
2. **Use CSS variables for theming**
3. **Never use `!important`**
4. **Use `::deep` sparingly**

### Using ::deep for Child Components

```css
/* Affects child components */
::deep .child-component {
    color: red;
}

/* Better: Target specific children */
.parent ::deep .child__element {
    color: red;
}
```

### Global Styles in Variables

```css
/* wwwroot/css/variables.css - Global */
:root {
    --primary: #6366F1;
    --radius-md: 0.75rem;
}

/* Component.razor.css - Uses variables */
.component {
    color: var(--primary);
    border-radius: var(--radius-md);
}
```

---

## Accessibility

### Required Attributes

```razor
<!-- Interactive elements need proper roles -->
<div role="button"
     tabindex="0"
     @onclick="HandleClick"
     @onkeydown="HandleKeyDown">

<!-- Forms need labels -->
<label for="@InputId">@Label</label>
<input id="@InputId"
       aria-describedby="@ErrorId"
       aria-invalid="@HasError" />
<span id="@ErrorId" role="alert">@ErrorMessage</span>

<!-- Loading states -->
<button aria-busy="@IsLoading"
        aria-disabled="@IsDisabled">

<!-- Icons need descriptions -->
<span aria-hidden="true">🎉</span>
<span class="sr-only">Celebration</span>
```

### Screen Reader Only Class

```css
/* Add to base.css */
.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
}
```

### Keyboard Navigation

```csharp
private void HandleKeyDown(KeyboardEventArgs e)
{
    switch (e.Key)
    {
        case "Enter":
        case " ":
            HandleClick();
            break;
        case "Escape":
            HandleClose();
            break;
    }
}
```

### Focus Management

```csharp
private ElementReference _inputRef;

protected override async Task OnAfterRenderAsync(bool firstRender)
{
    if (firstRender && AutoFocus)
    {
        await _inputRef.FocusAsync();
    }
}
```

---

## Performance

### Minimize Re-renders

```csharp
// Use ShouldRender to skip unnecessary renders
protected override bool ShouldRender()
{
    return _hasChanged;
}

// Use StateHasChanged sparingly
private void UpdateValue(string value)
{
    _value = value;
    // Only call if truly needed
    StateHasChanged();
}
```

### Virtualization for Lists

```razor
@* Use Virtualize for long lists *@
<Virtualize Items="@Items" Context="item">
    <TodoItem Task="@item" />
</Virtualize>
```

### Debounce Input

```csharp
private System.Timers.Timer? _debounceTimer;
private string _searchValue = string.Empty;

private void HandleSearchInput(ChangeEventArgs e)
{
    _searchValue = e.Value?.ToString() ?? string.Empty;

    _debounceTimer?.Stop();
    _debounceTimer = new System.Timers.Timer(300);
    _debounceTimer.Elapsed += async (s, e) =>
    {
        await InvokeAsync(async () =>
        {
            await OnSearch.InvokeAsync(_searchValue);
            StateHasChanged();
        });
    };
    _debounceTimer.AutoReset = false;
    _debounceTimer.Start();
}

public void Dispose()
{
    _debounceTimer?.Dispose();
}
```

### Lazy Loading

```razor
@* Only render expensive components when visible *@
@if (IsVisible)
{
    <ExpensiveChart Data="@Data" />
}
```

---

## Testing

### bUnit Test Setup

```csharp
public class ButtonTests : TestContext
{
    [Fact]
    public void Button_RendersCorrectly()
    {
        // Arrange & Act
        var cut = RenderComponent<Button>(parameters => parameters
            .Add(p => p.Variant, ButtonVariant.Primary)
            .AddChildContent("Click Me"));

        // Assert
        cut.Find("button").ClassList.Should().Contain("btn--primary");
        cut.Find(".btn__text").TextContent.Should().Be("Click Me");
    }

    [Fact]
    public void Button_DisabledState_PreventClick()
    {
        // Arrange
        var clicked = false;
        var cut = RenderComponent<Button>(parameters => parameters
            .Add(p => p.IsDisabled, true)
            .Add(p => p.OnClick, () => clicked = true));

        // Act
        cut.Find("button").Click();

        // Assert
        clicked.Should().BeFalse();
    }

    [Fact]
    public void Button_Click_InvokesCallback()
    {
        // Arrange
        var clicked = false;
        var cut = RenderComponent<Button>(parameters => parameters
            .Add(p => p.OnClick, () => clicked = true));

        // Act
        cut.Find("button").Click();

        // Assert
        clicked.Should().BeTrue();
    }
}
```

### Test Categories

```csharp
// 1. Rendering tests
[Fact] public void Component_RendersWithDefaults() { }
[Fact] public void Component_RendersAllVariants() { }
[Fact] public void Component_RendersChildContent() { }

// 2. Interaction tests
[Fact] public void Component_HandleClick() { }
[Fact] public void Component_HandleKeyboard() { }
[Fact] public void Component_HandleFocus() { }

// 3. State tests
[Fact] public void Component_DisabledState() { }
[Fact] public void Component_LoadingState() { }
[Fact] public void Component_ErrorState() { }

// 4. Accessibility tests
[Fact] public void Component_HasAriaLabels() { }
[Fact] public void Component_KeyboardNavigable() { }
```

---

## Documentation

### XML Documentation

```csharp
/// <summary>
/// A versatile button component supporting multiple variants and states.
/// </summary>
/// <remarks>
/// The button component follows the design system guidelines and supports
/// primary, secondary, ghost, and danger variants.
/// </remarks>
/// <example>
/// Basic usage:
/// <code>
/// &lt;Button OnClick="HandleClick"&gt;Click Me&lt;/Button&gt;
/// </code>
///
/// With variant:
/// <code>
/// &lt;Button Variant="ButtonVariant.Secondary"&gt;Secondary&lt;/Button&gt;
/// </code>
/// </example>
public partial class Button : ComponentBase
```

---

## Quick Reference Checklist

### New Component Checklist

- [ ] Create folder `Components/[Category]/[Name]/`
- [ ] Create `[Name].razor` with clean markup
- [ ] Create `[Name].razor.cs` with CodeBehind
- [ ] Create `[Name].razor.css` with scoped styles
- [ ] Add XML documentation to class
- [ ] Document all parameters
- [ ] Add `[CaptureUnmatchedValues]` for flexibility
- [ ] Use `CssBuilder` for class generation
- [ ] Add accessibility attributes
- [ ] Add keyboard event handlers
- [ ] Test with bUnit
- [ ] Export in `_Imports.razor`
