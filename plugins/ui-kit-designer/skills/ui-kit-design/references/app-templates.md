# App Type Templates

This document provides starting templates for common app types.

## Productivity / Todo App

### Screens to Include
1. Home (Task list with progress)
2. Add Task (Modal)
3. Task Detail (with subtasks)
4. Settings
5. Empty State
6. Snooze Options

### Key Components
- Checkbox/radio for tasks
- Priority indicators (color dots)
- Progress bars
- Due date pills
- Swipe actions

### Design Considerations
- Clear visual hierarchy for urgency
- Easy quick-add functionality
- Satisfying completion animations
- Non-judgmental empty states

---

## Fitness / Health App

### Screens to Include
1. Dashboard (Today's stats)
2. Workout List
3. Workout Detail / Active Workout
4. Progress Charts
5. Profile / Goals
6. Settings

### Key Components
- Circular progress rings
- Stat cards with icons
- Timer/stopwatch
- Heart rate zones
- Streak counters

### Design Considerations
- High contrast for gym lighting
- Large touch targets for sweaty fingers
- Motivational empty states
- Achievement celebrations

### Sample Stats Card
```html
<div style="margin: 20px; padding: 24px; background: rgba(255,255,255,0.08); border-radius: 20px; border: 1px solid rgba(255,255,255,0.1);">
  <p style="color: #94A3B8; font-size: 14px; margin: 0 0 4px 0;">Today's Activity</p>
  <p style="color: white; font-size: 32px; font-weight: 700; margin: 0 0 4px 0;">8,432</p>
  <p style="color: #22C55E; font-size: 14px; margin: 0;">↑ 12% from yesterday</p>
</div>
```

---

## Social / Messaging App

### Screens to Include
1. Feed / Timeline
2. Chat List
3. Chat Conversation
4. Profile
5. Notifications
6. Create Post / Compose

### Key Components
- Avatar circles
- Message bubbles
- Like/react animations
- Typing indicators
- Read receipts

### Design Considerations
- Fast scrolling performance
- Clear message ownership
- Timestamp visibility
- Online status indicators

### Sample Message Bubble
```html
<!-- Received message -->
<div style="display: flex; gap: 8px; margin-bottom: 12px; padding: 0 16px;">
  <div style="width: 32px; height: 32px; border-radius: 50%; background: linear-gradient(135deg, #6366F1, #8B5CF6);"></div>
  <div style="max-width: 70%;">
    <div style="background: rgba(255,255,255,0.08); border-radius: 16px 16px 16px 4px; padding: 12px 16px;">
      <p style="color: white; font-size: 15px; margin: 0;">Hey! How are you doing?</p>
    </div>
    <p style="color: #64748B; font-size: 11px; margin: 4px 0 0 8px;">2:34 PM</p>
  </div>
</div>

<!-- Sent message -->
<div style="display: flex; justify-content: flex-end; margin-bottom: 12px; padding: 0 16px;">
  <div style="max-width: 70%;">
    <div style="background: #6366F1; border-radius: 16px 16px 4px 16px; padding: 12px 16px;">
      <p style="color: white; font-size: 15px; margin: 0;">I'm great! Just finished my workout 💪</p>
    </div>
    <p style="color: #64748B; font-size: 11px; margin: 4px 8px 0 0; text-align: right;">2:35 PM ✓✓</p>
  </div>
</div>
```

---

## E-Commerce / Shopping App

### Screens to Include
1. Home (Featured + Categories)
2. Product List / Grid
3. Product Detail
4. Cart
5. Checkout
6. Order Confirmation

### Key Components
- Product cards with images
- Price displays
- Add to cart buttons
- Quantity selectors
- Shipping options
- Payment methods

### Design Considerations
- High-quality image placeholders
- Clear pricing hierarchy
- Trust indicators
- Easy cart access

### Sample Product Card
```html
<div style="width: calc(50% - 8px); background: rgba(255,255,255,0.06); border-radius: 16px; overflow: hidden;">
  <div style="width: 100%; height: 140px; background: linear-gradient(135deg, #1A1A2E, #252540);"></div>
  <div style="padding: 12px;">
    <p style="color: white; font-size: 14px; font-weight: 500; margin: 0 0 4px 0;">Product Name</p>
    <p style="color: #64748B; font-size: 12px; margin: 0 0 8px 0;">Brand</p>
    <div style="display: flex; justify-content: space-between; align-items: center;">
      <p style="color: #6366F1; font-size: 16px; font-weight: 700; margin: 0;">$49.99</p>
      <div style="width: 32px; height: 32px; background: #6366F1; border-radius: 50%; display: flex; align-items: center; justify-content: center;">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M12 5v14M5 12h14"/></svg>
      </div>
    </div>
  </div>
</div>
```

---

## Finance / Banking App

### Screens to Include
1. Dashboard (Balance + Recent)
2. Transaction List
3. Transaction Detail
4. Transfer / Send Money
5. Cards Management
6. Settings / Security

### Key Components
- Balance displays
- Transaction rows
- Card visuals
- Security indicators
- Quick actions

### Design Considerations
- Clear number formatting
- Color for +/- amounts
- Security reassurance
- Biometric indicators

### Sample Balance Card
```html
<div style="margin: 20px; padding: 24px; background: linear-gradient(135deg, #6366F1, #8B5CF6); border-radius: 20px; box-shadow: 0 8px 32px rgba(99,102,241,0.4);">
  <p style="color: rgba(255,255,255,0.8); font-size: 14px; margin: 0 0 8px 0;">Total Balance</p>
  <p style="color: white; font-size: 36px; font-weight: 700; margin: 0 0 16px 0;">$12,458.00</p>
  <div style="display: flex; gap: 16px;">
    <div style="flex: 1; background: rgba(255,255,255,0.2); border-radius: 12px; padding: 12px; text-align: center;">
      <p style="color: white; font-size: 12px; margin: 0 0 4px 0;">Income</p>
      <p style="color: white; font-size: 16px; font-weight: 600; margin: 0;">+$5,200</p>
    </div>
    <div style="flex: 1; background: rgba(255,255,255,0.2); border-radius: 12px; padding: 12px; text-align: center;">
      <p style="color: white; font-size: 12px; margin: 0 0 4px 0;">Expenses</p>
      <p style="color: white; font-size: 16px; font-weight: 600; margin: 0;">-$2,100</p>
    </div>
  </div>
</div>
```

---

## Music / Podcast App

### Screens to Include
1. Home (Discover + Recent)
2. Library / Playlists
3. Now Playing
4. Search
5. Artist / Album Detail
6. Settings

### Key Components
- Album art displays
- Playback controls
- Progress slider
- Queue management
- Waveform visualizations

### Design Considerations
- Large album artwork
- High contrast controls
- Lock screen compatibility
- Background playback indicator

### Sample Now Playing
```html
<div style="display: flex; flex-direction: column; align-items: center; padding: 40px 20px;">
  <!-- Album Art -->
  <div style="width: 280px; height: 280px; background: linear-gradient(135deg, #6366F1, #EC4899); border-radius: 20px; box-shadow: 0 16px 48px rgba(99,102,241,0.4); margin-bottom: 32px;"></div>

  <!-- Track Info -->
  <p style="color: white; font-size: 22px; font-weight: 700; margin: 0 0 4px 0; text-align: center;">Song Title</p>
  <p style="color: #94A3B8; font-size: 16px; margin: 0 0 24px 0;">Artist Name</p>

  <!-- Progress -->
  <div style="width: 100%; margin-bottom: 24px;">
    <div style="width: 100%; height: 4px; background: rgba(255,255,255,0.1); border-radius: 2px; overflow: hidden;">
      <div style="width: 35%; height: 100%; background: white; border-radius: 2px;"></div>
    </div>
    <div style="display: flex; justify-content: space-between; margin-top: 8px;">
      <span style="color: #64748B; font-size: 12px;">1:24</span>
      <span style="color: #64748B; font-size: 12px;">3:45</span>
    </div>
  </div>

  <!-- Controls -->
  <div style="display: flex; align-items: center; gap: 32px;">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#94A3B8" stroke-width="2"><path d="M19 20L9 12l10-8v16z"/><line x1="5" y1="4" x2="5" y2="20"/></svg>
    <div style="width: 64px; height: 64px; background: white; border-radius: 50%; display: flex; align-items: center; justify-content: center;">
      <svg width="28" height="28" viewBox="0 0 24 24" fill="#0D0D1A"><polygon points="5 3 19 12 5 21 5 3"/></svg>
    </div>
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#94A3B8" stroke-width="2"><path d="M5 4l10 8-10 8V4z"/><line x1="19" y1="4" x2="19" y2="20"/></svg>
  </div>
</div>
```

---

## Meditation / Wellness App

### Screens to Include
1. Home (Daily suggestions)
2. Session Browser
3. Active Session
4. Stats / Streak
5. Sleep Sounds
6. Profile / Settings

### Key Components
- Breathing animations
- Timer displays
- Streak calendars
- Ambient sound mixers
- Session cards

### Design Considerations
- Calming color palette
- Minimal distractions
- Dark mode for night use
- Gentle animations

### Sample Breathing Circle
```html
<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 400px;">
  <div style="width: 200px; height: 200px; border-radius: 50%; background: rgba(99,102,241,0.2); display: flex; align-items: center; justify-content: center; animation: breathe 4s infinite ease-in-out;">
    <div style="width: 160px; height: 160px; border-radius: 50%; background: rgba(99,102,241,0.3); display: flex; align-items: center; justify-content: center;">
      <div style="width: 120px; height: 120px; border-radius: 50%; background: linear-gradient(135deg, #6366F1, #8B5CF6); display: flex; align-items: center; justify-content: center;">
        <p style="color: white; font-size: 24px; font-weight: 700; margin: 0;">Breathe</p>
      </div>
    </div>
  </div>
  <p style="color: #94A3B8; font-size: 16px; margin: 32px 0 0 0;">Inhale slowly...</p>
</div>
```

---

## Recipe / Cooking App

### Screens to Include
1. Home (Featured recipes)
2. Recipe List / Search
3. Recipe Detail
4. Cooking Mode (step by step)
5. Shopping List
6. Saved / Favorites

### Key Components
- Food imagery placeholders
- Ingredient lists
- Step cards
- Timer integration
- Nutrition info

### Design Considerations
- Kitchen-friendly (large text)
- Step-by-step clarity
- Shopping list integration
- Voice control hints

### Sample Recipe Card
```html
<div style="margin: 0 20px 16px; background: rgba(255,255,255,0.06); border-radius: 16px; overflow: hidden;">
  <div style="width: 100%; height: 160px; background: linear-gradient(135deg, #F59E0B, #EF4444);"></div>
  <div style="padding: 16px;">
    <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 8px;">
      <p style="color: white; font-size: 18px; font-weight: 600; margin: 0;">Pasta Carbonara</p>
      <div style="display: flex; align-items: center; gap: 4px;">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="#F59E0B"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
        <span style="color: #F59E0B; font-size: 14px; font-weight: 600;">4.8</span>
      </div>
    </div>
    <div style="display: flex; gap: 16px;">
      <div style="display: flex; align-items: center; gap: 4px;">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#64748B" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
        <span style="color: #64748B; font-size: 13px;">25 min</span>
      </div>
      <div style="display: flex; align-items: center; gap: 4px;">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#64748B" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
        <span style="color: #64748B; font-size: 13px;">4 servings</span>
      </div>
    </div>
  </div>
</div>
```

---

## Travel / Booking App

### Screens to Include
1. Home (Search + Deals)
2. Search Results
3. Listing Detail
4. Booking / Checkout
5. Trips / Itinerary
6. Profile / Settings

### Key Components
- Search bars with dates
- Price cards
- Image galleries
- Map integration
- Booking summary

### Design Considerations
- Trust and reviews
- Clear pricing
- Date pickers
- Location context
