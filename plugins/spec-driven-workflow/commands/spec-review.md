---
description: Manually review a completed task against requirements and design
argument-hint: [task-id]
allowed-tools: Read, Bash(ls:*), Bash(cat:*), Bash(git diff:*), Task
---

# Manual Task Review

Think deeply about code quality and requirement fulfillment. Use extended thinking for thorough analysis.

## Input
- Task ID: $ARGUMENTS (required)

## Process

### 1. Load Context

First, locate the task in wave files:
1. Read `tasks/index.md` → Find which wave contains the task
2. Read `tasks/wave-N.md` → Get task definition, acceptance criteria

Then read supporting context:
- `.specs/[project]/requirements.md` → Requirements to validate
- `.specs/[project]/design.md` → Architecture to check
- Task output files (from task definition)

### 2. Spawn Review Subagents

Run parallel reviews using specialized subagents:

**Requirements Review** (requirements-reviewer):
```
Review Task [ID] against requirements.

Task Output Files:
[List of files]

Relevant Requirements:
[From requirements.md]

Check each acceptance criterion.
Report PASS/FAIL with details.
```

**Architecture Review** (architecture-reviewer):
```
Review Task [ID] against design.

Task Output Files:
[List of files]

Design Specifications:
[From design.md]

Check architectural compliance.
Report PASS/FAIL with details.
```

**Code Quality Review** (code-quality-reviewer):
```
Review Task [ID] code quality.

Files to Review:
[List of files]

Check:
- Security vulnerabilities
- Performance issues
- Clean code principles
- Error handling

Report PASS/FAIL with details.
```

### 3. Aggregate Results

Collect all review results:

```markdown
## Review Report: Task [ID]

### Requirements Review
**Reviewer:** requirements-reviewer
**Status:** ✅ PASS / ❌ FAIL

**Criteria Checked:**
- [x] Criterion 1: [result]
- [x] Criterion 2: [result]
- [ ] Criterion 3: [issue]

**Issues:** [if any]

### Architecture Review
**Reviewer:** architecture-reviewer  
**Status:** ✅ PASS / ❌ FAIL

**Compliance:**
- [x] Component structure: OK
- [x] API design: OK
- [ ] Data model: [issue]

**Issues:** [if any]

### Code Quality Review
**Reviewer:** code-quality-reviewer
**Status:** ✅ PASS / ❌ FAIL

**Checks:**
- Security: ✅ / ⚠️ / ❌
- Performance: ✅ / ⚠️ / ❌
- Clean Code: ✅ / ⚠️ / ❌
- Error Handling: ✅ / ⚠️ / ❌

**Issues:** [if any]
```

### 4. Overall Verdict

```
═══════════════════════════════════════
REVIEW VERDICT: Task [ID]
═══════════════════════════════════════

Overall: ✅ PASS / ❌ FAIL

Requirements: [status]
Architecture: [status]
Code Quality: [status]
```

### 5. Handle Verdict

**On PASS:**
```
✅ Task [ID] PASSED review

All criteria met. Task can be marked complete.

Update tasks/wave-N.md? (y/n)
```

If yes, also update `tasks/index.md` progress counts.

**On FAIL:**
```
❌ Task [ID] FAILED review

Issues Found:
1. [Issue 1 - category]
2. [Issue 2 - category]

Recommendations:
- [How to fix issue 1]
- [How to fix issue 2]

Options:
1. Auto-fix with executor subagent
2. Manual fix required
3. Mark as blocked

Choice? [1/2/3]
```

## Output Format

```
═══════════════════════════════════════
📋 REVIEW: Task [ID] - [Name]
═══════════════════════════════════════

## Summary

| Review | Status | Issues |
|--------|--------|--------|
| Requirements | ✅/❌ | [count] |
| Architecture | ✅/❌ | [count] |
| Code Quality | ✅/❌ | [count] |

**Overall:** ✅ PASS / ❌ FAIL ([X]/3 reviews passed)

## Details

[Detailed findings from each reviewer]

## Recommendations

[If failed: specific fixes needed]
[If passed: optional improvements]
```

## Rules
- Run ALL three review types
- Be specific about issues (file, line, problem)
- Provide actionable fix recommendations
- Update wave file status after review
- Update index.md progress counts after status change
