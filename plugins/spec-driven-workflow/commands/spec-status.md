---
description: Show current project status and progress overview
argument-hint: [project-name]
model: claude-sonnet-4-5-20250514
allowed-tools: Read
---

# Project Status

## Input
- Project: $ARGUMENTS or detect from `.specs/`

## Process

### 1. Scan Project Files
Read spec files and extract:
- idea.md → Project overview, status
- requirements.md → Requirements count, priorities
- design.md → Components, tech stack
- tasks/index.md → Task status, wave progress (primary source)
- bugs/index.md → Bug counts by status (if exists)
- features/index.md → Feature counts by status (if exists)
- reports/ → Recent wave reports (if exists)

**Note:** Only read index files for status - they contain summaries. Don't load individual files unless details needed.

### 2. Calculate Metrics

```python
# Metrics to calculate
total_tasks = count(tasks)
completed = count(tasks where status == "Completed")
in_progress = count(tasks where status == "In Progress")
blocked = count(tasks where status == "Blocked")
not_started = count(tasks where status == "Not Started")

progress_pct = (completed / total_tasks) * 100

# By type
backend_tasks = count(tasks where type == "backend")
frontend_tasks = count(tasks where type == "frontend")
# etc.
```

### 3. Identify Blockers
Find:
- Tasks marked as blocked
- Failed reviews
- Missing dependencies

## Output

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
| 3 | ⬜ Blocked | 0/6 |

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

## Rules
- Show accurate counts
- Highlight blockers prominently
- Show bugs requiring attention (Critical/High)
- Show features ready for implementation
- Suggest next actions
