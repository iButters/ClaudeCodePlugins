# Glassmorphism Style Guide

## Core Characteristics

Glassmorphism creates a "frosted glass" effect with:
- Semi-transparent backgrounds
- Background blur (backdrop-filter)
- Subtle borders
- Light/glow effects
- Works best on colorful backgrounds

## Required Tokens

```css
:root {
  /* Glass backgrounds */
  --glass-white-5: rgba(255, 255, 255, 0.05);
  --glass-white-10: rgba(255, 255, 255, 0.10);
  --glass-white-15: rgba(255, 255, 255, 0.15);
  --glass-white-20: rgba(255, 255, 255, 0.20);

  /* Glass borders */
  --border-glass-subtle: rgba(255, 255, 255, 0.08);
  --border-glass-light: rgba(255, 255, 255, 0.12);
  --border-glass-medium: rgba(255, 255, 255, 0.18);

  /* Backdrop filters */
  --backdrop-filter-glass-light: blur(8px) saturate(180%);
  --backdrop-filter-glass-medium: blur(12px) saturate(180%);
  --backdrop-filter-glass-heavy: blur(16px) saturate(200%);

  /* Glass shadows */
  --shadow-glass-sm: 0 4px 16px rgba(0, 0, 0, 0.15), inset 0 1px 0 rgba(255, 255, 255, 0.1);
  --shadow-glass-md: 0 8px 32px rgba(0, 0, 0, 0.2), inset 0 1px 0 rgba(255, 255, 255, 0.1);
  --shadow-glass-lg: 0 16px 48px rgba(0, 0, 0, 0.25), inset 0 1px 0 rgba(255, 255, 255, 0.15);

  /* Glow effects */
  --shadow-glow-primary: 0 0 20px rgba(139, 92, 246, 0.3), 0 0 40px rgba(139, 92, 246, 0.15);
}
```

## Component Pattern

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

/* Hover state with glow */
.glass-component:hover {
  border-color: var(--border-glass-medium);
  box-shadow: var(--shadow-glass-lg), var(--shadow-glow-primary);
}
```

## Background Requirements

Glassmorphism needs a colorful background to show the blur effect:

```css
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background:
    radial-gradient(ellipse at 20% 20%, var(--color-primary-600) 0%, transparent 50%),
    radial-gradient(ellipse at 80% 80%, var(--color-secondary-600) 0%, transparent 50%),
    radial-gradient(ellipse at 50% 50%, var(--color-accent-600) 0%, transparent 50%);
  opacity: 0.15;
  z-index: -1;
}
```

## Browser Fallback

```css
@supports not (backdrop-filter: blur(10px)) {
  .glass-component {
    background: var(--color-background-elevated);
  }
}
```

## Dark Theme

Glassmorphism works best on dark themes:
- Dark gradient backgrounds
- White semi-transparent overlays
- Subtle colored glows
