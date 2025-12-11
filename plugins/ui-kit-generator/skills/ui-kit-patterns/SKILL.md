---
description: |
  This skill provides knowledge about UI-Kit generation patterns, Atomic Design methodology,
  and design system best practices using Web Components. Use when generating components,
  planning architecture, or implementing specific design styles (glassmorphism, neumorphism, etc.).
---

# UI-Kit Patterns & Best Practices

## Architecture Overview

This UI-Kit generator creates **Web Components** (Custom Elements with Shadow DOM) following Atomic Design methodology. All components are reusable JavaScript classes that can be composed together.

```
tokens/tokens.css              ← CSS Custom Properties (design tokens)
    ↓
components/atoms/              ← Basic Web Components (ui-button, ui-input)
    ↓
components/molecules/          ← Composite Web Components (ui-card, ui-form-field)
    ↓
components/organisms/          ← Complex Web Components (ui-header, ui-sidebar)
    ↓
components/templates/          ← Layout Web Components (ui-dashboard-layout)
    ↓
pages/                         ← HTML files composing all components
```

## Atomic Design Methodology

### Hierarchy (Bottom to Top)

1. **Tokens** - CSS Custom Properties (colors, spacing, typography)
2. **Atoms** - Basic Web Components (`<ui-button>`, `<ui-input>`, `<ui-badge>`)
3. **Molecules** - Composite Web Components (`<ui-card>`, `<ui-form-field>`)
4. **Organisms** - Complex Web Components (`<ui-header>`, `<ui-sidebar>`, `<ui-modal>`)
5. **Templates** - Layout Web Components (`<ui-dashboard-layout>`, `<ui-auth-layout>`)
6. **Pages** - HTML files that compose all components together

### Key Principles

- **Top-down planning**: Plan from pages down to identify needed components
- **Parallel generation**: All component levels generate simultaneously after tokens
- **Single responsibility**: Each component does one thing well
- **Composition via imports**: Higher-level components import their dependencies
- **Attribute-based API**: Components configured via HTML attributes
- **Slot-based content**: Named slots for flexible content insertion

## Web Components Architecture

### Why Web Components?

| Benefit | Description |
|---------|-------------|
| **No style duplication** | Each component defined once, styles encapsulated |
| **Guaranteed consistency** | Same component = same appearance everywhere |
| **Full parallelization** | All levels can generate simultaneously |
| **True reusability** | Components work like React/Vue but native |
| **Attribute-based API** | `<ui-button variant="primary" size="lg">` |
| **Slot-based composition** | Named slots for flexible content |

### Component Pattern

All components extend `BaseComponent`:

```javascript
import { BaseComponent, defineComponent, html, css } from '../base-component.js';

class UiButton extends BaseComponent {
  static get observedAttributes() {
    return ['variant', 'size', 'disabled', 'loading'];
  }

  render() {
    const variant = this.attr('variant', 'primary');
    const size = this.attr('size', 'md');
    const disabled = this.hasAttr('disabled');
    const loading = this.hasAttr('loading');

    this.shadowRoot.innerHTML = html`
      <style>
        ${this.getBaseStyles()}

        button {
          /* Styles using CSS Custom Properties */
          padding: var(--spacing-3) var(--spacing-6);
          font-family: var(--font-family-primary);
          border-radius: var(--radius-lg);
          transition: var(--transition-base);
        }

        /* Variant styles */
        button.variant-primary {
          background: var(--glass-white-10);
          backdrop-filter: var(--backdrop-filter-glass-medium);
          border: 1px solid var(--border-glass-light);
          color: var(--text-primary);
        }

        button.variant-primary:hover {
          background: var(--glass-white-15);
          box-shadow: var(--shadow-glow-primary);
        }
      </style>

      <button
        class="variant-${variant} size-${size}"
        ?disabled=${disabled}
      >
        ${loading ? '<span class="spinner"></span>' : ''}
        <slot></slot>
      </button>
    `;

    // Event listeners
    this.shadowRoot.querySelector('button')
      .addEventListener('click', (e) => {
        if (!disabled && !loading) {
          this.emit('ui-click', { originalEvent: e });
        }
      });
  }
}

defineComponent('ui-button', UiButton);
export { UiButton };
```

### CSS Custom Properties Inheritance

Web Components inherit CSS Custom Properties through Shadow DOM:

```css
/* tokens.css - loaded in document */
:root {
  --color-primary-500: #8b5cf6;
  --spacing-4: 1rem;
}

/* Inside Shadow DOM - these work! */
button {
  background: var(--color-primary-500);
  padding: var(--spacing-4);
}
```

### Slot System

Named slots allow flexible content composition:

```javascript
// ui-card.js
this.shadowRoot.innerHTML = html`
  <article class="card">
    <header><slot name="header"></slot></header>
    <div class="body"><slot></slot></div>
    <footer><slot name="footer"></slot></footer>
  </article>
`;
```

```html
<!-- Usage -->
<ui-card>
  <span slot="header">Card Title</span>
  <p>Card content goes in default slot</p>
  <ui-button slot="footer" variant="primary">Save</ui-button>
</ui-card>
```

## Design Styles

For detailed style guides, see:
- `references/glassmorphism.md` - Glass effect style guide
- `references/neumorphism.md` - Soft UI style guide
- `references/material.md` - Material Design patterns
- `references/web-components.md` - Web Components implementation guide

## File Organization

```
{app-name}-ui-kit/
├── tokens/
│   ├── tokens.css          # CSS Custom Properties
│   └── tokens.json         # JSON representation
├── components/
│   ├── base-component.js   # Base class for all components
│   ├── atoms/
│   │   ├── ui-button.js
│   │   ├── ui-input.js
│   │   ├── ui-badge.js
│   │   └── ui-avatar.js
│   ├── molecules/
│   │   ├── ui-card.js
│   │   ├── ui-form-field.js
│   │   └── ui-search-bar.js
│   ├── organisms/
│   │   ├── ui-header.js
│   │   ├── ui-sidebar.js
│   │   └── ui-modal.js
│   ├── templates/
│   │   ├── ui-dashboard-layout.js
│   │   └── ui-auth-layout.js
│   └── index.js            # Barrel export
├── pages/
│   ├── dashboard.html
│   ├── login.html
│   └── settings.html
├── showcase/               # Component documentation
│   ├── atoms/
│   │   └── button.html
│   ├── molecules/
│   ├── organisms/
│   └── templates/
├── manifest.json           # Component registry
└── preview.html            # Interactive preview
```

## Token System

### Required Token Categories

1. **Colors**: Primary, secondary, accent, neutral, semantic, glass backgrounds
2. **Typography**: Families, sizes, weights, line-heights, letter-spacing
3. **Spacing**: Scale from 0 to 96 (0.25rem increments)
4. **Border Radius**: none, sm, md, lg, xl, full
5. **Shadows**: sm, md, lg, xl + glass shadows
6. **Backdrop Filters**: Glass blur effects
7. **Transitions**: fast, base, medium, slow
8. **Z-Index**: dropdown, sticky, modal, tooltip

### Style-Specific Tokens

**Glassmorphism**:
```css
--glass-white-5: rgba(255, 255, 255, 0.05);
--glass-white-10: rgba(255, 255, 255, 0.10);
--backdrop-filter-glass-medium: blur(12px) saturate(180%);
--shadow-glow-primary: 0 0 20px rgba(139, 92, 246, 0.3);
```

**Neumorphism**: `--neu-shadow-raised`, `--neu-shadow-inset`

**Material**: `--elevation-*`, `--ripple-*`

## Generation Workflow

### Parallel Execution

After tokens are generated, ALL component levels run in parallel:

```
Discovery → Planning → Tokens ─┬─→ Atoms (parallel)     ─┐
                               ├─→ Molecules (parallel)  │
                               ├─→ Organisms (parallel)  ├─→ Assembly → Done
                               ├─→ Templates (parallel)  │
                               ├─→ Pages (parallel)      │
                               └─→ Showcase (parallel)  ─┘
```

This is possible because:
- Components import dependencies via ES6 `import` statements
- Browser resolves imports at runtime
- No build-time dependency between levels
- `tokens.css` is the only external dependency

### Speedup

| Metric | Before (BEM) | After (Web Components) |
|--------|--------------|------------------------|
| Sequential steps | ~15 | ~4 |
| Style duplication | ~500 lines/component | 0 |
| Parallelization | Level-based | Full parallel |
| Estimated speedup | N/A | ~80% |

## Best Practices

### For Components

1. Use tokens for ALL values (no hardcoded colors, sizes)
2. Include all variants, sizes, and states
3. Show realistic content in examples
4. Add proper focus states for accessibility
5. Use semantic HTML inside Shadow DOM
6. Emit custom events with `ui-` prefix

### For Composition

1. Import dependencies at the top of the file
2. Use named slots for flexible content areas
3. Forward relevant attributes to inner elements
4. Keep Shadow DOM structure minimal

### For Pages

1. Import components via barrel export (`index.js`)
2. Load `tokens.css` in document head
3. Use template components for layout
4. Compose organisms in template slots

### Component Usage Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="stylesheet" href="tokens/tokens.css">
  <script type="module" src="components/index.js"></script>
</head>
<body>
  <ui-dashboard-layout>
    <ui-sidebar slot="sidebar">
      <ui-nav-item icon="📊" active>Dashboard</ui-nav-item>
      <ui-nav-item icon="⚙️">Settings</ui-nav-item>
    </ui-sidebar>

    <ui-header slot="header" sticky>
      <ui-search-bar slot="search" placeholder="Search..."></ui-search-bar>
      <ui-button slot="actions" variant="primary">New</ui-button>
    </ui-header>

    <ui-card-grid columns="3">
      <ui-card interactive>
        <span slot="header">Card Title</span>
        <p>Content here</p>
        <ui-button slot="footer" variant="ghost">View</ui-button>
      </ui-card>
    </ui-card-grid>
  </ui-dashboard-layout>
</body>
</html>
```

## References

See the `references/` directory for:
- Design style guides
- Web Components implementation details
- Token templates
- Component examples
