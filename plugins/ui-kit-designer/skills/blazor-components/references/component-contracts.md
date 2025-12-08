# Component Contracts

Component Contracts definieren die Schnittstellen zwischen Blazor-Komponenten. Sie ermöglichen es dem Orchestrator, Subagenten mit den notwendigen Informationen zu versorgen, um korrekt interagierende Komponenten zu generieren.

## Contract Format

### Basis-Struktur

```json
{
  "ComponentName": {
    "namespace": "ProjectName.Components.Category",
    "parameters": [...],
    "events": [...],
    "slots": [...],
    "cssClass": "component-name",
    "variants": [...],
    "sizes": [...],
    "dependencies": [...]
  }
}
```

### Parameter Definition

```json
{
  "name": "ParameterName",
  "type": "string | bool | int | enum | RenderFragment | RenderFragment<T>",
  "default": "defaultValue | null",
  "required": true | false,
  "twoWay": true | false,
  "description": "Parameter description"
}
```

**Beispiele:**

```json
// Einfacher Parameter
{ "name": "Title", "type": "string", "default": null }

// Enum Parameter
{ "name": "Variant", "type": "ButtonVariant", "default": "Primary" }

// Boolean mit Default
{ "name": "Disabled", "type": "bool", "default": false }

// Pflicht-Parameter
{ "name": "ChildContent", "type": "RenderFragment", "required": true }

// Two-Way Binding (für @bind-)
{ "name": "IsOpen", "type": "bool", "twoWay": true, "default": false }

// Generic RenderFragment
{ "name": "ItemTemplate", "type": "RenderFragment<TItem>", "default": null }
```

### Event Definition

```json
{
  "name": "EventName",
  "type": "EventCallback | EventCallback<T>",
  "description": "Event description"
}
```

**Beispiele:**

```json
// Einfaches Event
{ "name": "OnClick", "type": "EventCallback" }

// Event mit Parameter
{ "name": "OnClick", "type": "EventCallback<MouseEventArgs>" }

// Value Changed (für Two-Way Binding)
{ "name": "IsOpenChanged", "type": "EventCallback<bool>" }

// Custom Event
{ "name": "OnItemSelected", "type": "EventCallback<TodoItem>" }
```

### Slot Definition

Slots sind benannte RenderFragments für Content-Projection:

```json
{
  "name": "SlotName",
  "type": "RenderFragment | RenderFragment<T>",
  "description": "Slot description"
}
```

**Beispiele:**

```json
// Standard Content
{ "name": "ChildContent", "type": "RenderFragment" }

// Benannte Slots
{ "name": "Header", "type": "RenderFragment" }
{ "name": "Footer", "type": "RenderFragment" }

// Template Slot
{ "name": "ItemTemplate", "type": "RenderFragment<TItem>" }
```

### CSS Information

```json
{
  "cssClass": "block-name",
  "variants": ["Primary", "Secondary", "Ghost"],
  "sizes": ["Small", "Medium", "Large"],
  "states": ["loading", "disabled", "active"]
}
```

### Dependencies

Liste der Komponenten, die diese Komponente verwendet:

```json
{
  "dependencies": ["Button", "Icon", "Badge"]
}
```

---

## Vollständige Beispiele

### Atom: Button

```json
{
  "Button": {
    "namespace": "MyApp.Components.Atoms",
    "parameters": [
      { "name": "Variant", "type": "ButtonVariant", "default": "Primary" },
      { "name": "Size", "type": "ButtonSize", "default": "Medium" },
      { "name": "Type", "type": "string", "default": "button" },
      { "name": "Disabled", "type": "bool", "default": false },
      { "name": "IsLoading", "type": "bool", "default": false },
      { "name": "Icon", "type": "RenderFragment", "default": null },
      { "name": "IconPosition", "type": "IconPosition", "default": "Left" },
      { "name": "ChildContent", "type": "RenderFragment", "required": true }
    ],
    "events": [
      { "name": "OnClick", "type": "EventCallback<MouseEventArgs>" }
    ],
    "cssClass": "button",
    "variants": ["Primary", "Secondary", "Ghost", "Danger"],
    "sizes": ["Small", "Medium", "Large"],
    "states": ["loading", "disabled"],
    "dependencies": []
  }
}
```

### Molecule: Card

```json
{
  "Card": {
    "namespace": "MyApp.Components.Molecules",
    "parameters": [
      { "name": "Variant", "type": "CardVariant", "default": "Default" },
      { "name": "IsClickable", "type": "bool", "default": false },
      { "name": "IsHighlighted", "type": "bool", "default": false },
      { "name": "Header", "type": "RenderFragment", "default": null },
      { "name": "ChildContent", "type": "RenderFragment", "required": true },
      { "name": "Footer", "type": "RenderFragment", "default": null }
    ],
    "events": [
      { "name": "OnClick", "type": "EventCallback<MouseEventArgs>" }
    ],
    "cssClass": "card",
    "variants": ["Default", "Elevated", "Solid", "Featured"],
    "states": ["clickable", "highlighted"],
    "dependencies": ["Button", "Badge"]
  }
}
```

### Organism: Modal

```json
{
  "Modal": {
    "namespace": "MyApp.Components.Organisms",
    "parameters": [
      { "name": "IsOpen", "type": "bool", "twoWay": true, "default": false },
      { "name": "Title", "type": "string", "default": null },
      { "name": "Size", "type": "ModalSize", "default": "Medium" },
      { "name": "ShowCloseButton", "type": "bool", "default": true },
      { "name": "CloseOnBackdropClick", "type": "bool", "default": true },
      { "name": "ChildContent", "type": "RenderFragment", "required": true },
      { "name": "Footer", "type": "RenderFragment", "default": null }
    ],
    "events": [
      { "name": "IsOpenChanged", "type": "EventCallback<bool>" },
      { "name": "OnClose", "type": "EventCallback" },
      { "name": "OnOpen", "type": "EventCallback" }
    ],
    "cssClass": "modal",
    "variants": [],
    "sizes": ["Small", "Medium", "Large", "FullScreen"],
    "states": ["open"],
    "dependencies": ["Button", "Icon"]
  }
}
```

### Page: HomePage

```json
{
  "HomePage": {
    "namespace": "MyApp.Components.Pages",
    "parameters": [],
    "events": [],
    "cssClass": "home-page",
    "dependencies": ["Header", "TodoItem", "Card", "Button", "Modal", "Fab", "EmptyState"],
    "services": ["ITaskService", "NavigationManager"],
    "layout": "MainLayout"
  }
}
```

---

## Contract-Dateien Struktur

Der Orchestrator generiert diese Dateien im `.blazor-gen/` Ordner:

```
.blazor-gen/
├── contracts/
│   ├── atoms.contract.json       # Alle Atom-Contracts
│   ├── molecules.contract.json   # Alle Molecule-Contracts
│   ├── organisms.contract.json   # Alle Organism-Contracts
│   └── pages.contract.json       # Alle Page-Contracts
├── dependency-graph.json         # Abhängigkeits-Reihenfolge
└── enums.json                    # Abgeleitete Enum-Definitionen
```

### dependency-graph.json

```json
{
  "generationOrder": [
    {
      "phase": "atoms",
      "components": ["Button", "Input", "Badge", "Avatar", "Icon", "Spinner", "Checkbox", "Toggle"],
      "parallel": true
    },
    {
      "phase": "molecules",
      "components": [
        { "name": "Card", "dependsOn": ["Button", "Badge"] },
        { "name": "ListItem", "dependsOn": ["Badge", "Avatar", "Checkbox"] },
        { "name": "SearchBar", "dependsOn": ["Input", "Icon"] },
        { "name": "FormField", "dependsOn": ["Input", "Icon"] },
        { "name": "NavItem", "dependsOn": ["Icon", "Badge"] }
      ],
      "parallel": true
    },
    {
      "phase": "organisms",
      "components": [
        { "name": "Header", "dependsOn": ["Button", "SearchBar", "Avatar"] },
        { "name": "BottomNav", "dependsOn": ["NavItem"] },
        { "name": "Modal", "dependsOn": ["Button", "Icon"] },
        { "name": "BottomSheet", "dependsOn": ["Button"] },
        { "name": "TodoItem", "dependsOn": ["Badge", "Button", "Checkbox", "Icon"] }
      ],
      "parallel": false
    },
    {
      "phase": "pages",
      "components": [
        { "name": "HomePage", "dependsOn": ["Header", "BottomNav", "TodoItem", "Card", "Modal", "Fab"] },
        { "name": "SettingsPage", "dependsOn": ["Header", "ListItem", "Toggle", "Card"] }
      ],
      "parallel": false
    }
  ]
}
```

### enums.json

```json
{
  "ButtonVariant": {
    "namespace": "MyApp.Components.Models",
    "values": ["Primary", "Secondary", "Ghost", "Danger"]
  },
  "ButtonSize": {
    "namespace": "MyApp.Components.Models",
    "values": ["Small", "Medium", "Large"]
  },
  "IconPosition": {
    "namespace": "MyApp.Components.Models",
    "values": ["Left", "Right"]
  },
  "CardVariant": {
    "namespace": "MyApp.Components.Models",
    "values": ["Default", "Elevated", "Solid", "Featured"]
  },
  "ModalSize": {
    "namespace": "MyApp.Components.Models",
    "values": ["Small", "Medium", "Large", "FullScreen"]
  },
  "Priority": {
    "namespace": "MyApp.Components.Models",
    "values": ["Low", "Medium", "High"]
  }
}
```

---

## Contract-Ableitung aus UI Kit

Der Orchestrator leitet Contracts aus dem UI Kit ab:

### Aus HTML-Kommentar

```html
<!--
  Button Component
  ================
  Block: .btn
  Elements: .btn__text, .btn__icon, .btn__spinner
  Modifiers: --primary, --secondary, --ghost, --danger, --small, --medium, --large
  States: :disabled, .btn--loading
-->
```

**Wird zu:**

```json
{
  "cssClass": "btn",
  "variants": ["primary", "secondary", "ghost", "danger"],
  "sizes": ["small", "medium", "large"],
  "states": ["disabled", "loading"]
}
```

### Aus HTML-Struktur

```html
<button class="btn btn--primary">
  <span class="btn__icon">...</span>
  <span class="btn__text">Click me</span>
</button>
```

**Wird zu:**

```json
{
  "parameters": [
    { "name": "Icon", "type": "RenderFragment", "default": null },
    { "name": "ChildContent", "type": "RenderFragment", "required": true }
  ]
}
```

### Aus CSS-Variablen

```css
.btn {
  padding: var(--space-md) var(--space-lg);
  border-radius: var(--radius-md);
  background: var(--primary-gradient);
}
```

**Wird zu:**

```json
{
  "designTokens": {
    "usedVariables": ["--space-md", "--space-lg", "--radius-md", "--primary-gradient"]
  }
}
```

---

## Two-Way Binding Pattern

Für Komponenten mit Two-Way Binding:

### Contract

```json
{
  "name": "IsOpen",
  "type": "bool",
  "twoWay": true,
  "default": false
}
```

### Generierter Code

```csharp
[Parameter]
public bool IsOpen { get; set; }

[Parameter]
public EventCallback<bool> IsOpenChanged { get; set; }

private async Task SetIsOpen(bool value)
{
    if (IsOpen != value)
    {
        IsOpen = value;
        await IsOpenChanged.InvokeAsync(value);
    }
}
```

### Verwendung

```razor
<!-- Parent Component -->
<Modal @bind-IsOpen="isModalOpen">
    Content
</Modal>
```
