---
name: Design Tokens
description: This skill should be used when the user asks to "create design tokens", "generate a design system", "define color palette", "set up typography scale", "configure spacing system", "create CSS variables", "generate Tailwind config", "export tokens to JSON", "implement dark mode", "create theme variables", or needs guidance on design token structure, naming conventions, or multi-format token generation for UI kits.
version: 0.1.0
---

# Design Tokens for UI-Kit Generator

## Overview

Design tokens are the atomic values of a design system - colors, typography, spacing, shadows, and more. This skill generates consistent, scalable design tokens in multiple output formats with full theming support.

**Key capabilities:**
- Generate complete token sets from minimal input
- Support multiple output formats (CSS, Tailwind, JSON, TypeScript)
- Implement Light/Dark mode theming
- Follow industry naming conventions
- Validate token consistency

## Token Categories

### Colors

Generate semantic color tokens from a base palette:

**Input (minimal):**
```json
{
  "primary": "#3B82F6",
  "secondary": "#8B5CF6",
  "accent": "#F59E0B"
}
```

**Generated tokens:**
- Primary scale (50-900)
- Semantic colors (background, surface, text)
- State colors (success, warning, error, info)
- Neutral scale (gray 50-900)

### Typography

Define typography tokens:

```json
{
  "fontFamilies": {
    "heading": "Inter, system-ui, sans-serif",
    "body": "Inter, system-ui, sans-serif",
    "mono": "JetBrains Mono, monospace"
  },
  "fontSizes": {
    "xs": "0.75rem",
    "sm": "0.875rem",
    "md": "1rem",
    "lg": "1.125rem",
    "xl": "1.25rem",
    "2xl": "1.5rem",
    "3xl": "1.875rem",
    "4xl": "2.25rem"
  }
}
```

**Additional typography tokens:**
- Font weights (light: 300, regular: 400, medium: 500, semibold: 600, bold: 700)
- Line heights (tight: 1.25, normal: 1.5, relaxed: 1.75)
- Letter spacing (tight: -0.025em, normal: 0, wide: 0.025em)

### Spacing

Use a consistent spacing scale based on a base unit (typically 4px):

```
0: 0px
1: 0.25rem (4px)
2: 0.5rem (8px)
3: 0.75rem (12px)
4: 1rem (16px)
5: 1.25rem (20px)
6: 1.5rem (24px)
8: 2rem (32px)
10: 2.5rem (40px)
12: 3rem (48px)
16: 4rem (64px)
20: 5rem (80px)
24: 6rem (96px)
```

### Borders

```json
{
  "radius": {
    "none": "0",
    "sm": "0.125rem",
    "md": "0.375rem",
    "lg": "0.5rem",
    "xl": "0.75rem",
    "2xl": "1rem",
    "full": "9999px"
  },
  "width": {
    "0": "0px",
    "1": "1px",
    "2": "2px",
    "4": "4px"
  }
}
```

### Shadows

```json
{
  "none": "none",
  "sm": "0 1px 2px 0 rgb(0 0 0 / 0.05)",
  "md": "0 4px 6px -1px rgb(0 0 0 / 0.1)",
  "lg": "0 10px 15px -3px rgb(0 0 0 / 0.1)",
  "xl": "0 20px 25px -5px rgb(0 0 0 / 0.1)",
  "2xl": "0 25px 50px -12px rgb(0 0 0 / 0.25)"
}
```

### Transitions

```json
{
  "duration": {
    "fast": "150ms",
    "normal": "300ms",
    "slow": "500ms"
  },
  "easing": {
    "ease-in": "cubic-bezier(0.4, 0, 1, 1)",
    "ease-out": "cubic-bezier(0, 0, 0.2, 1)",
    "ease-in-out": "cubic-bezier(0.4, 0, 0.2, 1)"
  }
}
```

### Breakpoints

```json
{
  "sm": "640px",
  "md": "768px",
  "lg": "1024px",
  "xl": "1280px",
  "2xl": "1536px"
}
```

## Output Formats

### CSS Custom Properties

Generate `:root` variables with optional dark mode:

```css
:root {
  --color-primary-500: #3B82F6;
  --font-size-md: 1rem;
  --spacing-4: 1rem;
}

[data-theme="dark"] {
  --color-background: #1F2937;
  --color-text: #F9FAFB;
}
```

### Tailwind Configuration

Generate `tailwind.config.js` extending default theme:

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: { 500: '#3B82F6' }
      }
    }
  }
}
```

### JSON Token File

Standard token format for tooling integration:

```json
{
  "color": {
    "primary": {
      "500": { "value": "#3B82F6", "type": "color" }
    }
  }
}
```

### TypeScript Constants

Type-safe token exports:

```typescript
export const colors = {
  primary: { 500: '#3B82F6' }
} as const;

export type ColorToken = keyof typeof colors;
```

## Theming Support

### Light/Dark Mode

Generate paired token sets:

1. Define base semantic tokens
2. Create light theme values
3. Create dark theme values
4. Generate theme-aware output

**Pattern:**
```json
{
  "themes": {
    "light": {
      "background": "{color.white}",
      "text": "{color.gray.900}"
    },
    "dark": {
      "background": "{color.gray.900}",
      "text": "{color.gray.50}"
    }
  }
}
```

## Token Generation Workflow

1. **Gather requirements:**
   - Ask for brand colors (primary, secondary, accent)
   - Determine typography preferences
   - Identify target output formats

2. **Generate base tokens:**
   - Create color scales from base colors
   - Build typography scale
   - Define spacing system

3. **Apply theming:**
   - Generate light mode defaults
   - Create dark mode variants
   - Map semantic tokens to theme values

4. **Output transformation:**
   - Convert to requested formats
   - Validate token consistency
   - Generate documentation

## Quick Reference

### Naming Conventions

| Category | Pattern | Example |
|----------|---------|---------|
| Colors | `color-{semantic}-{shade}` | `color-primary-500` |
| Typography | `font-{property}-{size}` | `font-size-lg` |
| Spacing | `spacing-{scale}` | `spacing-4` |
| Borders | `border-{property}-{size}` | `border-radius-md` |
| Shadows | `shadow-{size}` | `shadow-lg` |

### Color Scale Generation

From a base color, generate:
- 50: 95% lightness
- 100: 90% lightness
- 200: 80% lightness
- 300: 70% lightness
- 400: 60% lightness
- 500: Base color
- 600: 40% lightness
- 700: 30% lightness
- 800: 20% lightness
- 900: 10% lightness

## Best Practices

**DO:**
- Use semantic naming (primary, danger) over descriptive (blue, red)
- Maintain consistent scale progressions
- Document token purpose and usage
- Include fallback values
- Test contrast ratios

**DON'T:**
- Hard-code values in components
- Skip intermediate scale steps
- Mix naming conventions
- Ignore accessibility requirements

## Additional Resources

- **`references/output-formats.md`** - Detailed format templates
- **`references/theming-guide.md`** - Advanced theming patterns
- **`examples/tokens-complete.json`** - Full token example
- **`examples/css-variables.css`** - CSS output example
- **`examples/tailwind.config.js`** - Tailwind config example
