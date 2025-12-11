# Web Components Implementation Guide

## Overview

This UI-Kit uses native Web Components (Custom Elements + Shadow DOM) for all components. This provides true encapsulation, reusability, and enables full parallel generation.

## Core Concepts

### Custom Elements

Custom Elements allow you to define new HTML tags:

```javascript
class UiButton extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
  }

  connectedCallback() {
    this.render();
  }
}

customElements.define('ui-button', UiButton);
```

Usage:
```html
<ui-button variant="primary">Click me</ui-button>
```

### Shadow DOM

Shadow DOM provides style encapsulation - styles inside don't leak out, outside styles don't leak in:

```javascript
this.shadowRoot.innerHTML = `
  <style>
    /* These styles ONLY affect this component */
    button { background: blue; }
  </style>
  <button><slot></slot></button>
`;
```

### CSS Custom Properties Inheritance

CSS Custom Properties (variables) DO pass through Shadow DOM:

```css
/* In tokens.css (document level) */
:root {
  --color-primary: #8b5cf6;
}

/* Inside Shadow DOM - this works! */
button {
  background: var(--color-primary);
}
```

This is the key to our token system working with Web Components.

## BaseComponent Class

All components extend `BaseComponent` from `base-component.js`:

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

    this.shadowRoot.innerHTML = html`
      <style>
        ${this.getBaseStyles()}
        /* Component-specific styles */
      </style>
      <button class="variant-${variant} size-${size}" ${disabled ? 'disabled' : ''}>
        <slot></slot>
      </button>
    `;
  }
}

defineComponent('ui-button', UiButton);
export { UiButton };
```

### BaseComponent Methods

| Method | Purpose |
|--------|---------|
| `attr(name, default)` | Get attribute value with default |
| `hasAttr(name)` | Check if boolean attribute is present |
| `emit(eventName, detail)` | Dispatch custom event |
| `getBaseStyles()` | Get common base styles |
| `render()` | Override to render component |

## Observed Attributes

To react to attribute changes, define `observedAttributes`:

```javascript
static get observedAttributes() {
  return ['variant', 'size', 'disabled'];
}

attributeChangedCallback(name, oldValue, newValue) {
  if (oldValue !== newValue && this._initialized) {
    this.render();
  }
}
```

## Slots

Slots allow content projection from light DOM into Shadow DOM.

### Default Slot

```javascript
// Component
this.shadowRoot.innerHTML = `<div class="card"><slot></slot></div>`;
```

```html
<!-- Usage -->
<ui-card>This content goes in the default slot</ui-card>
```

### Named Slots

```javascript
// Component
this.shadowRoot.innerHTML = `
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
  <h3 slot="header">Card Title</h3>
  <p>Body content (default slot)</p>
  <ui-button slot="footer">Action</ui-button>
</ui-card>
```

### Slot Styling

Style slotted content with `::slotted()`:

```css
::slotted(h3) {
  margin: 0;
  font-size: var(--font-size-lg);
}

::slotted([slot="footer"]) {
  margin-top: auto;
}
```

## Custom Events

Emit events with the `ui-` prefix for consistency:

```javascript
// Inside component
this.shadowRoot.querySelector('button').addEventListener('click', (e) => {
  if (!this.hasAttr('disabled')) {
    this.emit('ui-click', { originalEvent: e });
  }
});
```

```html
<!-- Usage -->
<ui-button id="myBtn">Click</ui-button>
<script>
  document.getElementById('myBtn').addEventListener('ui-click', (e) => {
    console.log('Button clicked!', e.detail);
  });
</script>
```

### Event Options

The `emit()` method uses these defaults:

```javascript
emit(eventName, detail = null) {
  this.dispatchEvent(new CustomEvent(eventName, {
    bubbles: true,     // Event bubbles up
    composed: true,    // Crosses Shadow DOM boundary
    detail
  }));
}
```

## Component Composition

Higher-level components import their dependencies:

```javascript
// ui-header.js (organism)
import '../atoms/ui-button.js';
import '../atoms/ui-avatar.js';
import '../molecules/ui-search-bar.js';

class UiHeader extends BaseComponent {
  render() {
    this.shadowRoot.innerHTML = html`
      <style>/* ... */</style>
      <header class="header">
        <div class="brand"><slot name="brand"></slot></div>
        <slot name="search"></slot>
        <div class="actions"><slot name="actions"></slot></div>
      </header>
    `;
  }
}
```

### Import Paths

Use relative paths from the component file:

```javascript
// From components/organisms/ui-header.js
import '../atoms/ui-button.js';        // → components/atoms/ui-button.js
import '../molecules/ui-card.js';       // → components/molecules/ui-card.js
```

## Glassmorphism Pattern

For glassmorphism style, use these token patterns:

```css
.glass-component {
  /* Semi-transparent background */
  background: var(--glass-white-10);

  /* Blur effect */
  backdrop-filter: var(--backdrop-filter-glass-medium);
  -webkit-backdrop-filter: var(--backdrop-filter-glass-medium);

  /* Subtle border */
  border: 1px solid var(--border-glass-light);

  /* Rounded corners */
  border-radius: var(--radius-lg);

  /* Shadow with inner highlight */
  box-shadow: var(--shadow-glass-md);
}

/* Top highlight line */
.glass-component::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.15), transparent);
}

/* Hover with glow */
.glass-component:hover {
  border-color: var(--border-glass-medium);
  box-shadow: var(--shadow-glass-lg), var(--shadow-glow-primary);
}
```

## Size Variants Pattern

```css
/* Sizes */
.size-sm {
  padding: var(--spacing-2) var(--spacing-3);
  font-size: var(--font-size-sm);
}

.size-md {
  padding: var(--spacing-3) var(--spacing-6);
  font-size: var(--font-size-base);
}

.size-lg {
  padding: var(--spacing-4) var(--spacing-8);
  font-size: var(--font-size-lg);
}
```

## State Handling

### Disabled State

```javascript
// In render()
const disabled = this.hasAttr('disabled');

this.shadowRoot.innerHTML = html`
  <style>
    button:disabled {
      opacity: 0.4;
      cursor: not-allowed;
      transform: none !important;
    }
  </style>
  <button ${disabled ? 'disabled' : ''}>
    <slot></slot>
  </button>
`;
```

### Loading State

```javascript
const loading = this.hasAttr('loading');

this.shadowRoot.innerHTML = html`
  <style>
    .spinner {
      width: 1em;
      height: 1em;
      border: 2px solid currentColor;
      border-right-color: transparent;
      border-radius: 50%;
      animation: spin 0.75s linear infinite;
    }

    @keyframes spin {
      to { transform: rotate(360deg); }
    }
  </style>
  <button ${loading ? 'disabled' : ''}>
    ${loading ? '<span class="spinner"></span>' : ''}
    <slot></slot>
  </button>
`;
```

## Interactive States

```css
/* Focus visible for keyboard navigation */
button:focus-visible {
  outline: 2px solid var(--color-primary-400);
  outline-offset: 2px;
}

/* Hover with transform */
button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: var(--shadow-glow-primary);
}

/* Active press effect */
button:active:not(:disabled) {
  transform: translateY(0);
}
```

## Accessibility

### Focus Management

```javascript
// Forward focus to inner element
this.shadowRoot.querySelector('button').focus();
```

### ARIA Attributes

Forward ARIA from host to inner element:

```javascript
const ariaLabel = this.getAttribute('aria-label');
const ariaDescribedBy = this.getAttribute('aria-describedby');

this.shadowRoot.innerHTML = html`
  <button
    ${ariaLabel ? `aria-label="${ariaLabel}"` : ''}
    ${ariaDescribedBy ? `aria-describedby="${ariaDescribedBy}"` : ''}
  >
    <slot></slot>
  </button>
`;
```

### Keyboard Support

```javascript
this.shadowRoot.querySelector('button').addEventListener('keydown', (e) => {
  if (e.key === 'Enter' || e.key === ' ') {
    e.preventDefault();
    this.emit('ui-click', { originalEvent: e });
  }
});
```

## Browser Support

Web Components are natively supported in:

| Browser | Version |
|---------|---------|
| Chrome | 54+ |
| Firefox | 63+ |
| Safari | 10.1+ |
| Edge | 79+ |

No polyfill required for modern browsers.

## Fallback Pattern

For browsers without `backdrop-filter`:

```css
@supports not (backdrop-filter: blur(10px)) {
  .glass-component {
    background: var(--color-background-elevated);
  }
}
```

## File Structure

```
components/
├── base-component.js       # Base class (shared)
├── atoms/
│   ├── ui-button.js
│   ├── ui-input.js
│   ├── ui-badge.js
│   ├── ui-avatar.js
│   ├── ui-spinner.js
│   └── ui-divider.js
├── molecules/
│   ├── ui-card.js
│   ├── ui-form-field.js
│   ├── ui-search-bar.js
│   └── ui-nav-item.js
├── organisms/
│   ├── ui-header.js
│   ├── ui-sidebar.js
│   ├── ui-modal.js
│   └── ui-card-grid.js
├── templates/
│   ├── ui-dashboard-layout.js
│   ├── ui-auth-layout.js
│   └── ui-content-layout.js
└── index.js                # Barrel export
```

## Barrel Export (index.js)

```javascript
// Atoms
export * from './atoms/ui-button.js';
export * from './atoms/ui-input.js';
export * from './atoms/ui-badge.js';
export * from './atoms/ui-avatar.js';
export * from './atoms/ui-spinner.js';
export * from './atoms/ui-divider.js';

// Molecules
export * from './molecules/ui-card.js';
export * from './molecules/ui-form-field.js';
export * from './molecules/ui-search-bar.js';
export * from './molecules/ui-nav-item.js';

// Organisms
export * from './organisms/ui-header.js';
export * from './organisms/ui-sidebar.js';
export * from './organisms/ui-modal.js';
export * from './organisms/ui-card-grid.js';

// Templates
export * from './templates/ui-dashboard-layout.js';
export * from './templates/ui-auth-layout.js';
export * from './templates/ui-content-layout.js';
```

## Usage in Pages

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dashboard - MyApp</title>

  <!-- Tokens must be loaded in document for CSS Custom Properties -->
  <link rel="stylesheet" href="../tokens/tokens.css">

  <!-- Import all components via barrel -->
  <script type="module" src="../components/index.js"></script>
</head>
<body>
  <ui-dashboard-layout>
    <ui-sidebar slot="sidebar">
      <ui-nav-item icon="📊" active>Dashboard</ui-nav-item>
      <ui-nav-item icon="⚙️">Settings</ui-nav-item>
    </ui-sidebar>

    <ui-header slot="header" sticky>
      <span slot="brand">MyApp</span>
      <ui-search-bar slot="search"></ui-search-bar>
      <ui-button slot="actions" variant="primary">+ New</ui-button>
    </ui-header>

    <main>
      <ui-card-grid columns="3">
        <ui-card interactive>
          <span slot="header">Statistics</span>
          <p>12 tasks completed today</p>
          <ui-button slot="footer" variant="ghost">View All</ui-button>
        </ui-card>
      </ui-card-grid>
    </main>
  </ui-dashboard-layout>
</body>
</html>
```
