---
description: Execute implementation tasks with parallel subagent orchestration
argument-hint: [T3|wave 2|all] [--git] [--git-push]
allowed-tools: Read, Write, Edit, Bash, Task
---

# Orchestrated Task Execution

Think step by step about execution order and delegation.

## Input

`$ARGUMENTS` options:
- Empty or `all`: Execute all pending waves sequentially
- `T3` or `3`: Execute specific task T3 only
- `wave 2` or `w2`: Execute all tasks in Wave 2
- `wave bugfix-1` or `wbf1`: Execute bug-fix wave

**Flags:**
- `--git`: Commit all changes after wave completion
- `--git-push`: Commit and push to remote after wave completion

## Prerequisites

Task files must exist:
- `.specs/[project]/tasks/index.md` - Overview
- `.specs/[project]/tasks/wave-N.md` - Wave files

## File Structure

```
.specs/[project]/tasks/
├── index.md          # Read for overview
├── wave-1.md         # Wave 1 tasks
├── wave-2.md         # Wave 2 tasks
└── ...
```

## Execution Flow

### 1. Load Overview
Read `tasks/index.md` to determine:
- Current progress
- Which waves are complete/pending
- Next executable wave

### 2. Determine Scope

Based on `$ARGUMENTS`:

| Input | Action |
|-------|--------|
| `all` or empty | Find first pending wave, execute it |
| `wave 2` or `w2` | Load and execute `wave-2.md` |
| `T3` or `3` | Find task in wave files, execute only T3 |

### 3. Load Wave File

For the target wave, read `tasks/wave-N.md`:
- Parse all tasks in that wave
- Identify tasks with status ⬜ Not Started
- Check dependencies are met

### 4. User Confirmation

```
🚀 Ready to execute [Project]

📋 Target: Wave [N] - [Description]
   Tasks: [X] pending of [Y] total

   T1: Database Schema (database)
   T2: Auth Setup (backend)
   T3: Frontend Init (frontend)

Continue? (y/n)
```

### 5. Parallel Subagent Execution

For each task in the wave (max 4 parallel):

**Select executor by task type:**
| Type | Subagent |
|------|----------|
| backend | backend-executor |
| frontend | frontend-executor |
| database | database-executor |
| test | test-executor |
| docs | docs-executor |

**Delegate with context:**
```
Execute Task T[N]: [Name]

Context from specs:
- Requirements: [relevant from requirements.md]
- Design: [relevant from design.md]

Subtasks:
[from wave file]

Acceptance Criteria:
[from wave file]

Files to create/modify:
[from wave file]

Implement and report back.
```

### 6. Review Pipeline

After each task completion, spawn reviewers:
- `requirements-reviewer` → Check acceptance criteria
- `architecture-reviewer` → Check design compliance
- `code-quality-reviewer` → Check code quality

### 7. Update Files

**On task PASS:**
Update `tasks/wave-N.md`:
```markdown
**Status:** ⬜ Not Started  →  **Status:** ✅ Completed
**Completed:** [timestamp]
**Review:** PASS
```

Mark subtasks as done:
```markdown
- [x] 1.1: Initialize Prisma
```

**Update `tasks/index.md`:**
- Increment ✅ count for wave
- Update overall progress percentage

### 8. Handle Failures

**On task FAIL:**
```
⚠️ Task T[N] failed review

Issues:
- [Issue 1]
- [Issue 2]

Retry 1/2: Sending feedback to executor...
```

After 2 failures, escalate:
```
❌ Task T[N] still failing

Options:
1. Try different approach
2. Skip task, continue wave
3. Stop execution

Choice? [1/2/3]
```

## Progress Output

**Per task:**
```
✅ T1: Database Schema completed
   Files: prisma/schema.prisma, prisma/migrations/...
   Review: PASS
```

**Per wave:**
```
═══════════════════════════════════════
📊 Wave 1 Complete
═══════════════════════════════════════
Tasks: 3/3 ✅
Files created: 12
Time: 4m 23s

Next: Wave 2 (5 tasks)
Continue? (y/n)
```

## Final Output

### Success
```
═══════════════════════════════════════
✅ EXECUTION COMPLETE
═══════════════════════════════════════

Wave [N]: [X]/[X] tasks ✅

Files Created/Modified:
- src/services/UserService.ts
- src/controllers/userController.ts
- ...

Updated:
- tasks/wave-N.md
- tasks/index.md

🚀 Next: /spec-execute wave [N+1]
   Or: /spec-status
```

### Partial
```
═══════════════════════════════════════
⚠️ WAVE PARTIALLY COMPLETE
═══════════════════════════════════════

Completed: T1, T2
Failed: T3
Skipped: -

To retry: /spec-execute T3
To continue: /spec-execute wave [N+1]
```

### 9. Generate Wave Report

After wave completion, create report in `reports/`:

**Create `.specs/[project]/reports/wave-N-report.md`:**
- Use template from `assets/templates/wave-report.md`
- Include all completed tasks
- Include files created/modified
- Include review results
- Include any issues encountered

### 10. Git Commit (if --git flag)

If `--git` or `--git-push` flag is present:

```bash
# Stage all changes
git add -A

# Create commit with structured message
git commit -m "feat(spec): Complete Wave N - [Project]

Tasks completed:
- T1: [Task Name]
- T2: [Task Name]

Files changed: [count]

Generated by spec-driven-workflow"
```

If `--git-push`:
```bash
git push
```

**Commit included in output:**
```
🔀 Git: Committed wave changes
   Commit: [hash]
   Files: [count] changed
   [Pushed to remote] (if --git-push)
```

## Final Output

### Success (with --git)
```
═══════════════════════════════════════
✅ EXECUTION COMPLETE
═══════════════════════════════════════

Wave [N]: [X]/[X] tasks ✅

Files Created/Modified:
- src/services/UserService.ts
- src/controllers/userController.ts
- ...

📋 Report: .specs/[project]/reports/wave-N-report.md

🔀 Git:
   Commit: abc1234
   Message: feat(spec): Complete Wave N - [Project]
   Pushed: ✅ (if --git-push)

Updated:
- tasks/wave-N.md
- tasks/index.md
- reports/wave-N-report.md

🚀 Next: /spec-execute wave [N+1]
   Or: /spec-status
```

## Rules
- Load only the relevant wave file (not all tasks)
- Maximum 4 parallel subagents
- Update wave file after EACH task
- Update index.md after wave completion
- Generate report after wave completion
- Git commit only if --git flag present
- Always confirm before starting
