---
description: Generate a complete UI-Kit based on Atomic Design methodology
argument-hint: "[app description]"
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
  - Task
  - TodoWrite
  - AskUserQuestion
---

# UI-Kit Generator (Web Components Edition)

You are orchestrating the generation of a complete UI-Kit using **Web Components** and **Atomic Design methodology**.

## Architecture Overview

This generator creates **native Web Components** that:
- Use Shadow DOM for encapsulation
- Compose via ES6 imports (no style duplication)
- Support attributes for configuration
- Use slots for content projection
- Can run **fully parallel** after tokens are generated

## Workflow Overview

```
Discovery → Planning → Tokens ─┬─→ Atoms (parallel)     ─┐
                               ├─→ Molecules (parallel)  │
                               ├─→ Organisms (parallel)  ├─→ Assembly → Done
                               ├─→ Templates (parallel)  │
                               ├─→ Pages (parallel)      │
                               └─→ Showcase (parallel)  ─┘
```

**Key: All component agents run in PARALLEL after tokens!**

---

## Phase 1: Discovery

If the user provided an app description in the arguments, use that. Otherwise, ask clarifying questions.

**Gather this information:**

1. **App/WebApp Description**: What is the purpose? Who are the users?

2. **Required Pages/Screens**: Ask the user to list all pages they need, e.g.:
   - Login / Register
   - Dashboard
   - Profile / Settings
   - Home / Landing

3. **Design Style**: Ask which visual style they prefer:
   - **Glassmorphism** - Semi-transparent glass effects with blur
   - **Material Design** - Google's design system with elevation
   - **Neumorphism** - Soft UI with subtle shadows
   - **Bootstrap** - Classic web design
   - **Custom** - Let user describe

4. **Color Palette** (optional): Primary, secondary, accent colors

5. **Output Directory**: Where to generate the UI-Kit (default: `./ui-kit`)

**Use AskUserQuestion to gather this information efficiently.**

When the user confirms they want to proceed to planning, move to Phase 2.

---

## Phase 2: Planning

Launch the planning-agent to analyze requirements and create the component tree.

```
Task: planning-agent
Prompt: |
  Analyze the following requirements and create a complete component tree.

  App: {app_description}
  Pages: {pages_list}
  Style: {design_style}
  Colors: {color_info}

  Create a hierarchical component breakdown for Web Components:
  - Atoms (ui-button, ui-input, etc.)
  - Molecules (ui-card, ui-form-field, etc.)
  - Organisms (ui-header, ui-sidebar, etc.)
  - Templates (ui-dashboard-layout, etc.)
  - Pages (dashboard.html, login.html, etc.)
```

Present the plan to the user for approval before continuing.

---

## Phase 3: Generation (PARALLEL)

After tokens are generated, launch ALL component agents **in parallel**.

### 3.1 Generate Tokens (Sequential - Must be first)
```
Task: token-agent
Prompt: |
  Generate design tokens for {design_style} style.
  Output: {output_dir}/tokens/tokens.css and tokens.json
  Include: colors, typography, spacing, shadows, glass effects, etc.
```

### 3.2 Copy Base Component
Copy the base component template to the output directory:
```bash
mkdir -p {output_dir}/components
cp templates/components/base-component.js {output_dir}/components/
```

### 3.3 Generate ALL Components in PARALLEL

**IMPORTANT: Launch these agents simultaneously using multiple Task tool calls in a single message:**

```
# Launch ALL of these in PARALLEL (single message, multiple tool calls):

Task: atom-agent [run_in_background: true]
Prompt: Generate atoms: {atom_list}. Style: {style}. Output: {output_dir}/components/atoms/

Task: molecule-agent [run_in_background: true]
Prompt: Generate molecules: {molecule_list}. Style: {style}. Output: {output_dir}/components/molecules/

Task: organism-agent [run_in_background: true]
Prompt: Generate organisms: {organism_list}. Style: {style}. Output: {output_dir}/components/organisms/

Task: template-agent [run_in_background: true]
Prompt: Generate templates: {template_list}. Style: {style}. Output: {output_dir}/components/templates/

Task: page-agent [run_in_background: true]
Prompt: Generate pages: {page_list}. App: {app_name}. Style: {style}. Output: {output_dir}/pages/

Task: showcase-agent [run_in_background: true]
Prompt: Generate showcases for all components. Style: {style}. Output: {output_dir}/showcase/
```

**Wait for all agents to complete using AgentOutputTool.**

---

## Phase 4: Assembly

After all components are generated, run the assembly agent:

```
Task: assembly-agent
Prompt: |
  Assemble the final UI-Kit:
  - Scan {output_dir}/components/ for all Web Components
  - Generate {output_dir}/components/index.js (barrel export)
  - Create {output_dir}/manifest.json
  - Copy preview template to {output_dir}/preview.html
```

---

## Output Structure

```
{output_dir}/
├── tokens/
│   ├── tokens.css           # CSS custom properties
│   └── tokens.json          # JSON representation
├── components/
│   ├── base-component.js    # Base class for all components
│   ├── index.js             # Barrel export (auto-generated)
│   ├── atoms/
│   │   ├── ui-button.js
│   │   ├── ui-input.js
│   │   └── ...
│   ├── molecules/
│   │   ├── ui-card.js
│   │   └── ...
│   ├── organisms/
│   │   ├── ui-header.js
│   │   └── ...
│   └── templates/
│       ├── ui-dashboard-layout.js
│       └── ...
├── pages/
│   ├── dashboard.html
│   ├── login.html
│   └── ...
├── showcase/
│   ├── atoms/
│   │   └── button.html
│   ├── molecules/
│   ├── organisms/
│   └── templates/
├── manifest.json
└── preview.html
```

---

## Why Parallel Works

With Web Components:
1. **No Style Duplication**: Components import dependencies via ES6
2. **Runtime Resolution**: Browser resolves imports at runtime
3. **Single Source of Truth**: Each component defined once
4. **Only tokens.css Required**: All components reference the same tokens

This enables **~80% speedup** compared to sequential generation!

---

## Guidelines

1. **Parallel First**: Always launch agents in parallel where possible
2. **Wait for Tokens**: Only tokens must complete before other agents
3. **Use Background Tasks**: Set `run_in_background: true` for parallel agents
4. **Single Message**: Launch all parallel agents in ONE message with multiple tool calls
5. **User Confirmation**: Get approval after planning before generating

---

## Start

Begin with Phase 1: Discovery. Ask the user about their app if no description was provided.
