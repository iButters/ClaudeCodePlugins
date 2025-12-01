---
description: Create implementation task breakdown with dependencies and wave-based file structure
argument-hint: [project-name]
allowed-tools: Read, Write, Edit, Bash(mkdir:*)
---

# Task Planning

<thinking_instruction>
Think deeply about task decomposition and dependencies. Use extended thinking to optimize execution order.
</thinking_instruction>

## Input

<input_handling>
- Project: `$ARGUMENTS` or detect from `.specs/`
- If no project specified, scan `.specs/` for single project or ask user
</input_handling>

<prerequisites>
- `.specs/[project]/design.md` must exist with components defined
</prerequisites>

## Output Structure

<file_structure>

Create a `tasks/` directory with separate files per wave:

```
.specs/[project]/tasks/
├── index.md          # Overview & status summary
├── wave-1.md         # Wave 1 tasks (no dependencies)
├── wave-2.md         # Wave 2 tasks
└── wave-N.md         # Additional waves as needed
```
</file_structure>

## Process

### 1. Analyze Design
Extract from design.md:
- All components
- Dependencies between components
- Tech stack (affects task type)

### 2. Task Decomposition

<task_structure>
For each component, define tasks with this structure:

```markdown
## T[N]: [Task Name]

**Type:** [backend|frontend|database|test|docs]
**Component:** [From design.md]
**Priority:** P1
**Effort:** [S|M|L|XL]

**Description:**
[What needs to be done]

**Subtasks:**
- [ ] [N].1: [Subtask 1]
- [ ] [N].2: [Subtask 2]

**Acceptance Criteria:**
- [ ] [Criterion linked to requirement]

**Files:**
- `path/to/file.ts` (new)

**Status:** ⬜ Not Started
**Completed:** -
**Review:** -
```
</task_structure>

### 3. Dependency Analysis & Wave Assignment

<wave_assignment>

Build dependency graph and assign waves:
- **Wave 1:** Tasks with no dependencies
- **Wave 2:** Tasks depending only on Wave 1
- **Wave 3:** Tasks depending on earlier waves
- Maximum 4 parallel tasks recommended per wave
</wave_assignment>

### 4. Create tasks/index.md

<index_template>

```markdown
# Implementation Plan

## Overview
**Project:** [Name]
**Total Tasks:** [N]
**Waves:** [W]
**Created:** [Date]

## Progress

| Wave | Description | Total | ✅ | 🔄 | ⬜ | ❌ |
|------|-------------|-------|----|----|----|----|
| 1 | Foundation | [n] | 0 | 0 | [n] | 0 |
| 2 | Core Features | [n] | 0 | 0 | [n] | 0 |
| 3 | Integration | [n] | 0 | 0 | [n] | 0 |

**Overall:** 0/[N] (0%)

## Dependency Graph

```
Wave 1: T1, T2, T3 (parallel, no deps)
    ↓
Wave 2: T4, T5, T6 (parallel, needs W1)
    ↓
Wave 3: T7, T8 (needs W2)
```

## Wave Files

| Wave | File | Status | Tasks |
|------|------|--------|-------|
| 1 | [wave-1.md](wave-1.md) | ⬜ Pending | T1, T2, T3 |
| 2 | [wave-2.md](wave-2.md) | ⬜ Blocked | T4, T5, T6 |
| 3 | [wave-3.md](wave-3.md) | ⬜ Blocked | T7, T8 |

## Task Index

| ID | Task | Type | Wave | Status |
|----|------|------|------|--------|
| T1 | [Name] | database | 1 | ⬜ |
| T2 | [Name] | backend | 1 | ⬜ |
| T3 | [Name] | frontend | 1 | ⬜ |
| T4 | [Name] | backend | 2 | ⬜ |

## Requirements Traceability

| Requirement | Tasks |
|-------------|-------|
| R1 | T1, T4, T7 |
| R2 | T2, T5, T7 |

## Execution Notes
- Max 4 parallel tasks per wave
- Review required after each wave
- Update index.md after each task completion
```
</index_template>

### 5. Create tasks/wave-N.md (for each wave)

<wave_template>

```markdown
# Wave [N]: [Description]

## Status
- **State:** ⬜ Pending | 🔄 In Progress | ✅ Complete
- **Dependencies:** [Wave N-1 or "None"]
- **Tasks:** [X] total, [Y] complete

## Task Summary

| ID | Task | Type | Status | Effort |
|----|------|------|--------|--------|
| T1 | Database Schema | database | ⬜ | M |
| T2 | Auth Setup | backend | ⬜ | M |

---

## T1: Database Schema

**Type:** database
**Component:** Data Layer
**Priority:** P1
**Effort:** M

**Description:**
Set up database schema with Prisma, create initial migrations.

**Subtasks:**
- [ ] 1.1: Initialize Prisma
- [ ] 1.2: Define User model
- [ ] 1.3: Define [Entity] model
- [ ] 1.4: Create migration
- [ ] 1.5: Add seed data

**Acceptance Criteria:**
- [ ] Schema matches design.md data model (R1.1)
- [ ] Migration runs without errors (R1.2)
- [ ] Seed data creates test records (R1.3)

**Files:**
- `prisma/schema.prisma` (new)
- `prisma/migrations/` (new)
- `prisma/seed.ts` (new)

**Status:** ⬜ Not Started
**Completed:** -
**Review:** -

---

## T2: Auth Setup

**Type:** backend
...

---

## Wave Completion Checklist

- [ ] All tasks completed
- [ ] All reviews passed
- [ ] index.md updated
- [ ] Ready for Wave [N+1]
```
</wave_template>

### 6. Validate Plan

<validation>

Check:
- Every requirement has implementing tasks
- No circular dependencies
- Reasonable wave distribution (aim for 3-6 tasks per wave)
- Clear acceptance criteria linked to requirements
</validation>

## Output

<output_format>

```
✅ Task plan created for "[project]"

📁 Created:
.specs/[project]/tasks/
├── index.md      (overview)
├── wave-1.md     ([X] tasks)
├── wave-2.md     ([Y] tasks)
└── wave-3.md     ([Z] tasks)

📊 Summary:
- Total Tasks: [N]
- Waves: [W]
- By Type: Backend [n], Frontend [n], Database [n], Test [n], Docs [n]

🚀 Next: /spec-execute
   Or: /spec-execute wave 1
```
</output_format>

<rules>
- One file per wave (keeps context manageable)
- Every task must have acceptance criteria linked to requirements
- Maximum ~200 lines per wave file
- Update index.md status after any task changes
- Include file paths for every task
</rules>
