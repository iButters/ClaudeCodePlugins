# UI Kit Designer - GitHub Copilot Chat Edition

Create beautiful, interactive UI designs and convert them to production-ready Blazor components.

## 📋 Overview

This is the GitHub Copilot Chat version of the UI Kit Designer plugin. It enables rapid UI prototyping and component generation:
- Design comprehensive UI kits with complete design systems
- Create reusable component libraries
- Design all screens with realistic content
- Convert designs to production-ready Blazor components
- Follow accessibility and responsive design best practices

## 🎨 Features

### UI Kit Design
- **Design System Creation**: Colors, typography, spacing, effects
- **Component Library**: Buttons, inputs, cards, navigation, modals
- **Screen Design**: All app screens in mobile frames
- **Dark Mode Support**: Built-in glassmorphism aesthetics
- **Iterative Refinement**: Update designs based on feedback

### Blazor Component Generation
- **Three-File Pattern**: `.razor`, `.razor.cs`, `.razor.css`
- **Atomic Design**: Atoms → Molecules → Organisms
- **CSS Isolation**: Scoped component styles
- **Full Documentation**: XML docs on all members
- **Accessibility**: WCAG 2.1 AA compliance

## 🚀 Installation

### Copy to Your Project

```bash
cp -r .github /path/to/your/project/
```

The instructions automatically activate when working with:
- HTML files (`.html`)
- Razor files (`.razor`)
- CSS files (`.css`)

## 💡 Usage

### Quick Start - Natural Language

**Just ask**:
```
Create a UI kit for a task management app with dark mode
Design a fitness tracking app with workout logging and stats
Show me what my meditation app could look like
Add a settings screen to my UI kit
The buttons need more rounded corners
```

### Specialized Chat Mode

For intensive design work:
```
@workspace use chatmode ui-kit-designer
```

This mode guides you through:
1. Design discovery (purpose, users, features)
2. Information architecture (screens, flows)
3. Design system creation (colors, typography)
4. Component library design
5. Screen design with realistic content
6. Iterative refinement

## 🎯 What You Get

### Complete UI Kit HTML File

A single, self-contained HTML file with:

**1. Design System Section**
- Color palette with all semantic colors
- Typography scale and weights
- Spacing system
- Effects (shadows, borders, radius)

**2. Component Library**
- Buttons (all variants and states)
- Inputs (default, error, success, disabled)
- Cards (header, body, footer)
- Navigation components
- Modals and dialogs
- All other UI elements

**3. Application Screens**
- All screens in mobile frames
- Realistic content and data
- Interactive states shown
- Loading and empty states
- Error handling

## 🏗️ Design System Example

### Color Palette (Dark Mode)

```css
:root {
    /* Brand */
    --primary: #6366f1;
    --secondary: #8b5cf6;
    --accent: #ec4899;
    
    /* Semantic */
    --success: #10b981;
    --warning: #f59e0b;
    --error: #ef4444;
    
    /* Surface */
    --surface: rgba(30, 30, 46, 0.8);
    --background: #1a1a2e;
    
    /* Text */
    --text-primary: #ffffff;
    --text-secondary: #a1a1aa;
    
    /* Effects */
    --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
    --radius-md: 0.5rem;
}
```

### Typography Scale

```css
:root {
    --text-xs: 0.75rem;    /* 12px */
    --text-sm: 0.875rem;   /* 14px */
    --text-base: 1rem;     /* 16px */
    --text-lg: 1.125rem;   /* 18px */
    --text-xl: 1.25rem;    /* 20px */
    --text-2xl: 1.5rem;    /* 24px */
    --text-3xl: 1.875rem;  /* 30px */
}
```

## 🧩 Component Examples

### Button Component

**All variants**:
```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-outline">Outline</button>
<button class="btn btn-ghost">Ghost</button>
<button class="btn btn-danger">Delete</button>
```

**All states**:
```html
<button class="btn btn-primary">Default</button>
<button class="btn btn-primary" disabled>Disabled</button>
<button class="btn btn-primary btn-loading">Loading</button>
```

**All sizes**:
```html
<button class="btn btn-primary btn-sm">Small</button>
<button class="btn btn-primary btn-md">Medium</button>
<button class="btn btn-primary btn-lg">Large</button>
```

### Input Component

```html
<!-- Default -->
<div class="input-group">
    <label class="input-label">Email</label>
    <input type="email" class="input" placeholder="you@example.com">
</div>

<!-- Error State -->
<div class="input-group input-error">
    <label class="input-label">Email</label>
    <input type="email" class="input" value="invalid">
    <span class="input-error-message">Invalid email address</span>
</div>

<!-- Success State -->
<div class="input-group input-success">
    <label class="input-label">Email</label>
    <input type="email" class="input" value="user@example.com">
    <span class="input-success-message">✓ Email is valid</span>
</div>
```

### Card Component

```html
<div class="card">
    <div class="card-header">
        <h3>Card Title</h3>
        <button class="btn btn-ghost btn-sm">⋮</button>
    </div>
    <div class="card-body">
        <p>Card content with description and details.</p>
    </div>
    <div class="card-footer">
        <button class="btn btn-outline btn-sm">Cancel</button>
        <button class="btn btn-primary btn-sm">Save</button>
    </div>
</div>
```

## 📱 Screen Design

### Essential Screens

Every app should include:

**Authentication**:
- Login, Signup, Password Reset, Email Verification

**Core Functionality**:
- Home/Dashboard (overview and quick actions)
- List View (browse, search, filter)
- Detail View (full information)
- Create/Edit Form (data entry)

**User Management**:
- Profile, Settings, Preferences

**Edge Cases**:
- Empty State (no data yet)
- Loading State (fetching data)
- Error State (something went wrong)
- Success State (action completed)

### Mobile Frame Example

```html
<div class="phone-frame">
    <div class="screen">
        <header class="screen-header">
            <button class="icon-btn">←</button>
            <h1>Screen Title</h1>
            <button class="icon-btn">⋮</button>
        </header>
        
        <main class="screen-content">
            <!-- Screen content -->
        </main>
        
        <nav class="bottom-nav">
            <!-- Bottom navigation tabs -->
        </nav>
    </div>
</div>
```

## 🔄 Blazor Component Generation

### Component Structure

```
Components/
├── Atoms/              (Basic elements)
│   ├── Button.razor
│   ├── Button.razor.cs
│   └── Button.razor.css
├── Molecules/          (Simple combinations)
│   ├── InputField.razor
│   ├── InputField.razor.cs
│   └── InputField.razor.css
└── Organisms/          (Complex sections)
    ├── LoginForm.razor
    ├── LoginForm.razor.cs
    └── LoginForm.razor.css
```

### Example: Button Component

**Button.razor**:
```razor
@namespace MyApp.Components.Atoms

<button class="@CssClass" 
        type="@Type"
        disabled="@IsDisabled"
        @onclick="OnClick">
    @if (IsLoading)
    {
        <span class="spinner"></span>
    }
    @ChildContent
</button>
```

**Button.razor.cs**:
```csharp
namespace MyApp.Components.Atoms;

/// <summary>
/// A reusable button component with variants and states.
/// </summary>
public partial class Button
{
    [Parameter]
    public RenderFragment? ChildContent { get; set; }
    
    [Parameter]
    public ButtonVariant Variant { get; set; } = ButtonVariant.Primary;
    
    [Parameter]
    public ButtonSize Size { get; set; } = ButtonSize.Medium;
    
    [Parameter]
    public bool IsDisabled { get; set; }
    
    [Parameter]
    public bool IsLoading { get; set; }
    
    [Parameter]
    public EventCallback<MouseEventArgs> OnClick { get; set; }
    
    private string CssClass => new CssBuilder("btn")
        .AddClass($"btn-{Variant.ToString().ToLower()}")
        .AddClass($"btn-{Size.ToString().ToLower()}")
        .AddClass("btn-loading", IsLoading)
        .Build();
}
```

**Button.razor.css**:
```css
.btn {
    display: inline-flex;
    align-items: center;
    gap: var(--space-2);
    padding: var(--space-3) var(--space-4);
    border: none;
    border-radius: var(--radius-md);
    font-weight: var(--font-medium);
    cursor: pointer;
    transition: all 0.2s;
}

.btn-primary {
    background: var(--primary);
    color: white;
}

.btn-primary:hover:not(:disabled) {
    background: var(--primary-hover);
}
```

## 🎨 Usage Scenarios

### Scenario 1: New App Design

**You**: "Create a UI kit for a meditation app with breathing exercises, session tracking, and ambient sounds"

**Copilot** (with UI Kit Designer mode): Will create:
- Complete design system with calming color palette
- Component library (timer, session cards, audio player)
- Screens for home, breathing exercise, session history, sound library
- Dark mode with gradients and glassmorphism
- Realistic content (exercise names, session data, sound titles)

### Scenario 2: Design Iteration

**You**: "The buttons need more padding and the cards should have more rounded corners"

**Copilot**: Will update:
- Design token variables (--btn-padding, --card-radius)
- All affected components automatically inherit changes
- Consistency maintained across all screens

### Scenario 3: Blazor Component Generation

**You**: "Convert this UI kit to Blazor components"

**Copilot**: Will generate:
- Atomic design folder structure
- Three-file pattern for each component
- CSS isolation with design tokens
- Full XML documentation
- Props and EventCallbacks for interactivity
- Accessibility attributes (ARIA labels, keyboard support)

## ♿ Accessibility Features

Always included:
- **Semantic HTML**: Proper heading hierarchy, `<nav>`, `<main>`, `<button>`
- **ARIA Labels**: For icons and buttons without text
- **Focus States**: Visible keyboard navigation indicators
- **Color Contrast**: WCAG AA compliance (4.5:1 for text)
- **Alt Text**: For all images and icons
- **Keyboard Support**: Tab navigation, Enter/Space for actions
- **Screen Reader Support**: Proper roles and labels

## 📱 Responsive Design

Mobile-first approach:
```css
/* Mobile (default) */
.container { padding: 1rem; }

/* Tablet */
@media (min-width: 768px) {
    .container { padding: 2rem; }
}

/* Desktop */
@media (min-width: 1024px) {
    .container { 
        padding: 3rem;
        max-width: 1200px;
        margin: 0 auto;
    }
}
```

## 💡 Pro Tips

1. **Be specific**: "Create a UI kit for [specific app type]"
2. **Mention preferences**: "with dark mode", "minimalist style", "vibrant colors"
3. **Provide context**: "for users aged 18-25", "enterprise SaaS", "consumer mobile app"
4. **Use chat mode**: For complex projects with many screens
5. **Iterate**: Start simple, refine based on what you see
6. **Request Blazor conversion**: After finalizing UI design

## 📁 File Structure

```
.github/
├── copilot-instructions.md              # Main UI design guidance
├── chatmodes/
│   └── ui-kit-designer.md              # Specialized design mode
└── README-COPILOT.md                   # This file
```

## 🆚 Differences from Claude Code Version

| Feature | Claude Code | GitHub Copilot Chat |
|---------|-------------|---------------------|
| **Commands** | `/ui-kit create`, `/ui-kit refine` | Natural language requests |
| **Agents** | Automatic agent triggering | Chat mode activation |
| **File Creation** | Creates HTML files directly | Provides HTML content |
| **Blazor Generation** | Separate command | Request in conversation |
| **Integration** | Claude Code IDE | VS Code, Visual Studio |

## 🚦 Getting Started

1. **Copy files**:
   ```bash
   cp -r .github /path/to/your/project/
   ```

2. **Start designing**:
   ```
   Create a UI kit for my project management app
   ```

3. **Or use chat mode**:
   ```
   @workspace use chatmode ui-kit-designer
   ```

4. **Iterate**:
   ```
   Make the colors more vibrant
   Add a dark mode toggle to settings
   Show me loading states for all screens
   ```

5. **Convert to Blazor**:
   ```
   Generate Blazor components from this UI kit
   ```

## 🐛 Troubleshooting

**Generic designs**:
- Provide more context about the app type and users
- Mention design preferences (modern, minimal, playful)
- Use the ui-kit-designer chat mode

**Missing screens**:
- List specific screens you need: "Include login, dashboard, settings"
- Mention user flows: "Show the checkout process"

**Inconsistent styling**:
- Ask to "update design tokens" rather than individual elements
- Request: "Make all buttons consistent"

**Need component generation**:
- Be explicit: "Generate Blazor components with three-file pattern"
- Specify: "Use atomic design structure"

## 📄 License

MIT License - Same as the original Claude Code plugin

---

**Design Beautiful Interfaces! 🎨✨**
