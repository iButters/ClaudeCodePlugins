# Index.html Template Reference

The `index.html` serves as the central preview hub for the UI kit, displaying all screens in phone frames and providing navigation to explore components.

## Complete Index Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[AppName] - UI Kit</title>

  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <!-- Design Tokens -->
  <link rel="stylesheet" href="tokens/variables.css">
  <link rel="stylesheet" href="tokens/base.css">

  <!-- Atom Styles -->
  <link rel="stylesheet" href="atoms/button/button.css">
  <link rel="stylesheet" href="atoms/input/input.css">
  <link rel="stylesheet" href="atoms/badge/badge.css">
  <link rel="stylesheet" href="atoms/avatar/avatar.css">
  <link rel="stylesheet" href="atoms/checkbox/checkbox.css">
  <link rel="stylesheet" href="atoms/toggle/toggle.css">
  <link rel="stylesheet" href="atoms/spinner/spinner.css">
  <link rel="stylesheet" href="atoms/progress-bar/progress-bar.css">

  <!-- Molecule Styles -->
  <link rel="stylesheet" href="molecules/card/card.css">
  <link rel="stylesheet" href="molecules/list-item/list-item.css">
  <link rel="stylesheet" href="molecules/search-bar/search-bar.css">
  <link rel="stylesheet" href="molecules/form-field/form-field.css">
  <link rel="stylesheet" href="molecules/nav-item/nav-item.css">
  <link rel="stylesheet" href="molecules/todo-item/todo-item.css">

  <!-- Organism Styles -->
  <link rel="stylesheet" href="organisms/header/header.css">
  <link rel="stylesheet" href="organisms/bottom-nav/bottom-nav.css">
  <link rel="stylesheet" href="organisms/modal/modal.css">
  <link rel="stylesheet" href="organisms/bottom-sheet/bottom-sheet.css">
  <link rel="stylesheet" href="organisms/toast/toast.css">

  <!-- Page Styles -->
  <link rel="stylesheet" href="pages/home/home.css">
  <link rel="stylesheet" href="pages/detail/detail.css">
  <link rel="stylesheet" href="pages/settings/settings.css">

  <!-- Preview Styles -->
  <style>
    /* Preview Container Styles */
    .preview-container {
      min-height: 100vh;
      padding: 40px;
      background: var(--bg-primary);
    }

    .preview-header {
      text-align: center;
      margin-bottom: 48px;
    }

    .preview-header h1 {
      font-size: 32px;
      font-weight: 700;
      color: var(--text-primary);
      margin-bottom: 8px;
    }

    .preview-header p {
      font-size: 16px;
      color: var(--text-secondary);
    }

    /* Navigation Tabs */
    .nav-tabs {
      display: flex;
      gap: 8px;
      justify-content: center;
      margin-bottom: 48px;
      flex-wrap: wrap;
    }

    .nav-tab {
      background: var(--glass-bg);
      color: var(--text-secondary);
      padding: 12px 24px;
      border-radius: var(--radius-md);
      cursor: pointer;
      border: 1px solid transparent;
      font-family: var(--font-family);
      font-size: 14px;
      font-weight: 500;
      transition: all var(--transition-base);
    }

    .nav-tab:hover {
      background: var(--glass-bg-hover);
      color: var(--text-primary);
    }

    .nav-tab.active {
      background: var(--primary);
      color: white;
    }

    /* Frames Grid */
    .frames-grid {
      display: flex;
      flex-wrap: wrap;
      gap: 40px;
      justify-content: center;
    }

    .frames-section {
      display: none;
    }

    .frames-section.active {
      display: flex;
      flex-wrap: wrap;
      gap: 40px;
      justify-content: center;
    }

    /* Phone Frame */
    .phone-frame {
      width: var(--phone-width);
      height: var(--phone-height);
      background: var(--bg-primary);
      border-radius: var(--phone-radius);
      border: var(--phone-border) solid var(--bg-secondary);
      overflow: hidden;
      position: relative;
      box-shadow: var(--shadow-phone);
    }

    .phone-frame::before {
      content: '';
      position: absolute;
      top: 12px;
      left: 50%;
      transform: translateX(-50%);
      width: 120px;
      height: 28px;
      background: var(--bg-secondary);
      border-radius: 20px;
      z-index: 100;
    }

    .phone-content {
      height: 100%;
      overflow-y: auto;
      padding-top: 48px;
    }

    .phone-label {
      text-align: center;
      margin-top: 16px;
      color: var(--text-secondary);
      font-size: 14px;
      font-weight: 500;
    }

    /* Component Library Section */
    .component-library {
      max-width: 1200px;
      margin: 0 auto;
      padding: 48px 0;
    }

    .component-library h2 {
      font-size: 24px;
      color: var(--text-primary);
      margin-bottom: 32px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--glass-border);
    }

    .component-category {
      margin-bottom: 48px;
    }

    .component-category h3 {
      font-size: 18px;
      color: var(--text-secondary);
      margin-bottom: 24px;
    }

    .component-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 24px;
    }

    .component-preview {
      background: var(--glass-bg);
      border: 1px solid var(--glass-border);
      border-radius: var(--radius-lg);
      padding: 24px;
    }

    .component-preview h4 {
      font-size: 14px;
      color: var(--text-primary);
      margin-bottom: 16px;
    }

    .component-demo {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      align-items: center;
    }
  </style>
</head>
<body>
  <div class="preview-container">
    <!-- Header -->
    <header class="preview-header">
      <h1>[AppName] UI Kit</h1>
      <p>Interactive design specification • [X] Screens • [Y] Components</p>
    </header>

    <!-- Navigation -->
    <nav class="nav-tabs">
      <button class="nav-tab active" onclick="showSection('screens')">All Screens</button>
      <button class="nav-tab" onclick="showSection('home')">Home</button>
      <button class="nav-tab" onclick="showSection('detail')">Detail</button>
      <button class="nav-tab" onclick="showSection('settings')">Settings</button>
      <button class="nav-tab" onclick="showSection('components')">Components</button>
      <button class="nav-tab" onclick="showSection('design')">Design System</button>
    </nav>

    <!-- All Screens Section -->
    <section class="frames-section active" id="section-screens">
      <!-- Home Screen -->
      <div>
        <div class="phone-frame">
          <div class="phone-content">
            <!-- Include home page content here -->
          </div>
        </div>
        <p class="phone-label">Home</p>
      </div>

      <!-- Detail Screen -->
      <div>
        <div class="phone-frame">
          <div class="phone-content">
            <!-- Include detail page content here -->
          </div>
        </div>
        <p class="phone-label">Detail</p>
      </div>

      <!-- Settings Screen -->
      <div>
        <div class="phone-frame">
          <div class="phone-content">
            <!-- Include settings page content here -->
          </div>
        </div>
        <p class="phone-label">Settings</p>
      </div>
    </section>

    <!-- Individual Screen Sections -->
    <section class="frames-section" id="section-home">
      <div>
        <div class="phone-frame">
          <div class="phone-content">
            <!-- Home page content -->
          </div>
        </div>
        <p class="phone-label">Home</p>
      </div>
    </section>

    <section class="frames-section" id="section-detail">
      <div>
        <div class="phone-frame">
          <div class="phone-content">
            <!-- Detail page content -->
          </div>
        </div>
        <p class="phone-label">Detail</p>
      </div>
    </section>

    <section class="frames-section" id="section-settings">
      <div>
        <div class="phone-frame">
          <div class="phone-content">
            <!-- Settings page content -->
          </div>
        </div>
        <p class="phone-label">Settings</p>
      </div>
    </section>

    <!-- Components Section -->
    <section class="frames-section" id="section-components">
      <div class="component-library">
        <h2>Component Library</h2>

        <!-- Atoms -->
        <div class="component-category">
          <h3>Atoms</h3>
          <div class="component-grid">
            <div class="component-preview">
              <h4>Buttons</h4>
              <div class="component-demo">
                <button class="btn btn--primary">Primary</button>
                <button class="btn btn--secondary">Secondary</button>
                <button class="btn btn--ghost">Ghost</button>
              </div>
            </div>

            <div class="component-preview">
              <h4>Inputs</h4>
              <div class="component-demo">
                <div class="input input--text" style="width: 100%;">
                  <input type="text" class="input__field" placeholder="Text input">
                </div>
              </div>
            </div>

            <div class="component-preview">
              <h4>Badges</h4>
              <div class="component-demo">
                <span class="badge badge--info">Info</span>
                <span class="badge badge--success">Success</span>
                <span class="badge badge--warning">Warning</span>
                <span class="badge badge--error">Error</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Molecules -->
        <div class="component-category">
          <h3>Molecules</h3>
          <div class="component-grid">
            <div class="component-preview">
              <h4>Cards</h4>
              <div class="component-demo" style="width: 100%;">
                <div class="card" style="width: 100%;">
                  <div class="card__body">Card content example</div>
                </div>
              </div>
            </div>

            <div class="component-preview">
              <h4>List Items</h4>
              <div class="component-demo" style="width: 100%;">
                <div class="list-item" style="width: 100%;">
                  <div class="list-item__content">
                    <p class="list-item__title">List Item</p>
                    <p class="list-item__subtitle">Subtitle</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Design System Section -->
    <section class="frames-section" id="section-design">
      <div class="component-library">
        <h2>Design System</h2>

        <!-- Colors -->
        <div class="component-category">
          <h3>Colors</h3>
          <div class="component-grid">
            <div class="component-preview">
              <h4>Brand Colors</h4>
              <div class="component-demo">
                <div style="width: 48px; height: 48px; background: var(--primary); border-radius: 8px;"></div>
                <div style="width: 48px; height: 48px; background: var(--accent); border-radius: 8px;"></div>
              </div>
            </div>

            <div class="component-preview">
              <h4>Semantic Colors</h4>
              <div class="component-demo">
                <div style="width: 48px; height: 48px; background: var(--success); border-radius: 8px;"></div>
                <div style="width: 48px; height: 48px; background: var(--warning); border-radius: 8px;"></div>
                <div style="width: 48px; height: 48px; background: var(--error); border-radius: 8px;"></div>
                <div style="width: 48px; height: 48px; background: var(--info); border-radius: 8px;"></div>
              </div>
            </div>
          </div>
        </div>

        <!-- Typography -->
        <div class="component-category">
          <h3>Typography</h3>
          <div class="component-preview" style="max-width: 600px;">
            <h4>Type Scale</h4>
            <div style="display: flex; flex-direction: column; gap: 16px;">
              <p style="font-size: var(--font-size-2xl); font-weight: 700; color: var(--text-primary);">Display (28px)</p>
              <p style="font-size: var(--font-size-xl); font-weight: 700; color: var(--text-primary);">Heading (22px)</p>
              <p style="font-size: var(--font-size-lg); font-weight: 600; color: var(--text-primary);">Title (18px)</p>
              <p style="font-size: var(--font-size-base); color: var(--text-primary);">Body (15px)</p>
              <p style="font-size: var(--font-size-sm); color: var(--text-secondary);">Caption (13px)</p>
              <p style="font-size: var(--font-size-xs); color: var(--text-muted);">Micro (11px)</p>
            </div>
          </div>
        </div>

        <!-- Spacing -->
        <div class="component-category">
          <h3>Spacing</h3>
          <div class="component-preview" style="max-width: 600px;">
            <h4>Spacing Scale</h4>
            <div style="display: flex; flex-direction: column; gap: 8px;">
              <div style="display: flex; align-items: center; gap: 16px;">
                <div style="width: var(--space-xs); height: 24px; background: var(--primary);"></div>
                <span style="color: var(--text-secondary); font-size: 14px;">xs (4px)</span>
              </div>
              <div style="display: flex; align-items: center; gap: 16px;">
                <div style="width: var(--space-sm); height: 24px; background: var(--primary);"></div>
                <span style="color: var(--text-secondary); font-size: 14px;">sm (8px)</span>
              </div>
              <div style="display: flex; align-items: center; gap: 16px;">
                <div style="width: var(--space-md); height: 24px; background: var(--primary);"></div>
                <span style="color: var(--text-secondary); font-size: 14px;">md (16px)</span>
              </div>
              <div style="display: flex; align-items: center; gap: 16px;">
                <div style="width: var(--space-lg); height: 24px; background: var(--primary);"></div>
                <span style="color: var(--text-secondary); font-size: 14px;">lg (24px)</span>
              </div>
              <div style="display: flex; align-items: center; gap: 16px;">
                <div style="width: var(--space-xl); height: 24px; background: var(--primary);"></div>
                <span style="color: var(--text-secondary); font-size: 14px;">xl (32px)</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>

  <script>
    function showSection(section) {
      // Hide all sections
      document.querySelectorAll('.frames-section').forEach(s => {
        s.classList.remove('active');
      });

      // Deactivate all tabs
      document.querySelectorAll('.nav-tab').forEach(t => {
        t.classList.remove('active');
      });

      // Show selected section
      document.getElementById('section-' + section).classList.add('active');

      // Activate clicked tab
      event.target.classList.add('active');
    }
  </script>
</body>
</html>
```

## Key Sections

### 1. CSS Links
All component CSS files are linked in the `<head>`. The order matters:
1. Design tokens (variables.css, base.css)
2. Atoms
3. Molecules
4. Organisms
5. Pages

### 2. Navigation Tabs
Allow switching between:
- All Screens (default)
- Individual screens
- Component Library
- Design System documentation

### 3. Phone Frames
Each screen is displayed in a realistic phone frame:
- iPhone 14 Pro dimensions (390×844)
- Dynamic Island notch
- Proper border radius and shadows

### 4. Component Library
Showcases all components grouped by atomic level:
- Interactive demos
- All variants visible

### 5. Design System
Documents:
- Color palette with swatches
- Typography scale
- Spacing system
- Border radii

## Customization Points

Replace these placeholders when generating:
- `[AppName]` - Application name
- `[X] Screens` - Number of screens
- `[Y] Components` - Number of components
- CSS link paths based on actual components created
- Page content in phone frames
