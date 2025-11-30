# Copilot Instructions for Claude Code Plugins

This is a Claude Code plugin marketplace containing curated plugins for structured AI-assisted development workflows.

## Architecture Overview

```
plugins/
├── spec-driven-workflow/    # IDEA → REQUIREMENTS → DESIGN → TASKS → EXECUTE workflow
├── dotnet-development/      # .NET/DDD guidance (skill + references)
├── maui-blazor-development/ # MAUI Blazor Hybrid patterns
├── serena-mcp/              # Semantic code operations via LSP
├── skill-creator/           # Guide for authoring new skills
└── plugin-reviewer/         # Multi-agent quality review system
```

**Plugin Components:**
- `skills/[name]/SKILL.md` — Auto-activating skill with YAML frontmatter (`name`, `description` required)
- `commands/*.md` — Slash command definitions (e.g., `/spec-start`)
- `agents/*.md` — Subagent behavior definitions with model assignments
- `references/*.md` — Detailed documentation loaded on-demand

## Key Conventions

### SKILL.md Frontmatter Pattern
```yaml
---
name: skill-name
description: |
  What the skill does AND when to use it. This is the trigger mechanism.
  Include file types, phrases, and contexts that should activate the skill.
---
```

### Model Assignments (spec-driven-workflow)
| Role | Model | Rationale |
|------|-------|-----------|
| Planning & Review | Opus 4.5 | Deep analysis |
| Documentation | Haiku 4.5 | Efficient |
| Implementation | Sonnet 4.5 | Balanced |

### EARS Requirements Notation
Used throughout spec-driven-workflow for requirements, bugs, and features:
```
WHEN [trigger] THE SYSTEM SHALL [behavior]        # Event-driven
IF [condition] THEN THE SYSTEM SHALL [behavior]   # Unwanted/error
WHILE [state] THE SYSTEM SHALL [behavior]         # State-driven
```

## Plugin Development

### Creating a New Plugin
1. Create `plugins/[name]/.claude-plugin/plugin.json`:
   ```json
   {
     "name": "plugin-name",
     "version": "1.0.0",
     "description": "What the plugin does",
     "author": { "name": "Author Name" }
   }
   ```
2. Add `skills/[name]/SKILL.md` with proper frontmatter
3. Add commands in `commands/` (optional)
4. Add agents in `agents/` (optional)
5. Register in root `.claude-plugin/marketplace.json`

### Skill Design Principles
- **Concise is key**: Context window is shared; only include non-obvious knowledge
- **Progressive disclosure**: Metadata (~100 words) → SKILL.md body (<5k words) → references (unlimited)
- **Avoid duplication**: Information lives in SKILL.md OR references, not both
- **Use scripts for deterministic tasks**: Place in `scripts/` for repeated operations

### Reference File Organization
Keep references one level deep from SKILL.md:
```
skill-name/
├── SKILL.md          # Core workflow, links to references
└── references/
    ├── domain-a.md   # Loaded when user needs domain A
    └── domain-b.md   # Loaded when user needs domain B
```

## Working with spec-driven-workflow

### Project Structure
All specifications in `.specs/[project]/`:
- `idea.md`, `requirements.md`, `design.md` — Planning artifacts
- `tasks/wave-N.md` — Implementation tasks split into waves
- `bugs/BUG-NNN.md` — Bug reports using EARS notation
- `features/FEAT-NNN.md` — Feature requests

### Subagent Roster
- **Executors**: backend, frontend, database, test, docs
- **Reviewers**: requirements, architecture, code-quality
- **Orchestrator**: task-orchestrator (coordinates parallel execution)

## Important Patterns

### Version Bumping
Always update `version` in `.claude-plugin/plugin.json` when modifying a plugin.

### Language Requirement
Always use English when editing or creating files.

### Command File Format
Commands are markdown files that expand into prompts. They specify model recommendations and define the interaction flow.

### Agent File Format
Pure markdown defining agent behavior, available tools, and model assignment. See `plugins/spec-driven-workflow/agents/` for examples.

## Testing & Validation

For skill-creator plugin, use provided scripts:
```bash
python scripts/init_skill.py <name> --path <dir>   # Scaffold new skill
python scripts/quick_validate.py <skill-path>       # Validate structure
python scripts/package_skill.py <skill-path>        # Package to .skill file
```

## External Integration

- **Serena MCP**: Semantic code operations via LSP (requires separate installation)
- **Git integration**: `/spec-execute --git` commits after successful waves
