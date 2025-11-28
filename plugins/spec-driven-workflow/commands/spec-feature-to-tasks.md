---
description: Convert an approved feature request into implementation tasks and waves
argument-hint: [FEAT-ID]
allowed-tools: Read, Write, Edit, Bash(mkdir:*), Bash(ls:*)
---

# Convert Feature to Tasks

Think deeply about how to break down the feature into implementable tasks.

## Input
- Feature ID: $ARGUMENTS (e.g., FEAT-001)

## Prerequisites
- Feature file must exist: `.specs/[project]/features/FEAT-[ID].md`
- Feature status should be "Approved" (warn if not)
- `tasks/` directory must exist

## Process

### 1. Load Feature Definition

Read `.specs/[project]/features/FEAT-[ID].md`:
- Extract EARS requirements (FR-1, FR-2, etc.)
- Extract acceptance criteria
- Extract dependencies
- Extract effort estimate

### 2. Analyze Existing Tasks

Read `tasks/index.md`:
- Identify current wave count
- Check for conflicts with existing tasks
- Identify which wave(s) to add to

### 3. User Confirmation

```
🔄 Convert Feature to Tasks

Feature: FEAT-[ID] - [Title]
Status: [Approved/Proposed] (⚠️ Warning if not Approved)
Effort: [S/M/L/XL]

Requirements to implement:
- FR-1: [Description]
- FR-2: [Description]
- FR-E1: [Error handling]

Proposed Tasks:
| ID | Task | Type | Wave |
|----|------|------|------|
| T[N] | [Task Name] | backend | New Wave [W] |
| T[N+1] | [Task Name] | frontend | New Wave [W] |
| T[N+2] | [Task Name] | test | New Wave [W+1] |

Options:
1. Create new wave for this feature
2. Add to existing wave [N]
3. Customize task breakdown

Choice? [1/2/3]
```

### 4. Generate Tasks

For each EARS requirement, create task(s):

**Task Structure:**
```markdown
## T[N]: [Task Name] (FEAT-[ID])

**Type:** [backend|frontend|database|test|docs]
**Component:** [From design.md or new]
**Priority:** [From feature priority]
**Effort:** [S|M|L]
**Feature:** [FEAT-[ID]](../../features/FEAT-[ID].md)

**Description:**
Implement [FR-X] from FEAT-[ID].

**EARS Requirement:**
[Copy EARS statement from feature]

**Subtasks:**
- [ ] [N].1: [Subtask 1]
- [ ] [N].2: [Subtask 2]

**Acceptance Criteria:**
- [ ] [From feature acceptance criteria]

**Files:**
- `path/to/file.ts` (new/modify)

**Status:** ⬜ Not Started
**Completed:** -
**Review:** -
```

### 5. Create/Update Wave File

**If creating new wave:**
Create `tasks/wave-[N].md` with generated tasks.

**If adding to existing wave:**
Append tasks to `tasks/wave-[N].md`.

### 6. Update Task Index

Update `tasks/index.md`:
- Add new tasks to task list
- Update wave information
- Add feature traceability

```markdown
## Feature Traceability

| Feature | Tasks | Status |
|---------|-------|--------|
| FEAT-001 | T15, T16, T17 | ⬜ Not Started |
```

### 7. Update Feature File

Update `.specs/[project]/features/FEAT-[ID].md`:

```markdown
## Implementation
**Planned Wave:** [N]
**Related Tasks:** T15, T16, T17
**Integrated Into Requirements:** [x] Yes
**Status:** Proposed → In Progress
```

## Output

```
✅ Feature Converted to Tasks

📁 Feature: FEAT-[ID] - [Title]

📋 Created Tasks:
| ID | Task | Type | Wave |
|----|------|------|------|
| T15 | Backend API | backend | Wave 5 |
| T16 | Frontend UI | frontend | Wave 5 |
| T17 | Unit Tests | test | Wave 6 |

📝 Updated Files:
- tasks/index.md (added tasks, traceability)
- tasks/wave-5.md (new/updated)
- tasks/wave-6.md (new/updated)
- features/FEAT-[ID].md (status → In Progress)

🔗 Traceability:
- FEAT-[ID] → T15, T16, T17
- FR-1 → T15
- FR-2 → T16
- FR-E1 → T15, T16

🚀 Next: /spec-execute wave 5
   Or: /spec-status
```

## Rules
- One task per major EARS requirement (combine small ones)
- Always include test task for features
- Maintain bidirectional traceability (Feature ↔ Tasks)
- Update feature status to "In Progress" after conversion
- Warn if feature is not "Approved" status
