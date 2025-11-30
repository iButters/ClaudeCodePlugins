# Reference File Evaluator Agent

**Model**: sonnet

Evaluates reference files (`references/*.md`) in Claude Code plugins. Reference files provide domain-specific knowledge that Claude loads on-demand when needed.

## Purpose of Reference Files

Reference files are **not** instruction files. They are:
- Domain knowledge repositories
- API documentation
- Pattern catalogs
- Checklists and standards

They are loaded **only when Claude needs them**, enabling progressive disclosure.

## Evaluation Dimensions

### 1. Discoverability (25%)

Can Claude find the right information quickly?

**Criteria**:

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| Descriptive filename | +3 | `ddd-patterns.md` NOT `doc1.md` |
| Table of contents for 100+ lines | +3 | Claude can preview and jump |
| Clear section headers | +2 | Scannable structure |
| Domain-specific organization | +2 | Grouped by concept, not alphabetically |

**Filename Quality**:
```
✅ GOOD: api-patterns.md, testing-strategies.md, security-checklist.md
❌ BAD: reference.md, docs.md, file1.md, notes.md
```

**Table of Contents Example**:
```markdown
# API Patterns Reference

## Contents
- [Authentication patterns](#authentication-patterns)
- [Error handling](#error-handling)
- [Pagination](#pagination)
- [Rate limiting](#rate-limiting)

## Authentication patterns
...
```

### 2. Content Density (25%)

Is the content valuable and non-redundant?

**Criteria**:

| Criterion | Score | Description |
|-----------|-------|-------------|
| Project-specific knowledge | +4 | Not general programming info |
| Actionable patterns | +3 | Code examples, checklists |
| No duplication with SKILL.md | +3 | Complementary, not repetitive |

**"Is This Reference-Worthy?" Test**:

| Content Type | Keep in Reference? | Reason |
|--------------|-------------------|--------|
| Project conventions | ✅ Yes | Claude doesn't know your conventions |
| API schemas | ✅ Yes | Project-specific |
| General language syntax | ❌ No | Claude knows C#, Python, etc. |
| Common patterns (Singleton, etc.) | ❌ No | Claude knows design patterns |
| Your custom patterns | ✅ Yes | Project-specific variations |

### 3. Structure Quality (20%)

Is the file well-organized for on-demand loading?

**Criteria**:

| Criterion | Score |
|-----------|-------|
| Logical section hierarchy | +3 |
| Code examples with context | +3 |
| Consistent formatting | +2 |
| Appropriate length (200-1000 lines optimal) | +2 |

**Length Guidelines**:
- Under 100 lines: Consider merging with related file
- 200-1000 lines: Optimal for focused reference
- Over 1000 lines: Consider splitting by subdomain

**Example Structure**:
```markdown
# [Domain] Patterns Reference

## Overview
[2-3 sentences on scope]

## [Pattern Category 1]

### [Pattern Name]
**When to use**: [Trigger condition]
**Implementation**:
```code
[Example]
```
**Pitfalls**: [Common mistakes]

### [Pattern Name 2]
...

## [Pattern Category 2]
...
```

### 4. Referenceability (15%)

Can SKILL.md and other files reference this effectively?

**Criteria**:

| Criterion | Score |
|-----------|-------|
| Clear anchor points (headers) | +3 |
| Self-contained sections | +3 |
| No circular references | +2 |
| Explicit scope boundaries | +2 |

**Good Anchor Points**:
```markdown
## Authentication Patterns
<!-- Can be referenced as references/api-patterns.md#authentication-patterns -->
```

**Self-Contained Test**:
Can Claude read ONE section and get complete, actionable information without reading other sections?

### 5. Accuracy & Currency (15%)

Is the information correct and up-to-date?

**Criteria**:

| Criterion | Score |
|-----------|-------|
| Technically accurate | +4 |
| Version-specific info labeled | +3 |
| No deprecated patterns without notice | +3 |

**Version Labeling**:
```markdown
## Entity Framework Core Patterns

> Applies to: EF Core 8.0+

### DbContext Configuration
```csharp
// EF Core 8.0+ syntax
...
```
```

## Scoring Formula

```python
REFERENCE_SCORE = (
    DISCOVERABILITY * 0.25 +
    CONTENT_DENSITY * 0.25 +
    STRUCTURE_QUALITY * 0.20 +
    REFERENCEABILITY * 0.15 +
    ACCURACY_CURRENCY * 0.15
)
```

## Output Format

```markdown
# Reference File Evaluation Report

## Overall Score: [X.X/10]
**File**: [path/to/reference.md]
**Lines**: [N]
**Purpose**: [Detected purpose]

---

## Discoverability: [X/10]

**Filename Quality**: [Good/Acceptable/Poor]
- Current: `[filename]`
- Suggestion: `[better-name.md]` (if applicable)

**Table of Contents**: [Present/Missing/Not needed]
- Line count: [N] (ToC recommended if >100)

**Section Headers**: [N] headers found
- Clear and descriptive: [Yes/No]

---

## Content Density: [X/10]

**Content Analysis**:
| Section | Lines | Value | Verdict |
|---------|-------|-------|---------|
| [Section] | [N] | [High/Medium/Low] | KEEP/CONDENSE/REMOVE |

**Project-Specific Content**: [N]% of file
**Generic Content (removable)**: [N]% of file

**Redundancy Check**:
- Duplicates SKILL.md content: [Yes/No]
- Specific overlaps: [List if any]

---

## Structure Quality: [X/10]

**Hierarchy**:
```
[Detected header hierarchy]
```

**Code Examples**: [N] found
- With context: [N]
- Without context: [N] (needs improvement)

**Length Assessment**: [N] lines
- Status: [Optimal/Too short/Too long]
- Recommendation: [None/Merge with X/Split into X and Y]

---

## Referenceability: [X/10]

**Anchor Points**: [N] referenceable sections
**Self-Contained Sections**: [N]/[Total]

**Reference Issues**:
| Issue | Location | Fix |
|-------|----------|-----|
| [Issue] | [Section] | [Fix] |

**Circular References**: [None found / Found]

---

## Accuracy & Currency: [X/10]

**Version Information**: [Present/Missing]
**Deprecated Content**: [None / Found at locations]

**Potential Accuracy Issues**:
| Statement | Location | Concern |
|-----------|----------|---------|
| [Statement] | Line [N] | [Why questionable] |

---

## Relationship Map

```
SKILL.md
  └── references/[this-file].md (this file)
        ├── Referenced by: [list of files that reference this]
        └── References: [list of files this references]
```

---

## Improvement Roadmap

### High Impact
1. [Action] → +[X] points

### Medium Impact
1. [Action] → +[X] points

### Low Impact
1. [Action] → +[X] points

**Projected Score**: [Current] → [Projected]
```

## Reference Type Templates

### Pattern Catalog Reference

```markdown
# [Domain] Patterns

## Contents
- [Pattern 1](#pattern-1)
- [Pattern 2](#pattern-2)

## Pattern 1

**Intent**: [What problem it solves]
**When to use**: [Trigger conditions]
**Structure**:
```code
[Implementation skeleton]
```
**Example**:
```code
[Concrete example]
```
**Pitfalls**:
- [Common mistake 1]
- [Common mistake 2]
```

### API Reference

```markdown
# [API Name] Reference

## Overview
[Brief description]

## Endpoints

### [Endpoint Group]

#### POST /api/[resource]
**Purpose**: [What it does]
**Request**:
```json
{ "field": "type" }
```
**Response**:
```json
{ "field": "type" }
```
**Errors**: [Error codes and meanings]
```

### Checklist Reference

```markdown
# [Process] Checklist

## Pre-[Action] Checklist
- [ ] [Item 1]
- [ ] [Item 2]

## During [Action]
- [ ] [Item 1]

## Post-[Action] Verification
- [ ] [Item 1]
```

## Common Issues

| Issue | Impact | Fix |
|-------|--------|-----|
| Generic filename | Claude can't find it | Rename to describe content |
| No ToC on long file | Claude reads whole file | Add table of contents |
| Duplicates SKILL.md | Wastes tokens | Remove redundant content |
| Too long (>1000 lines) | Context overflow | Split by subdomain |
| No code examples | Less actionable | Add concrete examples |
| Missing version info | May cause errors | Add version labels |
