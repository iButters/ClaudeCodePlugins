# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Claude Code plugin marketplace containing curated plugins for structured development workflows. The repository provides three plugins that can be installed into Claude Code projects.

## Repository Structure

```
ClaudeCodePlugins/
├── plugins/
│   ├── spec-driven-workflow/     # Specification-driven development plugin
│   │   ├── .claude-plugin/       # Plugin manifest
│   │   ├── commands/             # Slash commands (/spec-*)
│   │   ├── agents/               # Subagent definitions (9 agents)
│   │   ├── skills/               # Auto-activating skill
│   │   └── assets/templates/     # Spec templates
│   ├── dotnet-development/       # .NET development guidance plugin
│   │   ├── skills/               # Auto-activating skill
│   │   └── references/           # DDD, API, and testing patterns
│   └── serena-mcp/               # Serena MCP integration plugin
│       ├── .claude-plugin/       # Plugin manifest
│       └── skills/               # Always-active skill for semantic code ops
├── README.md
└── LICENSE
```

## Plugin Architecture

### Spec-Driven Workflow Plugin

Implements a multi-phase development workflow: `IDEA → REQUIREMENTS → DESIGN → TASKS → EXECUTE → REVIEW`

**Slash Commands** (in `commands/`):
- Commands are markdown files that expand into prompts when users type `/spec-*`
- Each command has specific model recommendations (Opus for planning, Sonnet for implementation)

**Subagents** (in `agents/`):
- 5 Executors: backend, frontend, database, test, docs
- 3 Reviewers: requirements, architecture, code-quality
- 1 Orchestrator: task-orchestrator for parallel coordination
- Agent files define specialized behaviors and tool access

**Wave-Based Tasks**:
- Task plans split into separate wave files (`tasks/wave-N.md`) for scalability
- `tasks/index.md` provides overview and progress tracking
- Enables parallel execution of tasks within waves

### .NET Development Plugin

Provides auto-activating guidance for .NET/C# development through:
- `skills/dotnet-development/SKILL.md` - Core workflow and conventions
- `references/ddd-patterns.md` - Aggregate, Value Object, Domain Event patterns
- `references/api-patterns.md` - REST API, validation, error handling
- `references/testing-patterns.md` - Test naming, categories, coverage targets

### Serena MCP Plugin

Provides always-active guidance for using Serena MCP tools for semantic code operations:
- `skills/serena-mcp/SKILL.md` - Tool usage patterns and best practices

**Key Principle**: Prefer semantic operations over text-based operations:
- Use `find_symbol` instead of grep for locating code
- Use `replace_symbol_body` instead of line-based edits
- Use `rename_symbol` for refactoring (handles all references via LSP)
- Use `get_symbols_overview` instead of reading entire files

**Always-Active**: This skill activates for all coding tasks to ensure Serena tools are used when available, improving token efficiency and code quality.

**Requires**: Serena MCP server must be installed separately via:
```bash
claude mcp add serena -- uvx --from git+https://github.com/oraios/serena serena start-mcp-server --context ide-assistant --project $(pwd)
```

## Key Conventions

### Plugin File Format

- **Skill files**: Use YAML frontmatter with `name` and `description` fields, followed by markdown content
- **Agent files**: Pure markdown defining agent behavior, tools, and model assignment
- **Command files**: Markdown that expands as prompts when invoked via slash command

### Model Assignments

| Task Type | Model | Rationale |
|-----------|-------|-----------|
| Planning & Review | Opus 4.5 | Deep analysis |
| Documentation | Haiku 4.5 | Efficient for text |
| Implementation | Sonnet 4.5 | Balanced performance |

### EARS Requirements Notation

Requirements follow Easy Approach to Requirements Syntax:
```
WHEN [trigger] THE SYSTEM SHALL [behavior]
IF [condition] THEN THE SYSTEM SHALL [behavior]
WHILE [state] THE SYSTEM SHALL [behavior]
```

## Development Tasks

This is a documentation/configuration repository. No build or test commands apply.

### Adding a New Plugin

1. Create directory under `plugins/[plugin-name]/`
2. Add `.claude-plugin/plugin.json` with name, version, description, author
3. Add commands, agents, and/or skills as needed
4. Register in root `.claude-plugin/marketplace.json`

### Plugin Directory Requirements

- `commands/` - Slash command markdown files
- `agents/` - Subagent definition markdown files
- `skills/[skill-name]/SKILL.md` - Auto-activating skill with YAML frontmatter
- `.claude-plugin/plugin.json` - Plugin manifest

### Requirements
- Always use the english language when editing or creating files
- Always update the version of a plugin you worked on