# Material Design Style Guide

## Core Characteristics

Material Design uses:
- Elevation-based shadows
- Bold colors
- Ripple effects on interaction
- Clear visual hierarchy
- Motion and transitions
- Grid-based layouts

## Required Tokens

```css
:root {
  /* Elevation shadows */
  --elevation-0: none;
  --elevation-1: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
  --elevation-2: 0 3px 6px rgba(0,0,0,0.15), 0 2px 4px rgba(0,0,0,0.12);
  --elevation-3: 0 10px 20px rgba(0,0,0,0.15), 0 3px 6px rgba(0,0,0,0.10);
  --elevation-4: 0 15px 25px rgba(0,0,0,0.15), 0 5px 10px rgba(0,0,0,0.05);
  --elevation-5: 0 20px 40px rgba(0,0,0,0.2);

  /* Surface colors */
  --surface-ground: #fafafa;
  --surface-card: #ffffff;
  --surface-overlay: rgba(0, 0, 0, 0.5);

  /* Material transitions */
  --motion-standard: 300ms cubic-bezier(0.4, 0, 0.2, 1);
  --motion-decelerate: 300ms cubic-bezier(0, 0, 0.2, 1);
  --motion-accelerate: 300ms cubic-bezier(0.4, 0, 1, 1);

  /* State layers */
  --state-hover: rgba(0, 0, 0, 0.04);
  --state-focus: rgba(0, 0, 0, 0.12);
  --state-pressed: rgba(0, 0, 0, 0.16);
  --state-dragged: rgba(0, 0, 0, 0.08);
}
```

## Component Patterns

### Card

```css
.material-card {
  background: var(--surface-card);
  border-radius: 4px;
  box-shadow: var(--elevation-1);
  transition: box-shadow var(--motion-standard);
}

.material-card:hover {
  box-shadow: var(--elevation-3);
}
```

### Button (Contained)

```css
.material-button {
  background: var(--color-primary-500);
  color: white;
  border: none;
  border-radius: 4px;
  padding: 0 16px;
  min-height: 36px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  box-shadow: var(--elevation-2);
  transition: box-shadow var(--motion-standard);
  position: relative;
  overflow: hidden;
}

.material-button:hover {
  box-shadow: var(--elevation-3);
}

.material-button:active {
  box-shadow: var(--elevation-4);
}
```

### Ripple Effect (CSS-only approximation)

```css
.material-button::after {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle, rgba(255,255,255,0.3) 0%, transparent 70%);
  transform: scale(0);
  opacity: 0;
  transition: transform 0.3s, opacity 0.3s;
}

.material-button:active::after {
  transform: scale(2);
  opacity: 1;
  transition: transform 0s, opacity 0s;
}
```

### Text Field

```css
.material-input {
  border: none;
  border-bottom: 1px solid var(--color-neutral-400);
  background: transparent;
  padding: 16px 0 8px;
  font-size: 16px;
  transition: border-color var(--motion-standard);
}

.material-input:focus {
  outline: none;
  border-bottom: 2px solid var(--color-primary-500);
}

/* Floating label pattern */
.material-field {
  position: relative;
}

.material-label {
  position: absolute;
  top: 16px;
  left: 0;
  color: var(--color-neutral-500);
  transition: all var(--motion-standard);
  pointer-events: none;
}

.material-input:focus + .material-label,
.material-input:not(:placeholder-shown) + .material-label {
  top: 0;
  font-size: 12px;
  color: var(--color-primary-500);
}
```

## Elevation Guidelines

| Component | Resting | Raised |
|-----------|---------|--------|
| Card | 1 | 3 |
| Button | 2 | 4 |
| FAB | 3 | 5 |
| Dialog | 5 | 5 |
| Navigation drawer | 4 | 4 |

## Key Design Rules

1. **Elevation creates hierarchy**: Higher = more important
2. **Consistent shadows**: Use the elevation scale
3. **Bold primary colors**: Use 500 shade as primary
4. **State layers**: Overlay on hover/focus/pressed
5. **8dp grid**: Spacing should be multiples of 8
6. **Motion**: Use standard curves for transitions
