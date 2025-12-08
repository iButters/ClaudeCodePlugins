---
name: Modular UI Kit
description: This skill should be used when generating UI kits with a modular folder structure following Atomic Design principles. It enables creating separate HTML and CSS files for each component (atoms, molecules, organisms) with vertical slices architecture, making components reusable and easy to convert to Blazor.
version: 1.0.0
---

# Modular UI Kit Generation

## Overview

This skill enables generating UI kits as a modular folder structure instead of a single HTML file. Components are organized following Atomic Design principles with separate HTML and CSS files per component - similar to vertical slices architecture.

## Output Structure

```
[AppName]-UI-Kit/
├── index.html                    # Preview hub with phone frames
├── tokens/
│   ├── variables.css             # Design tokens (colors, spacing, etc.)
│   └── base.css                  # Reset & base styles
│
├── atoms/                        # Basic building blocks
│   ├── button/
│   │   ├── button.html           # All variants as visual spec
│   │   └── button.css            # BEM-scoped styles
│   ├── input/
│   ├── badge/
│   ├── avatar/
│   ├── checkbox/
│   ├── toggle/
│   ├── spinner/
│   └── progress-bar/
│
├── molecules/                    # Combinations of atoms
│   ├── card/
│   ├── list-item/
│   ├── search-bar/
│   ├── form-field/
│   ├── nav-item/
│   └── todo-item/
│
├── organisms/                    # Complex UI sections
│   ├── header/
│   ├── bottom-nav/
│   ├── modal/
│   ├── bottom-sheet/
│   └── toast/
│
├── pages/                        # Complete screens
│   ├── home/
│   ├── settings/
│   ├── detail/
│   └── empty-state/
│
└── docs/
    └── design-system.html        # Design system documentation
```

## Component File Format

### HTML Files

Each component HTML file contains **all variants** as a visual specification:

```html
<!--
  [ComponentName] Component
  =========================
  Block: .[block-name]
  Elements: .[block]__[element], ...
  Modifiers: --[modifier], ...
  States: :disabled, .[block]--loading, ...
-->

<!-- Variants -->
<section class="component-variants">
  <h3>Variants</h3>
  <!-- All variant examples -->
</section>

<!-- Sizes -->
<section class="component-sizes">
  <h3>Sizes</h3>
  <!-- All size examples -->
</section>

<!-- States -->
<section class="component-states">
  <h3>States</h3>
  <!-- All state examples -->
</section>
```

### CSS Files

Each component CSS file uses BEM naming and CSS variables:

```css
/* [ComponentName] Component */
/* BEM: .[block], .[block]__[element], .[block]--[modifier] */

.[block] {
  /* Base styles using CSS variables */
  display: [value];
  font-family: var(--font-family);
  transition: all var(--transition-base);
}

.[block]__[element] {
  /* Element styles */
}

.[block]--[modifier] {
  /* Modifier styles */
}
```

## Generation Workflow

1. **Create tokens/** first
   - Extract colors, typography, spacing from design requirements
   - Generate `variables.css` with all CSS custom properties
   - Generate `base.css` with reset and base styles

2. **Create atoms/** (bottom-up)
   - Button, Input, Badge, Avatar, Checkbox, Toggle, Spinner, ProgressBar
   - Each with all variants documented

3. **Create molecules/** (compose atoms)
   - Card, ListItem, SearchBar, FormField, NavItem, TodoItem
   - Reference atom classes in markup

4. **Create organisms/** (compose molecules + atoms)
   - Header, BottomNav, Modal, BottomSheet, Toast
   - Complex layouts with multiple components

5. **Create pages/** (compose all levels)
   - Complete screen layouts
   - Real content and realistic data

6. **Create index.html** last
   - Link all CSS files
   - Create phone frame previews
   - Add navigation between pages

## Atomic Design Categories

### Atoms (Basic Elements)
| Component | Block Class | Key Modifiers |
|-----------|-------------|---------------|
| Button | `.btn` | `--primary`, `--secondary`, `--ghost`, `--danger` |
| Input | `.input` | `--text`, `--search`, `--password` |
| Badge | `.badge` | `--info`, `--success`, `--warning`, `--error` |
| Avatar | `.avatar` | `--small`, `--medium`, `--large` |
| Checkbox | `.checkbox` | `--checked`, `--indeterminate` |
| Toggle | `.toggle` | `--on`, `--off` |
| Spinner | `.spinner` | `--small`, `--medium`, `--large` |
| ProgressBar | `.progress` | `--determinate`, `--indeterminate` |

### Molecules (Combinations)
| Component | Composed Of |
|-----------|-------------|
| Card | Container + Content slots |
| ListItem | Avatar + Text + Action |
| SearchBar | Input + Button + Icon |
| FormField | Label + Input + Error |
| NavItem | Icon + Text + Badge |
| TodoItem | Checkbox + Text + Actions |

### Organisms (Complex Sections)
| Component | Composed Of |
|-----------|-------------|
| Header | Logo + NavItems + Avatar |
| BottomNav | NavItems (3-5) |
| Modal | Overlay + Card + Actions |
| BottomSheet | Overlay + Content + Handle |
| Toast | Icon + Message + Action |

## Benefits for Blazor Generator

This modular structure maps directly to Blazor RCL:

| UI Kit | Blazor RCL |
|--------|------------|
| `atoms/button/button.html` | `Components/Atoms/Button/Button.razor` |
| `atoms/button/button.css` | `Components/Atoms/Button/Button.razor.css` |
| `tokens/variables.css` | `wwwroot/css/variables.css` |

The Blazor generator can:
1. Parse HTML header comments for BEM class documentation
2. Extract enums from `--modifier` classes
3. Convert CSS directly to scoped `.razor.css` files
4. Generate CodeBehind from component structure

## Related References

For detailed templates and examples, see:

- [Folder Structure](references/folder-structure.md) - Complete directory layout
- [Component Templates](references/component-templates.md) - HTML/CSS templates for each component type
- [Index Template](references/index-template.md) - Preview hub template
