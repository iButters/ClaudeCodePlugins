---
description: Create a bug-fix wave from open bugs
argument-hint: [project-name]
allowed-tools: Read, Write, Edit, Bash(mkdir:*), Bash(ls:*)
---

# Create Bug-Fix Wave

Collect open bugs and create a dedicated bug-fix wave for execution.

## Input

<input_handling>
- Project: `$ARGUMENTS` or detect from `.specs/`
- If no project specified, scan `.specs/` for single project or ask user
</input_handling>

<prerequisites>
- Project must exist in `.specs/[project]/`
- At least one open bug in `bugs/`
- `tasks/` directory must exist
</prerequisites>

## Process

### 1. Detect Project
If no project specified:
- List directories in `.specs/`
- If single project, use it
- If multiple, ask user to specify

### 2. Scan Open Bugs
Read all bug files in `.specs/[project]/bugs/`:
- Filter where Status = "Open"
- Sort by Severity (Critical > High > Medium > Low)
- Then by Priority (P1 > P2 > P3)

### 3. Determine Wave Number
- Scan `tasks/` for existing `wave-bugfix-N.md` files
- Increment to next number (e.g., wave-bugfix-1, wave-bugfix-2)

### 4. User Confirmation

<user_confirmation>
```
🐛 Bug-Fix Wave Creation

Found [N] open bugs:

| ID | Title | Severity | Priority |
|----|-------|----------|----------|
| BUG-001 | [Title] | Critical | P1 |
| BUG-003 | [Title] | High | P1 |
| BUG-002 | [Title] | Medium | P2 |

Create wave-bugfix-[N] with these [N] bugs? (y/n)

Or select specific bugs (e.g., "BUG-001, BUG-003"):
```
</user_confirmation>

### 5. Create Bug-Fix Wave File

<wave_template>

Create `tasks/wave-bugfix-N.md`:

```markdown
# Wave Bugfix-[N]: Bug Fixes

## Status
- **State:** ⬜ Pending
- **Dependencies:** None (can run anytime)
- **Tasks:** [X] total, 0 complete

## Task Summary

| ID | Bug | Type | Status | Severity |
|----|-----|------|--------|----------|
| BF1 | BUG-001: [Title] | backend | ⬜ | Critical |
| BF2 | BUG-003: [Title] | frontend | ⬜ | High |

---

## BF1: Fix BUG-001 - [Title]

**Type:** [backend|frontend|database|test]
**Bug Reference:** [BUG-001](../bugs/BUG-001.md)
**Priority:** P1
**Severity:** Critical

**Description:**
[From bug description]

**Steps to Reproduce:**
[From bug file]

**Fix Criteria (EARS):**
WHEN [trigger]
THE SYSTEM SHALL [corrected behavior]

**Subtasks:**
- [ ] BF1.1: Investigate root cause
- [ ] BF1.2: Implement fix
- [ ] BF1.3: Add regression test
- [ ] BF1.4: Verify fix

**Acceptance Criteria:**
- [ ] Bug no longer reproducible
- [ ] Regression test passes
- [ ] No new issues introduced

**Files:**
- `[files from bug context]` (modify)

**Status:** ⬜ Not Started
**Completed:** -
**Review:** -

---

## BF2: Fix BUG-003 - [Title]
...

---

## Wave Completion Checklist

- [ ] All bug fixes completed
- [ ] All reviews passed
- [ ] Bug statuses updated to "Resolved"
- [ ] index.md updated
- [ ] Ready for verification
```
</wave_template>

### 6. Update Task Index

<index_update>

Add wave to `tasks/index.md`:

```markdown
## Bug-Fix Waves

| Wave | File | Status | Bugs |
|------|------|--------|------|
| Bugfix-1 | [wave-bugfix-1.md](wave-bugfix-1.md) | ⬜ Pending | BUG-001, BUG-003 |
```
</index_update>

### 7. Update Bug Files

<bug_status_update>

For each included bug, update status:
```markdown
**Status:** Open → In Progress (wave-bugfix-N)
```
</bug_status_update>

## Output

<output_format>

```
✅ Bug-Fix Wave Created

📁 File: .specs/[project]/tasks/wave-bugfix-[N].md

🐛 Included Bugs:
   - BUG-001: [Title] (Critical/P1)
   - BUG-003: [Title] (High/P1)

📊 Summary:
   Total Tasks: [N]
   By Type: Backend [n], Frontend [n], Database [n]

📝 Updated:
   - tasks/index.md (added wave reference)
   - bugs/BUG-001.md (status → In Progress)
   - bugs/BUG-003.md (status → In Progress)

🚀 Next: /spec-execute wave bugfix-[N]
   Or: /spec-execute (will include in queue)
```
</output_format>

<rules>
- Bug-fix waves use separate numbering (bugfix-1, bugfix-2, not wave-4)
- Each bug becomes one task with subtasks
- Always include regression test subtask
- Update bug status when added to wave
- Sort by severity/priority in wave
</rules>
