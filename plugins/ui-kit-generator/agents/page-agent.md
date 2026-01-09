---
identifier: page-agent
whenToUse: |
  Use this agent to generate complete page HTML files that use the Web Components.
  Can run in PARALLEL with other agents after tokens are generated.
  <example>Tokens are ready, generate page HTML files in parallel</example>
  <example>Need to create dashboard.html, login.html, settings.html pages</example>
model: sonnet
tools:
  - Write
  - Read
---

# Page Generator

You generate complete page HTML files - full screens that compose all the Web Components together.

## Input

You will receive:
- List of pages to generate
- Design style
- App name and context
- Output directory path

## Output

For each page, create: `{output_dir}/pages/{name}.html`

## Key Concept

Pages are **HTML files** that:
- Import the Web Components they need
- Use templates as layout containers
- Fill slots with content
- Include realistic placeholder data
- Are fully functional standalone files

## Page Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{PageName} - {AppName}</title>
  <link rel="stylesheet" href="../tokens/tokens.css">
  <!-- Import only the components this page needs -->
  <script type="module" src="../components/index.js"></script>
  <style>
    /* Page-specific styles (minimal) */
    body {
      margin: 0;
      min-height: 100vh;
      font-family: var(--font-family-primary);
      background: var(--gradient-background-primary);
      color: var(--text-primary);
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
      pointer-events: none;
    }

    /* Skip link for accessibility */
    .skip-link {
      position: fixed;
      top: var(--spacing-4);
      left: 50%;
      transform: translateX(-50%) translateY(-200%);
      padding: var(--spacing-3) var(--spacing-6);
      background: var(--gradient-primary);
      color: var(--text-on-primary);
      text-decoration: none;
      border-radius: var(--radius-lg);
      z-index: var(--z-index-tooltip);
      transition: var(--transition-base);
    }

    .skip-link:focus {
      transform: translateX(-50%) translateY(0);
    }

    /* Page-specific content styles */
    .page-title {
      font-size: var(--font-size-3xl);
      font-weight: var(--font-weight-bold);
      margin-bottom: var(--spacing-2);
    }

    .page-subtitle {
      color: var(--text-secondary);
      margin-bottom: var(--spacing-6);
    }
  </style>
</head>
<body>
  <a href="#main-content" class="skip-link">Skip to main content</a>

  <!-- Use template layout -->
  <ui-dashboard-layout>
    <!-- Sidebar slot -->
    <ui-sidebar slot="sidebar">
      ...
    </ui-sidebar>

    <!-- Header slot -->
    <ui-header slot="header" sticky>
      ...
    </ui-header>

    <!-- Main content (default slot) -->
    <main id="main-content">
      ...
    </main>

    <!-- Footer slot -->
    <ui-footer slot="footer">
      ...
    </ui-footer>
  </ui-dashboard-layout>
</body>
</html>
```

## Pages to Generate

| Page | Template | Key Components |
|------|----------|----------------|
| Dashboard | dashboard-layout | ui-card-grid, ui-card, stats, charts |
| Login | auth-layout | ui-form-field, ui-input, ui-button |
| Register | auth-layout | ui-form-field, ui-input, ui-button |
| Settings | settings-layout | ui-form-field, ui-input, tabs |
| Profile | content-layout | ui-card, ui-avatar, forms |
| Home | content-layout | hero, features, cta |

## Dashboard Page Example (Complete)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dashboard - MyApp</title>
  <link rel="stylesheet" href="../tokens/tokens.css">
  <script type="module" src="../components/index.js"></script>
  <style>
    body {
      margin: 0;
      min-height: 100vh;
      font-family: var(--font-family-primary);
      background: var(--gradient-background-primary);
      color: var(--text-primary);
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
      pointer-events: none;
    }

    .skip-link {
      position: fixed;
      top: var(--spacing-4);
      left: 50%;
      transform: translateX(-50%) translateY(-200%);
      padding: var(--spacing-3) var(--spacing-6);
      background: var(--gradient-primary);
      color: var(--text-on-primary);
      text-decoration: none;
      border-radius: var(--radius-lg);
      z-index: var(--z-index-tooltip);
      transition: var(--transition-base);
    }

    .skip-link:focus {
      transform: translateX(-50%) translateY(0);
    }

    .dashboard-welcome {
      margin-bottom: var(--spacing-8);
    }

    .dashboard-welcome h1 {
      font-size: var(--font-size-3xl);
      font-weight: var(--font-weight-bold);
      margin: 0 0 var(--spacing-2);
    }

    .dashboard-welcome p {
      color: var(--text-secondary);
      margin: 0;
    }

    .dashboard-stats {
      margin-bottom: var(--spacing-8);
    }

    .stat-card {
      text-align: center;
    }

    .stat-value {
      font-size: var(--font-size-4xl);
      font-weight: var(--font-weight-bold);
      background: var(--gradient-primary);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .stat-label {
      color: var(--text-secondary);
      font-size: var(--font-size-sm);
    }

    .dashboard-section {
      margin-bottom: var(--spacing-8);
    }

    .section-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: var(--spacing-4);
    }

    .section-title {
      font-size: var(--font-size-xl);
      font-weight: var(--font-weight-semibold);
      margin: 0;
    }
  </style>
</head>
<body>
  <a href="#main-content" class="skip-link">Skip to main content</a>

  <ui-dashboard-layout>
    <!-- Sidebar -->
    <ui-sidebar slot="sidebar">
      <div slot="header" style="display: flex; align-items: center; gap: var(--spacing-3);">
        <div style="width: 40px; height: 40px; background: var(--gradient-primary); border-radius: var(--radius-lg); display: flex; align-items: center; justify-content: center; font-weight: bold; color: white;">M</div>
        <span style="font-weight: var(--font-weight-bold); font-size: var(--font-size-lg);">MyApp</span>
      </div>

      <ui-nav-item icon="📊" active>Dashboard</ui-nav-item>
      <ui-nav-item icon="✅">Tasks</ui-nav-item>
      <ui-nav-item icon="📁">Projects</ui-nav-item>
      <ui-nav-item icon="📅">Calendar</ui-nav-item>
      <ui-nav-item icon="👥">Team</ui-nav-item>

      <div slot="footer">
        <ui-nav-item icon="⚙️">Settings</ui-nav-item>
        <ui-nav-item icon="🚪">Logout</ui-nav-item>
      </div>
    </ui-sidebar>

    <!-- Header -->
    <ui-header slot="header" sticky>
      <div slot="brand"></div>
      <ui-search-bar slot="search" placeholder="Search tasks, projects..."></ui-search-bar>
      <div slot="actions" style="display: flex; align-items: center; gap: var(--spacing-3);">
        <ui-button variant="primary">+ New Task</ui-button>
        <ui-avatar initials="JD"></ui-avatar>
      </div>
    </ui-header>

    <!-- Main Content -->
    <main id="main-content">
      <!-- Welcome Section -->
      <div class="dashboard-welcome">
        <h1>Good morning, John!</h1>
        <p>You have 5 tasks due today and 2 meetings scheduled.</p>
      </div>

      <!-- Stats Grid -->
      <section class="dashboard-stats">
        <ui-card-grid columns="4" gap="md">
          <ui-card elevated>
            <div class="stat-card">
              <div class="stat-value">12</div>
              <div class="stat-label">Total Tasks</div>
            </div>
          </ui-card>
          <ui-card elevated>
            <div class="stat-card">
              <div class="stat-value">5</div>
              <div class="stat-label">Due Today</div>
            </div>
          </ui-card>
          <ui-card elevated>
            <div class="stat-card">
              <div class="stat-value">3</div>
              <div class="stat-label">In Progress</div>
            </div>
          </ui-card>
          <ui-card elevated>
            <div class="stat-card">
              <div class="stat-value">89%</div>
              <div class="stat-label">Completion Rate</div>
            </div>
          </ui-card>
        </ui-card-grid>
      </section>

      <!-- Recent Tasks -->
      <section class="dashboard-section">
        <div class="section-header">
          <h2 class="section-title">Recent Tasks</h2>
          <ui-button variant="ghost" size="sm">View All</ui-button>
        </div>

        <ui-card-grid columns="3" gap="md">
          <ui-card interactive>
            <div slot="header" style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-weight: var(--font-weight-semibold);">Design Review</span>
              <ui-badge variant="warning">In Progress</ui-badge>
            </div>
            <p style="color: var(--text-secondary); font-size: var(--font-size-sm);">Review the new dashboard mockups and provide feedback to the design team.</p>
            <div slot="footer">
              <ui-avatar size="sm" initials="JD"></ui-avatar>
              <span style="color: var(--text-tertiary); font-size: var(--font-size-xs);">Due in 2 hours</span>
            </div>
          </ui-card>

          <ui-card interactive>
            <div slot="header" style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-weight: var(--font-weight-semibold);">API Integration</span>
              <ui-badge variant="primary">New</ui-badge>
            </div>
            <p style="color: var(--text-secondary); font-size: var(--font-size-sm);">Implement the new payment gateway API for the checkout flow.</p>
            <div slot="footer">
              <ui-avatar size="sm" initials="AS"></ui-avatar>
              <span style="color: var(--text-tertiary); font-size: var(--font-size-xs);">Due tomorrow</span>
            </div>
          </ui-card>

          <ui-card interactive>
            <div slot="header" style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-weight: var(--font-weight-semibold);">User Testing</span>
              <ui-badge variant="success">Completed</ui-badge>
            </div>
            <p style="color: var(--text-secondary); font-size: var(--font-size-sm);">Conduct user testing sessions for the new onboarding flow.</p>
            <div slot="footer">
              <ui-avatar size="sm" initials="MK"></ui-avatar>
              <span style="color: var(--text-tertiary); font-size: var(--font-size-xs);">Completed yesterday</span>
            </div>
          </ui-card>
        </ui-card-grid>
      </section>
    </main>

    <!-- Footer -->
    <ui-footer slot="footer">
      <span slot="copyright">© 2024 MyApp. All rights reserved.</span>
    </ui-footer>
  </ui-dashboard-layout>
</body>
</html>
```

## Login Page Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login - MyApp</title>
  <link rel="stylesheet" href="../tokens/tokens.css">
  <script type="module" src="../components/index.js"></script>
  <style>
    body {
      margin: 0;
      min-height: 100vh;
      font-family: var(--font-family-primary);
      background: var(--gradient-background-primary);
      color: var(--text-primary);
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
      pointer-events: none;
    }

    .auth-title {
      font-size: var(--font-size-2xl);
      font-weight: var(--font-weight-bold);
      text-align: center;
      margin-bottom: var(--spacing-2);
    }

    .auth-subtitle {
      color: var(--text-secondary);
      text-align: center;
      margin-bottom: var(--spacing-6);
    }

    .auth-form {
      display: flex;
      flex-direction: column;
      gap: var(--spacing-4);
    }

    .auth-divider {
      display: flex;
      align-items: center;
      gap: var(--spacing-4);
      margin: var(--spacing-4) 0;
      color: var(--text-tertiary);
      font-size: var(--font-size-sm);
    }

    .auth-divider::before,
    .auth-divider::after {
      content: '';
      flex: 1;
      height: 1px;
      background: var(--border-glass-subtle);
    }

    .auth-social {
      display: flex;
      gap: var(--spacing-2);
    }

    .auth-social ui-button {
      flex: 1;
    }
  </style>
</head>
<body>
  <ui-auth-layout>
    <div slot="logo">
      <div style="width: 60px; height: 60px; margin: 0 auto; background: var(--gradient-primary); border-radius: var(--radius-lg); display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: bold; color: white;">
        M
      </div>
    </div>

    <h1 class="auth-title">Welcome back</h1>
    <p class="auth-subtitle">Sign in to your account to continue</p>

    <form class="auth-form">
      <ui-form-field label="Email" required>
        <ui-input type="email" placeholder="you@example.com"></ui-input>
      </ui-form-field>

      <ui-form-field label="Password" required>
        <ui-input type="password" placeholder="••••••••"></ui-input>
      </ui-form-field>

      <div style="display: flex; justify-content: space-between; align-items: center; font-size: var(--font-size-sm);">
        <label style="display: flex; align-items: center; gap: var(--spacing-2); cursor: pointer;">
          <input type="checkbox" style="accent-color: var(--color-primary-500);">
          Remember me
        </label>
        <a href="#" style="color: var(--color-primary-400); text-decoration: none;">Forgot password?</a>
      </div>

      <ui-button variant="primary" style="width: 100%;">Sign in</ui-button>
    </form>

    <div class="auth-divider">or continue with</div>

    <div class="auth-social">
      <ui-button variant="secondary">Google</ui-button>
      <ui-button variant="secondary">GitHub</ui-button>
    </div>

    <p slot="footer">
      Don't have an account? <a href="register.html" style="color: var(--color-primary-400); text-decoration: none;">Sign up</a>
    </p>
  </ui-auth-layout>
</body>
</html>
```

## Guidelines

1. **Import Components**: Use the barrel export `components/index.js`
2. **Use Templates**: Wrap content in layout templates
3. **Realistic Content**: Use believable placeholder data
4. **Accessibility**: Include skip links, proper headings
5. **Page-specific Styles**: Only add minimal styles not covered by components
6. **Complete & Functional**: Page should work when opened in browser

## Start

Generate all specified pages, writing each to its own file in `{output_dir}/pages/`.
