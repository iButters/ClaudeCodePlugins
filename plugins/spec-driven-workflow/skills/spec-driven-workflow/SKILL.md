---
name: spec-driven-workflow
description: >
  Specification-Driven Development Workflow for transforming ideas into production-ready software.
  Use when users want to (1) Start a new software project with structured planning, (2) Create
  requirements, architecture, or task breakdowns, (3) Execute development tasks with multi-agent
  orchestration, (4) Follow a spec-driven approach with IDEA → REQUIREMENTS → DESIGN → TASKS →
  EXECUTE → REVIEW workflow, (5) Use /spec-* commands, or (6) Request project initialization,
  ideation help, requirement generation, architecture design, or task execution in natural language.
  Ideal for structured development with automated quality checks and parallel task execution.
---

# Spec-Driven Workflow

A comprehensive system for specification-driven software development.

## Workflow Overview

```
IDEA → REQUIREMENTS → DESIGN → TASKS → EXECUTE → REVIEW
```

## Available Commands

| Command | Purpose |
|---------|---------|
| `/spec-start [name]` | Initialize new project |
| `/spec-idea` | Refine project concept |
| `/spec-requirements` | Generate EARS requirements |
| `/spec-design` | Create technical architecture |
| `/spec-tasks` | Plan implementation tasks |
| `/spec-execute` | Run orchestrated execution |
| `/spec-status` | Show project progress |
| `/spec-review [task]` | Manual task review |

## Natural Language Triggers

This skill activates when users say things like:
- "Start a new project for..."
- "Help me plan a software project"
- "Generate requirements for..."
- "Create the technical design"
- "Break this down into tasks"
- "Execute the implementation"
- "What's the project status?"

## Specialized Subagents

### Executors (Implementation)
- **backend-executor** - APIs, server logic, business rules
- **frontend-executor** - UI components, styling, interactions
- **database-executor** - Schema, migrations, queries
- **test-executor** - Unit tests, integration tests
- **docs-executor** - README, API docs, code comments

### Reviewers (Quality Assurance)
- **requirements-reviewer** - Validates against EARS criteria
- **architecture-reviewer** - Validates against design.md
- **code-quality-reviewer** - Security, performance, clean code

### Orchestration
- **task-orchestrator** - Coordinates parallel execution

## Model Configuration

| Role | Model | Reason |
|------|-------|--------|
| Planning & Review | Opus 4.5 | Deep analysis needed |
| Documentation | Haiku 4.5 | Efficient for text |
| Implementation | Sonnet 4.5 | Balanced performance |

All models use extended thinking for better results.

## Project Structure

All specifications stored in `.specs/`:

```
.specs/
├── [project-name]/
│   ├── idea.md              # Project concept
│   ├── requirements.md      # EARS requirements
│   ├── design.md            # Technical architecture
│   └── tasks/               # Implementation plan
│       ├── index.md         # Overview & progress
│       ├── wave-1.md        # Wave 1 tasks
│       ├── wave-2.md        # Wave 2 tasks
│       └── wave-N.md        # Additional waves
└── steering/
    └── project-rules.md     # Cross-project standards
```

## EARS Notation

Requirements use EARS (Easy Approach to Requirements Syntax):

```
WHEN [trigger] THE SYSTEM SHALL [behavior]
IF [condition] THEN THE SYSTEM SHALL [behavior]
WHILE [state] THE SYSTEM SHALL [behavior]
```

## Parallel Execution

Tasks are split into wave files for efficient execution:
- Each wave in separate file (`wave-N.md`)
- Wave N+1 blocked until Wave N complete
- Maximum 4 parallel subagents per wave
- `index.md` tracks overall progress

Execute with:
- `/spec-execute` - Next pending wave
- `/spec-execute wave 2` - Specific wave
- `/spec-execute T5` - Single task

## Review Pipeline

After each task:
1. Requirements Review → Meets EARS criteria?
2. Architecture Review → Follows design.md?
3. Code Quality Review → Clean, secure, performant?

PASS → Mark complete, continue
FAIL → Feedback loop (max 2 retries)

## Quick Start

```
User: "I want to build a task management app"

Claude: [Uses /spec-start]
        "What would you like to call this project?"

User: "task-manager"

Claude: [Creates .specs/task-manager/]
        "Project initialized! Use /spec-idea to refine your concept."
```
