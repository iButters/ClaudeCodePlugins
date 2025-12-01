---
description: Show current project status and progress overview
argument-hint: [project-name]
allowed-tools: Read
---

# Project Status

<thinking_instruction>
Analyze all project files to provide accurate status overview.
</thinking_instruction>

## Input

- Project: `$ARGUMENTS` or detect from `.specs/`

<input_validation>
Before processing $ARGUMENTS, validate the input:

1. **Sanitize project name:**
   - Convert to kebab-case (lowercase, hyphens only)
   - Remove path traversal sequences: `../`, `..\`, `..`
   - Allow only characters: `[a-z0-9-]`

2. **Auto-detection (if no argument):**
   - List directories in `.specs/`
   - Exclude `steering/` from list
   - If single project → Use it
   - If multiple → Ask user to specify
   - If none → Error: "No projects found"
</input_validation>

## Process

### 1. Scan Project Files

<file_scanning>
Read spec files and extract status:

| File | Extract |
|------|---------|
| `idea.md` | Project overview, status |
| `requirements.md` | Requirements count, priorities |
| `design.md` | Components, tech stack |
| `tasks/index.md` | Task status, wave progress (primary source) |
| `bugs/index.md` | Bug counts by status (if exists) |
| `features/index.md` | Feature counts by status (if exists) |
| `reports/` | Recent wave reports (if exists) |

**Performance note:** Only read index files for status - they contain summaries. Don't load individual task/bug/feature files unless specific details needed.
</file_scanning>

<error_handling>
Handle missing or corrupted files:

- `idea.md` missing → Show "⚠️ Project not initialized properly"
- `tasks/index.md` missing → Show "📋 No tasks defined yet"
- `bugs/index.md` missing → Show "No bug tracking active"
- `features/index.md` missing → Show "No feature backlog"
- Parse error → Log warning, show partial data with "⚠️ Some data unavailable"
</error_handling>

### 2. Calculate Metrics

<metrics_calculation>
Calculate the following metrics from parsed data:

**Task Metrics:**
- Total tasks: Count all tasks in index
- Completed: Count tasks with status ✅ or "Completed"
- In Progress: Count tasks with status 🔄 or "In Progress"
- Blocked: Count tasks with status ❌ or "Blocked"
- Not Started: Count tasks with status ⬜ or "Not Started"
- Progress percentage: (Completed / Total) × 100

**Type Distribution:**
- Count tasks by type (backend, frontend, database, test, docs)
- Calculate completion per type

**Wave Status:**
- For each wave file, determine: Complete / Active / Pending / Blocked

**Bug Metrics:**
- Open (Critical/High): Count severity Critical or High with status Open
- Open (Medium/Low): Count severity Medium or Low with status Open
- In Progress: Count status "In Progress"
- Resolved: Count status "Resolved" or "Closed"

**Feature Metrics:**
- Proposed: Count status "Proposed"
- Approved: Count status "Approved"
- In Progress: Count status "In Progress"
- Completed: Count status "Completed"
</metrics_calculation>

### 3. Identify Blockers

<blocker_detection>
Find blocking issues:

- Tasks marked as blocked (❌)
- Failed reviews in recent reports
- Missing dependencies
- Critical/High bugs that may block progress
- Unresolved issues from previous waves
</blocker_detection>

## Output

<output_format>
```
═══════════════════════════════════════
📊 PROJECT STATUS: [Name]
═══════════════════════════════════════

## Workflow Progress

IDEA ──► REQUIREMENTS ──► DESIGN ──► TASKS ──► EXECUTE
  ✅          ✅            ✅         ✅        🔄

## Task Progress

[████████░░░░░░░░] 47% Complete

| Status | Count |
|--------|-------|
| ✅ Completed | [X] |
| 🔄 In Progress | [Y] |
| ⬜ Not Started | [Z] |
| ❌ Blocked | [W] |

**Total:** [N] tasks

## By Type

| Type | Done | Total |
|------|------|-------|
| Backend | [x] | [n] |
| Frontend | [x] | [n] |
| Database | [x] | [n] |
| Tests | [x] | [n] |
| Docs | [x] | [n] |

## Current Wave

**Wave [N]:** [description] → [wave-N.md](tasks/wave-N.md)
- 🔄 T5: [Task name] - In Progress
- ⬜ T6: [Task name] - Waiting

## Wave Overview

| Wave | Status | Progress |
|------|--------|----------|
| 1 | ✅ Complete | 5/5 |
| 2 | 🔄 Active | 2/4 |
| 3 | ⬜ Pending | 0/6 |

## Blockers

[If any blocked tasks:]
⚠️ T7: [Name] - Blocked by [reason]

[If no blockers:]
✅ No blockers

## Next Actions

1. [Most urgent next step]
2. [Second priority]

## Bug Tracker

[If bugs/ directory exists:]

| Status | Count |
|--------|-------|
| 🔴 Open (Critical/High) | [N] |
| 🟡 Open (Medium/Low) | [N] |
| 🔄 In Progress | [N] |
| ✅ Resolved | [N] |

**Attention Required:**
- BUG-001: [Title] (Critical/P1)
- BUG-003: [Title] (High/P1)

[If no bugs/ directory:]
📋 No bug tracking active. Use `/spec-bug` to report bugs.

## Feature Backlog

[If features/ directory exists:]

| Status | Count |
|--------|-------|
| 📝 Proposed | [N] |
| ✅ Approved | [N] |
| 🔄 In Progress | [N] |
| ✨ Completed | [N] |

**Ready for Implementation:**
- FEAT-001: [Title] (P1/M)
- FEAT-002: [Title] (P1/S)

[If no features/ directory:]
📋 No feature backlog. Use `/spec-feature` to request features.

## Recent Reports

[If reports/ directory exists:]

| Wave | Completed | Tasks | Status |
|------|-----------|-------|--------|
| Wave 3 | [Date] | 4/4 | ✅ |
| Wave 2 | [Date] | 5/5 | ✅ |

## Quick Commands

**Execution:**
- Continue execution: `/spec-execute`
- Execute with git: `/spec-execute --git`
- Execute specific wave: `/spec-execute wave 2`
- Execute bug-fix wave: `/spec-execute wave bugfix-1`

**Bug Tracking:**
- Report bug: `/spec-bug`
- List bugs: `/spec-bugs`
- Create bug-fix wave: `/spec-bug-wave`

**Feature Management:**
- Request feature: `/spec-feature`
- List features: `/spec-features`
- Convert to tasks: `/spec-feature-to-tasks FEAT-ID`

**Other:**
- Review task: `/spec-review T5`
- View wave details: Read `.specs/[project]/tasks/wave-N.md`
```
</output_format>

<output_error>
```
❌ Cannot show status

Reason: [specific reason]

Suggestions:
- Run `/spec-start [project-name]` to initialize a project
- Check if `.specs/` directory exists
```
</output_error>

<rules>
- Show accurate counts from index files
- Highlight blockers prominently
- Show bugs requiring attention (Critical/High priority)
- Show features ready for implementation (Approved status)
- Suggest relevant next actions
- Handle missing files gracefully with appropriate messages
- Do not modify any files (read-only command)
</rules>
