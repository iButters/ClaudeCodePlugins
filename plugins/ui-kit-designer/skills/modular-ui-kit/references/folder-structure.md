# Modular UI Kit Folder Structure

## Complete Directory Layout

```
[AppName]-UI-Kit/
│
├── index.html                          # Main preview hub
│
├── tokens/                             # Design System Tokens
│   ├── variables.css                   # All CSS custom properties
│   └── base.css                        # Reset & base styles
│
├── atoms/                              # Level 1: Basic Elements
│   ├── button/
│   │   ├── button.html
│   │   └── button.css
│   ├── input/
│   │   ├── input.html
│   │   └── input.css
│   ├── badge/
│   │   ├── badge.html
│   │   └── badge.css
│   ├── avatar/
│   │   ├── avatar.html
│   │   └── avatar.css
│   ├── checkbox/
│   │   ├── checkbox.html
│   │   └── checkbox.css
│   ├── toggle/
│   │   ├── toggle.html
│   │   └── toggle.css
│   ├── spinner/
│   │   ├── spinner.html
│   │   └── spinner.css
│   ├── progress-bar/
│   │   ├── progress-bar.html
│   │   └── progress-bar.css
│   └── icon/
│       ├── icon.html
│       └── icon.css
│
├── molecules/                          # Level 2: Combinations
│   ├── card/
│   │   ├── card.html
│   │   └── card.css
│   ├── list-item/
│   │   ├── list-item.html
│   │   └── list-item.css
│   ├── search-bar/
│   │   ├── search-bar.html
│   │   └── search-bar.css
│   ├── form-field/
│   │   ├── form-field.html
│   │   └── form-field.css
│   ├── nav-item/
│   │   ├── nav-item.html
│   │   └── nav-item.css
│   └── todo-item/
│       ├── todo-item.html
│       └── todo-item.css
│
├── organisms/                          # Level 3: Complex Sections
│   ├── header/
│   │   ├── header.html
│   │   └── header.css
│   ├── bottom-nav/
│   │   ├── bottom-nav.html
│   │   └── bottom-nav.css
│   ├── modal/
│   │   ├── modal.html
│   │   └── modal.css
│   ├── bottom-sheet/
│   │   ├── bottom-sheet.html
│   │   └── bottom-sheet.css
│   └── toast/
│       ├── toast.html
│       └── toast.css
│
├── pages/                              # Level 4: Complete Screens
│   ├── home/
│   │   ├── home.html
│   │   └── home.css
│   ├── detail/
│   │   ├── detail.html
│   │   └── detail.css
│   ├── settings/
│   │   ├── settings.html
│   │   └── settings.css
│   ├── empty-state/
│   │   ├── empty-state.html
│   │   └── empty-state.css
│   └── loading/
│       ├── loading.html
│       └── loading.css
│
└── docs/
    └── design-system.html              # Design system documentation
```

## tokens/variables.css

```css
:root {
  /* === Colors === */
  /* Backgrounds */
  --bg-primary: #0D0D1A;
  --bg-secondary: #1A1A2E;
  --bg-tertiary: #252540;

  /* Brand */
  --primary: #6366F1;
  --primary-light: #818CF8;
  --primary-dark: #4F46E5;
  --primary-gradient: linear-gradient(135deg, #6366F1, #8B5CF6);

  /* Accent */
  --accent: #8B5CF6;

  /* Semantic */
  --success: #22C55E;
  --warning: #F59E0B;
  --error: #EF4444;
  --info: #3B82F6;

  /* Text */
  --text-primary: #FFFFFF;
  --text-secondary: #94A3B8;
  --text-muted: #64748B;

  /* Glass Effects */
  --glass-bg: rgba(255, 255, 255, 0.05);
  --glass-bg-hover: rgba(255, 255, 255, 0.08);
  --glass-border: rgba(255, 255, 255, 0.1);

  /* === Typography === */
  --font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-size-xs: 11px;
  --font-size-sm: 13px;
  --font-size-base: 15px;
  --font-size-lg: 18px;
  --font-size-xl: 22px;
  --font-size-2xl: 28px;

  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;

  /* === Spacing === */
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;
  --space-2xl: 48px;

  /* === Border Radius === */
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;
  --radius-xl: 20px;
  --radius-full: 9999px;

  /* === Shadows === */
  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.4);
  --shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.5);
  --shadow-primary: 0 8px 24px rgba(99, 102, 241, 0.4);
  --shadow-phone: 0 25px 50px -12px rgba(0, 0, 0, 0.5);

  /* === Transitions === */
  --transition-fast: 150ms ease;
  --transition-base: 200ms ease;
  --transition-slow: 300ms ease;

  /* === Layout === */
  --phone-width: 390px;
  --phone-height: 844px;
  --phone-radius: 40px;
  --phone-border: 8px;
  --bottom-nav-height: 70px;
  --header-height: 56px;
}
```

## tokens/base.css

```css
/* CSS Reset */
*, *::before, *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Base HTML */
html {
  font-size: 16px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body {
  font-family: var(--font-family);
  font-size: var(--font-size-base);
  line-height: 1.5;
  color: var(--text-primary);
  background: var(--bg-primary);
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
  font-weight: var(--font-weight-bold);
  line-height: 1.3;
}

/* Links */
a {
  color: var(--primary);
  text-decoration: none;
}

/* Buttons */
button {
  font-family: inherit;
  cursor: pointer;
  border: none;
  background: none;
}

/* Images */
img {
  max-width: 100%;
  height: auto;
  display: block;
}

/* Screen Reader Only */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

## Naming Conventions

### Files
| Type | Convention | Example |
|------|------------|---------|
| Folder | kebab-case | `search-bar/`, `bottom-nav/` |
| HTML | kebab-case | `search-bar.html` |
| CSS | kebab-case | `search-bar.css` |

### CSS Classes (BEM)
| Type | Convention | Example |
|------|------------|---------|
| Block | kebab-case | `.search-bar` |
| Element | `__` suffix | `.search-bar__input` |
| Modifier | `--` suffix | `.search-bar--focused` |
| State | `--` or `is-` | `.btn--loading`, `.is-active` |

### CSS Variables
| Type | Convention | Example |
|------|------------|---------|
| Color | `--[category]-[name]` | `--bg-primary`, `--text-secondary` |
| Spacing | `--space-[size]` | `--space-md`, `--space-lg` |
| Radius | `--radius-[size]` | `--radius-md`, `--radius-full` |
| Shadow | `--shadow-[size]` | `--shadow-sm`, `--shadow-primary` |
