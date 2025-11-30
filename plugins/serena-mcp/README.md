# serena-mcp

Serena MCP integrates a semantic code understanding server (via Language Server Protocol) into Claude Code, enabling IDE‑like navigation and refactoring directly from the assistant.

> **TL;DR:** Use this plugin to give Claude semantic awareness of your codebase (symbols, references, refactorings) instead of relying on plain text search and manual edits.

---

## Overview

- **Category:** Code intelligence, navigation, refactoring
- **Primary goal:** Let Claude interact with your codebase at the symbol level (classes, functions, references) using Serena, rather than line‑based text operations.
- **Typical use cases:**
  - Navigating large codebases by symbol name instead of grep
  - Locating all references to a function, class, or variable before making changes
  - Performing safe, symbol‑aware refactors (rename, replace body, insert near symbols)
  - Understanding project structure, entry points, and module relationships
  - Reducing token usage by avoiding full‑file reads
- **Requirements:** Ability to run the Serena MCP server (`uvx --from git+https://github.com/oraios/serena serena start-mcp-server …`) from your environment.

---

## Installation

### Via Claude Code Marketplace

```bash
/plugin marketplace add <MARKETPLACE-NAME>
/plugin install serena-mcp@<MARKETPLACE-NAME>
```

After installation, the plugin configures an MCP server named `serena` (see `.claude-plugin/plugin.json`) that Claude can use for semantic operations.

### Prerequisites

The Serena MCP server requires `uv` to be installed:

```bash
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

The plugin’s `mcpServers.serena` configuration shows the exact `uvx` command used to start the server.

---

## Quick Start

1. Open a project in your IDE and start a Claude Code session in the project root.
2. Ensure the Serena plugin is enabled and the MCP server can be started (Python/uvx installed).
3. Ask Claude to use Serena tools, for example:

```text
Use the serena-mcp integration.
First onboard this project, then find the symbol `UserService` and show where it is referenced.
```

Claude will:
- Run onboarding (if needed) to analyze the project structure.
- Activate the project context.
- Use semantic tools (e.g. `find_symbol`, `find_referencing_symbols`) instead of plain text search.

---

## Core Principle

**Prefer semantic operations over text‑based operations.**

| Instead of…                  | Use Serena…                              |
|------------------------------|------------------------------------------|
| Grep for function/class name | `find_symbol`                            |
| Read entire file             | `get_symbols_overview` + targeted reads  |
| String replace across files  | `rename_symbol`                          |
| Manual line counting         | `insert_after_symbol` / `replace_symbol_body` |

This keeps edits safer, more precise, and far more token‑efficient.

---

## Setup & Activation

Before using Serena tools in a project:

1. **Check onboarding status:**  
   Use `check_onboarding_performed` to see if Serena already analyzed the project.
2. **Onboard if needed:**  
   Run `onboarding` to detect project structure, languages, build/test commands.
3. **Activate the project:**  
   Use `activate_project` with the project path so Serena knows which workspace to operate on.

Once active, all Serena tools operate relative to the chosen project.

---

## Tool Categories

### Symbol Navigation (primary)

Use these to understand and explore the codebase:

| Tool                     | Purpose                              | When to use                                |
|--------------------------|--------------------------------------|--------------------------------------------|
| `find_symbol`            | Locate symbols by name/substring     | Finding classes, functions, variables      |
| `find_referencing_symbols` | List all usages of a symbol       | Impact analysis before changes             |
| `get_symbols_overview`   | List top‑level symbols in a file     | Quick structural overview of a file        |

### Symbol‑level editing (preferred)

Use these instead of raw line‑based edits:

| Tool                 | Purpose                         | When to use                                  |
|----------------------|---------------------------------|----------------------------------------------|
| `insert_before_symbol` | Insert code before a symbol  | Adding imports, decorators, annotations      |
| `insert_after_symbol`  | Insert code after a symbol   | Adding related methods or helper functions   |
| `replace_symbol_body`  | Replace an entire symbol body | Refactoring function/class implementation    |
| `rename_symbol`        | Rename a symbol project‑wide | Safe, reference‑aware renames                |

### File operations (fallback)

Use these only when symbol‑level operations are not applicable:

| Tool                     | Purpose                         |
|--------------------------|---------------------------------|
| `read_file`              | Read file contents              |
| `create_text_file`       | Create or overwrite files       |
| `list_dir`               | List directory contents         |
| `find_file`              | Locate files by path/pattern    |
| `delete_lines` / `insert_at_line` / `replace_lines` | Line‑based edits |

### Project management

| Tool                    | Purpose                                  |
|-------------------------|------------------------------------------|
| `activate_project`      | Select active project/workspace          |
| `onboarding`            | Analyze project structure & commands     |
| `get_current_config`    | Show active configuration                |
| `restart_language_server` | Restart LSP server after external changes |

### Memory system

Persist information across sessions:

| Tool           | Purpose                         |
|----------------|---------------------------------|
| `write_memory` | Store project‑specific notes    |
| `read_memory`  | Retrieve stored information     |
| `list_memories`| List stored memories            |

---

## Typical Workflows

### Understanding a codebase

```text
1. activate_project     → Ensure project is active
2. onboarding           → Get project overview, build/test commands
3. get_symbols_overview → Understand key files and symbols
4. find_symbol          → Locate specific entities
5. find_referencing_symbols → Trace dependencies and call chains
```

### Implementing a feature

```text
1. find_symbol          → Locate where to extend functionality
2. get_symbols_overview → Understand surrounding context
3. insert_after_symbol  → Add new code in the right place
4. find_referencing_symbols → Verify no breaking changes or missed references
```

### Refactoring

```text
1. find_symbol          → Locate the target symbol
2. find_referencing_symbols → Understand all usages
3. rename_symbol        → Perform safe project‑wide rename
   OR
3. replace_symbol_body  → Rewrite the implementation
```

### Debugging

```text
1. find_symbol          → Jump to the suspected function/class
2. find_referencing_symbols → Follow the call chain
3. read_file            → Read only the relevant sections for context
4. replace_symbol_body  → Apply a focused fix
```

---

## Best Practices & Tips

### DO
- Run `onboarding` when opening a new project so Serena understands its layout and commands.
- Prefer `find_symbol` over raw text search for navigation.
- Use `replace_symbol_body` instead of manual line edits where possible.
- Use `rename_symbol` for refactoring to avoid missed references.
- Store key decisions and findings with `write_memory` for future sessions.

### DON’T
- Read entire large files if you only need specific symbols.
- Use grep‑style searches when semantic `find_symbol` is available.
- Do line‑based edits where symbol‑based tools are applicable.
- Forget to `restart_language_server` after heavy external changes (mass renames, re‑generation, etc.).

---

## Language Support

Serena provides LSP‑based semantic support for 30+ languages, including (non‑exhaustive):

- C#, C/C++, Java, Kotlin, Go, Rust
- JavaScript, TypeScript, Python, Ruby, PHP
- Elixir, Erlang, Haskell, Scala, Clojure
- And many more, depending on installed language servers

---

## Token Efficiency

Serena significantly reduces token usage and noise by:

- Navigating via symbols instead of reading whole files
- Performing targeted, semantic edits rather than line‑based patches
- Providing structured overviews (symbols, references, project layout)

For large codebases, always prefer Serena’s semantic tools over text‑based alternatives when available.

---

## Versioning, Maintenance & Compatibility

- **Current version:** `1.1.0`
- **Integration:** Configured as an MCP server named `serena` in `.claude-plugin/plugin.json`.
- **Compatibility:** Designed to work with the Serena project at `github.com/oraios/serena`, including the `ide-assistant` context and current LSP integrations.

---

## License & Contribution

- **License:** MIT (see `plugins/serena-mcp/.claude-plugin/plugin.json` and the main repository `LICENSE`).
- **Contributions:** Improvements typically happen in the Serena project itself; you can also adjust how this plugin describes and uses tools via its SKILL and command definitions.
- **Support:** For server‑side issues, consult the Serena repository; for plugin wiring, use the issue tracker of this Claude Code marketplace repo.
