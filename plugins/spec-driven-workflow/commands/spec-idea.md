---
description: Refine project idea through interactive dialog with deep analysis
argument-hint: [project-name]
model: opus
allowed-tools: Read, Write, Edit
---

# Idea Refinement Dialog

Think deeply and thoroughly about the project concept. Use extended thinking to explore all angles.

## Input
- Project: $ARGUMENTS or detect from `.specs/*/idea.md`

## Process

### 1. Load Current State
Read `.specs/[project]/idea.md` to understand current state.

### 2. Interactive Dialog

Guide user through these questions (one at a time, adapt based on answers):

**Core Problem:**
- "What specific problem are you trying to solve?"
- "Who experiences this problem most acutely?"
- "What happens if this problem isn't solved?"

**Target Users:**
- "Who will use this? Describe your ideal user."
- "What's their technical level?"
- "How do they currently solve this problem?"

**Solution Vision:**
- "What does success look like?"
- "What's the ONE thing this must do well?"
- "What explicitly is NOT in scope?"

**Constraints:**
- "Any technical constraints (language, framework, platform)?"
- "Timeline or budget constraints?"
- "Integration requirements?"

### 3. Synthesize and Update

After gathering answers, think deeply about:
- Core value proposition
- MVP scope
- Potential risks
- Success metrics

Update `.specs/[project]/idea.md`:

```markdown
# [Project Name]

## Status
🟢 Refined

## Description
[Refined 2-3 sentence description]

## Core Problem
[Clear problem statement based on dialog]

## Target Users
### Primary Persona: [Name]
- **Who:** [Description]
- **Pain Points:** [List]
- **Current Solution:** [How they solve it now]

## Solution Vision
[What the solution will do]

### Must Have (MVP)
- [Feature 1]
- [Feature 2]

### Out of Scope (v1)
- [Explicit exclusion 1]
- [Explicit exclusion 2]

## Constraints
- **Technical:** [constraints]
- **Timeline:** [constraints]
- **Other:** [constraints]

## Success Metrics
- [Metric 1]
- [Metric 2]

## Open Questions
- [Any unresolved questions]

## Notes
- Created: [date]
- Refined: [today]
```

## Output

```
✅ Idea refined for "[project]"

📋 Summary:
- Problem: [one-liner]
- Users: [primary persona]
- MVP Scope: [X] features defined
- Constraints: [key constraints]

🚀 Next: /spec-requirements
   Generate detailed requirements from this idea.
```

## Rules
- Ask ONE question at a time
- Adapt questions based on previous answers
- Summarize understanding before updating file
- Mark any assumptions clearly
