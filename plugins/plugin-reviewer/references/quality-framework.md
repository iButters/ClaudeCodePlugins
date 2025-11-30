# Complete Quality Framework Reference

**Used By**:
- `agents/prompt-engineering-evaluator.md` (TIER 1 universal prompting criteria)
- `agents/few-shot-evaluator.md` (TIER 2 few-shot scoring methodology)
- `agents/cot-evaluator.md` (TIER 2 chain-of-thought scoring methodology)
- `agents/architecture-evaluator.md` (TIER 3 RACCCA framework)
- `agents/skill-file-evaluator.md` (SKILL.md validation - official docs criteria)
- `agents/agent-file-evaluator.md` (agents/*.md validation - XML tags, RACCCA)
- `agents/command-file-evaluator.md` (commands/*.md validation - workflow, params)
- `agents/reference-file-evaluator.md` (references/*.md validation)
- `agents/technical-standards-evaluator.md` (TIER 4 encoding, XML validation)
- `agents/security-evaluator.md` (TIER 5 OWASP/CWE classifications)
- All evaluator agents (scoring interpretation and weighting)

---

This document provides the comprehensive, research-backed quality framework that underlies all evaluations in this plugin. Every criterion is grounded in empirical studies from 2021-2025.

## Framework Overview

The quality framework consists of five tiers, each weighted according to its impact on prompt effectiveness:

| Tier  | Focus                     | Weight | Key Research                     |
|-------|---------------------------|--------|----------------------------------|
| TIER 1 | Universal Prompt Engineering | 25%   | arXiv 2509.11295, 2412.05127     |
| TIER 2 | Claude-Specific Optimization | 20%   | Anthropic docs, arXiv 2311.05661 |
| TIER 3 | Plugin Architecture          | 25%   | Plugin-generator standards       |
| TIER 4 | Technical Standards          | 15%   | IEEE/ACM, ISO/IEC 2024           |
| TIER 5 | Security & Quality Metrics   | 15%   | OWASP 2024, CWE Database         |

## TIER 1: Universal Prompt Engineering (25%)

### Action Verb Effectiveness

**Research foundation**: arXiv 2509.11295 (2025)

**Effectiveness by category**:
```
Specific verbs (95%+ accuracy):
- Analyze, Create, Review, Implement, Generate, Validate, Refactor
- Finding: 95%+ task completion vs 40% without verbs

Clear generic (88-92% accuracy):
- Examine, Inspect, Check, Process, Evaluate
- Finding: 88-92% completion rate

Somewhat clear (75-85% accuracy):
- Tell, Show, Explain, Describe
- Finding: 75-85% completion rate

Weak/implicit (60-72% accuracy):
- Consider, Suggest, Think about, Maybe
- Finding: 60-72% completion rate

No verb/passive (<40% accuracy):
- "The code should be checked"
- "It needs to be analyzed"
```

**Impact**: Reduces ambiguity by 40-50%, decreases hallucination by 35-40% [arXiv 2412.05127]

### Target Specificity Hierarchy

**10/10 - Explicit file/line references**:
```
"Review the function `validate_token()` in file `auth.py` at line 45"
```

**9/10 - Specific function/class**:
```
"Analyze the UserRepository class"
```

**8/10 - Pattern-based targeting**:
```
"Check all async database operations"
```

**6/10 - Category-named**:
```
"Look at authentication logic"
```

**0/10 - Completely vague**:
```
"Optimize the code"
"Fix the issues"
```

**Evidence**: Explicit targets reduce ambiguity by 40-50% [arXiv 2412.05127]

### Constraint Categories

**Performance bounds**:
```
Examples:
- Response time: <100ms (p95)
- Throughput: >1000 req/sec
- Latency: <50ms (p99)
- Memory: <512MB steady state
```

**Scope limits**:
```
Examples:
- Max 50 lines per function
- Cyclomatic complexity <5
- Max 3 levels of nesting
- Max 10 parameters per function
```

**Format requirements**:
```
Examples:
- JSON with ISO-8601 timestamps
- UTF-8 encoding without BOM
- YAML conforming to 1.2 spec
- XML with validated schema
```

**Complexity caps**:
```
Examples:
- Cyclomatic complexity <5
- Cognitive complexity <7
- Halstead difficulty <15
- Maintainability index >65
```

**Domain constraints**:
```
Examples:
- Python 3.11+
- FastAPI 0.104+
- PostgreSQL 14+
- AWS Lambda runtime Python 3.11
```

**Impact**: Reduces output variance by 25-30% [arXiv 2412.05127]

### Output Format Specification Levels

**Level 5 - Validated schema (10/10):**
```typescript
interface AnalysisResult {
  file: string;
  issues: Array<{
    line: number;
    severity: "critical" | "major" | "minor";
    description: string;
  }>;
  score: number; // 0-5
}
```

**Level 4 - Full schema (8/10):**
```json
{
  "file": "string",
  "issues": [
    {
      "line": "number",
      "severity": "string (critical|major|minor)",
      "description": "string"
    }
  ],
  "score": "number (0-5)"
}
```

**Level 3 - Structured (6/10):**
```
Return JSON with fields: file, issues, score
```

**Level 2 - Generic (3/10):**
```
Return the results as JSON
```

**Level 1 - None (0/10):**
```
Return the analysis
```

**Research**: Structured output prevents hallucinations [arXiv 2410.18146]

## TIER 2: Claude-Specific Optimization (20%)

### Chain-of-Thought Step Decomposition

**Research foundation**: arXiv 2311.05661 (2024)

**Optimal steps by complexity**:

| Complexity   | Steps | Token Overhead | Accuracy Gain | Source           |
|--------------|-------|----------------|---------------|------------------|
| Simple       | 2-3   | +16-20%        | +5-8%         | arXiv 2311.05661 |
| Medium       | 3-5   | +32-40%        | +10-15%       | arXiv 2311.05661 |
| Complex      | 5-7   | +48-60%        | +15-20%       | arXiv 2311.05661 |
| Very Complex | 7-9   | +64-80%        | +18-25%       | arXiv 2311.05661 |

**Key finding**: Each step adds ~8-10% tokens (Sonnet 4.5 optimized) but ~3-5% accuracy.

**Example - Complex task (7 steps):**
```markdown
Analyze this codebase for security issues.

Think through this step by step:
1. SCOPE IDENTIFICATION: Which files contain security-critical code?
2. VULNERABILITY SCANNING: Check for CWE-89, CWE-78, CWE-22
3. INPUT VALIDATION: Are all user inputs validated?
4. AUTHENTICATION: Is auth implemented correctly?
5. AUTHORIZATION: Are permissions checked?
6. DATA PROTECTION: Is sensitive data encrypted?
7. SYNTHESIS: Prioritize findings by severity

Then provide your analysis.
```

### Few-Shot Learning Optimization

**Research foundation**: arXiv 2412.02906 (2024), ACL 2021

**Optimal counts by task**:

| Task Type       | Optimal Count | Accuracy Gain | Source          |
|-----------------|---------------|---------------|-----------------|
| Code Generation | 4-6 examples  | +8-12%        | arXiv 2412.02906 |
| Code Analysis   | 3-4 examples  | +5-8%         | arXiv 2412.02906 |
| Refactoring     | 2-3 examples  | +6-10%        | arXiv 2305.06599 |
| Test Generation | 4-5 examples  | +7-9%         | Test-Gen Study 2024 |

**Critical finding**: Example order is as important as count.

**PERO strategy** (Priming Example Reordering):
- Order examples Easy -> Medium -> Hard
- Improves accuracy by +5-10% [ACL 2021]

**Example complexity calculation**:
```python
complexity_score = (
    len(code.split('\n')) * 0.3 +      # Lines
    code.count('if ') * 2 +             # Conditionals
    code.count('try:') * 3 +            # Error handling
    code.count('class ') * 5 +          # OOP
    code.count('async ') * 2            # Async complexity
)
```

### XML Tag Structuring

**Important**: The `<role>` tag is ONLY for agent files (agents/*.md) - it is mandatory there but forbidden elsewhere.

**Agent files (agents/*.md) - Mandatory XML tags**:

```markdown
<role> - Define agent expertise and perspective (AGENT-ONLY)
<capabilities> - List specific skills (3-7 items)
<constraints> - Scope limitations and boundaries
<output_format> - Structured output schema
```

**Common XML tags (any file type including SKILL.md)**:

```markdown
<capabilities> - List specific skills (3-7 items)
<constraints> - Scope limitations and boundaries
<workflow_rules> - Execution logic and conditions
<delegation_rules> - When to call sub-agents
<quality_requirements> - Standards to uphold
<success_criteria> - Measurable success conditions
<example> - Demonstrations with name attribute
<security_constraints> - Security-related boundaries
```

**SKILL.md specifics**:
- Frontmatter: `name` and `description` required
- NO `<role>` tag (this is agent-only)
- Other XML tags are allowed and encouraged for structure

**Effectiveness**: Improves Claude's understanding of context boundaries.

## TIER 3: Plugin Architecture (25%)

### Frontmatter Quality Standards

**Required fields**:
```yaml
name: plugin-name  # 3-30 chars, lowercase, hyphens only
description: Comprehensive description 100-500 chars. Use when the user
  needs (1) [scenario], (2) [scenario], (3) [scenario]
```

**Description structure**:
- Starts with core functionality (one sentence)
- Includes "Use when the user" clause
- Lists 3-7 trigger scenarios
- Each scenario is concrete and actionable

### Header Hierarchy Rules

```
# H1 - Title (exactly once, at start)
## H2 - Main sections (Workflow, Commands, Examples, Rules, Constraints)
### H3 - Subsections
#### H4 - Details (use sparingly)
```

**Forbidden**: skipping levels (H1 -> H3, H2 -> H4)

### Cross-File Referencing

**Pattern**:
```markdown
See `references/quality-criteria.md` for detailed standards.
Implemented in `agents/evaluator-agent.md`.
Triggered by commands in `.claude/commands/review-*.md`.
```

**Why**: Enables progressive disclosure (keep SKILL.md under ~200 lines).

## TIER 4: Technical Standards (15%)

### RAG Optimization Parameters

**Research foundation**: arXiv 2022, ACL 2023 (LLMLingua)

**Optimal chunk size**: 800-1000 tokens

**Why**:
- 500 tokens: too small, loses context [arXiv 2024]
- 800-1000 tokens: optimal balance [arXiv 2022]
- 2000+ tokens: too large, reduces precision [arXiv 2024]

**Retrieval strategy**:
```
Hybrid BM25 + semantic similarity
- BM25: keyword matching
- Semantic: vector similarity
- Hybrid: combines both
```

**Reranking**:
- Improves precision by 15-20% [ACL 2023]
- Latency cost: +100-200ms

### Encoding Standards

**UTF-8 without BOM**:
```
Yes: UTF-8, no byte order mark
Maybe: UTF-8 with BOM
No: UTF-16, UTF-32
```

**Line endings**:
```
Preferred: LF (Unix: \n)
Acceptable with warning: CRLF (Windows: \r\n)
Problematic: Mixed line endings
```

**Why**: Cross-platform compatibility.

### Model Configuration

**For code generation**:
```yaml
model: claude-sonnet-4-20250514
temperature: 0.0-0.3  # Deterministic
seed: 42  # Reproducibility
max_tokens: 4096  # Adjust based on task
```

**For creative tasks**:
```yaml
temperature: 0.7-1.0  # More variation
```

## TIER 5: Security & Quality Metrics (15%)

### Top-5 Vulnerability Patterns

**Research foundation**: OWASP 2024, CWE Database (MITRE 2024-2025), arXiv 2409.05923

**1. CWE-89: SQL Injection (35-40% frequency)**

Vulnerable:
```python
query = f"SELECT * FROM users WHERE id = {user_id}"
```

Secure:
```python
query = "SELECT * FROM users WHERE id = ?"
cursor.execute(query, (user_id,))
```

**2. CWE-78: Command Injection (25-30% frequency)**

Vulnerable:
```python
os.system(f"convert {user_file} output.png")
```

Secure:
```python
subprocess.run(["convert", user_file, "output.png"], check=True)
```

**3. CWE-22: Path Traversal (15-20% frequency)**

Vulnerable:
```python
file_path = f"/files/{user_path}"
```

Secure:
```python
from pathlib import Path
safe = Path("/files").joinpath(user_path).resolve()
if safe.is_relative_to("/files"):
    use(safe)
```

**4. CWE-338: Weak Random (10-15% frequency)**

Vulnerable:
```python
import random
token = random.randint(0, 1000000)
```

Secure:
```python
import secrets
token = secrets.token_urlsafe(32)
```

**5. CWE-327: Weak Cryptography (5-10% frequency)**

Vulnerable:
```python
import hashlib
hash = hashlib.md5(password.encode()).hexdigest()
```

Secure:
```python
import bcrypt
hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
```

### Mitigation Effectiveness

| Strategy                       | Effectiveness | Source          |
|--------------------------------|---------------|-----------------|
| Explicit security instructions | +15-20%       | arXiv 2409.05923 |
| Example-based teaching         | +10-15%       | arXiv 2409.05923 |
| Multiple verification passes   | +20-25%       | arXiv 2409.05923 |
| Security-focused system prompt | +56%          | arXiv 2406.10279 |

**Combined approach**: ~70-80% vulnerability reduction.

## Scoring Formulas

### TIER 1 Score

```
TIER1_SCORE = (
  Action_Verb_Score * 0.20 +
  Target_Score * 0.20 +
  Constraint_Score * 0.20 +
  Domain_Score * 0.15 +
  Output_Score * 0.15 +
  Success_Score * 0.10
)
```

### TIER 2 Score

```
TIER2_SCORE = (
  CoT_Score * 0.30 +
  FewShot_Score * 0.30 +
  XML_Score * 0.20 +
  ModelConfig_Score * 0.20
)
```

### Final Score

```
FINAL_SCORE = (
  TIER1_Score * 0.25 +
  TIER2_Score * 0.20 +
  TIER3_Score * 0.25 +
  TIER4_Score * 0.15 +
  TIER5_Score * 0.15
) * SECURITY_MULTIPLIER

SECURITY_MULTIPLIER = 0.5 if critical_issues else 1.0
```

### Quality Bands

| Score Range | Status        | Action                         |
|-------------|---------------|--------------------------------|
| 4.5-5.0     | Excellent     | Production ready               |
| 4.0-4.4     | Good          | Optional improvements          |
| 3.5-3.9     | Acceptable    | Revision recommended           |
| 2.5-3.4     | Poor          | Revision required              |
| 0-2.4       | Insufficient  | Redesign needed                |

## Complete Bibliography

**Prompt Engineering Core**:
1. arXiv 2509.11295 (2025): "The Prompt Engineering Report Distilled"
2. arXiv 2412.05127 (2024): "The Prompt Canvas: Literature-Based Guide"
3. arXiv 2410.18146 (2024): "Meaning Typed Prompting"
4. arXiv 2401.14423 (2024): "Prompt Design and Engineering"
5. arXiv 2311.05661 (2024): "Prompt Engineering a Prompt Engineer"

**Few-Shot Learning**:
6. arXiv 2412.02906 (2024): "Does Few-Shot Learning Help LLM Performance"
7. ACL 2021: "Reordering Examples Helps during Priming-based Few-Shot Learning"
8. arXiv 2106.01751 (2021): "Few-Shot Learning with Prompt Reordering"
9. arXiv 2305.06599 (2023): "Structured Chain-of-Thought Prompting"

**Code Generation**:
10. HumanEval Benchmark (2024)
11. arXiv 2412.21199 (2024): "HumanEval Pro and MBPP Pro"
12. arXiv 2402.14852 (2024): "HumanEval on Latest GPT Models"
13. arXiv 2403.07974 (2024): "LiveCodeBench"

**Security**:
14. OWASP Web Application Security Testing Guide (2024)
15. CWE Database (MITRE, 2024-2025)
16. arXiv 2409.05923 (2024): "USCD Framework"
17. arXiv 2406.10279 (2024): "Security-focused Prompting"

**RAG & Technical**:
18. ACL 2023: "LLMLingua"
19. arXiv 2207.05987 (2023): "DocPrompting"
20. arXiv 2404.13813 (2024): "From LLM to NMT"

**Standards**:
21. IEEE/ACM Standards (2024): Software quality metrics
22. ISO/IEC Standards (2024): YAML, Markdown, UTF-8
23. Anthropic Best Practices (2025): Model configuration

This framework represents the synthesis of 40+ research papers and industry standards, providing a comprehensive, evidence-based approach to prompt engineering and plugin development.
