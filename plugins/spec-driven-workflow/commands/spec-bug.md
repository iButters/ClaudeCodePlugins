---
description: Create and track bugs with EARS notation
argument-hint: [project-name]
allowed-tools: Read, Write, Edit, Bash(mkdir:*), Bash(ls:*)
---

# Create Bug Report

Think step by step about the bug details and ensure proper EARS notation.

## Input
- Project: $ARGUMENTS or detect from `.specs/`

## Prerequisites
- Project must exist in `.specs/[project]/`

## Process

### 1. Detect Project
If no project specified:
- List directories in `.specs/`
- If single project, use it
- If multiple, ask user to specify

### 2. Initialize Bugs Directory
If `.specs/[project]/bugs/` doesn't exist:
- Create directory
- Create `index.md` with initial structure

### 3. Generate Bug ID
- Read `bugs/index.md` to find highest BUG-NNN
- Increment to get new ID (e.g., BUG-001, BUG-002)

### 4. Gather Bug Information

Ask user for:

```
📋 New Bug Report for [Project]

1. Bug Title (short description):
   > [user input]

2. Severity (Critical/High/Medium/Low):
   > [user input]

3. Priority (P1/P2/P3):
   > [user input]

4. Steps to Reproduce:
   > [user input - can be multiline]

5. Expected Behavior:
   > [user input]

6. Actual Behavior:
   > [user input]

7. Environment (OS, runtime, browser):
   > [user input]

8. Related Requirements (R1, R2... or none):
   > [user input]

9. Related Tasks (T1, T2... or none):
   > [user input]

10. Discovered In (Wave N / Testing / Production):
    > [user input]
```

### 5. Create Bug File

Use template from `assets/templates/bug.md`:

**Convert to EARS notation:**

- Expected → `WHEN [action] THE SYSTEM SHALL [expected]`
- Actual → `IF [condition] THEN THE SYSTEM [unwanted behavior]`
- Fix Criteria → `WHEN [action] THE SYSTEM SHALL [corrected behavior]`

### 6. Update Index

Add entry to `bugs/index.md`:

```markdown
| BUG-[ID] | [Title] | [Severity] | [Priority] | Open | [Date] |
```

## Output

```
✅ Bug Report Created

📁 File: .specs/[project]/bugs/BUG-[ID].md

🐛 BUG-[ID]: [Title]
   Severity: [Severity]
   Priority: [Priority]
   Status: Open

📝 EARS Notation:
   Expected: WHEN [trigger] THE SYSTEM SHALL [behavior]
   Actual:   IF [condition] THEN THE SYSTEM [unwanted]

🔗 Traceability:
   Requirements: [R1, R2 or None]
   Tasks: [T5 or None]

📋 Next Steps:
   - View all bugs: /spec-bugs
   - Create bug-fix wave: /spec-bug-wave
   - Edit bug: Edit .specs/[project]/bugs/BUG-[ID].md
```

## Rules
- Always use EARS notation for behaviors
- Auto-increment bug IDs
- Update index after creation
- Link to requirements/tasks when provided
