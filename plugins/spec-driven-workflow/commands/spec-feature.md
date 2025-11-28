---
description: Create feature requests with EARS notation
argument-hint: [project-name]
model: sonnet
allowed-tools: Read, Write, Edit, Bash(mkdir:*), Bash(ls:*)
---

# Create Feature Request

Think step by step about the feature and ensure proper EARS notation for requirements.

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

### 2. Initialize Features Directory
If `.specs/[project]/features/` doesn't exist:
- Create directory
- Create `index.md` with initial structure

### 3. Generate Feature ID
- Read `features/index.md` to find highest FEAT-NNN
- Increment to get new ID (e.g., FEAT-001, FEAT-002)

### 4. Gather Feature Information

Ask user for:

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

### 5. Convert to EARS Notation

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

### 6. Create Feature File

Use template from `assets/templates/feature.md` with gathered information.

### 7. Update Index

Add entry to `features/index.md`:

```markdown
| FEAT-[ID] | [Title] | [Priority] | [Effort] | Proposed | [Date] |
```

## Output

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

## Rules
- Always use EARS notation for requirements
- Auto-increment feature IDs
- Update index after creation
- Keep features separate from main requirements until integration
- Include both functional and error handling requirements
