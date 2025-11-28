# Serena MCP Plugin

Semantic code understanding and intelligent editing via Language Server Protocol integration.

## What is Serena?

[Serena](https://github.com/oraios/serena) is a powerful coding agent toolkit that provides IDE-like features through the Model Context Protocol (MCP). It uses Language Server Protocol (LSP) to offer:

- **Semantic Code Navigation**: Find symbols, references, and definitions
- **Symbol-Level Editing**: Insert, replace, and rename at the symbol level
- **Multi-Language Support**: 30+ programming languages
- **Token Efficiency**: Reduces context usage by avoiding full file reads

## Prerequisites

[uv](https://docs.astral.sh/uv/) must be installed:

```bash
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Installation

### Option A: Install Plugin (Recommended)

```bash
/plugin install serena-mcp@claude-code-plugins
```

The Serena MCP server starts automatically when the plugin is enabled - no manual configuration needed!

### Option B: Global Installation (All Projects)

```bash
claude mcp add --scope user serena -- uvx --from git+https://github.com/oraios/serena serena start-mcp-server --context ide-assistant --project .
```

### Option C: Project-Only Installation

```bash
claude mcp add serena -- uvx --from git+https://github.com/oraios/serena serena start-mcp-server --context ide-assistant --project .
```

## Features

### Always-Active Skill

The included skill automatically activates for all coding tasks, guiding Claude to:

- Prefer semantic operations over text-based searches
- Use symbol-level editing instead of line replacements
- Navigate codebases efficiently with minimal token usage

### Key Tools

| Category | Tools |
|----------|-------|
| Navigation | `find_symbol`, `find_referencing_symbols`, `get_symbols_overview` |
| Editing | `insert_after_symbol`, `replace_symbol_body`, `rename_symbol` |
| Project | `activate_project`, `onboarding`, `get_current_config` |
| Memory | `write_memory`, `read_memory`, `list_memories` |

## Usage

Once installed, Claude will automatically use Serena tools when available:

```
User: "Find all usages of the UserService class"

Claude: [Uses find_symbol to locate UserService]
        [Uses find_referencing_symbols to find all usages]
        "Found UserService in src/services/UserService.ts with 15 references..."
```

## Supported Languages

C#, C/C++, Java, Kotlin, Go, Rust, JavaScript, TypeScript, Python, Ruby, PHP, Elixir, Erlang, Haskell, Scala, Clojure, and many more.

## Resources

- [Serena GitHub](https://github.com/oraios/serena)
- [Serena Documentation](https://oraios.github.io/serena/)
- [MCP Protocol](https://modelcontextprotocol.io/)

## License

MIT
