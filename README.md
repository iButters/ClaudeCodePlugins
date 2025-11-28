# Claude Code Marketplace

A curated collection of Claude Code plugins for structured development workflows, automation, and productivity.

## 🚀 Quick Start

```bash
# Add this marketplace
/plugin marketplace add YOUR_USERNAME/claude-code-marketplace

# Browse available plugins
/plugin

# Install a plugin
/plugin install spec-driven-workflow@claude-code-marketplace
```

## 📦 Available Plugins

| Plugin | Description | Version |
|--------|-------------|---------|
| [spec-driven-workflow](./plugins/spec-driven-workflow/) | Specification-Driven Development with multi-agent orchestration | 2.2.0 |

---

## 🛠️ spec-driven-workflow

A comprehensive system for specification-driven software development.

### Features

- **8 Slash Commands:** `/spec-start`, `/spec-idea`, `/spec-requirements`, `/spec-design`, `/spec-tasks`, `/spec-execute`, `/spec-status`, `/spec-review`
- **9 Subagents:** 5 Executors (backend, frontend, database, test, docs) + 3 Reviewers + 1 Orchestrator
- **Wave-based Task Management:** Tasks split into wave files for better scalability
- **EARS Requirements:** Easy Approach to Requirements Syntax
- **Parallel Execution:** Up to 4 subagents running simultaneously

### Workflow

```
IDEA → REQUIREMENTS → DESIGN → TASKS → EXECUTE → REVIEW
```

### Model Configuration

| Role | Model | Reason |
|------|-------|--------|
| Planning & Review | Opus 4.5 | Deep analysis |
| Documentation | Haiku 4.5 | Efficient for text |
| Implementation | Sonnet 4.5 | Balanced performance |

### Installation

```bash
/plugin install spec-driven-workflow@claude-code-marketplace
```

### Usage

```bash
# Start a new project
/spec-start my-app

# Refine the idea
/spec-idea

# Generate requirements
/spec-requirements

# Create architecture
/spec-design

# Plan tasks (creates wave files)
/spec-tasks

# Execute tasks
/spec-execute          # Next pending wave
/spec-execute wave 2   # Specific wave
/spec-execute T5       # Specific task

# Check status
/spec-status

# Review a task
/spec-review T5
```

[📖 Full Documentation](./plugins/spec-driven-workflow/README.md)

---

## 📁 Repository Structure

```
claude-code-marketplace/
├── .claude-plugin/
│   └── marketplace.json      # Marketplace manifest
├── .github/
│   └── workflows/
│       └── validate.yml      # Plugin validation
├── plugins/
│   └── spec-driven-workflow/ # Plugins go here
│       ├── .claude-plugin/
│       │   └── plugin.json
│       ├── commands/
│       ├── agents/
│       ├── skills/
│       └── assets/
├── README.md
└── LICENSE
```

## ➕ Adding More Plugins

1. Create a new directory under `plugins/`:
   ```bash
   mkdir -p plugins/my-plugin/.claude-plugin
   mkdir -p plugins/my-plugin/commands
   mkdir -p plugins/my-plugin/agents
   ```

2. Add `plugin.json`:
   ```json
   {
     "name": "my-plugin",
     "version": "1.0.0",
     "description": "What your plugin does",
     "author": {
       "name": "Your Name"
     }
   }
   ```

3. Add commands, agents, skills as needed

4. Register in `.claude-plugin/marketplace.json`:
   ```json
   {
     "name": "my-plugin",
     "description": "What your plugin does",
     "version": "1.0.0",
     "source": "./plugins/my-plugin",
     "category": "utilities"
   }
   ```

## 🔧 For Teams

Add to your project's `.claude/settings.json` for automatic installation:

```json
{
  "extraKnownMarketplaces": {
    "team-marketplace": {
      "source": {
        "source": "github",
        "repo": "YOUR_USERNAME/claude-code-marketplace"
      }
    }
  },
  "enabledPlugins": [
    "spec-driven-workflow@team-marketplace"
  ]
}
```

## 📄 License

MIT License - See [LICENSE](./LICENSE) for details.

---

## 🤝 Contributing

1. Fork this repository
2. Add your plugin to `plugins/`
3. Update `marketplace.json`
4. Submit a pull request

## 📞 Support

- [Open an Issue](https://github.com/YOUR_USERNAME/claude-code-marketplace/issues)
- [Discussions](https://github.com/YOUR_USERNAME/claude-code-marketplace/discussions)
