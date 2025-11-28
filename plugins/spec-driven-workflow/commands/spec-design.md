---
description: Create technical architecture and design based on requirements
argument-hint: [project-name]
allowed-tools: Read, Write, Edit
---

# Technical Design Generation

Think deeply about architecture and design decisions. Use extended thinking to evaluate tradeoffs.

## Input
- Project: $ARGUMENTS or detect from `.specs/`

## Prerequisites
- `.specs/[project]/requirements.md` must exist with requirements defined
- Check idea.md for technical constraints

## Process

### 1. Analyze Requirements
Read requirements.md and extract:
- All P1 requirements (must support)
- Non-functional requirements (performance, security)
- Constraints from idea.md

### 2. Design Decisions

Think deeply about each decision:

**Architecture Style:**
- Monolith vs Microservices?
- Event-driven vs Request-response?
- Justification based on requirements

**Tech Stack:**
- Language/Runtime (based on constraints)
- Framework selection with reasoning
- Database choice with reasoning
- Key libraries

**Component Design:**
- Core components/modules
- Responsibilities of each
- Interfaces between them

**Data Model:**
- Key entities
- Relationships
- Storage strategy

### 3. Create design.md

```markdown
# Technical Design

## Overview
[2-3 sentence architecture summary]

**Project:** [Name]
**Version:** 1.0
**Last Updated:** [Date]

## Architecture Decision Records

### ADR-1: Architecture Style
**Decision:** [Chosen approach]
**Context:** [Why this decision was needed]
**Options Considered:**
- Option A: [pros/cons]
- Option B: [pros/cons]
**Rationale:** [Why chosen option]

### ADR-2: Tech Stack
**Decision:** [Stack]
**Rationale:** [Why]

## Tech Stack

| Layer | Technology | Version | Rationale |
|-------|------------|---------|-----------|
| Language | [e.g., TypeScript] | [5.x] | [Why] |
| Runtime | [e.g., Node.js] | [20.x] | [Why] |
| Framework | [e.g., Express] | [4.x] | [Why] |
| Database | [e.g., PostgreSQL] | [15.x] | [Why] |
| ORM | [e.g., Prisma] | [5.x] | [Why] |

## System Architecture

```
[ASCII diagram of components]
```

## Component Design

### Component: [Name]
**Responsibility:** [Single responsibility]
**Interfaces:**
- Input: [What it receives]
- Output: [What it produces]
**Dependencies:** [Other components]

### Component: [Name]
...

## Data Model

### Entity: [Name]
```
[Field definitions with types]
```

### Relationships
- [Entity A] 1:N [Entity B]
- [Entity C] N:M [Entity D]

## API Design

### Endpoint: [METHOD /path]
**Purpose:** [What it does]
**Request:** [Schema]
**Response:** [Schema]
**Errors:** [Error codes]

## Security Design
- Authentication: [Strategy]
- Authorization: [Strategy]
- Data Protection: [Strategy]

## Deployment Architecture
- Environment: [Dev/Staging/Prod]
- Infrastructure: [Cloud/On-prem]
- CI/CD: [Pipeline description]

## Requirements Traceability

| Requirement | Component(s) | Notes |
|-------------|--------------|-------|
| R1 | [Components] | [How addressed] |
| R2 | [Components] | [How addressed] |
```

### 4. Validate Completeness

Verify:
- Every P1 requirement has a component
- Non-functional requirements addressed
- No orphan components

### 5. User Review

Present key decisions and ask:
- Architecture approach acceptable?
- Tech stack constraints met?
- Missing components?

## Output

```
✅ Design created for "[project]"

🏗️ Architecture:
- Style: [approach]
- Components: [count]
- Tech Stack: [summary]

📊 Traceability:
- Requirements covered: [X]/[Y]

🚀 Next: /spec-tasks
   Break down design into implementation tasks.
```

## Rules
- Every requirement must trace to components
- Document ALL architectural decisions with rationale
- Include security considerations
- Keep diagrams simple (ASCII preferred)
