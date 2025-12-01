---
description: Initialize a new spec-driven project with structured planning
argument-hint: [project-name]
allowed-tools: Read, Write, Edit, Bash(mkdir), Bash(ls)
---

# Initialize Spec-Driven Project

<thinking_instruction>
Think step by step about the project setup.
</thinking_instruction>

## Input

- Project name: `$ARGUMENTS` (if empty, ask user)

<input_validation>
Before processing $ARGUMENTS, validate the input:

1. **Sanitize project name:**
   - Convert to kebab-case (lowercase, hyphens only)
   - Remove path traversal sequences: `../`, `..\`, `..`
   - Allow only characters: `[a-z0-9-]`
   - Reject names starting with `-` or `.`
   - Limit length: 1-50 characters

2. **Reject invalid inputs:**
   - Empty after sanitization → Ask user for valid name
   - Contains special characters (`<`, `>`, `|`, `&`, `;`, `` ` ``) → Reject with error
   - Reserved names: `steering`, `templates`, `assets` → Reject

3. **Example transformations:**
   - `"My Project"` → `my-project` ✅
   - `"../hack"` → Rejected ❌
   - `"test project 123"` → `test-project-123` ✅
</input_validation>

## Prerequisites

<prerequisites>
- None (this is the first command in workflow)
</prerequisites>

## Process

### 1. Validate Project Name

Apply validation rules from `<input_validation>` section:
- Convert to kebab-case if needed
- Check if `.specs/$PROJECT_NAME/` already exists
- If exists, ask user: "Project already exists. Overwrite? (y/n)"

### 2. Validate Templates Exist

<template_validation>
Before creating files, verify templates exist:

```
Required templates:
- assets/templates/bugs-index.md
- assets/templates/features-index.md
- assets/templates/idea.md (optional, use inline if missing)

If template missing:
1. Log warning: "Template [name] not found, using inline default"
2. Use inline template content (provided below)
```
</template_validation>

### 3. Create Project Structure

```
.specs/
├── $PROJECT_NAME/
│   ├── idea.md
│   ├── requirements.md
│   ├── design.md
│   ├── tasks/           # Task waves (created by /spec-tasks)
│   ├── reports/         # Wave completion reports
│   ├── bugs/            # Bug tracking
│   │   └── index.md
│   └── features/        # Feature requests
│       └── index.md
└── steering/
    └── project-rules.md (only if not exists)
```

### 4. Initialize idea.md

<template name="idea">
```markdown
# [Project Name]

## Status
🟡 Ideation

## Description
[Ask user for 1-2 sentence description]

## Core Problem
[To be defined via /spec-idea]

## Target Users
[To be defined via /spec-idea]

## Known Constraints
- [None yet]

## Notes
- Created: [Today's date]
```
</template>

### 5. Initialize Other Files

Create placeholder content in `requirements.md` and `design.md` indicating next steps.

### 6. Initialize bugs/index.md

Use template from `assets/templates/bugs-index.md` or inline default.

### 7. Initialize features/index.md

Use template from `assets/templates/features-index.md` or inline default.

### 8. Create reports/ Directory

Create empty directory (will be populated by `/spec-execute`).

### 9. Create steering/project-rules.md (if not exists)

<template name="project-rules">
```markdown
# Project Steering Rules

## Code Style
- [Add project-specific rules]

## Architecture Principles
- [Add principles]

## Review Standards
- All tasks must pass requirements review
- Code quality review is mandatory
```
</template>

## Output

<output_format>
```
✅ Project "[name]" initialized!

📁 Created:
.specs/
├── [name]/
│   ├── idea.md          ← Start here
│   ├── requirements.md
│   ├── design.md
│   ├── tasks/           (created by /spec-tasks)
│   ├── reports/         (populated by /spec-execute)
│   ├── bugs/
│   │   └── index.md
│   └── features/
│       └── index.md
└── steering/
    └── project-rules.md

🚀 Next: /spec-idea
   Refine your project concept through guided questions.

📋 Also available:
   - Report bugs: /spec-bug
   - Request features: /spec-feature
```
</output_format>

<output_error>
If validation fails:
```
❌ Invalid project name: "[input]"

Reason: [specific reason]

Please provide a valid project name:
- Use lowercase letters, numbers, and hyphens only
- 1-50 characters
- No special characters or path sequences
```
</output_error>

<rules>
- NEVER overwrite existing files without user confirmation
- Always use kebab-case for project names
- Validate all user input before processing
- Do not run multiple spec commands concurrently on the same project
- Log template warnings but continue with inline defaults
</rules>
