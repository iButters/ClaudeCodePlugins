# maui-blazor-development

Expert guidance for building cross‑platform apps with .NET MAUI and Blazor Hybrid, combining native capabilities with a shared Blazor UI.

> **TL;DR:** Use this plugin whenever you build or refactor .NET MAUI Blazor Hybrid apps and want Claude to think like an experienced cross‑platform/mobile architect.

---

## Overview

- **Category:** Cross‑platform UI, mobile/desktop apps, Blazor Hybrid
- **Primary goal:** Help you design and implement robust, maintainable MAUI Blazor Hybrid applications that share UI across platforms.
- **Typical use cases:**
  - Setting up a new .NET MAUI Blazor Hybrid project
  - Sharing Razor components between mobile, desktop, and web
  - Integrating native platform features (camera, sensors, file system, notifications)
  - Designing navigation between MAUI pages and Blazor components
  - Choosing and structuring state management (MVVM, DI, component state)
- **Requirements:** A .NET MAUI project with BlazorWebView (or a plan to create one), and Claude Code with this plugin enabled.

---

## Installation

### Via Claude Code Marketplace

```bash
/plugin marketplace add <MARKETPLACE-NAME>
/plugin install maui-blazor-development@<MARKETPLACE-NAME>
```

After installation, Claude will use the MAUI Blazor Development skill whenever you work inside `.NET MAUI` + Blazor Hybrid projects or reference MAUI/Blazor concepts.

### Manual installation (optional)

If using this repository directly:

1. Clone this marketplace repository.
2. Ensure the `maui-blazor-development` folder is placed under your Claude marketplace `plugins/` directory.
3. Restart Claude so it can discover the plugin from `.claude-plugin/plugin.json`.

---

## Quick Start

1. Create or open a .NET MAUI Blazor Hybrid project (e.g. via `dotnet new maui-blazor`).
2. Start a Claude Code session in the project root.
3. Ask Claude to:
   - “Review my MAUI Blazor Hybrid setup.”
   - “Help me structure navigation between MAUI pages and Blazor components.”
   - “Design state management for this cross‑platform app.”

Example:

```text
Use the maui-blazor-development skill.
I’m building a MAUI Blazor Hybrid app targeting Android, iOS, and Windows.
Help me design the architecture (services, Blazor components, and navigation).
```

Claude will then rely on the guidance and patterns encoded in this plugin’s SKILL and reference docs.

---

## Feature Overview

- **App architecture:** Decide between pure MAUI Blazor, MAUI + shared Blazor Web, and hybrid layouts.
- **Blazor components:** Lifecycle, data binding, event handling, and composition for mobile scenarios.
- **Platform integration:** Using platform services (permissions, sensors, camera, storage) from Blazor components.
- **Navigation patterns:** Shell navigation, Blazor routing, and mixed MAUI/Blazor navigation strategies.
- **State management:** Component state, MVVM, DI‑backed services, and hybrid approaches.
- **Performance & UX:** Advice for startup time, resource usage, and responsive layouts across devices.

---

## Typical Workflows

### Workflow 1: Setting up a MAUI Blazor Hybrid app

1. Describe your app concept and target platforms.
2. Ask Claude which project template and structure to use (e.g. MAUI Blazor vs MAUI + shared RCL).
3. Let Claude propose a `MauiProgram.cs` configuration and DI setup.
4. Design `MainPage.xaml` and the `BlazorWebView` wiring using the recommended structure.
5. Add initial services and components (e.g. `Main.razor`) following the plugin’s patterns.

### Workflow 2: Integrating native features into Blazor components

1. Explain which native capability you need (camera, file picker, notifications, sensors, etc.).
2. Ask Claude to design the platform service abstraction and registration in `MauiProgram.cs`.
3. Generate example Razor components that inject and use these services.
4. Ensure permission handling and platform checks follow best practices.

### Workflow 3: Navigation and state management

1. Describe how you want users to move between screens (tabs, pages, deep links).
2. Ask Claude to propose a navigation strategy: Shell, Blazor routing, or mixed.
3. Design ViewModels/services (if using MVVM) or DI singletons (for shared state).
4. Implement components/pages with clear state boundaries and lifecycle handling.

---

## Configuration

The plugin is activated via its skill definition; no additional configuration is strictly required.

Example `.claude/settings.json`:

```json
{
  "enabledPlugins": [
    "maui-blazor-development@<MARKETPLACE-NAME>"
  ]
}
```

Claude automatically considers this skill when:
- Project files reference `.NET MAUI`, `BlazorWebView`, or MAUI targets.
- You explicitly mention MAUI Blazor Hybrid concepts in your prompts.

---

## Directory & Project Structure

```text
plugins/maui-blazor-development/
├─ .claude-plugin/
│  └─ plugin.json           # Plugin metadata (name, description, keywords, license, skills)
├─ references/              # Deep‑dive guides for MAUI Blazor
│  ├─ blazor-components.md  # Components, lifecycle, data binding, event patterns
│  ├─ navigation-routing.md # Routing, Shell, deep linking, navigation patterns
│  ├─ platform-integration.md # Platform APIs, permissions, device info
│  ├─ project-structure.md  # Recommended project layouts and RCL usage
│  └─ state-management.md   # MVVM, DI, component state, hybrid models
└─ skills/
   └─ maui-blazor-development/
      └─ SKILL.md           # Main MAUI Blazor development skill instructions
```

These files provide the detailed patterns and examples Claude follows when acting as a MAUI Blazor Hybrid expert.

---

## Best Practices & Tips

- Be explicit about target platforms (Android, iOS, Windows, macOS) and constraints (offline support, performance, etc.).
- Ask for alternative architectures (e.g. “pure Blazor navigation vs Shell + Blazor”) and let Claude compare trade‑offs.
- Keep native platform code behind interfaces and use DI so that your Blazor components stay testable.
- Use this plugin together with your usual tooling (e.g. Serena MCP) to navigate and modify code safely.

Good prompts:
- “Given this MAUI Blazor project, propose a state management approach and show sample code.”
- “Refactor navigation to use Shell while keeping Blazor components reusable.”

---

## Troubleshooting

- **Problem:** Claude treats the app like a regular web‑only Blazor app.  
  **Fix:** Clarify that it’s a `.NET MAUI Blazor Hybrid` project and ask to apply the `maui-blazor-development` skill.

- **Problem:** Native API calls are scattered across components and pages.  
  **Fix:** Ask for a refactor toward centralized platform services with DI, using the patterns in `platform-integration.md`.

- **Problem:** Navigation feels inconsistent between MAUI pages and Blazor components.  
  **Fix:** Ask Claude to design a unified navigation strategy using Shell + Blazor routing, with examples.

---

## Versioning, Maintenance & Compatibility

- **Current version:** `1.0.0`
- **Tested with:** .NET MAUI and Blazor Hybrid projects targeting modern platforms (Android, iOS, Windows, macOS).
- **Breaking changes:** Track changes via the main repository history or a dedicated changelog if added later.

---

## License & Contribution

- **License:** MIT (see `plugins/maui-blazor-development/.claude-plugin/plugin.json` and repository `LICENSE` where applicable).
- **Contributions:** Suggestions for new patterns, examples, or clarifications are welcome via pull requests or issues against the parent repo.
- **Contact/Support:** Use the issue tracker or discussions in the Claude Code marketplace repository that ships this plugin.

