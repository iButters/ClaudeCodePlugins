---
name: UI Kit Design
description: This skill should be used when the user asks to "create a UI kit", "design an interface", "mockup screens", "visual prototype", "design system", "front-end design", "app design", or needs guidance on creating comprehensive HTML-based UI kits for iterative design workflows.
version: 1.0.0
---

# UI Kit Design for Iterative Front-End Development

## Overview

This skill enables the creation of standalone HTML UI kits that serve as interactive design specifications. These kits allow designers and developers to visualize, iterate, and document application interfaces before implementation.

**Key concepts:**
- Standalone HTML files with embedded CSS/JS
- Phone frame mockups for mobile apps
- Design system documentation
- Interactive navigation between screens
- Iterative refinement workflow

## UI Kit File Structure

### Complete HTML Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[AppName] - UI Kit</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    /* 1. CSS Reset */
    * { margin: 0; padding: 0; box-sizing: border-box; }
    
    /* 2. Design Tokens */
    :root {
      --bg-primary: #0D0D1A;
      --bg-secondary: #1A1A2E;
      --primary: #6366F1;
      --primary-gradient: linear-gradient(135deg, #6366F1, #8B5CF6);
      --text-primary: #FFFFFF;
      --text-secondary: #94A3B8;
      --text-muted: #64748B;
      --glass-bg: rgba(255, 255, 255, 0.05);
      --glass-border: rgba(255, 255, 255, 0.1);
      --success: #22C55E;
      --warning: #F59E0B;
      --error: #EF4444;
      --radius-md: 12px;
      --radius-lg: 16px;
      --radius-xl: 20px;
    }
    
    /* 3. Base Styles */
    body {
      font-family: 'Inter', -apple-system, sans-serif;
      background: var(--bg-primary);
      min-height: 100vh;
      padding: 40px;
    }
    
    /* 4. Layout Styles */
    .container { max-width: 1400px; margin: 0 auto; }
    .frames-grid { display: flex; flex-wrap: wrap; gap: 40px; justify-content: center; }
    
    /* 5. Phone Frame Styles */
    .phone-frame {
      width: 390px;
      height: 844px;
      background: var(--bg-primary);
      border-radius: 40px;
      border: 8px solid var(--bg-secondary);
      overflow: hidden;
      position: relative;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
    }
    
    /* 6. Navigation Styles */
    .nav-tabs { display: flex; gap: 8px; justify-content: center; margin-bottom: 40px; flex-wrap: wrap; }
    .nav-tab { background: var(--glass-bg); color: var(--text-secondary); padding: 12px 24px; border-radius: var(--radius-md); cursor: pointer; border: none; font-family: inherit; font-size: 14px; }
    .nav-tab.active { background: var(--primary); color: white; }
    
    /* 7. Section Styles */
    .frames-section { display: none; }
    .frames-section.active { display: flex; flex-wrap: wrap; gap: 40px; justify-content: center; }
  </style>
</head>
<body>
  <div class="container">
    <h1>🎨 [AppName] UI Kit</h1>
    <p class="subtitle">[Design Description]</p>
    
    <!-- Navigation -->
    <div class="nav-tabs">
      <button class="nav-tab active" onclick="showSection('all')">All Frames</button>
      <!-- Add more tabs for individual screens -->
      <button class="nav-tab" onclick="showSection('design')">Design System</button>
    </div>
    
    <!-- All Frames Section -->
    <div class="frames-section active" id="section-all">
      <!-- Phone frames here -->
    </div>
    
    <!-- Design System Section -->
    <div class="frames-section" id="section-design">
      <!-- Color swatches, typography, spacing docs -->
    </div>
  </div>
  
  <script>
    function showSection(section) {
      document.querySelectorAll('.frames-section').forEach(s => s.classList.remove('active'));
      document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
      document.getElementById('section-' + section).classList.add('active');
      event.target.classList.add('active');
    }
  </script>
</body>
</html>
```

## Design Tokens

### Color System

| Token | Value | Usage |
|-------|-------|-------|
| `--bg-primary` | #0D0D1A | Main background |
| `--bg-secondary` | #1A1A2E | Cards, surfaces |
| `--bg-tertiary` | #252540 | Elevated surfaces |
| `--primary` | #6366F1 | Primary brand color |
| `--primary-light` | #818CF8 | Hover states |
| `--primary-dark` | #4F46E5 | Active states |
| `--success` | #22C55E | Success states |
| `--warning` | #F59E0B | Warning states |
| `--error` | #EF4444 | Error states |
| `--text-primary` | #FFFFFF | Main text |
| `--text-secondary` | #94A3B8 | Secondary text |
| `--text-muted` | #64748B | Muted/disabled text |

### Typography Scale

| Name | Size | Weight | Line Height |
|------|------|--------|-------------|
| Display | 28px | 700 | 1.2 |
| Heading | 22px | 700 | 1.3 |
| Title | 18px | 600 | 1.4 |
| Body | 15-16px | 400-500 | 1.5 |
| Caption | 13px | 400 | 1.5 |
| Label | 12px | 600 | 1.4 |
| Micro | 11px | 500 | 1.4 |

### Spacing Scale

| Name | Value | Usage |
|------|-------|-------|
| xs | 4px | Tight spacing |
| sm | 8px | Component internal |
| md | 16px | Default spacing |
| lg | 24px | Section spacing |
| xl | 32px | Large gaps |
| 2xl | 48px | Page sections |

### Border Radius

| Name | Value | Usage |
|------|-------|-------|
| sm | 8px | Small elements |
| md | 12px | Buttons, inputs |
| lg | 16px | Cards |
| xl | 20px | Large cards |
| full | 9999px | Pills, circles |

## Component Patterns

### Glass Card

```html
<div style="
  background: rgba(255, 255, 255, 0.06);
  backdrop-filter: blur(20px);
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 20px;
">
  <!-- Card content -->
</div>
```

### Primary Button

```html
<div style="
  background: linear-gradient(135deg, #6366F1, #8B5CF6);
  border-radius: 16px;
  padding: 16px 24px;
  text-align: center;
  box-shadow: 0 8px 24px rgba(99, 102, 241, 0.3);
  cursor: pointer;
">
  <span style="color: white; font-size: 16px; font-weight: 600;">
    Button Text
  </span>
</div>
```

### Text Input

```html
<div style="
  background: rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 16px;
">
  <input type="text" placeholder="Placeholder text" style="
    background: transparent;
    border: none;
    color: white;
    font-size: 16px;
    width: 100%;
    outline: none;
  "/>
</div>
```

### Toggle Switch

```html
<div style="
  width: 48px;
  height: 28px;
  background: #6366F1;
  border-radius: 14px;
  position: relative;
  cursor: pointer;
">
  <div style="
    width: 24px;
    height: 24px;
    background: white;
    border-radius: 50%;
    position: absolute;
    right: 2px;
    top: 2px;
  "></div>
</div>
```

### Bottom Navigation

```html
<div style="
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 70px;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(20px);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 80px;
">
  <div style="display: flex; flex-direction: column; align-items: center; gap: 4px;">
    <svg><!-- Icon --></svg>
    <span style="font-size: 11px; color: #6366F1; font-weight: 600;">Home</span>
  </div>
  <div style="display: flex; flex-direction: column; align-items: center; gap: 4px;">
    <svg><!-- Icon --></svg>
    <span style="font-size: 11px; color: #64748B;">Settings</span>
  </div>
</div>
```

### Floating Action Button (FAB)

```html
<div style="
  position: absolute;
  right: 24px;
  bottom: 100px;
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, #6366F1, #8B5CF6);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 8px 24px rgba(99, 102, 241, 0.4);
  cursor: pointer;
">
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
    <path d="M12 5V19M5 12H19" stroke="white" stroke-width="2.5" stroke-linecap="round"/>
  </svg>
</div>
```

## Screen Types

### Essential Screens

1. **Home/Dashboard**
   - Hero section with key metrics
   - Quick actions
   - Recent items list
   - Bottom navigation

2. **List View**
   - Search/filter bar
   - Sortable list items
   - Empty state
   - FAB for adding

3. **Detail View**
   - Header with back button
   - Hero image/icon
   - Content sections
   - Action buttons

4. **Create/Edit Modal**
   - Bottom sheet or full screen
   - Form inputs
   - Validation states
   - Submit button

5. **Settings**
   - Grouped options
   - Toggle switches
   - Navigation links
   - Version info

6. **Empty State**
   - Illustration/icon
   - Descriptive text
   - Call to action

## Iterative Design Workflow

### Phase 1: Discovery
1. Define app purpose and audience
2. List required screens
3. Choose design direction (dark/light, style)
4. Identify key components

### Phase 2: Initial Design
1. Create first complete UI kit
2. Include all essential screens
3. Add design system documentation
4. Use realistic content

### Phase 3: Iteration
1. Gather feedback on specific elements
2. Make targeted refinements
3. Update consistently across screens
4. Document design decisions

### Phase 4: Finalization
1. Complete accessibility review
2. Verify component consistency
3. Export design tokens if needed
4. Prepare handoff documentation

## Best Practices

### Visual Hierarchy
- Use size and weight to show importance
- Group related elements
- Maintain consistent spacing
- Guide eye with color accents

### Accessibility
- Minimum 4.5:1 contrast for text
- 44x44px minimum touch targets
- Don't rely only on color
- Support screen readers

### Consistency
- Same component = same style
- Unified spacing scale
- Consistent border radius
- Cohesive color application

### Performance
- Optimize images and icons
- Use efficient CSS
- Consider loading states
- Show progress indicators

## Quick Reference

### Phone Frame Dimensions
- Width: 390px
- Height: 844px
- Border radius: 40px
- Border: 8px

### Common Inline Styles

```css
/* Glass background */
background: rgba(255,255,255,0.06);
backdrop-filter: blur(20px);
border: 1px solid rgba(255,255,255,0.1);

/* Primary gradient */
background: linear-gradient(135deg, #6366F1, #8B5CF6);
box-shadow: 0 8px 24px rgba(99,102,241,0.3);

/* Text colors */
color: white;           /* Primary */
color: #94A3B8;         /* Secondary */
color: #64748B;         /* Muted */

/* Flex centering */
display: flex;
align-items: center;
justify-content: center;
```

### Icon SVG Patterns

```html
<!-- Plus -->
<svg width="24" height="24" viewBox="0 0 24 24" fill="none">
  <path d="M12 5V19M5 12H19" stroke="white" stroke-width="2.5" stroke-linecap="round"/>
</svg>

<!-- Checkmark -->
<svg width="24" height="24" viewBox="0 0 24 24" fill="none">
  <path d="M4 12.5L9 17.5L20 6.5" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
</svg>

<!-- Chevron Right -->
<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
  <path d="M9 18l6-6-6-6"/>
</svg>

<!-- Settings Gear -->
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
  <circle cx="12" cy="12" r="3"/>
  <path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/>
</svg>
```

## Implementation Workflow

To create a UI kit:

1. Start with the HTML template
2. Define design tokens (colors, typography, spacing)
3. Build phone frame container
4. Create each screen with realistic content
5. Add navigation between screens
6. Include design system documentation
7. Test in browser
8. Iterate based on feedback

---

## Related References

For detailed components and templates, consult these reference documents in `references/`:

- [Component Library](references/component-library.md) - Copy-paste ready HTML components including buttons, cards, inputs, navigation, modals, and more
- [Color Palettes](references/color-palettes.md) - Pre-designed color palettes for different app types and moods (7 dark mode + 2 light mode palettes)
- [App Templates](references/app-templates.md) - Starting templates for common app types (todo, fitness, social, e-commerce, finance, music, meditation, recipe, travel)
