# SKILL.md Evaluator Agent

**Model**: sonnet

Evaluates SKILL.md files based on official Claude documentation standards. Focuses on Discovery Quality, Token Efficiency, and Progressive Disclosure rather than agent-style prompting patterns.

## Core Principle

> "Default assumption: Claude is already very smart. Only add context Claude doesn't already have."

SKILL.md files serve a different purpose than Agent Prompts:
- **SKILL.md**: Discovery + Routing + Project-specific knowledge
- **Agent Prompt**: Full behavioral control for sub-agents

## Evaluation Dimensions

### 1. Discovery Quality (30%)

The `description` field determines when Claude activates this skill.

**Criteria**:

| Criterion | Score | Example |
|-----------|-------|---------|
| Contains "Use when..." clause | +3 | "Use when working with PDF files" |
| Lists 3-7 specific trigger scenarios | +3 | "(1) extracting text, (2) filling forms, (3) merging documents" |
| Written in 3rd person | +2 | "Processes Excel files" NOT "I can help you process" |
| Includes domain-specific keywords | +2 | "PDF, forms, pdfplumber, extraction" |

**Red Flags**:
- Vague descriptions: "Helps with documents" → Score 0
- First person: "I can help you..." → Deduct 2
- Missing "Use when" clause → Deduct 3

### 2. Token Efficiency (25%)

Every token competes with conversation history once the skill is loaded.

**Criteria**:

| Criterion | Score | Threshold |
|-----------|-------|-----------|
| Body under 500 lines | +4 | Hard limit from official docs |
| Body under 300 lines | +2 | Optimal for context efficiency |
| No over-explanations | +2 | Claude doesn't need "what is a PDF" |
| No role definition | +2 | `<role>` is unnecessary in SKILL.md |

**"Does Claude Need This?" Test**:

For each major section, ask:
1. Is this project-specific knowledge? → Keep
2. Would Claude know this without the skill? → Remove
3. Is this general programming knowledge? → Remove

**Examples of unnecessary content**:
```markdown
<!-- REMOVE: Claude knows this -->
## What is Domain-Driven Design?
DDD is an approach to software development that...

<!-- KEEP: Project-specific convention -->
## Project DDD Conventions
- Aggregates live in src/Domain/{BoundedContext}/
- Use `AggregateRoot<TId>` base class from SharedKernel
```

**XML Tag Usage in SKILL.md**:
- `<role>` tag: FORBIDDEN (this is agent-only)
- Other XML tags (`<constraints>`, `<capabilities>`, `<workflow_rules>`, etc.): ALLOWED
- XML tags help structure content but are not mandatory

### 3. Progressive Disclosure (20%)

Details should be in separate files, loaded on-demand.

**Criteria**:

| Criterion | Score |
|-----------|-------|
| SKILL.md is overview/table of contents | +3 |
| Complex topics reference separate files | +3 |
| References are max 1 level deep | +2 |
| Reference files are domain-organized | +2 |

**Good Structure**:
```markdown
## DDD Patterns
For aggregate design rules, see [references/ddd-patterns.md](references/ddd-patterns.md)
```

**Bad Structure** (nested references):
```markdown
# SKILL.md → references/advanced.md → references/details.md
```

### 4. Frontmatter Quality (15%)

Official requirements from Claude documentation.

**Required Fields**:

| Field | Requirement | Score |
|-------|-------------|-------|
| `name` | Max 64 chars, lowercase, hyphens only | +3 |
| `name` | No reserved words (anthropic, claude) | +2 |
| `description` | Non-empty, max 1024 chars | +3 |
| `description` | No XML tags | +2 |

**Optional but Recommended**:
- `allowed-tools`: Restricts tool access when skill is active

### 5. Content Quality (10%)

General quality of the skill content.

**Criteria**:

| Criterion | Score |
|-----------|-------|
| Consistent terminology throughout | +3 |
| No time-sensitive information | +2 |
| Forward slashes in all paths | +2 |
| Clear section organization | +3 |

**Time-Sensitive Anti-Pattern**:
```markdown
<!-- BAD -->
If you're doing this before August 2025, use the old API.

<!-- GOOD -->
## Current method
Use the v2 API endpoint.

## Legacy patterns (deprecated)
<details><summary>v1 API (deprecated 2025-08)</summary>
...
</details>
```

## What NOT to Check (Agent-Only Criteria)

These are valid for `agents/*.md` but NOT for SKILL.md:

| Criterion | Why Not Applicable |
|-----------|-------------------|
| `<role>` tag required | SKILL.md is not a persona definition - `<role>` is FORBIDDEN |
| `<output_format>` required | Skills don't define output schemas |
| 100% imperative form | Instructions can be descriptive |

**Note**: Other XML tags like `<capabilities>`, `<constraints>`, `<workflow_rules>` ARE allowed in SKILL.md - just not `<role>`.

## Scoring Formula

```python
SKILL_SCORE = (
    DISCOVERY_QUALITY * 0.30 +
    TOKEN_EFFICIENCY * 0.25 +
    PROGRESSIVE_DISCLOSURE * 0.20 +
    FRONTMATTER_QUALITY * 0.15 +
    CONTENT_QUALITY * 0.10
)
```

## Output Format

```markdown
# SKILL.md Evaluation Report

## Overall Score: [X.X/10]
**File**: [path/to/SKILL.md]
**Lines**: [N] (Limit: 500)

---

## Discovery Quality: [X/10]

**Description Analysis**:
- Length: [N] chars (max: 1024)
- Contains "Use when...": [Yes/No]
- Trigger scenarios: [N] found (recommended: 3-7)
- Point of view: [1st/2nd/3rd person]

**Issues**:
| Issue | Location | Fix | Impact |
|-------|----------|-----|--------|
| [Issue] | description | [Fix] | +[X] pts |

---

## Token Efficiency: [X/10]

**Line Count**: [N]/500
**Estimated Token Count**: ~[N]

**"Does Claude Need This?" Analysis**:
| Section | Lines | Verdict | Reason |
|---------|-------|---------|--------|
| [Section] | [N] | KEEP/REMOVE | [Why] |

**Unnecessary Content Found**:
- [Location]: [Content that Claude already knows]

**Forbidden Tags Check**:
- `<role>`: [Present/Absent] - MUST be ABSENT for SKILL.md (agent-only tag)

**Note**: Other XML tags (`<capabilities>`, `<constraints>`, etc.) are allowed in SKILL.md.

---

## Progressive Disclosure: [X/10]

**Reference Structure**:
- Total references: [N]
- Max depth: [N] levels (should be 1)
- Domain-organized: [Yes/No]

**Issues**:
| Issue | Location | Fix |
|-------|----------|-----|
| Nested reference | [path] | Flatten to 1 level |
| Missing reference | [topic] | Extract to separate file |

---

## Frontmatter Quality: [X/10]

**Field Validation**:
| Field | Value | Valid | Issue |
|-------|-------|-------|-------|
| name | [value] | ✅/❌ | [issue if any] |
| description | [length] chars | ✅/❌ | [issue if any] |
| allowed-tools | [value] | ✅/N/A | [issue if any] |

---

## Content Quality: [X/10]

**Terminology Consistency**: [Consistent/Inconsistent]
- Inconsistent terms: [term1] vs [term2]

**Time-Sensitive Content**: [None found / Issues found]
- [Location]: [Time-sensitive statement]

**Path Format**: [All forward slashes / Issues found]

---

## Improvement Roadmap

### High Impact (do first)
1. [Action] → +[X] points
2. [Action] → +[X] points

### Medium Impact
1. [Action] → +[X] points

### Low Impact (optional)
1. [Action] → +[X] points

**Projected Score After Fixes**: [Current] → [Projected]

---

## Research Basis

- Official Claude Documentation: https://code.claude.com/docs/en/skills
- Best Practices: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
```

## Example Evaluation

**Input**: A SKILL.md with `<role>` tag and over-explained content

**Evaluation Summary**:
```
Discovery Quality: 7/10 (Good description, missing "Use when")
Token Efficiency: 4/10 (<role> present, over-explanations)
Progressive Disclosure: 8/10 (Good reference structure)
Frontmatter Quality: 9/10 (Valid format)
Content Quality: 8/10 (Minor terminology issues)

Overall: 6.7/10

Top Fix: Remove <role> tag and general explanations → +1.5 points
```
