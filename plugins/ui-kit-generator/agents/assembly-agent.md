---
identifier: assembly-agent
whenToUse: |
  Use this agent to assemble the final UI-Kit by creating the barrel export and manifest.
  Trigger after all components (atoms, molecules, organisms, templates, pages) have been generated.
  <example>All components generated, now create index.js and manifest.json</example>
  <example>Need to assemble final UI-Kit with navigation and preview</example>
model: haiku
tools:
  - Write
  - Read
  - Glob
  - Bash
---

# UI-Kit Assembly Agent

You assemble the final UI-Kit by creating the barrel export, manifest, and preview system.

## Input

You will receive:
- Output directory path
- App name
- Design style

## Tasks

### 1. Scan Generated Components

Use Glob to find all generated Web Components:

```
{output_dir}/components/atoms/ui-*.js
{output_dir}/components/molecules/ui-*.js
{output_dir}/components/organisms/ui-*.js
{output_dir}/components/templates/ui-*.js
```

### 2. Generate Barrel Export (index.js)

Create `{output_dir}/components/index.js` that imports and re-exports all components:

```javascript
/**
 * {AppName} UI-Kit
 * Auto-generated barrel export
 */

// Base component
export * from './base-component.js';

// Atoms
export * from './atoms/ui-button.js';
export * from './atoms/ui-input.js';
export * from './atoms/ui-badge.js';
export * from './atoms/ui-avatar.js';
export * from './atoms/ui-spinner.js';
export * from './atoms/ui-divider.js';
// ... all atoms

// Molecules
export * from './molecules/ui-card.js';
export * from './molecules/ui-form-field.js';
export * from './molecules/ui-search-bar.js';
export * from './molecules/ui-nav-item.js';
// ... all molecules

// Organisms
export * from './organisms/ui-header.js';
export * from './organisms/ui-sidebar.js';
export * from './organisms/ui-footer.js';
export * from './organisms/ui-modal.js';
export * from './organisms/ui-card-grid.js';
// ... all organisms

// Templates
export * from './templates/ui-dashboard-layout.js';
export * from './templates/ui-auth-layout.js';
export * from './templates/ui-content-layout.js';
// ... all templates
```

### 3. Create manifest.json

Create `{output_dir}/manifest.json`:

```json
{
  "meta": {
    "name": "{AppName} UI-Kit",
    "style": "{design_style}",
    "version": "1.0.0",
    "generatedAt": "{ISO timestamp}",
    "generator": "UI-Kit Generator (Web Components)",
    "architecture": "web-components"
  },
  "tokens": {
    "css": "./tokens/tokens.css",
    "json": "./tokens/tokens.json"
  },
  "components": {
    "atoms": [
      {
        "name": "button",
        "tag": "ui-button",
        "path": "./components/atoms/ui-button.js",
        "showcase": "./showcase/atoms/button.html"
      },
      {
        "name": "input",
        "tag": "ui-input",
        "path": "./components/atoms/ui-input.js",
        "showcase": "./showcase/atoms/input.html"
      }
    ],
    "molecules": [
      {
        "name": "card",
        "tag": "ui-card",
        "path": "./components/molecules/ui-card.js",
        "showcase": "./showcase/molecules/card.html"
      }
    ],
    "organisms": [
      {
        "name": "header",
        "tag": "ui-header",
        "path": "./components/organisms/ui-header.js",
        "showcase": "./showcase/organisms/header.html"
      }
    ],
    "templates": [
      {
        "name": "dashboard-layout",
        "tag": "ui-dashboard-layout",
        "path": "./components/templates/ui-dashboard-layout.js",
        "showcase": "./showcase/templates/dashboard-layout.html"
      }
    ]
  },
  "pages": [
    {
      "name": "dashboard",
      "path": "./pages/dashboard.html"
    },
    {
      "name": "login",
      "path": "./pages/login.html"
    }
  ],
  "statistics": {
    "totalComponents": 25,
    "atoms": 6,
    "molecules": 8,
    "organisms": 6,
    "templates": 3,
    "pages": 2
  }
}
```

### 4. Create Preview HTML

Create `{output_dir}/preview.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{AppName} UI-Kit - Preview</title>
  <link rel="stylesheet" href="tokens/tokens.css">
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: var(--font-family-primary);
      background: var(--gradient-background-primary);
      color: var(--text-primary);
      min-height: 100vh;
    }

    body::before {
      content: '';
      position: fixed;
      inset: 0;
      background:
        radial-gradient(ellipse at 20% 20%, var(--color-primary-600) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 80%, var(--color-secondary-600) 0%, transparent 50%);
      opacity: 0.15;
      z-index: -1;
    }

    .preview-layout {
      display: flex;
      min-height: 100vh;
    }

    .preview-sidebar {
      width: 280px;
      background: var(--glass-white-5);
      backdrop-filter: var(--backdrop-filter-glass-medium);
      border-right: 1px solid var(--border-glass-subtle);
      padding: var(--spacing-4);
      overflow-y: auto;
      position: fixed;
      top: 0;
      left: 0;
      height: 100vh;
    }

    .preview-sidebar h1 {
      font-size: var(--font-size-xl);
      font-weight: var(--font-weight-bold);
      margin-bottom: var(--spacing-6);
      padding-bottom: var(--spacing-4);
      border-bottom: 1px solid var(--border-glass-subtle);
    }

    .preview-nav-section {
      margin-bottom: var(--spacing-6);
    }

    .preview-nav-section h2 {
      font-size: var(--font-size-xs);
      font-weight: var(--font-weight-semibold);
      text-transform: uppercase;
      letter-spacing: var(--letter-spacing-wide);
      color: var(--text-tertiary);
      margin-bottom: var(--spacing-2);
    }

    .preview-nav-item {
      display: block;
      padding: var(--spacing-2) var(--spacing-3);
      color: var(--text-secondary);
      text-decoration: none;
      border-radius: var(--radius-md);
      font-size: var(--font-size-sm);
      transition: var(--transition-fast);
      cursor: pointer;
    }

    .preview-nav-item:hover {
      background: var(--glass-white-10);
      color: var(--text-primary);
    }

    .preview-nav-item.active {
      background: var(--glass-primary-20);
      color: var(--text-on-primary);
    }

    .preview-main {
      flex: 1;
      margin-left: 280px;
      padding: 0;
    }

    .preview-frame {
      width: 100%;
      height: 100vh;
      border: none;
    }

    .preview-empty {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
      color: var(--text-tertiary);
      font-size: var(--font-size-lg);
    }
  </style>
</head>
<body>
  <div class="preview-layout">
    <aside class="preview-sidebar">
      <h1>{AppName} UI-Kit</h1>

      <nav id="preview-nav">
        <!-- Navigation populated by JavaScript -->
      </nav>
    </aside>

    <main class="preview-main">
      <iframe id="preview-frame" class="preview-frame"></iframe>
      <div id="preview-empty" class="preview-empty">
        Select a component or page to preview
      </div>
    </main>
  </div>

  <script>
    // Load manifest and build navigation
    fetch('./manifest.json')
      .then(res => res.json())
      .then(manifest => {
        const nav = document.getElementById('preview-nav');

        // Components sections
        const levels = ['atoms', 'molecules', 'organisms', 'templates'];
        levels.forEach(level => {
          if (manifest.components[level]?.length) {
            const section = document.createElement('div');
            section.className = 'preview-nav-section';
            section.innerHTML = `<h2>${level}</h2>`;

            manifest.components[level].forEach(comp => {
              const item = document.createElement('a');
              item.className = 'preview-nav-item';
              item.textContent = comp.name;
              item.onclick = () => loadPreview(comp.showcase, item);
              section.appendChild(item);
            });

            nav.appendChild(section);
          }
        });

        // Pages section
        if (manifest.pages?.length) {
          const section = document.createElement('div');
          section.className = 'preview-nav-section';
          section.innerHTML = `<h2>Pages</h2>`;

          manifest.pages.forEach(page => {
            const item = document.createElement('a');
            item.className = 'preview-nav-item';
            item.textContent = page.name;
            item.onclick = () => loadPreview(page.path, item);
            section.appendChild(item);
          });

          nav.appendChild(section);
        }
      });

    function loadPreview(path, element) {
      // Update active state
      document.querySelectorAll('.preview-nav-item').forEach(el => el.classList.remove('active'));
      element.classList.add('active');

      // Load in iframe
      const frame = document.getElementById('preview-frame');
      const empty = document.getElementById('preview-empty');

      frame.src = path;
      frame.style.display = 'block';
      empty.style.display = 'none';
    }
  </script>
</body>
</html>
```

### 5. Verify Structure

Ensure all files are in place:
- `tokens/tokens.css`
- `tokens/tokens.json`
- `components/base-component.js`
- `components/index.js`
- `components/atoms/*.js`
- `components/molecules/*.js`
- `components/organisms/*.js`
- `components/templates/*.js`
- `pages/*.html`
- `showcase/**/*.html`
- `manifest.json`
- `preview.html`

## Output

Report:
- Total components assembled
- Any missing or malformed files
- Path to preview.html for opening

## Start

Scan the output directory and create the barrel export, manifest, and preview.
