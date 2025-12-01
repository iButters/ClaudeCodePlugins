---
name: spec-driven-workflow
description: >
  Specification-Driven Development Workflow for transforming ideas into production-ready software.
  Use when users want to (1) Start a new software project with structured planning, (2) Create
  requirements, architecture, or task breakdowns, (3) Execute development tasks with multi-agent
  orchestration, (4) Follow a spec-driven approach with IDEA → REQUIREMENTS → DESIGN → TASKS →
  EXECUTE → REVIEW workflow, (5) Use /spec-* commands, (6) Report bugs or request features,
  (7) Track project progress, or (8) Request project initialization, ideation help, requirement
  generation, architecture design, task execution, bug tracking, or feature management in natural language.
  Ideal for structured development with automated quality checks and parallel task execution.
---

# Spec-Driven Workflow

A comprehensive system for specification-driven software development.

## Workflow Overview

```
IDEA → REQUIREMENTS → DESIGN → TASKS → EXECUTE → REVIEW
```

<project_completion_criteria>
## Project Completion Criteria

A project is considered **COMPLETE** when:

- [ ] All P1 (must-have) requirements implemented and verified
- [ ] All waves executed with ✅ status
- [ ] Zero open Critical or High severity bugs
- [ ] All P1 features implemented (if any)
- [ ] Test coverage meets project standards (≥80% recommended)
- [ ] Documentation complete (README, API docs if applicable)
- [ ] Security review passed (no 🔴 Critical issues)
- [ ] Final `/spec-status` shows no blockers

**Project Status Levels:**
| Status | Criteria |
|--------|----------|
| 🟡 Ideation | idea.md exists, requirements not complete |
| 🟠 Planning | requirements.md + design.md complete |
| 🔵 In Progress | Tasks created, execution started |
| 🟢 Complete | All completion criteria met |
| 🔴 Blocked | Critical issues preventing progress |
</project_completion_criteria>

## Available Commands

<commands>
### Core Workflow
| Command | Purpose |
|---------|---------|
| `/spec-start [name]` | Initialize new project |
| `/spec-idea` | Refine project concept |
| `/spec-requirements` | Generate EARS requirements |
| `/spec-design` | Create technical architecture |
| `/spec-tasks` | Plan implementation tasks |
| `/spec-execute [--git]` | Run orchestrated execution |
| `/spec-status` | Show project progress |
| `/spec-review [task]` | Manual task review |

### Bug Tracking
| Command | Purpose |
|---------|---------|
| `/spec-bug` | Report a bug with EARS notation |
| `/spec-bugs` | List all bugs for project |
| `/spec-bug-wave` | Create bug-fix wave from open bugs |

### Feature Management
| Command | Purpose |
|---------|---------|
| `/spec-feature` | Create feature request with EARS |
| `/spec-features` | List all feature requests |
| `/spec-feature-to-tasks` | Convert feature to tasks/waves |
</commands>

## Natural Language Triggers

<activation_triggers>
This skill activates when users say things like:

### Project Planning
- "Start a new project for..."
- "Help me plan a software project"
- "Initialize a project called..."
- "I want to build a..."
- "Create a new spec-driven project"

### Requirements & Design
- "Generate requirements for..."
- "Create the technical design"
- "Help me write requirements"
- "Design the architecture for..."
- "What requirements do I need?"

### Task Management
- "Break this down into tasks"
- "Create tasks from the design"
- "Plan the implementation"
- "What tasks are needed?"

### Execution
- "Execute the implementation"
- "Run the next wave"
- "Continue execution"
- "Execute wave 2"
- "Run task T5"

### Status & Progress
- "What's the project status?"
- "Show me the progress"
- "How far along are we?"
- "What's left to do?"

### Bug Tracking
- "Report a bug"
- "I found a bug in..."
- "There's an issue with..."
- "Show me all bugs"
- "List open bugs"
- "Create a bug fix wave"

### Feature Management
- "Add a feature request"
- "I want to add a new feature..."
- "Request a new feature"
- "Show feature requests"
- "Convert feature to tasks"

### Reviews
- "Review this task"
- "Check the quality"
- "Run the review pipeline"
</activation_triggers>

## Specialized Subagents

<subagents>
### Executors (Implementation)
| Agent | Role | Model |
|-------|------|-------|
| **backend-executor** | APIs, server logic, business rules | Sonnet |
| **frontend-executor** | UI components, styling, interactions | Sonnet |
| **database-executor** | Schema, migrations, queries | Sonnet |
| **test-executor** | Unit tests, integration tests | Sonnet |
| **docs-executor** | README, API docs, code comments | Haiku |

### Reviewers (Quality Assurance)
| Agent | Role | Model |
|-------|------|-------|
| **requirements-reviewer** | Validates against EARS criteria | Opus |
| **architecture-reviewer** | Validates against design.md | Opus |
| **code-quality-reviewer** | Security, performance, clean code | Opus |

### Orchestration
| Agent | Role | Model |
|-------|------|-------|
| **task-orchestrator** | Coordinates parallel execution | Opus |
</subagents>

## Model Configuration

| Role | Model | Reason |
|------|-------|--------|
| Planning & Review | Opus 4.5 | Deep analysis needed |
| Documentation | Haiku 4.5 | Efficient for text |
| Implementation | Sonnet 4.5 | Balanced performance |

All models use extended thinking for better results.

## Project Structure

<file_structure>
All specifications stored in `.specs/`:

```
.specs/
├── [project-name]/
│   ├── idea.md              # Project concept
│   ├── requirements.md      # EARS requirements
│   ├── design.md            # Technical architecture
│   ├── tasks/               # Implementation plan
│   │   ├── index.md         # Overview & progress
│   │   ├── wave-1.md        # Wave 1 tasks
│   │   ├── wave-2.md        # Wave 2 tasks
│   │   ├── wave-N.md        # Additional waves
│   │   ├── wave-bugfix-N.md # Bug-fix waves
│   │   └── .checkpoint      # Execution state (JSON)
│   ├── reports/             # Wave completion reports
│   │   ├── wave-1-report.md
│   │   └── wave-N-report.md
│   ├── bugs/                # Bug tracking
│   │   ├── index.md         # Bug overview
│   │   ├── BUG-001.md
│   │   └── BUG-NNN.md
│   └── features/            # Feature requests
│       ├── index.md         # Feature overview
│       ├── FEAT-001.md
│       └── FEAT-NNN.md
└── steering/
    └── project-rules.md     # Cross-project standards
```
</file_structure>

## EARS Notation

<ears_reference>
Requirements use EARS (Easy Approach to Requirements Syntax):

| Pattern | Syntax | Use Case |
|---------|--------|----------|
| **Event-Driven** | `WHEN [trigger] THE SYSTEM SHALL [behavior]` | User actions, events |
| **Unwanted Behavior** | `IF [condition] THEN THE SYSTEM SHALL [behavior]` | Errors, bugs |
| **State-Driven** | `WHILE [state] THE SYSTEM SHALL [behavior]` | Conditions |
| **Optional** | `WHERE [feature] THE SYSTEM SHALL [behavior]` | Feature flags |

**Bug Reports use the Unwanted Behavior pattern:**
```
Expected: WHEN [action] THE SYSTEM SHALL [correct behavior]
Actual:   IF [condition] THEN THE SYSTEM [unwanted behavior]
```
</ears_reference>

## Parallel Execution

<execution_options>
Tasks are split into wave files for efficient execution:
- Each wave in separate file (`wave-N.md`)
- Wave N+1 blocked until Wave N complete
- Maximum 4 parallel subagents per wave
- `index.md` tracks overall progress
- `.checkpoint` enables resume on interruption

Execute with:
| Command | Action |
|---------|--------|
| `/spec-execute` | Next pending wave |
| `/spec-execute wave 2` | Specific wave |
| `/spec-execute T5` | Single task |
| `/spec-execute wave bugfix-1` | Bug-fix wave |
| `/spec-execute --git` | Execute and commit |
| `/spec-execute --git-push` | Execute, commit, and push |
| `/spec-execute --resume` | Resume from checkpoint |
</execution_options>

## Review Pipeline

<review_pipeline>
After each task:
1. **Requirements Review** → Meets EARS criteria?
2. **Architecture Review** → Follows design.md?
3. **Code Quality Review** → Clean, secure, performant?

| Result | Action |
|--------|--------|
| All PASS | Mark complete, continue |
| Any FAIL | Feedback loop (max 2 retries) |
| 2 PASS + 1 WARN | Complete with notes |
| Repeated FAIL | Escalate to user |
</review_pipeline>

## Quick Start

<example>
```
User: "I want to build a task management app"

Claude: [Uses /spec-start]
        "What would you like to call this project?"

User: "task-manager"

Claude: [Creates .specs/task-manager/]
        "Project initialized! Use /spec-idea to refine your concept."

User: "Let's define the requirements"

Claude: [Uses /spec-requirements]
        "I'll help you create EARS requirements. Let's start with the core functionality..."
```
</example>

## Glossary

<glossary>
| Term | Definition |
|------|------------|
| **Wave** | A group of tasks that can be executed in parallel |
| **Subagent** | Specialized AI agent (executor or reviewer) |
| **Executor** | Subagent that implements code (backend, frontend, etc.) |
| **Reviewer** | Subagent that validates code quality |
| **Orchestrator** | Subagent that coordinates execution |
| **EARS** | Easy Approach to Requirements Syntax |
| **Checkpoint** | Saved execution state for resume capability |
| **Traceability** | Linking between requirements, tasks, and bugs |
</glossary>
