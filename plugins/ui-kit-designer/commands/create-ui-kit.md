---
name: create-ui-kit
description: Create a new UI kit for an application. Use this command to start designing a new app interface from scratch.
argument-hint: <app-name> [--type <type>] [--style <style>] [--palette <palette>]
allowed-tools: ["Read", "Write", "Glob", "Grep", "Bash"]
---

# Create UI Kit Command

Create a comprehensive UI kit for a new application with interactive phone mockups and design system documentation.

## Usage

```
/ui-kit create <app-name> [options]
```

## Arguments

- `<app-name>`: Name of the application (required)

## Options

- `--type <type>`: App type (todo, fitness, social, commerce, finance, music, meditation, recipe, travel, custom)
- `--style <style>`: Design style (dark, light, glassmorphism, minimal, vibrant)
- `--palette <palette>`: Color palette (indigo, ocean, rose, forest, ember, crimson, electric, custom)
- `--screens <screens>`: Comma-separated list of specific screens to include

## Examples

### Basic Usage
```
/ui-kit create "FitTrack"
```
Creates a UI kit with default settings, asking for app type and features.

### With App Type
```
/ui-kit create "FitTrack" --type fitness
```
Creates a fitness app UI kit with appropriate screens and components.

### Full Specification
```
/ui-kit create "MealPlanner" --type recipe --style dark --palette ember
```
Creates a recipe app with dark theme and warm orange colors.

### Custom Screens
```
/ui-kit create "MyApp" --screens "home,profile,settings,notifications"
```
Creates only the specified screens.

## What Gets Created

A modular folder structure `[AppName]-UI-Kit/` containing:

```
[AppName]-UI-Kit/
├── index.html              # Preview hub with phone frames
├── tokens/
│   ├── variables.css       # Design tokens (colors, spacing, typography)
│   └── base.css            # CSS reset & base styles
├── atoms/                  # Basic components
│   ├── button/             # button.html + button.css
│   ├── input/
│   ├── badge/
│   └── ...
├── molecules/              # Combined components
│   ├── card/
│   ├── list-item/
│   └── ...
├── organisms/              # Complex sections
│   ├── header/
│   ├── bottom-nav/
│   └── ...
├── pages/                  # Complete screens
│   ├── home/
│   ├── settings/
│   └── ...
└── docs/
    └── design-system.html
```

### Component Structure
Each component has:
- `[name].html` - All variants as visual specification
- `[name].css` - BEM-scoped styles using CSS variables

### Screens Created (based on app type)
- Home/Dashboard
- List/Detail views
- Create/Edit screens
- Settings
- Empty/Loading states

## Workflow

After creating the UI kit:

1. Open `[AppName]-UI-Kit/index.html` in your browser to preview
2. Request changes: "Make the buttons rounder" (updates atoms/button/button.css)
3. Add screens: "Add a notifications page" (creates pages/notifications/)
4. Export: "Generate Blazor components" (converts to RCL structure)

## Tips

- Start with a general description and let the agent ask clarifying questions
- Review each screen and provide specific feedback
- Use realistic content in your descriptions for better results
- Request multiple variations if unsure about direction
