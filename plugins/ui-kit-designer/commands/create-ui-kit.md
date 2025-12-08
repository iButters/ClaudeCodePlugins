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

1. **HTML File**: `[AppName]-UI-Kit.html`
   - Interactive phone frame mockups
   - Tab navigation between screens
   - Design system documentation

2. **Screens** (based on app type):
   - Home/Dashboard
   - List views
   - Detail views  
   - Create/Edit modals
   - Settings
   - Empty states
   - Loading states

3. **Design System Section**:
   - Color palette with swatches
   - Typography scale
   - Spacing system
   - Component examples
   - Effect documentation

## Workflow

After creating the initial UI kit:

1. Open the HTML file in your browser to preview
2. Request changes: "Make the buttons rounder"
3. Add screens: "Add a notification center screen"
4. Export: "Export the color palette as CSS variables"

## Tips

- Start with a general description and let the agent ask clarifying questions
- Review each screen and provide specific feedback
- Use realistic content in your descriptions for better results
- Request multiple variations if unsure about direction
