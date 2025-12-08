# Component Library Reference

This document provides copy-paste ready components for UI kit creation.

## Cards

### Stats Card

```html
<div style="margin: 20px; padding: 24px; background: rgba(255,255,255,0.08); backdrop-filter: blur(20px); border-radius: 20px; border: 1px solid rgba(255,255,255,0.1);">
  <p style="color: #94A3B8; font-size: 14px; margin: 0 0 8px 0;">Good morning! 👋</p>
  <p style="color: white; font-size: 20px; font-weight: 600; margin: 0 0 16px 0;">You have 5 tasks today</p>
  <div style="width: 100%; height: 8px; background: rgba(255,255,255,0.1); border-radius: 4px; overflow: hidden;">
    <div style="width: 60%; height: 100%; background: linear-gradient(90deg, #6366F1 0%, #22C55E 100%); border-radius: 4px;"></div>
  </div>
</div>
```

### Feature Card with Icon

```html
<div style="background: rgba(139,92,246,0.15); border-radius: 16px; border: 1px solid rgba(139,92,246,0.3); padding: 20px;">
  <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
    <span style="font-size: 24px;">🎯</span>
    <div>
      <p style="color: white; font-size: 15px; font-weight: 600; margin: 0;">Feature Title</p>
      <p style="color: #A5B4FC; font-size: 13px; margin: 4px 0 0;">Feature description</p>
    </div>
  </div>
  <div style="background: rgba(255,255,255,0.1); border-radius: 12px; padding: 14px 16px; display: flex; align-items: center; justify-content: space-between; cursor: pointer;">
    <span style="color: white; font-size: 14px; font-weight: 500;">Action button</span>
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#A5B4FC" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>
  </div>
</div>
```

### Selectable Card (Selected State)

```html
<div style="flex: 1; padding: 12px; background: #6366F1; border-radius: 12px; text-align: center; cursor: pointer;">
  <span style="font-size: 20px;">🌅</span>
  <p style="color: white; font-size: 12px; margin: 6px 0 0; font-weight: 500;">Morning</p>
</div>
```

### Selectable Card (Unselected State)

```html
<div style="flex: 1; padding: 12px; background: rgba(255,255,255,0.08); border-radius: 12px; text-align: center; cursor: pointer;">
  <span style="font-size: 20px;">🌙</span>
  <p style="color: #94A3B8; font-size: 12px; margin: 6px 0 0;">Evening</p>
</div>
```

## List Items

### Basic List Item

```html
<div style="padding: 16px 20px; display: flex; align-items: center; gap: 16px; border-bottom: 1px solid rgba(255,255,255,0.06);">
  <div style="width: 40px; height: 40px; border-radius: 12px; background: linear-gradient(135deg, #6366F1, #8B5CF6); display: flex; align-items: center; justify-content: center;">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
      <!-- Icon -->
    </svg>
  </div>
  <div style="flex: 1; min-width: 0;">
    <p style="color: white; font-size: 15px; font-weight: 500; margin: 0;">Item Title</p>
    <p style="color: #64748B; font-size: 13px; margin: 2px 0 0;">Item description</p>
  </div>
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#64748B" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>
</div>
```

### Todo Item (Unchecked)

```html
<div style="margin: 0 20px 12px; padding: 16px 20px; background: rgba(255,255,255,0.06); border-radius: 16px; border: 1px solid rgba(255,255,255,0.08); display: flex; align-items: center; gap: 16px;">
  <div style="width: 24px; height: 24px; border: 2px solid #6366F1; border-radius: 50%; flex-shrink: 0;"></div>
  <div style="flex: 1; min-width: 0;">
    <p style="color: white; font-size: 16px; font-weight: 500; margin: 0 0 4px 0;">Task title</p>
    <p style="color: #64748B; font-size: 13px; margin: 0;">Due tomorrow</p>
  </div>
  <div style="width: 12px; height: 12px; background: #F59E0B; border-radius: 50%; flex-shrink: 0;"></div>
</div>
```

### Todo Item (Checked)

```html
<div style="margin: 0 20px 12px; padding: 16px 20px; background: rgba(255,255,255,0.03); border-radius: 16px; display: flex; align-items: center; gap: 16px;">
  <div style="width: 24px; height: 24px; background: #22C55E; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
    <svg width="12" height="10" viewBox="0 0 12 10" fill="none">
      <path d="M1 5L4.5 8.5L11 1" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </div>
  <div style="flex: 1; min-width: 0;">
    <p style="color: #64748B; font-size: 16px; font-weight: 500; margin: 0; text-decoration: line-through;">Completed task</p>
  </div>
</div>
```

### Settings Item with Toggle

```html
<div style="padding: 16px 20px; display: flex; align-items: center; justify-content: space-between;">
  <div>
    <p style="color: white; font-size: 15px; font-weight: 500; margin: 0 0 2px 0;">Setting name</p>
    <p style="color: #64748B; font-size: 13px; margin: 0;">Setting description</p>
  </div>
  <div style="width: 48px; height: 28px; background: #6366F1; border-radius: 14px; position: relative; cursor: pointer;">
    <div style="width: 24px; height: 24px; background: white; border-radius: 50%; position: absolute; right: 2px; top: 2px;"></div>
  </div>
</div>
```

### Settings Item with Value

```html
<div style="padding: 16px 20px; display: flex; align-items: center; justify-content: space-between;">
  <div>
    <p style="color: white; font-size: 15px; font-weight: 500; margin: 0 0 2px 0;">Setting name</p>
    <p style="color: #64748B; font-size: 13px; margin: 0;">Setting description</p>
  </div>
  <div style="display: flex; align-items: center; gap: 8px; cursor: pointer;">
    <span style="color: #6366F1; font-size: 15px; font-weight: 600;">21:00</span>
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#64748B" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>
  </div>
</div>
```

## Buttons

### Primary Button (Large)

```html
<div style="background: linear-gradient(135deg, #6366F1, #8B5CF6); border-radius: 16px; padding: 18px; text-align: center; box-shadow: 0 8px 24px rgba(99,102,241,0.3); cursor: pointer;">
  <span style="color: white; font-size: 16px; font-weight: 600;">Button Text</span>
</div>
```

### Secondary Button

```html
<div style="background: rgba(255,255,255,0.08); border-radius: 12px; padding: 14px 24px; text-align: center; cursor: pointer;">
  <span style="color: #94A3B8; font-size: 14px; font-weight: 500;">Button Text</span>
</div>
```

### Pill Button (Selected)

```html
<div style="padding: 8px 16px; background: #6366F1; border-radius: 20px; cursor: pointer;">
  <span style="color: white; font-size: 13px; font-weight: 500;">🌅 Morning</span>
</div>
```

### Pill Button (Unselected)

```html
<div style="padding: 8px 16px; background: rgba(255,255,255,0.08); border-radius: 20px; cursor: pointer;">
  <span style="color: #94A3B8; font-size: 13px;">☀️ Afternoon</span>
</div>
```

### Icon Button

```html
<div style="width: 40px; height: 40px; border-radius: 12px; background: rgba(255,255,255,0.08); display: flex; align-items: center; justify-content: center; cursor: pointer;">
  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#94A3B8" stroke-width="2">
    <circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/><circle cx="5" cy="12" r="1"/>
  </svg>
</div>
```

## Form Inputs

### Text Input

```html
<div style="margin-bottom: 16px;">
  <p style="color: #94A3B8; font-size: 13px; font-weight: 500; margin: 0 0 8px 0;">Label</p>
  <div style="background: rgba(255,255,255,0.08); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.1);">
    <p style="color: white; font-size: 16px; margin: 0;">Input value</p>
  </div>
</div>
```

### Text Input (Focused)

```html
<div style="margin-bottom: 16px;">
  <p style="color: #94A3B8; font-size: 13px; font-weight: 500; margin: 0 0 8px 0;">Label</p>
  <div style="background: rgba(255,255,255,0.08); border-radius: 12px; padding: 16px; border: 1px solid rgba(99,102,241,0.5);">
    <p style="color: white; font-size: 16px; margin: 0;">Input value<span style="animation: blink 1s infinite;">|</span></p>
  </div>
</div>
```

### Segmented Control

```html
<div style="display: flex; gap: 8px;">
  <div style="flex: 1; background: #6366F1; border-radius: 12px; padding: 12px 16px; text-align: center; cursor: pointer;">
    <span style="color: white; font-size: 14px; font-weight: 500;">Today</span>
  </div>
  <div style="flex: 1; background: rgba(255,255,255,0.08); border-radius: 12px; padding: 12px 16px; text-align: center; cursor: pointer;">
    <span style="color: #94A3B8; font-size: 14px;">Tomorrow</span>
  </div>
  <div style="flex: 1; background: rgba(255,255,255,0.08); border-radius: 12px; padding: 12px 16px; text-align: center; cursor: pointer;">
    <span style="color: #94A3B8; font-size: 14px;">Custom</span>
  </div>
</div>
```

### Priority Selector

```html
<div style="display: flex; gap: 8px;">
  <div style="flex: 1; background: rgba(239,68,68,0.2); border: 2px solid #EF4444; border-radius: 12px; padding: 12px; text-align: center; cursor: pointer;">
    <div style="width: 12px; height: 12px; background: #EF4444; border-radius: 50%; margin: 0 auto 6px;"></div>
    <span style="color: #EF4444; font-size: 12px; font-weight: 500;">High</span>
  </div>
  <div style="flex: 1; background: rgba(255,255,255,0.08); border-radius: 12px; padding: 12px; text-align: center; cursor: pointer;">
    <div style="width: 12px; height: 12px; background: #F59E0B; border-radius: 50%; margin: 0 auto 6px;"></div>
    <span style="color: #94A3B8; font-size: 12px;">Medium</span>
  </div>
  <div style="flex: 1; background: rgba(255,255,255,0.08); border-radius: 12px; padding: 12px; text-align: center; cursor: pointer;">
    <div style="width: 12px; height: 12px; background: #22C55E; border-radius: 50%; margin: 0 auto 6px;"></div>
    <span style="color: #94A3B8; font-size: 12px;">Low</span>
  </div>
</div>
```

## Navigation

### Header Bar

```html
<div style="width: 100%; height: 100px; background: rgba(255,255,255,0.05); backdrop-filter: blur(20px); display: flex; align-items: center; justify-content: space-between; padding: 44px 24px 0 24px; box-sizing: border-box;">
  <div style="width: 40px;"></div>
  <span style="font-size: 18px; font-weight: 700; color: white;">App Name</span>
  <div style="width: 40px; height: 40px; border-radius: 12px; background: linear-gradient(135deg, #6366F1, #8B5CF6); display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 12px rgba(99,102,241,0.3);">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none">
      <path d="M4 12.5L9 17.5L20 6.5" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </div>
</div>
```

### Header with Back Button

```html
<div style="width: 100%; height: 100px; background: rgba(255,255,255,0.05); backdrop-filter: blur(20px); display: flex; align-items: center; justify-content: space-between; padding: 44px 24px 0 24px; box-sizing: border-box;">
  <div style="width: 40px; height: 40px; border-radius: 12px; display: flex; align-items: center; justify-content: center; cursor: pointer;">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
      <path d="M15 18l-6-6 6-6"/>
    </svg>
  </div>
  <span style="font-size: 18px; font-weight: 700; color: white;">Page Title</span>
  <div style="width: 40px;"></div>
</div>
```

### Bottom Tab Bar

```html
<div style="position: absolute; bottom: 0; left: 0; width: 100%; height: 70px; background: rgba(255,255,255,0.05); backdrop-filter: blur(20px); display: flex; align-items: center; justify-content: center; gap: 100px;">
  <div style="display: flex; flex-direction: column; align-items: center; gap: 4px; cursor: pointer;">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
      <rect x="3" y="3" width="18" height="18" rx="4" stroke="#6366F1" stroke-width="2"/>
      <path d="M8 12L11 15L16 9" stroke="#6366F1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    <span style="font-size: 11px; color: #6366F1; font-weight: 600;">Tasks</span>
  </div>
  <div style="display: flex; flex-direction: column; align-items: center; gap: 4px; cursor: pointer;">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#64748B" stroke-width="2">
      <circle cx="12" cy="12" r="3"/>
      <path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/>
    </svg>
    <span style="font-size: 11px; color: #64748B; font-weight: 500;">Settings</span>
  </div>
</div>
```

## Modals & Bottom Sheets

### Bottom Sheet Container

```html
<div class="phone-frame" style="background: rgba(0,0,0,0.7); backdrop-filter: blur(4px);">
  <div style="position: absolute; bottom: 0; left: 0; width: 100%; background: #1A1A2E; border-radius: 24px 24px 0 0; padding: 24px; box-sizing: border-box;">
    <!-- Handle -->
    <div style="width: 40px; height: 4px; background: rgba(255,255,255,0.2); border-radius: 2px; margin: 0 auto 24px;"></div>

    <!-- Title -->
    <p style="color: white; font-size: 20px; font-weight: 700; margin: 0 0 8px 0;">Sheet Title</p>
    <p style="color: #64748B; font-size: 14px; margin: 0 0 20px 0;">Sheet description</p>

    <!-- Content -->

    <!-- Bottom spacing -->
    <div style="height: 20px;"></div>
  </div>
</div>
```

### Option Item in Bottom Sheet

```html
<div style="background: rgba(255,255,255,0.08); border-radius: 12px; padding: 16px 20px; display: flex; align-items: center; gap: 16px; cursor: pointer; margin-bottom: 8px;">
  <span style="font-size: 20px;">☕</span>
  <div style="flex: 1;">
    <p style="color: white; font-size: 15px; font-weight: 500; margin: 0;">Option title</p>
    <p style="color: #64748B; font-size: 13px; margin: 2px 0 0;">Option description</p>
  </div>
</div>
```

## Empty States

### Empty State (Celebratory)

```html
<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 550px; padding: 40px;">
  <div style="width: 120px; height: 120px; background: rgba(99,102,241,0.1); border-radius: 60px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px;">
    <span style="font-size: 56px;">🎉</span>
  </div>
  <p style="color: white; font-size: 22px; font-weight: 700; margin: 0 0 12px 0; text-align: center;">All done!</p>
  <p style="color: #64748B; font-size: 16px; margin: 0 0 32px 0; text-align: center; line-height: 1.5;">You've completed all your tasks.<br/>Take a moment to celebrate! 🙌</p>
  <div style="background: linear-gradient(135deg, #6366F1, #8B5CF6); border-radius: 16px; padding: 16px 32px; box-shadow: 0 8px 24px rgba(99,102,241,0.3); cursor: pointer;">
    <span style="color: white; font-size: 16px; font-weight: 600;">Add a new task</span>
  </div>
</div>
```

### Empty State (Onboarding)

```html
<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 550px; padding: 40px;">
  <div style="width: 120px; height: 120px; background: rgba(99,102,241,0.1); border-radius: 60px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px;">
    <span style="font-size: 56px;">📝</span>
  </div>
  <p style="color: white; font-size: 22px; font-weight: 700; margin: 0 0 12px 0; text-align: center;">No items yet</p>
  <p style="color: #64748B; font-size: 16px; margin: 0 0 32px 0; text-align: center; line-height: 1.5;">Get started by adding your first item.<br/>Tap the button below to begin.</p>
  <div style="background: linear-gradient(135deg, #6366F1, #8B5CF6); border-radius: 16px; padding: 16px 32px; box-shadow: 0 8px 24px rgba(99,102,241,0.3); cursor: pointer;">
    <span style="color: white; font-size: 16px; font-weight: 600;">Get Started</span>
  </div>
</div>
```

## Progress Indicators

### Progress Bar

```html
<div style="width: 100%; height: 8px; background: rgba(255,255,255,0.1); border-radius: 4px; overflow: hidden;">
  <div style="width: 65%; height: 100%; background: linear-gradient(90deg, #6366F1 0%, #22C55E 100%); border-radius: 4px;"></div>
</div>
```

### Step Progress

```html
<div style="display: flex; align-items: center; gap: 8px;">
  <span style="color: #6366F1; font-size: 14px; font-weight: 600;">3/5</span>
  <div style="width: 60px; height: 6px; background: rgba(255,255,255,0.1); border-radius: 3px; overflow: hidden;">
    <div style="width: 60%; height: 100%; background: linear-gradient(90deg, #6366F1, #22C55E); border-radius: 3px;"></div>
  </div>
</div>
```

### Circular Badge

```html
<div style="width: 20px; height: 20px; background: #EF4444; border-radius: 50%; display: flex; align-items: center; justify-content: center;">
  <span style="color: white; font-size: 11px; font-weight: 600;">3</span>
</div>
```

## Section Headers

### Section Title

```html
<p style="color: white; font-size: 18px; font-weight: 600; padding: 0 20px; margin: 0 0 16px 0;">Section Title</p>
```

### Section Label (Uppercase)

```html
<p style="color: #64748B; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; margin: 0 0 12px 0;">Category Label 💭</p>
```

### Completed Section Header

```html
<p style="color: #64748B; font-size: 14px; font-weight: 600; padding: 0 20px; margin: 24px 0 12px 0;">Completed</p>
```
