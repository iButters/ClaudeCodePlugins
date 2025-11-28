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

**Note:** Only read `tasks/index.md` for status - it contains the summary. Don't load individual wave files unless details needed.

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

## Quick Commands

- Continue execution: `/spec-execute`
- Execute specific wave: `/spec-execute wave 2`
- Execute specific task: `/spec-execute T5`
- Review task: `/spec-review T5`
- View wave details: Read `.specs/[project]/tasks/wave-N.md`
```

## Rules
- Show accurate counts
- Highlight blockers prominently
- Suggest next actions
