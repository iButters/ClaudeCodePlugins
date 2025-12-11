# Neumorphism Style Guide

## Core Characteristics

Neumorphism (Soft UI) creates a soft, extruded plastic look with:
- Dual shadows (light and dark)
- Same background color as surface
- Soft, pillow-like appearance
- Minimal borders
- Subtle depth illusion

## Required Tokens

```css
:root {
  /* Base surface color */
  --neu-surface: #e0e5ec;
  --neu-surface-dark: #2d3748; /* For dark mode */

  /* Light source shadows */
  --neu-shadow-light: rgba(255, 255, 255, 0.8);
  --neu-shadow-dark: rgba(163, 177, 198, 0.6);

  /* Dark mode shadows */
  --neu-shadow-light-dark: rgba(255, 255, 255, 0.05);
  --neu-shadow-dark-dark: rgba(0, 0, 0, 0.5);

  /* Shadow distances */
  --neu-distance-sm: 4px;
  --neu-distance-md: 8px;
  --neu-distance-lg: 12px;

  /* Raised effect */
  --neu-shadow-raised:
    6px 6px 12px var(--neu-shadow-dark),
    -6px -6px 12px var(--neu-shadow-light);

  /* Inset/pressed effect */
  --neu-shadow-inset:
    inset 6px 6px 12px var(--neu-shadow-dark),
    inset -6px -6px 12px var(--neu-shadow-light);

  /* Flat (no shadow) */
  --neu-shadow-flat: none;
}
```

## Component Patterns

### Raised Element (Default State)

```css
.neu-raised {
  background: var(--neu-surface);
  border-radius: var(--radius-xl);
  box-shadow: var(--neu-shadow-raised);
  border: none; /* No borders in neumorphism */
}
```

### Pressed/Inset Element (Active State)

```css
.neu-inset {
  background: var(--neu-surface);
  border-radius: var(--radius-xl);
  box-shadow: var(--neu-shadow-inset);
}
```

### Button Pattern

```css
.neu-button {
  background: var(--neu-surface);
  border: none;
  border-radius: var(--radius-xl);
  box-shadow: var(--neu-shadow-raised);
  transition: box-shadow 0.2s ease;
}

.neu-button:hover {
  box-shadow:
    8px 8px 16px var(--neu-shadow-dark),
    -8px -8px 16px var(--neu-shadow-light);
}

.neu-button:active {
  box-shadow: var(--neu-shadow-inset);
}
```

### Input Pattern

```css
.neu-input {
  background: var(--neu-surface);
  border: none;
  border-radius: var(--radius-lg);
  box-shadow: var(--neu-shadow-inset);
  padding: 1rem;
}

.neu-input:focus {
  box-shadow:
    var(--neu-shadow-inset),
    0 0 0 2px var(--color-primary-400);
}
```

## Key Design Rules

1. **Same background color**: Elements should match the background
2. **Dual shadows**: Always use both light and dark shadows
3. **Light source**: Assume top-left light source
4. **No borders**: Use shadows instead of borders
5. **Soft corners**: Use large border-radius values
6. **Subtle contrast**: Avoid high contrast elements

## Accessibility Concerns

Neumorphism can have contrast issues:
- Ensure text has sufficient contrast
- Add focus indicators for interactive elements
- Consider providing a high-contrast mode

## Dark Mode Adaptation

```css
@media (prefers-color-scheme: dark) {
  :root {
    --neu-surface: var(--neu-surface-dark);
    --neu-shadow-light: var(--neu-shadow-light-dark);
    --neu-shadow-dark: var(--neu-shadow-dark-dark);
  }
}
```
