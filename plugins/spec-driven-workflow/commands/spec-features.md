---
description: List and display feature requests for a project
argument-hint: [project-name]
model: claude-sonnet-4-5-20250514
allowed-tools: Read
---

# List Feature Requests

Display all features for a project with filtering and summary.

## Input
- Project: $ARGUMENTS or detect from `.specs/`

## Prerequisites
- Project must exist in `.specs/[project]/`
- Features directory should exist (show empty state if not)

## Process

### 1. Detect Project
If no project specified:
- List directories in `.specs/`
- If single project, use it
- If multiple, ask user to specify

### 2. Check Features Directory
If `.specs/[project]/features/` doesn't exist:
```
📋 No feature requests for [Project]

To request a feature: /spec-feature [project]
```

### 3. Read Feature Index
Read `features/index.md` to get overview of all features.

### 4. Categorize Features

Group by status:
- 📝 Proposed (new ideas)
- ✅ Approved (ready for implementation)
- 🔄 In Progress (being implemented)
- ✨ Completed
- ❌ Rejected

## Output

```
═══════════════════════════════════════
✨ FEATURE BACKLOG: [Project]
═══════════════════════════════════════

## Summary

| Status | Count |
|--------|-------|
| 📝 Proposed | [N] |
| ✅ Approved | [N] |
| 🔄 In Progress | [N] |
| ✨ Completed | [N] |
| ❌ Rejected | [N] |

**Total:** [N] features

## Backlog (Proposed & Approved)

### 📝 Proposed Features

| ID | Title | Priority | Effort | Created |
|----|-------|----------|--------|---------|
| FEAT-003 | [Title] | P1 | M | [Date] |
| FEAT-005 | [Title] | P2 | L | [Date] |

### ✅ Approved (Ready for Implementation)

| ID | Title | Priority | Effort | Approved |
|----|-------|----------|--------|----------|
| FEAT-001 | [Title] | P1 | S | [Date] |
| FEAT-002 | [Title] | P1 | M | [Date] |

## In Progress

| ID | Title | Wave | Progress |
|----|-------|------|----------|
| FEAT-004 | [Title] | Wave 5 | 2/5 tasks |

## Recently Completed

| ID | Title | Completed | Wave |
|----|-------|-----------|------|
| FEAT-006 | [Title] | [Date] | Wave 3 |

## Effort Distribution

| Effort | Count | Features |
|--------|-------|----------|
| S (Small) | [N] | FEAT-001 |
| M (Medium) | [N] | FEAT-002, FEAT-003 |
| L (Large) | [N] | FEAT-005 |
| XL (Extra Large) | [N] | - |

## Dependency Graph

```
FEAT-001 (Approved)
    └── FEAT-004 (In Progress) - depends on FEAT-001
        └── FEAT-007 (Proposed) - depends on FEAT-004

FEAT-002 (Approved) - no dependencies
```

## Quick Actions

- Request new feature: `/spec-feature`
- Convert to tasks: `/spec-feature-to-tasks FEAT-[ID]`
- View specific feature: `Read .specs/[project]/features/FEAT-[ID].md`
- Edit feature: `Edit .specs/[project]/features/FEAT-[ID].md`
- Approve feature: Edit status to "Approved"
```

## Empty State

```
═══════════════════════════════════════
✨ FEATURE BACKLOG: [Project]
═══════════════════════════════════════

📋 No feature requests yet!

To request a feature: /spec-feature [project]
```

## Rules
- Show approved features prominently (ready for work)
- Group by status for easy scanning
- Show dependency relationships
- Provide effort summary for planning
- Include actionable next steps
