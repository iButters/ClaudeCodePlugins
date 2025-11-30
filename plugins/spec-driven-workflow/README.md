# spec-driven-workflow

Specification‑driven development workflow for transforming ideas into production‑ready software using a structured, multi‑agent process.

> **TL;DR:** Use this plugin to run projects through a repeatable IDEA → REQUIREMENTS → DESIGN → TASKS → EXECUTE → REVIEW workflow, with automated planning, execution, and quality checks.

---

## Overview

- **Category:** Project workflow, planning, and execution  
- **Primary goal:** Turn informal ideas into structured specifications, architecture, tasks, and implementation steps, managed by multiple specialized agents.  
- **Typical use cases:**
  - Starting a new software project from scratch in a structured way
  - Generating requirements, architecture, and task plans for existing projects
  - Executing development tasks in waves with automatic reviews
  - Tracking bugs and features using EARS‑based specs and wave files
- **Requirements:** A project repository (any tech stack), Claude Code with this plugin enabled; optional Serena MCP integration for semantic code operations.

---

## Workflow Overview

The core workflow is:

```text
IDEA → REQUIREMENTS → DESIGN → TASKS → EXECUTE → REVIEW
```

At each stage, this plugin writes structured artifacts into a `.specs/` directory (idea, requirements, design, tasks, reports, bugs, features) and orchestrates specialized agents for implementation and review.

---

## Commands

### Core workflow

| Command                   | Purpose                                  |
|---------------------------|------------------------------------------|
| `/spec-start [name]`      | Initialize a new project under `.specs/` |
| `/spec-idea`              | Refine and document the project concept  |
| `/spec-requirements`      | Generate EARS‑style requirements         |
| `/spec-design`            | Create technical architecture (`design.md`) |
| `/spec-tasks`             | Plan implementation tasks as waves       |
| `/spec-execute [options]` | Execute tasks via multi‑agent orchestration |
| `/spec-status`            | Show project status and wave progress    |
| `/spec-review [task]`     | Manually review a specific task          |

Execution options include flags like `--git` and `--git-push` to automatically commit and optionally push changes after a successful wave.

### Bug tracking

| Command           | Purpose                                             |
|-------------------|-----------------------------------------------------|
| `/spec-bug`       | Report a bug using EARS notation                    |
| `/spec-bugs`      | List all bugs for the current project               |
| `/spec-bug-wave`  | Create a dedicated bug‑fix wave from open bugs      |

Bug reports are stored under `.specs/<project>/bugs/` with structured EARS descriptions.

### Feature management

| Command                  | Purpose                                      |
|--------------------------|----------------------------------------------|
| `/spec-feature`          | Create an EARS‑based feature request         |
| `/spec-features`         | List all feature requests                    |
| `/spec-feature-to-tasks` | Convert a feature into implementation tasks and waves |

Feature specs are stored under `.specs/<project>/features/` and can be turned into tasks and waves for execution.

---

## Typical Workflows

### Workflow 1: New project from idea to execution

1. **Initialize:**  
   ```bash
   /spec-start my-app
   ```
   Creates `.specs/my-app/` with `idea.md`, `requirements.md`, `design.md`, and a `tasks/` directory.
2. **Refine idea:**  
   ```bash
   /spec-idea
   ```
3. **Generate requirements:**  
   ```bash
   /spec-requirements
   ```
4. **Create architecture:**  
   ```bash
   /spec-design
   ```
5. **Plan tasks:**  
   ```bash
   /spec-tasks
   ```
6. **Execute waves:**  
   ```bash
   /spec-execute        # next pending wave
   /spec-execute wave 2 # specific wave
   ```
7. **Review & iterate:**  
   Use `/spec-status` and `/spec-review` to track and refine work.

### Workflow 2: Bug‑driven improvement

1. Report bugs in EARS form via `/spec-bug` as they are discovered.  
2. Periodically run `/spec-bug-wave` to generate a bug‑fix wave document (`wave-bugfix-N.md`).  
3. Execute bug‑fix waves with `/spec-execute wave bugfix-N`.  
4. Track progress and verify fixes through auto‑generated reports.

### Workflow 3: Feature backlog to tasks

1. Capture new features with `/spec-feature` (each stored under `.specs/<project>/features/`).  
2. Use `/spec-features` to review the backlog and prioritize.  
3. Convert selected features into tasks and waves:
   ```bash
   /spec-feature-to-tasks FEAT-001
   ```
4. Execute the resulting waves and monitor with `/spec-status`.

---

## Agents & Orchestration

The plugin uses multiple specialized subagents:

- **Executors (implementation):**
  - `backend-executor` – APIs, server logic, business rules  
  - `frontend-executor` – UI components, styling, interactions  
  - `database-executor` – schema, migrations, queries  
  - `test-executor` – unit and integration tests  
  - `docs-executor` – README files, API docs, comments  

- **Reviewers (quality assurance):**
  - `requirements-reviewer` – checks EARS requirements quality  
  - `architecture-reviewer` – enforces `design.md` architecture  
  - `code-quality-reviewer` – focuses on security, performance, and code cleanliness  

- **Orchestrator:**
  - `task-orchestrator` – coordinates which executor handles which task and manages parallelization.  

Model configuration (Opus, Sonnet, Haiku) is tuned per role for deep planning, implementation, and documentation tasks.

---

## Project Structure

All specs live under `.specs/` in the project root:

```text
.specs/
└─ <project-name>/
   ├─ idea.md               # Project concept
   ├─ requirements.md       # EARS requirements
   ├─ design.md             # Technical architecture
   ├─ tasks/                # Implementation plan
   │  ├─ index.md           # Overview & progress
   │  ├─ wave-1.md          # Wave 1 tasks
   │  ├─ wave-2.md          # Wave 2 tasks
   │  ├─ wave-N.md          # Additional waves
   │  └─ wave-bugfix-N.md   # Bug‑fix waves
   ├─ reports/              # Wave completion reports
   │  ├─ wave-1-report.md
   │  └─ wave-N-report.md
   ├─ bugs/                 # Bug tracking
   │  ├─ index.md
   │  ├─ BUG-001.md
   │  └─ BUG-NNN.md
   └─ features/             # Feature backlog
      ├─ index.md
      ├─ FEAT-001.md
      └─ FEAT-NNN.md

steering/
└─ project-rules.md        # Cross‑project standards and constraints
```

This structure keeps the entire lifecycle—idea, requirements, architecture, tasks, execution reports, bugs, and features—in one place.

---

## EARS Notation

The plugin uses EARS (Easy Approach to Requirements Syntax) for requirements, bugs, and features:

| Pattern             | Syntax                                               | Use case             |
|---------------------|------------------------------------------------------|----------------------|
| **Event‑Driven**    | `WHEN [trigger] THE SYSTEM SHALL [behavior]`         | User actions, events |
| **Unwanted Behavior** | `IF [condition] THEN THE SYSTEM SHALL [behavior]` | Errors, bugs         |
| **State‑Driven**    | `WHILE [state] THE SYSTEM SHALL [behavior]`         | Long‑running states  |
| **Optional**        | `WHERE [feature] THE SYSTEM SHALL [behavior]`        | Feature flags        |

**Bug reports** typically use an “Expected vs Actual” pattern built on EARS:

```text
Expected: WHEN [action] THE SYSTEM SHALL [correct behavior]
Actual:   IF [condition] THEN THE SYSTEM [unwanted behavior]
```

This makes requirements and bugs precise, testable, and machine‑processable.

---

## Wave‑Based Execution

Tasks are organized into waves to keep context manageable and execution parallelizable:

- Each wave is stored in its own file (`wave-N.md`).  
- Later waves depend on earlier ones (Wave N+1 blocked until Wave N is complete).  
- Up to 4 executor agents can work in parallel within a wave.  
- `index.md` tracks overall progress (tasks, waves, completion status).  

Execution commands:

- `/spec-execute` – Run the next pending wave.  
- `/spec-execute wave 2` – Execute a specific wave.  
- `/spec-execute T5` – Execute a specific task ID.  
- `/spec-execute wave bugfix-1` – Run a bug‑fix wave.  
- `/spec-execute --git` – Execute and commit the changes.  
- `/spec-execute --git-push` – Execute, commit, and push.  

Each wave can generate a detailed report under `reports/`.

---

## Quick Start Example

```text
User: I want to build a task management app.

Claude: [uses /spec-start]
        "What would you like to call this project?"

User: task-manager

Claude: [creates .specs/task-manager/]
        "Project initialized! Use /spec-idea to refine your concept."
```

From there, you follow the workflow with `/spec-idea`, `/spec-requirements`, `/spec-design`, `/spec-tasks`, and `/spec-execute` until the project is implemented and reviewed.

---

## Versioning, Maintenance & Compatibility

- **Current version:** `2.2.2`  
- **Integration:** Can optionally use Serena MCP (see `.claude-plugin/plugin.json`) to operate on code semantically during execution.  
- **Compatibility:** Designed to work across languages and stacks as long as the repository contains a recognizable project structure.  

---

## License & Contribution

- **License:** MIT (see `plugins/spec-driven-workflow/.claude-plugin/plugin.json` and repository `LICENSE`).  
- **Contributions:** You can refine commands, agents, and templates to fit your own organization’s workflows, then extend or fork this plugin.  
- **Support:** Use the main Claude Code marketplace repository’s issue tracker or discussions to report problems or suggest enhancements.

