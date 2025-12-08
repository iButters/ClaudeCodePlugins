# Component Templates Reference

This document provides copy-paste templates for all component types following the modular UI kit structure.

---

## Atoms

### Button (atoms/button/)

**button.html:**
```html
<!--
  Button Component
  ================
  Block: .btn
  Elements: .btn__text, .btn__icon, .btn__spinner
  Modifiers: --primary, --secondary, --ghost, --danger, --small, --medium, --large
  States: :disabled, .btn--loading
-->

<!-- Variants -->
<section class="component-variants">
  <h3>Variants</h3>

  <button class="btn btn--primary">
    <span class="btn__text">Primary Button</span>
  </button>

  <button class="btn btn--secondary">
    <span class="btn__text">Secondary Button</span>
  </button>

  <button class="btn btn--ghost">
    <span class="btn__text">Ghost Button</span>
  </button>

  <button class="btn btn--danger">
    <span class="btn__text">Danger Button</span>
  </button>
</section>

<!-- Sizes -->
<section class="component-sizes">
  <h3>Sizes</h3>

  <button class="btn btn--primary btn--small">
    <span class="btn__text">Small</span>
  </button>

  <button class="btn btn--primary btn--medium">
    <span class="btn__text">Medium</span>
  </button>

  <button class="btn btn--primary btn--large">
    <span class="btn__text">Large</span>
  </button>
</section>

<!-- With Icons -->
<section class="component-icons">
  <h3>With Icons</h3>

  <button class="btn btn--primary">
    <span class="btn__icon">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M12 5v14M5 12h14"/>
      </svg>
    </span>
    <span class="btn__text">Add Item</span>
  </button>

  <button class="btn btn--secondary">
    <span class="btn__text">Settings</span>
    <span class="btn__icon">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M9 18l6-6-6-6"/>
      </svg>
    </span>
  </button>
</section>

<!-- States -->
<section class="component-states">
  <h3>States</h3>

  <button class="btn btn--primary" disabled>
    <span class="btn__text">Disabled</span>
  </button>

  <button class="btn btn--primary btn--loading">
    <span class="btn__spinner"></span>
    <span class="btn__text">Loading...</span>
  </button>
</section>
```

**button.css:**
```css
/* Button Component */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-sm);
  padding: var(--space-md) var(--space-lg);
  border-radius: var(--radius-md);
  font-family: var(--font-family);
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-semibold);
  cursor: pointer;
  transition: all var(--transition-base);
  border: none;
  outline: none;
}

/* Variants */
.btn--primary {
  background: var(--primary-gradient);
  color: var(--text-primary);
  box-shadow: var(--shadow-primary);
}

.btn--primary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 12px 28px rgba(99, 102, 241, 0.5);
}

.btn--secondary {
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  color: var(--text-primary);
}

.btn--secondary:hover:not(:disabled) {
  background: var(--glass-bg-hover);
}

.btn--ghost {
  background: transparent;
  color: var(--text-secondary);
}

.btn--ghost:hover:not(:disabled) {
  background: var(--glass-bg);
  color: var(--text-primary);
}

.btn--danger {
  background: var(--error);
  color: var(--text-primary);
}

/* Sizes */
.btn--small {
  padding: var(--space-sm) var(--space-md);
  font-size: var(--font-size-sm);
}

.btn--medium {
  padding: var(--space-md) var(--space-lg);
  font-size: var(--font-size-base);
}

.btn--large {
  padding: var(--space-lg) var(--space-xl);
  font-size: var(--font-size-lg);
}

/* Elements */
.btn__icon {
  display: flex;
  align-items: center;
  justify-content: center;
}

.btn__spinner {
  width: 20px;
  height: 20px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

/* States */
.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.btn--loading {
  pointer-events: none;
}

.btn:focus-visible {
  outline: 2px solid var(--primary);
  outline-offset: 2px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

---

### Input (atoms/input/)

**input.html:**
```html
<!--
  Input Component
  ===============
  Block: .input
  Elements: .input__field, .input__icon, .input__clear
  Modifiers: --text, --search, --password, --error, --success
  States: :focus, :disabled, .input--filled
-->

<!-- Variants -->
<section class="component-variants">
  <h3>Variants</h3>

  <div class="input input--text">
    <input type="text" class="input__field" placeholder="Enter text...">
  </div>

  <div class="input input--search">
    <span class="input__icon">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/>
      </svg>
    </span>
    <input type="text" class="input__field" placeholder="Search...">
    <button class="input__clear">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M18 6L6 18M6 6l12 12"/>
      </svg>
    </button>
  </div>

  <div class="input input--password">
    <input type="password" class="input__field" placeholder="Password">
    <button class="input__icon input__icon--toggle">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>
      </svg>
    </button>
  </div>
</section>

<!-- States -->
<section class="component-states">
  <h3>States</h3>

  <div class="input input--text input--error">
    <input type="text" class="input__field" placeholder="Error state" value="Invalid input">
  </div>

  <div class="input input--text input--success">
    <input type="text" class="input__field" placeholder="Success state" value="Valid input">
  </div>

  <div class="input input--text">
    <input type="text" class="input__field" placeholder="Disabled" disabled>
  </div>
</section>
```

**input.css:**
```css
/* Input Component */
.input {
  display: flex;
  align-items: center;
  gap: var(--space-sm);
  padding: var(--space-md);
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-md);
  transition: all var(--transition-base);
}

.input:focus-within {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2);
}

.input__field {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  color: var(--text-primary);
  font-family: var(--font-family);
  font-size: var(--font-size-base);
}

.input__field::placeholder {
  color: var(--text-muted);
}

.input__icon {
  color: var(--text-muted);
  display: flex;
  align-items: center;
}

.input__clear {
  color: var(--text-muted);
  padding: var(--space-xs);
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  cursor: pointer;
}

.input__clear:hover {
  background: var(--glass-bg-hover);
  color: var(--text-secondary);
}

/* States */
.input--error {
  border-color: var(--error);
}

.input--success {
  border-color: var(--success);
}

.input:has(.input__field:disabled) {
  opacity: 0.5;
  cursor: not-allowed;
}
```

---

### Badge (atoms/badge/)

**badge.html:**
```html
<!--
  Badge Component
  ===============
  Block: .badge
  Modifiers: --info, --success, --warning, --error, --small, --medium
-->

<section class="component-variants">
  <h3>Variants</h3>

  <span class="badge badge--info">Info</span>
  <span class="badge badge--success">Success</span>
  <span class="badge badge--warning">Warning</span>
  <span class="badge badge--error">Error</span>
</section>

<section class="component-sizes">
  <h3>Sizes</h3>

  <span class="badge badge--info badge--small">Small</span>
  <span class="badge badge--info badge--medium">Medium</span>
</section>

<section class="component-usage">
  <h3>With Numbers</h3>

  <span class="badge badge--error">3</span>
  <span class="badge badge--info">99+</span>
</section>
```

**badge.css:**
```css
/* Badge Component */
.badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-xs) var(--space-sm);
  border-radius: var(--radius-full);
  font-size: var(--font-size-xs);
  font-weight: var(--font-weight-semibold);
  line-height: 1;
}

/* Variants */
.badge--info {
  background: rgba(59, 130, 246, 0.2);
  color: var(--info);
}

.badge--success {
  background: rgba(34, 197, 94, 0.2);
  color: var(--success);
}

.badge--warning {
  background: rgba(245, 158, 11, 0.2);
  color: var(--warning);
}

.badge--error {
  background: rgba(239, 68, 68, 0.2);
  color: var(--error);
}

/* Sizes */
.badge--small {
  padding: 2px 6px;
  font-size: 10px;
}

.badge--medium {
  padding: var(--space-xs) var(--space-sm);
  font-size: var(--font-size-xs);
}
```

---

## Molecules

### Card (molecules/card/)

**card.html:**
```html
<!--
  Card Component
  ==============
  Block: .card
  Elements: .card__header, .card__body, .card__footer, .card__title, .card__subtitle
  Modifiers: --elevated, --outlined, --clickable, --featured
-->

<section class="component-variants">
  <h3>Variants</h3>

  <!-- Default Card -->
  <div class="card">
    <div class="card__header">
      <h3 class="card__title">Card Title</h3>
      <p class="card__subtitle">Subtitle text</p>
    </div>
    <div class="card__body">
      <p>Card content goes here. This is the main body of the card.</p>
    </div>
    <div class="card__footer">
      <button class="btn btn--ghost btn--small">Cancel</button>
      <button class="btn btn--primary btn--small">Action</button>
    </div>
  </div>

  <!-- Elevated Card -->
  <div class="card card--elevated">
    <div class="card__body">
      <p>Elevated card with stronger shadow.</p>
    </div>
  </div>

  <!-- Clickable Card -->
  <div class="card card--clickable">
    <div class="card__body">
      <p>Clickable card with hover effect.</p>
    </div>
  </div>

  <!-- Featured Card -->
  <div class="card card--featured">
    <div class="card__header">
      <span class="badge badge--info">Featured</span>
      <h3 class="card__title">Featured Card</h3>
    </div>
    <div class="card__body">
      <p>Card with gradient border accent.</p>
    </div>
  </div>
</section>
```

**card.css:**
```css
/* Card Component */
.card {
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-lg);
  overflow: hidden;
}

.card__header {
  padding: var(--space-md);
  border-bottom: 1px solid var(--glass-border);
}

.card__title {
  color: var(--text-primary);
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-semibold);
  margin-bottom: var(--space-xs);
}

.card__subtitle {
  color: var(--text-secondary);
  font-size: var(--font-size-sm);
}

.card__body {
  padding: var(--space-md);
  color: var(--text-secondary);
}

.card__footer {
  padding: var(--space-md);
  border-top: 1px solid var(--glass-border);
  display: flex;
  justify-content: flex-end;
  gap: var(--space-sm);
}

/* Variants */
.card--elevated {
  box-shadow: var(--shadow-lg);
}

.card--clickable {
  cursor: pointer;
  transition: all var(--transition-base);
}

.card--clickable:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
  border-color: var(--primary);
}

.card--featured {
  border: 2px solid transparent;
  background:
    linear-gradient(var(--bg-secondary), var(--bg-secondary)) padding-box,
    var(--primary-gradient) border-box;
}
```

---

### List Item (molecules/list-item/)

**list-item.html:**
```html
<!--
  List Item Component
  ===================
  Block: .list-item
  Elements: .list-item__avatar, .list-item__content, .list-item__title, .list-item__subtitle, .list-item__action
  Modifiers: --clickable, --selected, --with-divider
-->

<section class="component-variants">
  <h3>Variants</h3>

  <!-- Basic List Item -->
  <div class="list-item">
    <div class="list-item__avatar">
      <div class="avatar avatar--medium"></div>
    </div>
    <div class="list-item__content">
      <p class="list-item__title">List Item Title</p>
      <p class="list-item__subtitle">Secondary text goes here</p>
    </div>
    <div class="list-item__action">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M9 18l6-6-6-6"/>
      </svg>
    </div>
  </div>

  <!-- Clickable -->
  <div class="list-item list-item--clickable">
    <div class="list-item__content">
      <p class="list-item__title">Clickable Item</p>
      <p class="list-item__subtitle">Tap to interact</p>
    </div>
  </div>

  <!-- Selected -->
  <div class="list-item list-item--selected">
    <div class="list-item__content">
      <p class="list-item__title">Selected Item</p>
    </div>
    <div class="list-item__action">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="3">
        <path d="M20 6L9 17l-5-5"/>
      </svg>
    </div>
  </div>
</section>
```

**list-item.css:**
```css
/* List Item Component */
.list-item {
  display: flex;
  align-items: center;
  gap: var(--space-md);
  padding: var(--space-md);
  background: var(--glass-bg);
  border-radius: var(--radius-md);
}

.list-item__avatar {
  flex-shrink: 0;
}

.list-item__content {
  flex: 1;
  min-width: 0;
}

.list-item__title {
  color: var(--text-primary);
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-medium);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.list-item__subtitle {
  color: var(--text-secondary);
  font-size: var(--font-size-sm);
  margin-top: var(--space-xs);
}

.list-item__action {
  flex-shrink: 0;
  color: var(--text-muted);
}

/* Variants */
.list-item--clickable {
  cursor: pointer;
  transition: background var(--transition-base);
}

.list-item--clickable:hover {
  background: var(--glass-bg-hover);
}

.list-item--selected {
  background: rgba(99, 102, 241, 0.1);
  border: 1px solid rgba(99, 102, 241, 0.3);
}

.list-item--with-divider {
  border-bottom: 1px solid var(--glass-border);
  border-radius: 0;
}
```

---

## Organisms

### Header (organisms/header/)

**header.html:**
```html
<!--
  Header Component
  ================
  Block: .header
  Elements: .header__left, .header__center, .header__right, .header__title, .header__back
  Modifiers: --transparent, --blur, --sticky
-->

<section class="component-variants">
  <h3>Variants</h3>

  <!-- Default Header -->
  <header class="header">
    <div class="header__left">
      <button class="header__back">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M15 18l-6-6 6-6"/>
        </svg>
      </button>
    </div>
    <div class="header__center">
      <h1 class="header__title">Page Title</h1>
    </div>
    <div class="header__right">
      <button class="btn btn--ghost">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/><circle cx="5" cy="12" r="1"/>
        </svg>
      </button>
    </div>
  </header>

  <!-- Blur Header -->
  <header class="header header--blur">
    <div class="header__center">
      <h1 class="header__title">Blur Header</h1>
    </div>
  </header>

  <!-- With Avatar -->
  <header class="header">
    <div class="header__left">
      <h1 class="header__title">Hello, User</h1>
    </div>
    <div class="header__right">
      <div class="avatar avatar--medium"></div>
    </div>
  </header>
</section>
```

**header.css:**
```css
/* Header Component */
.header {
  display: flex;
  align-items: center;
  height: var(--header-height);
  padding: 0 var(--space-md);
  background: var(--bg-primary);
}

.header__left,
.header__right {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  gap: var(--space-sm);
}

.header__center {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.header__title {
  color: var(--text-primary);
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-semibold);
}

.header__back {
  color: var(--text-primary);
  padding: var(--space-sm);
  margin-left: calc(var(--space-sm) * -1);
  border-radius: var(--radius-full);
  display: flex;
  align-items: center;
  justify-content: center;
}

.header__back:hover {
  background: var(--glass-bg);
}

/* Variants */
.header--blur {
  background: rgba(13, 13, 26, 0.8);
  backdrop-filter: blur(20px);
}

.header--transparent {
  background: transparent;
}

.header--sticky {
  position: sticky;
  top: 0;
  z-index: 100;
}
```

---

### Bottom Navigation (organisms/bottom-nav/)

**bottom-nav.html:**
```html
<!--
  Bottom Nav Component
  ====================
  Block: .bottom-nav
  Elements: .bottom-nav__item, .bottom-nav__icon, .bottom-nav__label
  Modifiers: --blur
  States: .bottom-nav__item--active
-->

<section class="component-variants">
  <h3>Variants</h3>

  <nav class="bottom-nav">
    <a href="#" class="bottom-nav__item bottom-nav__item--active">
      <span class="bottom-nav__icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
          <path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
        </svg>
      </span>
      <span class="bottom-nav__label">Home</span>
    </a>
    <a href="#" class="bottom-nav__item">
      <span class="bottom-nav__icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/>
        </svg>
      </span>
      <span class="bottom-nav__label">Search</span>
    </a>
    <a href="#" class="bottom-nav__item">
      <span class="bottom-nav__icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M19 21l-7-5-7 5V5a2 2 0 012-2h10a2 2 0 012 2z"/>
        </svg>
      </span>
      <span class="bottom-nav__label">Saved</span>
    </a>
    <a href="#" class="bottom-nav__item">
      <span class="bottom-nav__icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 010 2.83 2 2 0 01-2.83 0l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 01-2 2 2 2 0 01-2-2v-.09A1.65 1.65 0 009 19.4a1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 01-2.83 0 2 2 0 010-2.83l.06-.06a1.65 1.65 0 00.33-1.82 1.65 1.65 0 00-1.51-1H3a2 2 0 01-2-2 2 2 0 012-2h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 010-2.83 2 2 0 012.83 0l.06.06a1.65 1.65 0 001.82.33H9a1.65 1.65 0 001-1.51V3a2 2 0 012-2 2 2 0 012 2v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 012.83 0 2 2 0 010 2.83l-.06.06a1.65 1.65 0 00-.33 1.82V9a1.65 1.65 0 001.51 1H21a2 2 0 012 2 2 2 0 01-2 2h-.09a1.65 1.65 0 00-1.51 1z"/>
        </svg>
      </span>
      <span class="bottom-nav__label">Settings</span>
    </a>
  </nav>
</section>
```

**bottom-nav.css:**
```css
/* Bottom Nav Component */
.bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: var(--bottom-nav-height);
  background: rgba(13, 13, 26, 0.9);
  backdrop-filter: blur(20px);
  border-top: 1px solid var(--glass-border);
  display: flex;
  align-items: center;
  justify-content: space-around;
  padding: 0 var(--space-md);
  padding-bottom: env(safe-area-inset-bottom);
}

.bottom-nav__item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-xs);
  padding: var(--space-sm);
  color: var(--text-muted);
  text-decoration: none;
  transition: color var(--transition-base);
}

.bottom-nav__item:hover {
  color: var(--text-secondary);
}

.bottom-nav__item--active {
  color: var(--primary);
}

.bottom-nav__icon {
  display: flex;
  align-items: center;
  justify-content: center;
}

.bottom-nav__label {
  font-size: var(--font-size-xs);
  font-weight: var(--font-weight-medium);
}
```
