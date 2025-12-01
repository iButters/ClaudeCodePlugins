---
description: Execute implementation tasks with parallel subagent orchestration
argument-hint: [T3|wave 2|all|--resume] [--git] [--git-push]
allowed-tools: Read, Write, Edit, Bash, Task
---

# Orchestrated Task Execution

<thinking_instruction>
Think step by step about execution order, dependency management, and delegation strategy.
Use extended thinking for complex wave coordination.
</thinking_instruction>

## Input

`$ARGUMENTS` options:
- Empty or `all`: Execute next pending wave
- `T3` or `3`: Execute specific task T3 only
- `wave 2` or `w2`: Execute all tasks in Wave 2
- `wave bugfix-1` or `wbf1`: Execute bug-fix wave
- `--resume`: Resume from last checkpoint

<input_validation>
Before processing $ARGUMENTS:

1. **Validate task/wave identifiers:**
   - Task ID: Must match pattern `^T?\d+$` (e.g., T3, 3, T12)
   - Wave ID: Must match pattern `^(wave\s+)?\d+$` or `^w\d+$`
   - Bugfix wave: Must match pattern `^(wave\s+)?bugfix-?\d+$` or `^wbf\d+$`

2. **Validate flags:**
   - `--git`: Enable git commit after wave
   - `--git-push`: Enable git commit and push
   - `--resume`: Resume from checkpoint
   - Unknown flags → Warning, continue

3. **Detect project:**
   - Check `.specs/` for single project or ask user
   - Validate project directory exists
</input_validation>

**Flags:**
- `--git`: Commit all changes after wave completion
- `--git-push`: Commit and push to remote after wave completion
- `--resume`: Resume from last saved checkpoint

<prerequisites>
Task files must exist:
- `.specs/[project]/tasks/index.md` - Overview
- `.specs/[project]/tasks/wave-N.md` - Wave files

If files missing, show error with suggestion to run `/spec-tasks` first.
</prerequisites>

## File Structure

```
.specs/[project]/tasks/
├── index.md          # Read for overview
├── wave-1.md         # Wave 1 tasks
├── wave-2.md         # Wave 2 tasks
├── .checkpoint       # Execution state (JSON)
└── ...
```

## Execution Flow

### 1. Check for Checkpoint (if --resume)

<checkpoint_handling>
If `--resume` flag or checkpoint exists:

1. Read `.specs/[project]/tasks/.checkpoint`
2. Parse JSON state:
   ```json
   {
     "wave": 2,
     "started_at": "2025-01-15T10:30:00Z",
     "tasks_completed": ["T1", "T2"],
     "tasks_in_progress": ["T3"],
     "tasks_pending": ["T4", "T5"],
     "last_updated": "2025-01-15T10:45:00Z"
   }
   ```
3. If checkpoint exists:
   ```
   📋 Found checkpoint from [timestamp]

   Wave: [N]
   Completed: T1, T2
   In Progress: T3
   Pending: T4, T5

   Resume from checkpoint? (y/n)
   ```
4. If user confirms → Resume from saved state
5. If user declines → Delete checkpoint, start fresh
</checkpoint_handling>

### 2. Load Overview

Read `tasks/index.md` to determine:
- Current progress
- Which waves are complete/pending
- Next executable wave

### 3. Determine Scope

<scope_determination>
Based on `$ARGUMENTS`:

| Input | Action |
|-------|--------|
| `all` or empty | Find first pending wave, execute it |
| `wave 2` or `w2` | Load and execute `wave-2.md` |
| `T3` or `3` | Find task in wave files, execute only T3 |
| `wave bugfix-1` | Load and execute `wave-bugfix-1.md` |
| `--resume` | Load from checkpoint |
</scope_determination>

### 4. Load Wave File

For the target wave, read `tasks/wave-N.md`:
- Parse all tasks in that wave
- Identify tasks with status ⬜ Not Started
- Check dependencies are met
- Detect file conflicts (same file = sequential execution)

### 5. User Confirmation

<user_confirmation>
```
🚀 Ready to execute [Project]

📋 Target: Wave [N] - [Description]
   Tasks: [X] pending of [Y] total

   T1: Database Schema (database)
   T2: Auth Setup (backend)
   T3: Frontend Init (frontend)

⚠️ Concurrent Execution Warning:
   Do not run multiple /spec-execute commands simultaneously.
   This could cause file conflicts and data corruption.

Continue? (y/n)
```
</user_confirmation>

### 6. Create/Update Checkpoint

<checkpoint_save>
Before starting execution, save checkpoint:

```json
{
  "wave": [N],
  "started_at": "[ISO timestamp]",
  "tasks_completed": [],
  "tasks_in_progress": [],
  "tasks_pending": ["T1", "T2", "T3", "T4"],
  "last_updated": "[ISO timestamp]"
}
```

Write to `.specs/[project]/tasks/.checkpoint`

Update checkpoint after each task completion.
</checkpoint_save>

### 7. Parallel Subagent Execution

<executor_selection>
For each task in the wave (max 4 parallel):

**Select executor by task type:**
| Type | Subagent |
|------|----------|
| backend | backend-executor |
| frontend | frontend-executor |
| database | database-executor |
| test | test-executor |
| docs | docs-executor |
| unknown | Ask user or use backend-executor as fallback |
</executor_selection>

<task_delegation>
Delegate with context:

```markdown
## Task Assignment

**Task:** T[N] - [Name]
**Type:** [type]

### Context

**From requirements.md:**
[Relevant requirements]

**From design.md:**
[Relevant design sections]

**Dependency Outputs:**
[What previous tasks produced]

### Subtasks
1. [ ] [Subtask 1]
2. [ ] [Subtask 2]

### Acceptance Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]

### Files to Create/Modify
- [file list from wave-N.md]

Implement this task and report back with:
1. Files created/modified
2. Implementation summary
3. Any blockers or issues
```
</task_delegation>

### 8. Review Pipeline

<review_pipeline>
After each task completion, spawn reviewers (can run parallel):

1. `requirements-reviewer` → Check acceptance criteria met
2. `architecture-reviewer` → Check design.md compliance
3. `code-quality-reviewer` → Check security, performance, clean code

**Aggregate verdict:**
- All 3 PASS → Task complete
- Any FAIL → Enter feedback loop
- 2 PASS, 1 WARN → Task complete with notes
</review_pipeline>

### 9. Update Files

<status_update>
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

**Update checkpoint:**
- Move task from `tasks_in_progress` to `tasks_completed`
</status_update>

### 10. Handle Failures

<failure_handling>
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

If user chooses to stop → Checkpoint is preserved for `--resume`
</failure_handling>

## Progress Output

<progress_output>
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
</progress_output>

### 11. Generate Wave Report

<report_generation>
After wave completion, create report in `reports/`:

**Create `.specs/[project]/reports/wave-N-report.md`:**

Use template from `assets/templates/wave-report.md` or inline:
- Include all completed tasks
- Include files created/modified
- Include review results
- Include any issues encountered
- Include execution duration
</report_generation>

### 12. Secret Detection (before git)

<secret_detection>
Before staging changes for git commit:

1. Scan modified files for secret patterns:
   - API keys: `/[A-Z]{2,}_API_KEY|api[_-]?key/i`
   - Tokens: `/token|jwt|bearer|secret/i`
   - Credentials: `/password\s*[:=]|secret\s*[:=]/i`
   - Private keys: `/-----BEGIN.*PRIVATE KEY-----/`

2. If potential secrets detected:
   ```
   ⚠️ Potential secrets detected in:
   - src/config.ts:15 (matches: API_KEY)
   - .env:3 (matches: password=)

   Options:
   1. Review and continue (I verified these are safe)
   2. Skip git commit (changes saved, not committed)
   3. Abort and review files

   Choice?
   ```

3. Only proceed with git if user confirms safety
</secret_detection>

### 13. Git Commit (if --git flag)

<git_operations>
If `--git` or `--git-push` flag is present:

1. **Check git repository:**
   ```bash
   git status
   ```
   If not a git repo → Skip with warning

2. **Stage changes:**
   ```bash
   git add -A
   ```

3. **Create commit with HEREDOC:**
   ```bash
   git commit -m "$(cat <<'EOF'
   feat(spec): Complete Wave [N] - [Project]

   Tasks completed:
   - T1: [Task Name]
   - T2: [Task Name]

   Files changed: [count]

   🤖 Generated with [Claude Code](https://claude.com/claude-code)

   Co-Authored-By: Claude <noreply@anthropic.com>
   EOF
   )"
   ```

4. **If `--git-push`:**
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
</git_operations>

### 14. Cleanup Checkpoint

<checkpoint_cleanup>
After successful wave completion:

1. Delete checkpoint file: `.specs/[project]/tasks/.checkpoint`
2. Or update for next wave if continuing
</checkpoint_cleanup>

## Final Output

<output_format>
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

📋 Report: .specs/[project]/reports/wave-N-report.md

Updated:
- tasks/wave-N.md
- tasks/index.md

🚀 Next: /spec-execute wave [N+1]
   Or: /spec-status
```

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

### Partial
```
═══════════════════════════════════════
⚠️ WAVE PARTIALLY COMPLETE
═══════════════════════════════════════

Completed: T1, T2
Failed: T3
Skipped: -

💾 Checkpoint saved - use `/spec-execute --resume` to continue

To retry: /spec-execute T3
To continue: /spec-execute wave [N+1]
```
</output_format>

<output_error>
```
❌ Execution failed

Reason: [specific reason]

Suggestions:
- Check if tasks exist: /spec-tasks
- View status: /spec-status
- Resume from checkpoint: /spec-execute --resume
```
</output_error>

<rules>
- Load only the relevant wave file (not all tasks)
- Maximum 4 parallel subagents
- Update wave file after EACH task completion
- Update index.md after wave completion
- Generate report after wave completion
- Save checkpoint before starting and after each task
- Git commit only if --git flag present
- Scan for secrets before git operations
- Use HEREDOC for multi-line commit messages
- Always confirm before starting execution
- Do not run multiple /spec-execute commands concurrently
- Preserve checkpoint on failure for resume capability
</rules>
