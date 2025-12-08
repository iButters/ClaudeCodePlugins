---
name: Blazor Components
description: This skill should be used when the user asks to "create Blazor components", "build a Razor Class Library", "implement component patterns", "CSS isolation in Blazor", "Blazor best practices", "three-file pattern", "atomic design for Blazor", "CssBuilder", "scoped CSS", or needs guidance on creating production-ready Blazor components with proper architecture, accessibility, and documentation.
version: 1.0.0
---

# Blazor Component Skill

## Overview

This skill enables expert-level creation of Blazor components following all industry best practices. Components are generated as part of a Razor Class Library (RCL) with proper file separation, CSS isolation, accessibility, and documentation.

## Core Competencies

### 1. Component Architecture
- Atomic design (atoms → molecules → organisms → templates)
- Three-file pattern (markup, CodeBehind, scoped CSS)
- Proper namespace organization
- Clean component composition

### 2. Code Separation
- `.razor` files contain ONLY markup
- `.razor.cs` CodeBehind contains ALL logic
- `.razor.css` scoped styles for component only
- No `@code` blocks in razor files

### 3. CSS Best Practices
- CSS isolation (scoped CSS)
- CSS custom properties for theming
- BEM naming convention
- No `!important` usage

### 4. Accessibility (A11y)
- WCAG 2.1 AA compliance
- Proper ARIA attributes
- Keyboard navigation
- Focus management
- Screen reader support

### 5. Performance
- Minimal re-renders
- Virtualization for lists
- Debounced inputs
- Lazy loading patterns

---

## Component Templates

### Atom Component

```
Component/
├── Component.razor       # Markup only
├── Component.razor.cs    # Full CodeBehind
└── Component.razor.css   # Scoped BEM styles
```

#### Markup Template (.razor)
```razor
@namespace [Namespace].Components.Atoms

<element @attributes="AdditionalAttributes"
         class="@CssClass"
         disabled="@IsDisabled"
         aria-[attribute]="@Value"
         @onclick="HandleClick">
    @ChildContent
</element>
```

#### CodeBehind Template (.razor.cs)
```csharp
using Microsoft.AspNetCore.Components;

namespace [Namespace].Components.Atoms;

/// <summary>
/// [Description of component]
/// </summary>
public partial class [ComponentName] : ComponentBase
{
    #region Parameters
    
    /// <summary>
    /// [Parameter description]
    /// </summary>
    [Parameter]
    public [Type] [Name] { get; set; } = [default];
    
    /// <summary>
    /// The component's child content.
    /// </summary>
    [Parameter]
    public RenderFragment? ChildContent { get; set; }
    
    /// <summary>
    /// Callback when [event description].
    /// </summary>
    [Parameter]
    public EventCallback<[EventArgs]> [OnEvent] { get; set; }
    
    /// <summary>
    /// Additional HTML attributes to apply.
    /// </summary>
    [Parameter(CaptureUnmatchedValues = true)]
    public Dictionary<string, object>? AdditionalAttributes { get; set; }
    
    #endregion
    
    #region Computed Properties
    
    private string CssClass => new CssBuilder("[base-class]")
        .AddClass("[modifier]", [condition])
        .Build();
    
    #endregion
    
    #region Event Handlers
    
    private async Task HandleClick([EventArgs] args)
    {
        if ([OnEvent].HasDelegate)
        {
            await [OnEvent].InvokeAsync(args);
        }
    }
    
    #endregion
}
```

#### CSS Template (.razor.css)
```css
/* Block */
.[component] {
    /* Base styles using CSS variables */
    display: [value];
    font-family: var(--font-family);
    transition: all var(--transition-base);
}

/* Elements */
.[component]__[element] {
    /* Element styles */
}

/* Modifiers */
.[component]--[modifier] {
    /* Variant styles */
}

/* States */
.[component]--disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

.[component]:hover:not(.[component]--disabled) {
    /* Hover styles */
}

.[component]:focus-visible {
    outline: 2px solid var(--primary);
    outline-offset: 2px;
}
```

---

## CssBuilder Utility

Always use `CssBuilder` for dynamic class generation:

```csharp
public sealed class CssBuilder
{
    private readonly List<string> _classes = new();

    public CssBuilder(string? baseClass = null)
    {
        if (!string.IsNullOrWhiteSpace(baseClass))
            _classes.Add(baseClass);
    }

    public CssBuilder AddClass(string? className)
    {
        if (!string.IsNullOrWhiteSpace(className))
            _classes.Add(className);
        return this;
    }

    public CssBuilder AddClass(string? className, bool condition)
    {
        if (condition && !string.IsNullOrWhiteSpace(className))
            _classes.Add(className);
        return this;
    }

    public string Build() => string.Join(" ", _classes);
    public override string ToString() => Build();
}
```

Usage:
```csharp
private string CssClass => new CssBuilder("btn")
    .AddClass($"btn--{Variant.ToString().ToLowerInvariant()}")
    .AddClass($"btn--{Size.ToString().ToLowerInvariant()}")
    .AddClass("btn--loading", IsLoading)
    .AddClass("btn--disabled", IsDisabled)
    .AddClass(AdditionalClass)
    .Build();
```

---

## Standard Enums

### Size
```csharp
public enum Size
{
    Small,
    Medium,
    Large
}
```

### ButtonVariant
```csharp
public enum ButtonVariant
{
    Primary,
    Secondary,
    Ghost,
    Danger,
    Success
}
```

### CardVariant
```csharp
public enum CardVariant
{
    Default,
    Elevated,
    Outlined,
    Featured
}
```

### IconPosition
```csharp
public enum IconPosition
{
    Left,
    Right
}
```

### Position
```csharp
public enum Position
{
    Top,
    Bottom,
    Left,
    Right,
    Center
}
```

---

## Project Structure Reference

```
[ProjectName].Components/
├── [ProjectName].Components.csproj
├── _Imports.razor
├── CssBuilder.cs
│
├── wwwroot/
│   └── css/
│       ├── variables.css
│       └── base.css
│
├── Components/
│   ├── Atoms/
│   │   ├── Button/
│   │   ├── Input/
│   │   ├── Badge/
│   │   ├── Icon/
│   │   ├── Avatar/
│   │   ├── Checkbox/
│   │   ├── ProgressBar/
│   │   └── Spinner/
│   │
│   ├── Molecules/
│   │   ├── Card/
│   │   ├── ListItem/
│   │   ├── SearchBar/
│   │   ├── FormField/
│   │   └── Toggle/
│   │
│   ├── Organisms/
│   │   ├── Header/
│   │   ├── BottomNav/
│   │   ├── Modal/
│   │   ├── BottomSheet/
│   │   └── Toast/
│   │
│   └── Templates/
│       ├── MainLayout/
│       └── AuthLayout/
│
├── Pages/
├── Services/
├── Models/
└── Extensions/
```

---

## Service Pattern

### Interface
```csharp
public interface IThemeService
{
    Theme CurrentTheme { get; }
    event Action<Theme>? ThemeChanged;
    void SetTheme(Theme theme);
    void ToggleTheme();
}
```

### Implementation
```csharp
public class ThemeService : IThemeService
{
    private Theme _currentTheme = Theme.Dark;
    
    public Theme CurrentTheme => _currentTheme;
    public event Action<Theme>? ThemeChanged;
    
    public void SetTheme(Theme theme)
    {
        if (_currentTheme != theme)
        {
            _currentTheme = theme;
            ThemeChanged?.Invoke(theme);
        }
    }
    
    public void ToggleTheme()
    {
        SetTheme(_currentTheme == Theme.Dark ? Theme.Light : Theme.Dark);
    }
}
```

### Registration
```csharp
public static class ServiceCollectionExtensions
{
    public static IServiceCollection Add[ProjectName]Components(
        this IServiceCollection services)
    {
        services.AddScoped<IThemeService, ThemeService>();
        services.AddScoped<IToastService, ToastService>();
        services.AddScoped<IModalService, ModalService>();
        return services;
    }
}
```

---

## Accessibility Checklist

- [ ] Semantic HTML elements
- [ ] `role` attribute where needed
- [ ] `aria-label` for icon-only buttons
- [ ] `aria-labelledby` for form fields
- [ ] `aria-describedby` for help text
- [ ] `aria-invalid` for error states
- [ ] `aria-busy` for loading states
- [ ] `aria-expanded` for collapsibles
- [ ] `aria-hidden` for decorative elements
- [ ] `tabindex` for custom interactive elements
- [ ] Keyboard event handlers (Enter, Space, Escape)
- [ ] Focus management for modals
- [ ] Color contrast 4.5:1 minimum
- [ ] Screen reader only text (`.sr-only`)

---

## Quality Checklist

### Code Quality
- [ ] No `@code` blocks (use CodeBehind)
- [ ] XML documentation on all public members
- [ ] Consistent naming conventions
- [ ] Proper error handling
- [ ] Clean separation of concerns

### Component Quality
- [ ] Three-file pattern
- [ ] CssBuilder for classes
- [ ] CaptureUnmatchedValues
- [ ] EventCallback for events
- [ ] Default parameter values

### CSS Quality
- [ ] BEM naming convention
- [ ] CSS variables for theming
- [ ] No `!important`
- [ ] Responsive styles
- [ ] Animation definitions

### Accessibility
- [ ] All interactive elements accessible
- [ ] Proper ARIA attributes
- [ ] Keyboard navigation
- [ ] Focus visible styles
- [ ] Screen reader support

---

## Related References

For detailed information, consult these reference documents in `references/`:

- [Blazor Best Practices](references/blazor-best-practices.md) - Comprehensive guide to project structure, file separation, naming conventions, parameters, events, CSS isolation, accessibility, performance, and testing
