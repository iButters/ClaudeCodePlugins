# <PLUGIN-NAME>

Short, clear description in 1–3 sentences:
- What does the plugin do?
- Who is it for (target users)?
- Which everyday problem does it solve?

> **TL;DR:** One plain-language sentence that explains what the plugin is and why it’s useful.

---

## Overview

- **Category:** e.g. “Backend development”, “Architecture”, “Project planning”, “Review”, …
- **Primary goal:** One sentence that captures the core benefit.
- **Typical use cases:** 3–5 bullets with realistic situations from a developer’s day-to-day work.
- **Requirements:** e.g. Claude Desktop / Claude Code, required tools (Node, .NET, Docker, …), access rights.

---

## Installation

### Via Claude Code Marketplace

Describe the recommended installation path:

```bash
# Add marketplace (adjust example)
/plugin marketplace add <MARKETPLACE-NAME>

# Install plugin
/plugin install <PLUGIN-NAME>@<MARKETPLACE-NAME>
```

Explain in 2–3 sentences:
- Where this marketplace comes from (e.g. this repository).
- What becomes available after installation (e.g. new slash commands, skills, agents).

### Manual installation (optional)

Only if relevant:
1. Clone/download this repository or the plugin folder.
2. Copy the plugin into your personal `.claude` directory (show path and example).
3. Briefly explain how to verify that Claude has picked up the plugin.

---

## Quick Start

Walk a new user through the first meaningful end-to-end run:

1. **Check prerequisites** – Which files/project structure/tools should exist?
2. **Activate the plugin** – What is the first useful command (e.g. `/spec-start`, `/dotnet-new`, …)?
3. **First complete flow** – In 5–10 steps, show how to achieve a small but realistic goal with the plugin.

Use concrete examples:

```bash
# Example: start a first project/session
/<PLUGIN-COMMAND> <EXAMPLE-PROJECT-NAME>
```

Add a short explanation below the code block describing what happens and how to recognize that everything works.

---

## Feature Overview

Describe at a higher level what this plugin can do:

- **Core capabilities:** 4–8 bullets with the most important abilities.
- **Strengths:** What makes this plugin better/different than a normal “chat with the model”?
- **Limitations:** What can or should the plugin explicitly NOT do? (e.g. no deployments, no handling of external API keys, …)

If helpful, include a diagram or ASCII sketch to illustrate the typical flow.

---

## Commands (Slash Commands)

List all relevant commands in a table. If there are many, start with the most important (“Top 5”) and add detailed tables below.

| Command | Short description | When to use | Example |
|---------|-------------------|-------------|---------|
| `/…`    | One sentence      | Typical context | `/<COMMAND> <PARAMS>` |

Below the table, add sub-sections for key commands:

### `/important-command`

- **Purpose:** What does it achieve?
- **Parameters:** Which parameters exist, what do they mean, what are reasonable values?
- **Examples:**

```bash
/important-command --option example
```

Add a short explanation of the expected output/results.

---

## Typical Workflows

Describe 2–4 common scenarios as step-by-step guides:

### Workflow 1: <Example scenario, e.g. “New project from idea to task plan”>

1. Step 1: …
2. Step 2: …
3. Step 3: …

Mention which files/artifacts are created (e.g. `idea.md`, `tasks/`, `reports/` etc.) and how to use them further.

### Workflow 2: <Example scenario, e.g. “Refactoring an existing codebase”>

1. …
2. …

---

## Configuration

Explain all settings that users can adjust:

- **.claude/settings.json:** Example snippet showing how to enable this plugin.
- **Environment variables / secrets:** Only if relevant; describe how to set them safely.
- **Plugin-specific options:** e.g. verbosity, language, project paths, feature flags, etc.

```json
{
  "enabledPlugins": [
    "<PLUGIN-NAME>@<MARKETPLACE-NAME>"
  ],
  "pluginSettings": {
    "<PLUGIN-NAME>": {
      "exampleOption": true
    }
  }
}
```

Briefly explain each relevant field.

---

## Directory & Project Structure

Show the most important folders and files that the plugin uses or generates:

```text
plugins/<plugin-name>/
├─ .claude-plugin/
│  └─ plugin.json           # Plugin metadata
├─ commands/                # Slash commands (if any)
├─ agents/                  # Subagents / roles (if any)
├─ skills/                  # Skills (if any)
└─ assets/                  # Additional resources (optional)
```

If the plugin generates project files (e.g. `.specs/`, `reports/`, `tasks/`…), list them as well and briefly explain each folder/file.

---

## Best Practices & Tips

Provide concrete, experience-based advice:

- How to get the most value out of the plugin.
- Which prompts/phrasings tend to work particularly well.
- Common pitfalls (e.g. very large files, missing context, wrong working directory).
- How to combine this plugin effectively with other plugins.

You can include small “Do/Don’t” examples:

- ✅ “Works well when you: …”
- ❌ “Avoid doing: …”

---

## Troubleshooting

List typical problems with clear solutions:

- **Problem:** Command is not recognized  
  **Cause:** Plugin not installed or marketplace not added  
  **Fix:** Steps to verify + example commands

- **Problem:** Files are not created/updated  
  **Cause:** Wrong working directory, missing permissions, unexpected project structure  
  **Fix:** Concrete checks, e.g. `ls` commands and expected paths.

Optional additional subsections:
- Logging / debugging hints
- Where to look if in doubt (e.g. generated files, logs)

---

## Versioning, Maintenance & Compatibility

- **Current version:** `x.y.z`
- **Tested with:** e.g. “Claude Code version …”, specific IDE versions, important dependencies.
- **Breaking changes:** If relevant, briefly highlight important changes compared to earlier versions.

Optionally, link to a more detailed `CHANGELOG.md` if available.

---

## License & Contribution

- **License:** e.g. MIT – link to `LICENSE` in the repository root or a plugin-specific license file.
- **Contributing:** Short note on how to propose changes, open issues, or contribute code.
- **Contact/Support:** Link to issues, discussions, or another support channel.

> **Note:** When filling out this template, you can drop sections that don’t make sense for a specific plugin (e.g. if it has no own agents/skills). The important part is that readers clearly understand:
> - what the plugin does,
> - how to install it,
> - how to use it in day-to-day work,
> - and how to troubleshoot typical problems.
