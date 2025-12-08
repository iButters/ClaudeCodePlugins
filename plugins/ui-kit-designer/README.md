# UI Kit Designer Plugin

**Version:** 2.0.0
**License:** MIT

A powerful plugin for iterative front-end design that generates beautiful, interactive UI Kit HTML files for mobile and web applications. Features orchestrated Blazor component generation with parallel subagents for efficient RCL creation.

## Overview

This plugin enables designers and developers to rapidly prototype UI designs through an iterative, conversational workflow. It generates a modular folder structure following Atomic Design principles, with separated components (atoms, molecules, organisms) and CSS files that directly map to Blazor component libraries.

## Features

- 🎨 **Iterative Design Process** - Refine designs through natural conversation
- 📱 **Mobile-First Phone Frames** - Realistic device mockups
- 🌙 **Dark Mode Support** - Built-in dark glassmorphism styles
- 🧩 **Component Library** - Buttons, cards, inputs, navigation, modals
- 📐 **Design System Generation** - Colors, typography, spacing, effects
- 🔄 **Version Control** - Track design iterations
- 📋 **Export Ready** - Copy CSS/components to your project
- 📁 **Modular Output** - Atomic Design folder structure (atoms, molecules, organisms)

## Agents

### `ui-kit-designer`
Main design agent for creating and iterating on UI kits. Use when:
- Creating a new UI kit from scratch
- Adding new screens or components
- Refining existing designs
- Generating design system documentation

### `ui-kit-reviewer`
Reviews UI kits for accessibility, consistency, and best practices.

### `blazor-component-generator`
Converts UI kits into production-ready Blazor components. Use when:
- Transforming UI kit designs into Blazor code
- Creating a Razor Class Library from designs
- Implementing screens as Blazor pages
- Building a reusable component library

**Features:**
- ✅ Three-file pattern (`.razor`, `.razor.cs`, `.razor.css`)
- ✅ CSS isolation (scoped CSS)
- ✅ CodeBehind separation
- ✅ Atomic design structure (atoms → molecules → organisms)
- ✅ Full XML documentation
- ✅ WCAG 2.1 AA accessibility
- ✅ CssBuilder utility for dynamic classes
- ✅ Design tokens as CSS variables

## Commands

### `/ui-kit create <app-name>`
Create a new UI kit for an application.

### `/ui-kit add-screen <screen-name>`
Add a new screen to an existing UI kit.

### `/ui-kit refine <feedback>`
Refine the current design based on feedback.

### `/ui-kit export <format>`
Export components or styles (css, tailwind, blazor).

### `/generate-blazor-components`
Convert a UI kit into a production-ready Razor Class Library.

**Arguments:**
- `--uiKitPath` - Path to the UI kit HTML file (required)
- `--projectName` - Name for the RCL project (required)
- `--outputPath` - Output directory (optional)
- `--targetFramework` - Target framework, e.g., net8.0 (optional)
- `--includePages` - Generate page components (optional, default: true)

## Usage Examples

```
User: Create a UI kit for a fitness tracking app
Agent: Creates comprehensive UI kit with workout screens, stats, settings

User: Add a dark mode toggle to the settings screen
Agent: Updates settings screen with dark mode toggle component

User: The buttons need more padding and rounder corners
Agent: Refines button styles across all screens

User: Export the color palette as CSS variables
Agent: Generates CSS custom properties file

User: Convert this UI kit to Blazor components
Agent: Creates complete RCL with atoms, molecules, organisms

User: Generate Blazor components from MicroTodo-UI-Kit.html
Agent: Creates MicroTodo.Components/ with all screens and components
```

## Complete Workflow Example

```
1. Create UI Kit
   User: "Create a todo app UI kit with home, add task, and settings screens"
   → Generates MicroTodo-UI-Kit/ folder:
     - tokens/variables.css, base.css
     - atoms/button/, input/, checkbox/
     - molecules/card/, todo-item/
     - organisms/header/, bottom-nav/
     - pages/home/, settings/
     - index.html (preview hub)

2. Iterate on Design
   User: "Make the cards more glassmorphic"
   → Updates molecules/card/card.css

3. Refine Components
   User: "The buttons need rounder corners"
   → Updates atoms/button/button.css

4. Review for Quality
   User: "Review this UI kit"
   → Gets accessibility and consistency feedback

5. Generate Blazor Code
   User: "Convert to Blazor components"
   → Creates MicroTodo.Components/ RCL with:
     - Components/Atoms/Button, Input, Badge...
     - Components/Molecules/Card, TodoItem...
     - Components/Organisms/Header, Modal...
     - Pages/HomePage, SettingsPage...
     - Full design tokens, services, models
```

## Design Principles

The generated UI kits follow these principles:
- **Accessibility First** - WCAG 2.1 AA compliant colors
- **Modern Aesthetics** - Glassmorphism, gradients, shadows
- **Responsive Design** - Works on all screen sizes
- **Component Consistency** - Unified design language
- **Developer Friendly** - Clean, reusable code

## Output Structure

The ui-kit-designer generates a **modular folder structure** following Atomic Design principles:

```
MyApp-UI-Kit/
├── index.html                     # Preview hub with phone frames
├── tokens/
│   ├── variables.css              # Design tokens (colors, spacing, typography)
│   └── base.css                   # CSS reset & base styles
├── atoms/                         # Basic elements
│   ├── button/
│   │   ├── button.html            # All button variants
│   │   └── button.css             # BEM-scoped styles
│   ├── input/
│   ├── badge/
│   ├── avatar/
│   ├── checkbox/
│   ├── toggle/
│   └── ...
├── molecules/                     # Combined components
│   ├── card/
│   ├── list-item/
│   ├── search-bar/
│   ├── form-field/
│   └── ...
├── organisms/                     # Complex sections
│   ├── header/
│   ├── bottom-nav/
│   ├── modal/
│   └── ...
├── pages/                         # Complete screens
│   ├── home/
│   ├── settings/
│   ├── detail/
│   └── empty-state/
└── docs/
    └── design-system.html         # Design system documentation
```

### Component File Format

Each component contains **all variants** as a visual specification:

```html
<!--
  Button Component
  ================
  Block: .btn
  Elements: .btn__text, .btn__icon
  Modifiers: --primary, --secondary, --ghost, --small, --large
  States: :disabled, .btn--loading
-->
<section class="component-variants">...</section>
<section class="component-sizes">...</section>
<section class="component-states">...</section>
```

This format enables automatic enum derivation when converting to Blazor components.

### Generated Blazor RCL

When exported to Blazor, the structure mirrors the UI kit:

```
MyApp.Components/
├── MyApp.Components.csproj
├── wwwroot/css/
│   ├── variables.css
│   └── base.css
├── Components/
│   ├── Atoms/Button/, Input/, Badge/...
│   ├── Molecules/Card/, ListItem/...
│   └── Organisms/Header/, Modal/...
├── Pages/
├── Services/
└── Models/
```

## Plugin Structure

```
ui-kit-designer/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── agents/
│   ├── ui-kit-designer.md       # Main design agent
│   ├── ui-kit-reviewer.md       # Review agent
│   └── blazor-component-generator.md
├── commands/
│   ├── create-ui-kit.md
│   ├── refine-ui-kit.md
│   ├── export-ui-kit.md
│   └── generate-blazor-components.md
├── skills/
│   ├── ui-kit-design/
│   │   ├── SKILL.md
│   │   └── references/          # Design references
│   │       ├── component-library.md
│   │       ├── color-palettes.md
│   │       └── app-templates.md
│   ├── modular-ui-kit/
│   │   ├── SKILL.md             # Modular folder structure skill
│   │   └── references/
│   │       ├── folder-structure.md
│   │       ├── component-templates.md
│   │       └── index-template.md
│   └── blazor-components/
│       ├── SKILL.md
│       └── references/          # Blazor references
│           └── blazor-best-practices.md
└── README.md
```

## Requirements

- Claude Code with plugin support
- Modern web browser for previewing UI kits

## License

MIT License
