---
name: generate-blazor-components
description: Converts a UI kit into a production-ready Razor Class Library with Blazor components following atomic design patterns.
argument-hint: --uiKitPath="<path>" --projectName="<name>" [--outputPath="<path>"] [--targetFramework="net8.0"] [--includePages="true"]
allowed-tools: ["Read", "Write", "Glob", "Grep", "Bash"]
arguments:
  - name: uiKitPath
    description: Path to the UI kit HTML file
    required: true
  - name: projectName
    description: Name for the generated RCL project (e.g., "MicroTodo")
    required: true
  - name: outputPath
    description: Output directory for the generated project
    required: false
  - name: targetFramework
    description: Target framework (net8.0, net9.0)
    required: false
    default: "net8.0"
  - name: includePages
    description: Whether to generate page components (true/false)
    required: false
    default: "true"
---

# Generate Blazor Components Command

This command transforms a UI kit HTML file into a complete Razor Class Library with production-ready Blazor components.

## Usage

```
/generate-blazor-components --uiKitPath="./MicroTodo-UI-Kit.html" --projectName="MicroTodo"
```

## Workflow

### Step 1: Analyze UI Kit

First, read and analyze the provided UI kit:

```markdown
1. Read the HTML file at {uiKitPath}
2. Extract design tokens:
   - Colors (backgrounds, text, borders, accents)
   - Typography (font families, sizes, weights)
   - Spacing (margins, paddings, gaps)
   - Border radii
   - Shadows
3. Identify components:
   - List all unique UI elements
   - Categorize as Atom, Molecule, or Organism
   - Note component variants and states
4. Map screens/pages:
   - Identify each frame/screen in the kit
   - Determine page hierarchy
   - Note navigation patterns
```

### Step 2: Create Project Structure

Generate the Razor Class Library:

```
{outputPath}/{projectName}.Components/
├── {projectName}.Components.csproj
├── _Imports.razor
├── CssBuilder.cs
├── wwwroot/
│   └── css/
│       ├── variables.css
│       └── base.css
├── Components/
│   ├── Atoms/
│   ├── Molecules/
│   ├── Organisms/
│   └── Templates/
├── Pages/
├── Services/
├── Models/
└── Extensions/
```

### Step 3: Generate Design Tokens

Create `wwwroot/css/variables.css` with extracted design tokens:

```css
:root {
    /* Extract all CSS custom properties from UI kit */
    /* Colors, typography, spacing, radii, shadows */
}
```

### Step 4: Generate Components

For each identified component:

1. **Create folder structure:**
   ```
   Components/{Category}/{ComponentName}/
   ├── {ComponentName}.razor
   ├── {ComponentName}.razor.cs
   └── {ComponentName}.razor.css
   ```

2. **Generate markup (.razor):**
   - Clean, semantic HTML
   - Proper Blazor bindings
   - Accessibility attributes

3. **Generate CodeBehind (.razor.cs):**
   - Proper namespace
   - XML documentation
   - Parameters with attributes
   - EventCallbacks
   - Private methods

4. **Generate scoped CSS (.razor.css):**
   - BEM-style naming
   - CSS variables for theming
   - Responsive styles
   - Animation definitions

### Step 5: Generate Pages (if includePages=true)

For each screen in the UI kit:

1. Create page component
2. Compose from generated components
3. Add page-specific logic
4. Include navigation handlers

### Step 6: Generate Services

Create supporting services:

- `IThemeService` / `ThemeService` - Theme management
- `IToastService` / `ToastService` - Toast notifications
- Service registration extension

### Step 7: Generate Models

Create required enums and models:

- Button variants/sizes
- Card variants
- Priority levels
- Theme options
- Any domain models from UI kit

### Step 8: Generate Documentation

Create README.md with:

- Installation instructions
- Usage examples
- Component API documentation
- Theming guide

## Component Checklist

For each component, ensure:

- [ ] `.razor` file with clean markup
- [ ] `.razor.cs` CodeBehind with full logic
- [ ] `.razor.css` scoped styles
- [ ] XML documentation on class and parameters
- [ ] `[Parameter]` attributes on all public properties
- [ ] `EventCallback` for all events
- [ ] `CaptureUnmatchedValues` for flexibility
- [ ] Proper accessibility attributes
- [ ] CssBuilder for dynamic classes

## Output Summary

After generation, provide:

```markdown
## ✅ Blazor Component Library Generated

**Project:** {projectName}.Components
**Location:** {outputPath}/{projectName}.Components/

### Statistics
- **Atoms:** {count} components
- **Molecules:** {count} components  
- **Organisms:** {count} components
- **Pages:** {count} pages
- **Services:** {count} services
- **Models:** {count} enums/classes

### Generated Components
#### Atoms
- Button (Primary, Secondary, Ghost, Danger)
- Input (Text, Search, Password)
- Badge (Info, Success, Warning, Error)
- Icon
- Avatar
- ProgressBar

#### Molecules
- Card
- ListItem
- SearchBar
- Toggle
- NavItem

#### Organisms
- Header
- BottomNav
- Modal
- BottomSheet
- TodoItem

### How to Use

1. **Add Reference:**
   ```xml
   <ProjectReference Include="..\\{projectName}.Components\\{projectName}.Components.csproj" />
   ```

2. **Register Services (Program.cs):**
   ```csharp
   builder.Services.Add{projectName}Components();
   ```

3. **Add Styles (index.html):**
   ```html
   <link href="_content/{projectName}.Components/css/variables.css" rel="stylesheet" />
   <link href="{projectName}.Components.bundle.scp.css" rel="stylesheet" />
   ```

4. **Import Components (_Imports.razor):**
   ```razor
   @using {projectName}.Components.Components.Atoms
   @using {projectName}.Components.Components.Molecules
   @using {projectName}.Components.Components.Organisms
   ```

5. **Use in Razor:**
   ```razor
   <Button Variant="ButtonVariant.Primary" OnClick="HandleClick">
       Click Me
   </Button>
   
   <Card Variant="CardVariant.Elevated" IsClickable="true">
       <Header>Card Title</Header>
       <ChildContent>Card content goes here</ChildContent>
   </Card>
   ```
```

## Trigger Phrases

- "Convert UI kit to Blazor"
- "Generate Blazor components from design"
- "Create Razor Class Library from UI kit"
- "Build Blazor components"
- "Implement UI kit in Blazor"
