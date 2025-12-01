---
description: Create and track bugs with EARS notation
argument-hint: [project-name]
allowed-tools: Read, Write, Edit, Bash(mkdir), Bash(ls)
---

# Create Bug Report

<thinking_instruction>
Think step by step about the bug details and ensure proper EARS notation.
</thinking_instruction>

## Input

- Project: `$ARGUMENTS` or detect from `.specs/`

<input_validation>
Before processing $ARGUMENTS, validate the input:

1. **Sanitize project name:**
   - Convert to kebab-case (lowercase, hyphens only)
   - Remove path traversal sequences: `../`, `..\`, `..`
   - Allow only characters: `[a-z0-9-]`
   - Limit length: 1-50 characters

2. **Validate project exists:**
   - Check `.specs/[project]/` directory exists
   - If not exists → Error: "Project not found"

3. **Auto-detection (if no argument):**
   - List directories in `.specs/`
   - Exclude `steering/` from list
   - If single project → Use it
   - If multiple → Ask user to specify
   - If none → Error: "No projects found. Run /spec-start first"
</input_validation>

<prerequisites>
- Project must exist in `.specs/[project]/`
- Run `/spec-start` first if no project exists
</prerequisites>

## Process

### 1. Detect Project

Apply `<input_validation>` rules to determine target project.

### 2. Initialize Bugs Directory

If `.specs/[project]/bugs/` doesn't exist:
- Create directory
- Create `index.md` with initial structure from template

<template_validation>
Verify template exists: `assets/templates/bug.md`
If missing: Use inline template provided in step 5
</template_validation>

### 3. Generate Bug ID

<id_generation>
Robust ID generation:

1. Scan `.specs/[project]/bugs/` for files matching pattern `BUG-(\d+)\.md`
2. Extract all numeric IDs using regex
3. Find maximum ID number
4. Increment by 1 for new ID
5. Format with zero-padding: `BUG-001`, `BUG-002`, etc.

**Edge cases:**
- Empty directory → Start at `BUG-001`
- Non-sequential IDs (001, 003, 005) → Next is `BUG-006`
- Parse failure → Log warning, scan files manually
- Fallback: Count files + 1

**Example:**
```
Existing: BUG-001.md, BUG-003.md, BUG-007.md
Next ID: BUG-008
```
</id_generation>

### 4. Gather Bug Information

<user_dialog>
Ask user for information sequentially:

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
</user_dialog>

### 5. Create Bug File

Use template from `assets/templates/bug.md` or inline template:

<ears_conversion>
Convert user input to EARS notation:

- **Expected Behavior** → `WHEN [action] THE SYSTEM SHALL [expected]`
- **Actual Behavior** → `IF [condition] THEN THE SYSTEM [unwanted behavior]`
- **Fix Criteria** → `WHEN [action] THE SYSTEM SHALL [corrected behavior]`

**Example:**
```
User says: "Expected: Login should redirect to dashboard"
EARS: WHEN user successfully logs in THE SYSTEM SHALL redirect to dashboard

User says: "Actual: Shows blank page"
EARS: IF login credentials are valid THEN THE SYSTEM shows blank page instead of redirecting
```
</ears_conversion>

<template name="bug">
```markdown
# BUG-[ID]: [Title]

## Status
🔴 Open

## Classification
- **Severity:** [Critical/High/Medium/Low]
- **Priority:** [P1/P2/P3]
- **Discovered In:** [Wave N / Testing / Production]

## EARS Specification

### Expected Behavior
WHEN [trigger action]
THE SYSTEM SHALL [expected behavior]

### Actual Behavior
IF [condition that triggers bug]
THEN THE SYSTEM [unwanted behavior]

### Fix Criteria
WHEN [trigger action]
THE SYSTEM SHALL [corrected behavior]

## Reproduction

### Steps
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Environment
- OS: [operating system]
- Runtime: [node version, etc.]
- Browser: [if applicable]

## Traceability
- **Requirements:** [R1, R2 or None]
- **Tasks:** [T5 or None]
- **Related Bugs:** [BUG-XXX or None]

## Resolution
- **Status:** Open
- **Fixed In:** [Wave N or N/A]
- **Fix Date:** [Date or N/A]
- **Verified:** [ ] Yes / [x] No

## Notes
- Created: [Date]
- Reporter: [User or Claude]
```
</template>

### 6. Check for Duplicates

<duplicate_detection>
Before creating bug file:

1. Read existing bug files in `.specs/[project]/bugs/`
2. Compare new bug title with existing titles (case-insensitive)
3. If similarity > 80%:
   ```
   ⚠️ Potential duplicate detected:

   New: "[new title]"
   Existing: BUG-003 "[existing title]"

   Options:
   1. Create anyway (new bug)
   2. View existing bug
   3. Cancel

   Choice?
   ```
</duplicate_detection>

### 7. Update Index

Add entry to `bugs/index.md`:

```markdown
| BUG-[ID] | [Title] | [Severity] | [Priority] | Open | [Date] |
```

## Output

<output_format>
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
</output_format>

<output_error>
```
❌ Error creating bug report

Reason: [specific reason]
- Project not found
- Template missing
- Write permission error

Suggestion: [actionable fix]
```
</output_error>

<rules>
- Always use EARS notation for behaviors
- Auto-increment bug IDs with robust parsing
- Update index after creation
- Link to requirements/tasks when provided
- Check for potential duplicates before creating
- Do not include sensitive data (passwords, tokens) in bug reports
- Validate all user input before processing
</rules>
