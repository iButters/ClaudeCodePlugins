---
description: List and display bug reports for a project
argument-hint: [project-name]
allowed-tools: Read
---

# List Bug Reports

Display all bugs for a project with filtering and summary.

## Input

<input_handling>
- Project: `$ARGUMENTS` or detect from `.specs/`
- If no project specified, scan `.specs/` for single project or ask user
</input_handling>

<prerequisites>
- Project must exist in `.specs/[project]/`
- Bugs directory should exist (show empty state if not)
</prerequisites>

## Process

### 1. Detect Project
If no project specified:
- List directories in `.specs/`
- If single project, use it
- If multiple, ask user to specify

### 2. Check Bugs Directory
If `.specs/[project]/bugs/` doesn't exist:
```
📋 No bugs tracked for [Project]

To report a bug: /spec-bug [project]
```

### 3. Read Bug Index
Read `bugs/index.md` to get overview of all bugs.

### 4. Categorize Bugs

<status_categories>
Group by status:
- 🔴 Open (Critical/High)
- 🟡 Open (Medium/Low)
- 🔄 In Progress
- ✅ Resolved
- ⬜ Closed
</status_categories>

## Output

<output_format>

```
═══════════════════════════════════════
🐛 BUG TRACKER: [Project]
═══════════════════════════════════════

## Summary

| Status | Count |
|--------|-------|
| 🔴 Open (Critical/High) | [N] |
| 🟡 Open (Medium/Low) | [N] |
| 🔄 In Progress | [N] |
| ✅ Resolved | [N] |
| ⬜ Closed | [N] |

**Total:** [N] bugs

## Open Bugs (Requires Attention)

### 🔴 Critical/High Priority

| ID | Title | Severity | Priority | Discovered |
|----|-------|----------|----------|------------|
| BUG-001 | [Title] | Critical | P1 | Wave 2 |
| BUG-003 | [Title] | High | P1 | Testing |

### 🟡 Medium/Low Priority

| ID | Title | Severity | Priority | Discovered |
|----|-------|----------|----------|------------|
| BUG-002 | [Title] | Medium | P2 | Production |

## In Progress

| ID | Title | Assigned To | Wave |
|----|-------|-------------|------|
| BUG-004 | [Title] | wave-bugfix-1 | T15 |

## Recently Resolved

| ID | Title | Fixed In | Verified |
|----|-------|----------|----------|
| BUG-005 | [Title] | T12 (Wave 3) | ✅ Yes |

## Traceability

| Bug | Related Requirements | Related Tasks |
|-----|---------------------|---------------|
| BUG-001 | R1, R3 | T5 |
| BUG-002 | R2 | - |

## Quick Actions

- Report new bug: `/spec-bug`
- Create bug-fix wave: `/spec-bug-wave`
- View specific bug: `Read .specs/[project]/bugs/BUG-[ID].md`
- Edit bug: `Edit .specs/[project]/bugs/BUG-[ID].md`
```
</output_format>

## Empty State

<empty_state>

```
═══════════════════════════════════════
🐛 BUG TRACKER: [Project]
═══════════════════════════════════════

✨ No bugs reported yet!

To report a bug: /spec-bug [project]
```
</empty_state>

<rules>
- Show most critical bugs first
- Group by status for easy scanning
- Include traceability information
- Provide actionable next steps
</rules>
