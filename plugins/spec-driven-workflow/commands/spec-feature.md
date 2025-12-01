---
description: Create feature requests with EARS notation
argument-hint: [project-name]
allowed-tools: Read, Write, Edit, Bash(mkdir), Bash(ls)
---

# Create Feature Request

<thinking_instruction>
Think step by step about the feature and ensure proper EARS notation for requirements.
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

### 2. Initialize Features Directory

If `.specs/[project]/features/` doesn't exist:
- Create directory
- Create `index.md` with initial structure

<template_validation>
Verify template exists: `assets/templates/feature.md`
If missing: Use inline template provided in step 6
</template_validation>

### 3. Generate Feature ID

<id_generation>
Robust ID generation:

1. Scan `.specs/[project]/features/` for files matching pattern `FEAT-(\d+)\.md`
2. Extract all numeric IDs using regex
3. Find maximum ID number
4. Increment by 1 for new ID
5. Format with zero-padding: `FEAT-001`, `FEAT-002`, etc.

**Edge cases:**
- Empty directory → Start at `FEAT-001`
- Non-sequential IDs (001, 003, 005) → Next is `FEAT-006`
- Parse failure → Log warning, count files + 1

**Example:**
```
Existing: FEAT-001.md, FEAT-002.md, FEAT-005.md
Next ID: FEAT-006
```
</id_generation>

### 4. Gather Feature Information

<user_dialog>
Ask user for information sequentially:

```
📋 New Feature Request for [Project]

1. Feature Title (short name):
   > [user input]

2. Description (what should it do?):
   > [user input]

3. User Story:
   As a [role]...
   > [user input]

   I want to [action]...
   > [user input]

   So that [benefit]...
   > [user input]

4. Priority (P1/P2/P3):
   > [user input]

5. Effort Estimate (S/M/L/XL):
   > [user input]

6. Key Requirements (list main behaviors):
   > [user input - will be converted to EARS]

7. Error Scenarios (what could go wrong?):
   > [user input - will be converted to EARS unwanted behavior]

8. Dependencies (other features, requirements):
   > [user input]

9. Out of Scope (what is NOT included):
   > [user input]
```
</user_dialog>

### 5. Convert to EARS Notation

<ears_conversion>
Transform user input to EARS patterns:

**Event-Driven (user actions):**
```
WHEN [user action]
THE SYSTEM SHALL [response]
```

**State-Driven (conditions):**
```
WHILE [condition is true]
THE SYSTEM SHALL [maintain behavior]
```

**Optional (feature flags):**
```
WHERE [feature is enabled]
THE SYSTEM SHALL [provide functionality]
```

**Unwanted Behavior (errors):**
```
IF [error condition]
THEN THE SYSTEM SHALL [graceful handling]
```

**Conversion Examples:**
```
User: "User can filter tasks by date"
EARS: WHEN user selects a date filter THE SYSTEM SHALL display only tasks matching that date

User: "Handle network errors"
EARS: IF network connection is lost THEN THE SYSTEM SHALL display offline indicator and queue changes
```
</ears_conversion>

### 6. Create Feature File

<template name="feature">
```markdown
# FEAT-[ID]: [Title]

## Status
📝 Proposed

## Classification
- **Priority:** [P1/P2/P3]
- **Effort:** [S/M/L/XL]
- **Category:** [Enhancement/New Feature/Improvement]

## User Story

**As a** [role]
**I want to** [action]
**So that** [benefit]

## Description

[Detailed description of the feature]

## EARS Requirements

### Functional Requirements

FR-1: WHEN [trigger]
THE SYSTEM SHALL [behavior]

FR-2: WHILE [state]
THE SYSTEM SHALL [behavior]

### Error Handling

FR-E1: IF [error condition]
THEN THE SYSTEM SHALL [graceful handling]

## Acceptance Criteria

- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

## Dependencies

- **Requires:** [FEAT-XXX, R1 or None]
- **Blocks:** [FEAT-YYY or None]
- **Related:** [FEAT-ZZZ or None]

## Out of Scope

- [What this feature does NOT include]

## Implementation Notes

- [Technical considerations]
- [Suggested approach]

## History

- **Created:** [Date]
- **Approved:** [Date or Pending]
- **Implemented:** [Wave N or Pending]
```
</template>

### 7. Check for Duplicates

<duplicate_detection>
Before creating feature file:

1. Read existing feature files in `.specs/[project]/features/`
2. Compare new feature title with existing titles (case-insensitive)
3. If similarity > 80%:
   ```
   ⚠️ Potential duplicate detected:

   New: "[new title]"
   Existing: FEAT-002 "[existing title]"

   Options:
   1. Create anyway (new feature)
   2. View existing feature
   3. Cancel

   Choice?
   ```
</duplicate_detection>

### 8. Update Index

Add entry to `features/index.md`:

```markdown
| FEAT-[ID] | [Title] | [Priority] | [Effort] | Proposed | [Date] |
```

## Output

<output_format>
```
✅ Feature Request Created

📁 File: .specs/[project]/features/FEAT-[ID].md

✨ FEAT-[ID]: [Title]
   Priority: [Priority]
   Effort: [Effort]
   Status: Proposed

📝 EARS Requirements:
   FR-1: WHEN [trigger] THE SYSTEM SHALL [behavior]
   FR-2: WHILE [state] THE SYSTEM SHALL [behavior]
   FR-E1: IF [error] THEN THE SYSTEM SHALL [handling]

👤 User Story:
   As a [role]
   I want to [action]
   So that [benefit]

🔗 Dependencies:
   Requires: [FEAT-XXX, R1 or None]
   Blocks: [FEAT-YYY or None]

📋 Next Steps:
   - View all features: /spec-features
   - Convert to tasks: /spec-feature-to-tasks FEAT-[ID]
   - Edit feature: Edit .specs/[project]/features/FEAT-[ID].md
```
</output_format>

<output_error>
```
❌ Error creating feature request

Reason: [specific reason]

Suggestion: [actionable fix]
```
</output_error>

<rules>
- Always use EARS notation for requirements
- Auto-increment feature IDs with robust parsing
- Update index after creation
- Keep features separate from main requirements until integration
- Include both functional and error handling requirements
- Check for potential duplicates before creating
- Validate all user input before processing
</rules>
