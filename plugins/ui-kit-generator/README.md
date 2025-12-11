# UI-Kit Generator Plugin

Generate complete UI-Kits based on **Atomic Design methodology** with customizable design styles.

## Features

- **Atomic Design**: Generates tokens → atoms → molecules → organisms → templates → pages
- **Multiple Styles**: Glassmorphism, Neumorphism, Material Design, Bootstrap, and more
- **Smart Planning**: Top-down analysis, bottom-up generation
- **Interactive Preview**: Dynamic preview system with iframe loading (no duplication)
- **Token-Efficient**: Hybrid agent architecture to optimize context usage

## Quick Start

```bash
# Start UI-Kit generation
/ui-kit-generator:generate "A task management app with dashboard, login, settings pages in glassmorphism style"
```

## Workflow

### Phase 1: Discovery
- Describe your app/webapp
- List required pages/screens
- Choose design style (Glassmorphism, Material, etc.)
- Agent asks clarifying questions

### Phase 2: Planning
- Agent analyzes requirements top-down (pages → atoms)
- Creates component hierarchy
- User approves the plan

### Phase 3: Generation
- Tokens generated first
- Then atoms, molecules, organisms, templates, pages
- Each level builds on the previous
- Hybrid agents (split large batches)

### Phase 4: Assembly
- Creates manifest.json
- Sets up preview system
- Components loaded via iframe (no duplication)

## Output Structure

```
your-ui-kit/
├── tokens/
│   ├── tokens.css       # CSS custom properties
│   └── tokens.json      # JSON representation
├── atoms/
│   └── button/
│       └── button.html  # All button variants
├── molecules/
│   └── card/
│       └── card.html
├── organisms/
│   └── header/
│       └── header.html
├── templates/
│   └── dashboard-layout/
│       └── dashboard-layout.html
├── pages/
│   └── dashboard/
│       └── dashboard.html
├── manifest.json        # Component registry
├── preview.html         # Interactive preview
└── preview.css
```

## Preview System

The preview uses a **static template + dynamic manifest** approach:

- `preview.html` reads `manifest.json` to build navigation
- Components loaded via `<iframe>` (no inline duplication)
- Category → Component → Variants navigation
- Keyboard navigation (← →)

## Design Styles

### Glassmorphism
- Semi-transparent backgrounds with backdrop blur
- Subtle borders and glow effects
- Works best on colorful backgrounds

### Neumorphism
- Dual shadows (light + dark)
- Soft, pillow-like appearance
- Same-color backgrounds

### Material Design
- Elevation-based shadows
- Bold colors, ripple effects
- Clear visual hierarchy

## Components

| Type | Count | Examples |
|------|-------|----------|
| Atoms | 8 | Button, Input, Badge, Avatar, Icon, Spinner, Label, Divider |
| Molecules | 8 | Card, FormField, SearchBar, NavItem, ButtonGroup, InputGroup, ListItem, MediaObject |
| Organisms | 8 | Header, Sidebar, Footer, Modal, Form, NavigationMenu, CardGrid, ContentSection |
| Templates | 4 | DashboardLayout, AuthLayout, ContentLayout, SettingsLayout |
| Pages | 5 | Dashboard, Login, Home, Profile, Settings |

## Plugin Structure

```
ui-kit-generator/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   └── generate.md         # Main command
├── agents/
│   ├── planning-agent.md   # Architecture planning
│   ├── token-agent.md      # Design tokens
│   ├── atom-agent.md       # Atomic components
│   ├── molecule-agent.md   # Molecule components
│   ├── organism-agent.md   # Organism components
│   ├── template-agent.md   # Layout templates
│   ├── page-agent.md       # Page implementations
│   └── assembly-agent.md   # Final assembly
├── skills/
│   └── ui-kit-patterns/
│       ├── SKILL.md
│       └── references/
│           ├── glassmorphism.md
│           ├── neumorphism.md
│           └── material.md
└── templates/
    └── preview/
        ├── preview.html    # Static preview template
        └── preview.css
```

## Requirements

- Claude Code CLI
- Modern browser (for preview with backdrop-filter support)

## License

MIT
