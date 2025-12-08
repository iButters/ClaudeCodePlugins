# Design Token Theming Guide

## Overview

Design tokens support multiple themes through semantic token mapping. This guide covers light/dark mode implementation and custom theme creation.

## Theme Architecture

### Token Layers

1. **Primitive Tokens** - Raw values (colors, sizes)
2. **Semantic Tokens** - Purpose-based (background, text)
3. **Component Tokens** - Component-specific (button-bg)

## Theme Switching Strategies

### CSS Custom Properties (Recommended)

```css
:root {
  --color-bg: var(--color-white);
  --color-text: var(--color-gray-900);
}

[data-theme="dark"] {
  --color-bg: var(--color-gray-900);
  --color-text: var(--color-gray-50);
}
```

### CSS Class Toggle

```css
.light { --color-bg: #ffffff; }
.dark { --color-bg: #1f2937; }
```

### System Preference

```css
@media (prefers-color-scheme: dark) {
  :root { --color-bg: #1f2937; }
}
```

## Color Contrast Requirements

### WCAG 2.1 Standards

| Level | Normal Text | Large Text |
|-------|-------------|------------|
| AA    | 4.5:1       | 3:1        |
| AAA   | 7:1         | 4.5:1      |

### Recommended Pairings

**Light Mode:**
- Background: neutral-50 (#F9FAFB)
- Text: neutral-900 (#111827)
- Contrast: 15.8:1

**Dark Mode:**
- Background: neutral-900 (#111827)
- Text: neutral-50 (#F9FAFB)
- Contrast: 15.8:1

## Semantic Token Mapping

```typescript
const semanticTokens = {
  light: {
    // Backgrounds
    'bg-primary': 'white',
    'bg-secondary': 'neutral-50',
    'bg-tertiary': 'neutral-100',

    // Text
    'text-primary': 'neutral-900',
    'text-secondary': 'neutral-600',
    'text-muted': 'neutral-400',
    'text-inverse': 'white',

    // Borders
    'border-default': 'neutral-200',
    'border-strong': 'neutral-300',
    'border-focus': 'primary-500',

    // Interactive
    'interactive-primary': 'primary-600',
    'interactive-hover': 'primary-700',
    'interactive-active': 'primary-800',
  },
  dark: {
    // Backgrounds
    'bg-primary': 'neutral-900',
    'bg-secondary': 'neutral-800',
    'bg-tertiary': 'neutral-700',

    // Text
    'text-primary': 'neutral-50',
    'text-secondary': 'neutral-300',
    'text-muted': 'neutral-500',
    'text-inverse': 'neutral-900',

    // Borders
    'border-default': 'neutral-700',
    'border-strong': 'neutral-600',
    'border-focus': 'primary-400',

    // Interactive
    'interactive-primary': 'primary-500',
    'interactive-hover': 'primary-400',
    'interactive-active': 'primary-300',
  },
};
```

## Implementation Examples

### React Context Theme Provider

```typescript
import { createContext, useContext, useState, useEffect } from 'react';

type Theme = 'light' | 'dark' | 'system';

interface ThemeContextValue {
  theme: Theme;
  setTheme: (theme: Theme) => void;
  resolvedTheme: 'light' | 'dark';
}

const ThemeContext = createContext<ThemeContextValue | null>(null);

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useState<Theme>('system');
  const [resolvedTheme, setResolvedTheme] = useState<'light' | 'dark'>('light');

  useEffect(() => {
    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');

    const updateResolvedTheme = () => {
      if (theme === 'system') {
        setResolvedTheme(mediaQuery.matches ? 'dark' : 'light');
      } else {
        setResolvedTheme(theme);
      }
    };

    updateResolvedTheme();
    mediaQuery.addEventListener('change', updateResolvedTheme);

    return () => mediaQuery.removeEventListener('change', updateResolvedTheme);
  }, [theme]);

  useEffect(() => {
    document.documentElement.dataset.theme = resolvedTheme;
  }, [resolvedTheme]);

  return (
    <ThemeContext.Provider value={{ theme, setTheme, resolvedTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

export function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) throw new Error('useTheme must be used within ThemeProvider');
  return context;
}
```

### Theme Toggle Component

```typescript
function ThemeToggle() {
  const { theme, setTheme, resolvedTheme } = useTheme();

  return (
    <button
      onClick={() => setTheme(resolvedTheme === 'light' ? 'dark' : 'light')}
      aria-label={`Switch to ${resolvedTheme === 'light' ? 'dark' : 'light'} mode`}
    >
      {resolvedTheme === 'light' ? '🌙' : '☀️'}
    </button>
  );
}
```

## Custom Theme Creation

### Step 1: Define Base Palette

```json
{
  "brand": {
    "primary": "#custom-color",
    "secondary": "#custom-color"
  }
}
```

### Step 2: Generate Scales

Use color manipulation to create 50-900 scale from base.

### Step 3: Map Semantic Tokens

```json
{
  "themes": {
    "custom": {
      "background": "{color.brand.50}",
      "text": "{color.brand.900}"
    }
  }
}
```

### Step 4: Export Theme

Generate CSS, Tailwind, or JSON output for theme.

## Best Practices

1. **Use semantic tokens** - Reference by purpose, not value
2. **Test contrast ratios** - Ensure accessibility in all themes
3. **Provide system option** - Respect user preferences
4. **Persist selection** - Remember user's theme choice
5. **Prevent flash** - Apply theme before render
