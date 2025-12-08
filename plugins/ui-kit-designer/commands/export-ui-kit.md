---
name: export-ui-kit
description: Export design assets from a UI kit in various formats (CSS, Tailwind, JSON tokens, Blazor, React, SCSS).
argument-hint: <format> [--output <path>] [--components] [--only <items>]
allowed-tools: ["Read", "Write", "Glob"]
---

# Export UI Kit Command

Extract design tokens, CSS, or component code from your UI kit for use in development.

## Usage

```
/ui-kit export <format> [options]
```

## Formats

### CSS Variables
```
/ui-kit export css
```
Exports design tokens as CSS custom properties:
```css
:root {
  --color-primary: #6366F1;
  --color-success: #22C55E;
  --spacing-md: 16px;
  --radius-lg: 16px;
  /* ... */
}
```

### Tailwind Config
```
/ui-kit export tailwind
```
Generates a Tailwind CSS configuration:
```js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: '#6366F1',
        success: '#22C55E',
      },
      spacing: {
        // ...
      }
    }
  }
}
```

### Design Tokens JSON
```
/ui-kit export tokens
```
Exports structured design tokens:
```json
{
  "colors": {
    "primary": { "value": "#6366F1" },
    "success": { "value": "#22C55E" }
  },
  "spacing": {
    "md": { "value": "16px" }
  }
}
```

### Blazor Components
```
/ui-kit export blazor
```
Generates Blazor component templates with CSS.

### React Components
```
/ui-kit export react
```
Generates React components with styled-components or CSS modules.

### SCSS Variables
```
/ui-kit export scss
```
Exports as SCSS variables:
```scss
$color-primary: #6366F1;
$color-success: #22C55E;
$spacing-md: 16px;
```

## Options

- `--output <path>`: Specify output file/directory
- `--components`: Include component definitions
- `--only <items>`: Export only specific items (colors, typography, spacing)

## Examples

### Export Colors Only
```
/ui-kit export css --only colors
```

### Export to Specific File
```
/ui-kit export css --output ./src/styles/tokens.css
```

### Export Components
```
/ui-kit export blazor --components
```

## Output Files

Exports are saved to:
```
output/
├── exports/
│   ├── tokens.css
│   ├── tokens.json
│   ├── tailwind.config.js
│   └── components/
│       ├── Button.razor
│       ├── Card.razor
│       └── ...
```

## Integration Tips

### With CSS Variables
Import the CSS file and use variables:
```css
.button {
  background: var(--color-primary);
  padding: var(--spacing-md);
}
```

### With Tailwind
Add the config to your tailwind.config.js:
```js
const designTokens = require('./exports/tailwind.config.js');
module.exports = {
  ...designTokens,
  // your other config
}
```

### With Blazor
Copy components to your project:
```
cp exports/components/*.razor src/Components/
```
