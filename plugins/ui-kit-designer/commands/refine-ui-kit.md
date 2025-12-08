---
name: refine-ui-kit
description: Refine and iterate on an existing UI kit based on feedback.
argument-hint: <feedback>
allowed-tools: ["Read", "Write", "Glob", "Grep"]
---

# Refine UI Kit Command

Make targeted improvements to an existing UI kit based on your feedback.

## Usage

```
/ui-kit refine <feedback>
```

## Arguments

- `<feedback>`: Description of what to change or improve

## Examples

### Visual Changes
```
/ui-kit refine "The buttons need more padding and rounder corners"
```

```
/ui-kit refine "Use a warmer color palette, more orange tones"
```

```
/ui-kit refine "Make the text larger for better readability"
```

### Component Changes
```
/ui-kit refine "Add icons to all navigation items"
```

```
/ui-kit refine "The cards should have a subtle border"
```

```
/ui-kit refine "Add a loading skeleton to the list view"
```

### Screen Changes
```
/ui-kit refine "The settings page needs a dark mode toggle"
```

```
/ui-kit refine "Add a confirmation modal before deleting items"
```

```
/ui-kit refine "The empty state should be more encouraging"
```

### Layout Changes
```
/ui-kit refine "Use a 2-column grid for the product cards"
```

```
/ui-kit refine "Add more whitespace between sections"
```

```
/ui-kit refine "The bottom navigation should have labels"
```

### Style Changes
```
/ui-kit refine "Make it feel more premium and luxurious"
```

```
/ui-kit refine "Add subtle animations to the buttons"
```

```
/ui-kit refine "The glassmorphism effect is too strong, tone it down"
```

## What Gets Updated

With the modular UI kit structure, refinements target specific files:

| Feedback Type | Files Updated |
|--------------|---------------|
| Button styling | `atoms/button/button.css` |
| Card layout | `molecules/card/card.css` |
| Color changes | `tokens/variables.css` |
| Typography | `tokens/variables.css`, `tokens/base.css` |
| Screen layout | `pages/[screen]/[screen].css` |
| New component | Creates new folder in `atoms/`, `molecules/`, or `organisms/` |
| New screen | Creates new folder in `pages/` |

The `index.html` automatically reflects changes since it links all CSS files.

## Workflow

1. Open `[AppName]-UI-Kit/index.html` in browser
2. Note specific improvements needed
3. Run refine command with feedback
4. Refresh browser to see changes
5. Repeat until satisfied

## Tips

- Be specific about what elements to change
- Reference screen names when targeting specific areas
- Describe the feeling/emotion you want, not just technical specs
- Request before/after comparison if needed
- Use "Keep X but change Y" format for partial changes

## Multiple Changes

For multiple independent changes, list them:

```
/ui-kit refine "1. Increase button padding to 16px, 2. Use a purple accent color instead of blue, 3. Add subtle shadows to cards"
```
