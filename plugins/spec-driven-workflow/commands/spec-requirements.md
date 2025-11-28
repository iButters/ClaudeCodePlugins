---
description: Generate detailed requirements with EARS notation from refined idea
argument-hint: [project-name]
model: opus
allowed-tools: Read, Write, Edit
---

# Requirements Generation

Think deeply about requirements engineering. Use extended thinking to ensure completeness.

## Input
- Project: $ARGUMENTS or detect from `.specs/`

## Prerequisites
- `.specs/[project]/idea.md` must have Status: 🟢 Refined
- If not refined, suggest `/spec-idea` first

## EARS Notation Reference

Use EARS (Easy Approach to Requirements Syntax) for all acceptance criteria:

| Pattern | Usage | Example |
|---------|-------|---------|
| WHEN...SHALL | Event-driven | WHEN user clicks login THE SYSTEM SHALL validate credentials |
| WHILE...SHALL | State-driven | WHILE offline THE SYSTEM SHALL queue requests |
| IF...THEN | Conditional | IF password invalid THEN THE SYSTEM SHALL show error |
| WHERE...SHALL | Feature-specific | WHERE premium user THE SYSTEM SHALL show analytics |
| THE SYSTEM SHALL | Ubiquitous | THE SYSTEM SHALL encrypt all passwords |

## Process

### 1. Analyze Idea
Extract from idea.md:
- Core features from "Must Have"
- User personas
- Constraints
- Success metrics

### 2. Generate Requirements

For each feature, create:

**User Story:**
```
As a [Persona]
I want to [Action/Feature]
So that [Benefit/Goal]
```

**EARS Acceptance Criteria:**
- At least 3 testable criteria per requirement
- Include happy path AND error cases
- Use measurable values (not "fast" but "< 2 seconds")

**Priority:**
- P1 (Must-have): MVP won't work without this
- P2 (Should-have): Important but not blocking
- P3 (Nice-to-have): Can wait for v2

### 3. Create requirements.md

```markdown
# Requirements Document

## Introduction
[2-3 sentence overview from idea.md]

**Project:** [Name]
**Version:** 1.0
**Status:** Draft
**Last Updated:** [Date]

## Personas

### [Persona Name]
- **Description:** [Who]
- **Goals:** [What they want]
- **Pain Points:** [Current problems]

## Requirements Overview

| ID | Feature | Priority | Status |
|----|---------|----------|--------|
| R1 | [Name] | P1 | Draft |
| R2 | [Name] | P1 | Draft |

## Detailed Requirements

### R1: [Feature Name]

**User Story:**
As a [Persona] I want to [Action] so that [Benefit].

**Priority:** P1 - Must-have

**Acceptance Criteria:**

1. WHEN [trigger]
   THE SYSTEM SHALL [behavior]

2. WHEN [trigger]  
   THE SYSTEM SHALL [behavior]

3. IF [error condition]
   THEN THE SYSTEM SHALL [error handling]

**Notes:**
- [Implementation hints]

---

### R2: [Feature Name]
...

## Non-Functional Requirements

### Performance
- THE SYSTEM SHALL respond within [X] seconds under normal load
- THE SYSTEM SHALL support [Y] concurrent users

### Security
- THE SYSTEM SHALL encrypt sensitive data at rest
- THE SYSTEM SHALL require authentication for [actions]

### Usability
- THE SYSTEM SHALL work on mobile devices
- THE SYSTEM SHALL meet WCAG 2.1 AA standards

## Out of Scope
- [Explicit exclusions from idea.md]

## Glossary
| Term | Definition |
|------|------------|
| [Term] | [Definition] |
```

### 4. Validate with User

Present summary and ask:
- Missing requirements?
- Correct priorities?
- Clear acceptance criteria?

## Output

```
✅ Requirements generated for "[project]"

📊 Summary:
- P1 (Must-have): [X] requirements
- P2 (Should-have): [Y] requirements  
- P3 (Nice-to-have): [Z] requirements
- Total Acceptance Criteria: [N]

🚀 Next: /spec-design
   Create technical architecture based on requirements.
```

## Rules
- Every requirement needs at least 3 EARS criteria
- All criteria must be testable
- No vague terms - use specific, measurable values
- Include both functional AND non-functional requirements
