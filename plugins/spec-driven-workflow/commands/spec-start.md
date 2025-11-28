---
description: Initialize a new spec-driven project with structured planning
argument-hint: [project-name]
allowed-tools: Read, Write, Edit, Bash(mkdir:*), Bash(ls:*)
---

# Initialize Spec-Driven Project

Think step by step about the project setup.

## Input
- Project name: $ARGUMENTS (if empty, ask user)

## Process

1. **Validate project name**
   - Convert to kebab-case if needed
   - Check if `.specs/$ARGUMENTS/` already exists

2. **Create project structure**
   ```
   .specs/
   ├── $ARGUMENTS/
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

3. **Initialize idea.md** with template:
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

4. **Initialize other files** with placeholder content indicating next steps

5. **Initialize bugs/index.md** with template from `assets/templates/bugs-index.md`

6. **Initialize features/index.md** with template from `assets/templates/features-index.md`

7. **Create reports/ directory** (empty, will be populated by /spec-execute)

8. **Create steering/project-rules.md** (if not exists):
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

## Output

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

## Rules
- NEVER overwrite existing files without confirmation
- Always use kebab-case for project names
