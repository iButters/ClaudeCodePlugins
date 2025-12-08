# Subagent Interface

Dieses Dokument definiert das Interface zwischen dem Orchestrator (`blazor-component-generator`) und den Subagenten (`blazor-atom-generator`, `blazor-molecule-generator`, etc.).

## Prinzipien

1. **Minimaler Kontext:** Subagenten erhalten nur die Informationen, die sie brauchen
2. **Selbstständig:** Subagenten arbeiten ohne weitere Interaktion
3. **Deterministisch:** Gleicher Input → Gleicher Output
4. **Keine Akkumulation:** Jeder Subagent startet frisch

---

## Input-Format

Der Orchestrator übergibt dem Subagenten einen JSON-Block im Prompt:

### Atom Generator Input

```json
{
  "task": "generate-atom",
  "projectName": "MyApp",
  "componentName": "Button",
  "outputPath": "D:/Projects/MyApp.Components/Components/Atoms/Button/",

  "contract": {
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
    "states": ["loading", "disabled"]
  },

  "cssSource": "/* Original CSS from UI Kit atoms/button/button.css */\n.btn { ... }",

  "htmlSource": "<!-- Original HTML from UI Kit atoms/button/button.html -->\n<button class=\"btn\">...",

  "designTokens": {
    "usedVariables": ["--primary-gradient", "--space-md", "--radius-md", "--shadow-glow"]
  }
}
```

### Molecule Generator Input

```json
{
  "task": "generate-molecule",
  "projectName": "MyApp",
  "componentName": "Card",
  "outputPath": "D:/Projects/MyApp.Components/Components/Molecules/Card/",

  "contract": {
    "namespace": "MyApp.Components.Molecules",
    "parameters": [...],
    "events": [...],
    "cssClass": "card",
    "variants": ["Default", "Elevated", "Solid", "Featured"],
    "dependencies": ["Button", "Badge"]
  },

  "dependencyContracts": {
    "Button": {
      "namespace": "MyApp.Components.Atoms",
      "parameters": [...],
      "events": [...]
    },
    "Badge": {
      "namespace": "MyApp.Components.Atoms",
      "parameters": [...],
      "events": [...]
    }
  },

  "cssSource": "/* Original CSS */",
  "htmlSource": "<!-- Original HTML -->",
  "designTokens": { ... }
}
```

### Organism Generator Input

```json
{
  "task": "generate-organism",
  "projectName": "MyApp",
  "componentName": "Modal",
  "outputPath": "D:/Projects/MyApp.Components/Components/Organisms/Modal/",

  "contract": {
    "namespace": "MyApp.Components.Organisms",
    "parameters": [
      { "name": "IsOpen", "type": "bool", "twoWay": true, "default": false },
      { "name": "Title", "type": "string" },
      { "name": "ChildContent", "type": "RenderFragment", "required": true },
      { "name": "Footer", "type": "RenderFragment" }
    ],
    "events": [
      { "name": "IsOpenChanged", "type": "EventCallback<bool>" },
      { "name": "OnClose", "type": "EventCallback" }
    ],
    "cssClass": "modal",
    "dependencies": ["Button", "Icon"]
  },

  "dependencyContracts": {
    "Button": { ... },
    "Icon": { ... }
  },

  "cssSource": "/* Original CSS */",
  "htmlSource": "<!-- Original HTML -->",
  "designTokens": { ... }
}
```

### Page Generator Input

```json
{
  "task": "generate-page",
  "projectName": "MyApp",
  "componentName": "HomePage",
  "outputPath": "D:/Projects/MyApp.Components/Pages/HomePage/",

  "contract": {
    "namespace": "MyApp.Components.Pages",
    "layout": "MainLayout",
    "route": "/",
    "dependencies": ["Header", "BottomNav", "TodoItem", "Card", "Modal", "Fab"],
    "services": ["ITaskService", "NavigationManager"]
  },

  "dependencyContracts": {
    "Header": { ... },
    "BottomNav": { ... },
    "TodoItem": { ... },
    "Card": { ... },
    "Modal": { ... },
    "Fab": { ... }
  },

  "pageStructure": {
    "sections": [
      { "name": "stats", "component": "StatsCard" },
      { "name": "taskList", "component": "TodoItem", "loop": true },
      { "name": "emptyState", "component": "EmptyState", "conditional": true }
    ]
  },

  "cssSource": "/* Original CSS */",
  "htmlSource": "<!-- Original HTML -->",
  "designTokens": { ... }
}
```

---

## Output-Format

Jeder Subagent gibt einen strukturierten Report zurück:

### Erfolgs-Output

```markdown
## Component Generated: Button

### Status: SUCCESS

### Files Created
| File | Path | Size |
|------|------|------|
| Button.razor | Components/Atoms/Button/Button.razor | 42 lines |
| Button.razor.cs | Components/Atoms/Button/Button.razor.cs | 89 lines |
| Button.razor.css | Components/Atoms/Button/Button.razor.css | 124 lines |

### Component Interface
```csharp
// Parameters
[Parameter] public ButtonVariant Variant { get; set; } = ButtonVariant.Primary;
[Parameter] public ButtonSize Size { get; set; } = ButtonSize.Medium;
[Parameter] public bool Disabled { get; set; }
[Parameter] public bool IsLoading { get; set; }
[Parameter] public RenderFragment? Icon { get; set; }
[Parameter] public RenderFragment? ChildContent { get; set; }

// Events
[Parameter] public EventCallback<MouseEventArgs> OnClick { get; set; }
```

### CSS Classes Generated
- `.button` (base)
- `.button--primary`, `.button--secondary`, `.button--ghost`, `.button--danger` (variants)
- `.button--small`, `.button--medium`, `.button--large` (sizes)
- `.button--loading`, `.button--disabled` (states)
- `.button__icon`, `.button__content`, `.button__spinner` (elements)

### Usage Example
```razor
<Button Variant="ButtonVariant.Primary"
        Size="ButtonSize.Medium"
        OnClick="HandleClick">
    Click Me
</Button>

<Button Variant="ButtonVariant.Ghost" IsLoading="true">
    <Icon>
        <svg>...</svg>
    </Icon>
    Loading...
</Button>
```

### Dependencies Used
- None (Atom component)

### Notes
- Implements CssBuilder for dynamic class composition
- Includes loading spinner animation
- Supports icon positioning (left/right)
```

### Fehler-Output

```markdown
## Component Generation Failed: Card

### Status: FAILED

### Error
Unable to resolve dependency: `GlassPanel` is referenced but not in dependencyContracts.

### Partial Files Created
- Components/Molecules/Card/Card.razor (incomplete)

### Required Action
Orchestrator should provide GlassPanel contract or remove dependency.

### Debug Info
```json
{
  "missingDependency": "GlassPanel",
  "availableDependencies": ["Button", "Badge"],
  "failedAtStep": "markup-generation"
}
```
```

---

## Subagent Responsibilities

### blazor-atom-generator

**Input:** Einzelner Atom-Contract + CSS/HTML Source
**Output:** 3 Dateien (.razor, .razor.cs, .razor.css)

**Verantwortlich für:**
- Parameter mit Defaults generieren
- EventCallbacks definieren
- CssBuilder-Integration
- Scoped CSS mit BEM-Naming
- XML-Dokumentation
- AdditionalAttributes Support

**Nicht verantwortlich für:**
- Andere Komponenten verwenden
- Services injizieren
- Navigation

### blazor-molecule-generator

**Input:** Molecule-Contract + Dependency-Contracts + CSS/HTML Source
**Output:** 3 Dateien (.razor, .razor.cs, .razor.css)

**Verantwortlich für:**
- Atom-Komponenten korrekt einbinden
- Parameter/Events durchreichen wo nötig
- Content Slots (Header, Footer, ChildContent)
- Composition Pattern

**Zusätzlich:**
- Kennt Atom-Interfaces aus dependencyContracts
- Verwendet Atoms mit korrekten Parametern

### blazor-organism-generator

**Input:** Organism-Contract + alle Dependency-Contracts + CSS/HTML Source
**Output:** 3 Dateien (.razor, .razor.cs, .razor.css)

**Verantwortlich für:**
- Komplexe Komposition
- Two-Way Binding implementieren
- Event-Bubbling/Handling
- Zustandsmanagement (open/closed, etc.)

**Zusätzlich:**
- Implementiert IsOpenChanged Pattern
- Backdrop-Click Handling
- Keyboard Events (Escape, etc.)

### blazor-page-generator

**Input:** Page-Contract + alle Dependency-Contracts + CSS/HTML Source
**Output:** 3 Dateien (.razor, .razor.cs, .razor.css)

**Verantwortlich für:**
- Layout-Referenz (@layout)
- Route-Attribut (@page)
- Service-Injection
- Lifecycle (OnInitializedAsync)
- Datenladung und Zustand

**Zusätzlich:**
- IDisposable wo nötig
- Navigation
- Modals öffnen/schließen

---

## Prompt-Template für Subagenten

Der Orchestrator verwendet dieses Template:

```markdown
Generate a Blazor component based on the following specification:

## Component Specification
```json
{INPUT_JSON}
```

## Requirements
1. Create exactly 3 files:
   - `{ComponentName}.razor` - Markup only, no @code block
   - `{ComponentName}.razor.cs` - Full CodeBehind with all logic
   - `{ComponentName}.razor.css` - Scoped CSS with BEM naming

2. Follow these patterns:
   - Use CssBuilder for dynamic classes
   - Add XML documentation to all public members
   - Support [Parameter(CaptureUnmatchedValues = true)]
   - Implement IDisposable only if needed

3. Use the contract to:
   - Generate correct parameters with types and defaults
   - Create EventCallbacks for all events
   - Handle two-way binding for twoWay: true parameters
   - Reference dependencies with correct namespaces

4. Transform CSS:
   - Convert BEM classes to scoped CSS
   - Keep CSS variable references (var(--...))
   - Add hover/focus/active states

## Output Format
Return a markdown report with:
- Status (SUCCESS/FAILED)
- Files created with paths
- Component interface summary
- Usage example
- Any notes or warnings

Write the files using the Write tool, then provide the report.
```

---

## Parallelisierung

### Atoms (alle parallel)
```
Orchestrator spawnt gleichzeitig:
├── blazor-atom-generator (Button)
├── blazor-atom-generator (Input)
├── blazor-atom-generator (Badge)
├── blazor-atom-generator (Avatar)
├── blazor-atom-generator (Icon)
└── blazor-atom-generator (Spinner)

→ Wartet auf alle mit AgentOutputTool
```

### Molecules (parallel wenn unabhängig)
```
Gruppe 1 (parallel):
├── blazor-molecule-generator (Card)      dependsOn: [Button, Badge]
├── blazor-molecule-generator (SearchBar) dependsOn: [Input, Icon]
└── blazor-molecule-generator (NavItem)   dependsOn: [Icon, Badge]

Gruppe 2 (nach Gruppe 1):
└── blazor-molecule-generator (FormField) dependsOn: [Input, Icon, Button]
```

### Organisms & Pages (sequentiell)
```
blazor-organism-generator (Header)    → warten
blazor-organism-generator (Modal)     → warten
blazor-organism-generator (BottomNav) → warten
blazor-page-generator (HomePage)      → warten
blazor-page-generator (SettingsPage)  → warten
```

---

## Fehlerbehandlung

### Subagent-Fehler

Wenn ein Subagent fehlschlägt:
1. Orchestrator liest Fehler-Report
2. Entscheidet: Retry, Skip, oder Abort
3. Bei Retry: Korrigiert Input und spawnt erneut

### Dependency-Fehler

Wenn eine Abhängigkeit fehlt:
1. Subagent meldet fehlende Dependency
2. Orchestrator prüft ob Dependency existiert
3. Wenn ja: Fügt Contract hinzu und retried
4. Wenn nein: Markiert Komponente als übersprungen

### Timeout

Subagenten haben implizites Timeout:
- Atom: ~2 Minuten
- Molecule: ~3 Minuten
- Organism: ~5 Minuten
- Page: ~10 Minuten

Bei Timeout: Orchestrator loggt Warnung und fährt fort.
