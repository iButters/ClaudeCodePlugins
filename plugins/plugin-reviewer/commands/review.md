# Review Command

**Purpose**: Central entry point for multi-dimensional quality analysis. Delegates to the Review Orchestrator, which automatically decides which specialized evaluators to activate based on input analysis.

**Trigger**: The user wants to evaluate a prompt, plugin, or code.

## Workflow

The Review Command immediately delegates to the Review Orchestrator Agent, which coordinates the entire analysis process.

### Phase 1: Input Analysis (Orchestrator)

The Orchestrator analyzes the input and classifies it.

**Content Type Detection**:
- SKILL.md file -> Plugin Architecture Review
- Command.md file -> Command Structure Review
- Code snippet -> Code Generation + Security Review
- Prompt/Instruction -> Prompt Engineering Review
- Examples present -> Few-Shot Review
- Step-by-step present -> Chain-of-Thought Review
- Architecture description -> Architecture Review

**Complexity Assessment**:
- Simple (<50 lines, single focus) -> Quick Review Profile
- Medium (50-200 lines, 2-4 concerns) -> Standard Review Profile
- Complex (>200 lines, multi-dimensional) -> Comprehensive Review Profile

**Domain Detection**:
- Contains code patterns -> Activate Security Review
- Contains XML tags -> Validate against Technical Standards
- Contains examples -> Activate Few-Shot Review

### Phase 2: Review Profile Selection (Orchestrator)

The Orchestrator automatically selects one of four profiles.

**Quick Review** (5-10 minutes):
- Prompt Engineering Evaluator (TIER 1)
- Security Evaluator (Top-5 Vulnerabilities)
- Status: Basic quality assurance

**Standard Review** (10-20 minutes):
- Quick Review +
- Few-Shot Evaluator
- Chain-of-Thought Evaluator
- Status: Production-readiness check

**Comprehensive Review** (20-40 minutes):
- Standard Review +
- Architecture Evaluator
- Technical Standards Evaluator
- Status: Complete quality analysis

**Code-Focused Review** (10-15 minutes):
- Prompt Engineering Evaluator
- Security Evaluator (extended)
- Technical Standards Evaluator
- Status: Specialized for code generation

**Custom Review**:
- User can select specific evaluators
- Status: Custom configuration

### Phase 3: Mode Selection (Optional)

The Orchestrator can operate in two modes.

**Automatic Mode** (Default):
- Orchestrator decides independently
- Executes all relevant reviews
- Delivers consolidated report
- Fast and efficient

**Advisory Mode** (with `--advisory` flag):
- Orchestrator provides recommendation
- Asks user for confirmation
- Allows adjustment of review selection
- Maximum control

Activation of Advisory Mode:
```
/review --advisory [input]
```

### Phase 4: Parallel Execution (Orchestrator)

The Orchestrator executes reviews intelligently.

**Parallelizable Reviews** (run simultaneously):
- Prompt Engineering + Security + Few-Shot
- Technical Standards + Architecture

**Sequential Dependencies** (run sequentially):
1. Prompt Engineering (base check)
2. If Score >6.0 -> specialized reviews
3. If Score <6.0 -> stop with recommendation to improve

**Timeout Handling**:
- Per evaluator: 5 minutes maximum
- Total: 40 minutes maximum
- On timeout: partial results with warning

### Phase 5: Synthesis & Reporting (Orchestrator)

The Orchestrator aggregates all evaluator outputs into a consolidated report.

**Prioritization by Severity**:
1. Critical issues (Score <5.0 in any dimension)
2. Major issues (Score 5.0-7.0)
3. Minor issues (Score 7.0-9.0)
4. Optimizations (Score >9.0)

**Cross-Dimensional Insights**:
- Recognize patterns across dimensions
- "Security weaknesses correlate with missing constraints" (Prompt Eng + Security)
- "Few-shot ordering could improve CoT quality" (Few-Shot + CoT)

**Actionable Roadmap**:
Prioritized list of next steps with impact estimation

## Parameters

```
/review [input]                    # Automatic mode, auto-detect profile
/review --advisory [input]         # Advisory mode, ask before executing
/review --profile=quick [input]    # Force specific profile
/review --profile=standard [input]
/review --profile=comprehensive [input]
/review --profile=code [input]
/review --evaluators=pe,sec [input] # Custom: only specific evaluators
```

**Evaluator Codes**:
- `pe` = Prompt Engineering
- `sec` = Security
- `fs` = Few-Shot
- `cot` = Chain-of-Thought
- `arch` = Architecture
- `tech` = Technical Standards

## Output Format

The output comes from the Review Orchestrator Agent and follows this schema.

<output_schema>
```markdown
# Multi-Dimensional Quality Analysis

**Input Type**: [Detected type]
**Review Profile**: [Quick|Standard|Comprehensive|Code-Focused|Custom]
**Execution Time**: [X minutes Y seconds]

## Executive Summary

**Overall Quality Score**: [X.X/10]
**Status**: [Excellent | Good | Acceptable | Deficient | Insufficient]

**Critical Issues**: [N]
**Major Issues**: [N]
**Minor Issues**: [N]

**Recommendation**: [1-2 sentence actionable summary]

## Dimensional Scores

| Dimension | Score | Status | Priority |
|-----------|-------|--------|----------|
| Prompt Engineering | [X/10] | [Status] | [High/Med/Low] |
| Security | [X/10] | [Status] | [High/Med/Low] |
| Few-Shot | [X/10] | [Status] | [High/Med/Low] |
| Chain-of-Thought | [X/10] | [Status] | [High/Med/Low] |
| Architecture | [X/10] | [Status] | [High/Med/Low] |
| Technical Standards | [X/10] | [Status] | [High/Med/Low] |

## Critical Issues (Immediate Action Required)

### [Dimension]: [Issue Title]
**Severity**: CRITICAL
**Location**: [Where in input]
**Impact**: [Why this matters]
**Fix**: [Specific solution]
**Estimated Improvement**: +[X] points

## Major Issues (Strongly Recommended)

[Similar structure]

## Minor Issues (Optional Improvements)

[Similar structure]

## Cross-Dimensional Insights

[Patterns noticed across multiple dimensions]

## Actionable Roadmap

**Phase 1 - Critical Fixes** (Estimated Impact: +[X] points):
1. [Action]: [Expected outcome]
2. [Action]: [Expected outcome]

**Phase 2 - Major Improvements** (Estimated Impact: +[X] points):
1. [Action]: [Expected outcome]

**Phase 3 - Optimizations** (Estimated Impact: +[X] points):
1. [Action]: [Expected outcome]

**Total Potential Score**: [X/10] to [Y/10] (+[Z] points)

## Detailed Reports

[Links to individual evaluator reports]
- [Prompt Engineering Detailed Report](#pe-report)
- [Security Detailed Report](#sec-report)
- [Etc.]

---

## Research References
[All sources used across all evaluators]
```
</output_schema>

## Examples

<example name="simple-prompt-review">
**Input**:
```
/review "Write a function to calculate fibonacci numbers"
```

**Orchestrator Decision**:
- Content Type: Simple prompt
- Complexity: Simple
- Profile: Quick Review
- Evaluators: Prompt Engineering, Security (code implied)
- Mode: Automatic
- Execution: Parallel

**Output Summary**:
```
Overall Score: 4.2/10 (Acceptable)

Critical Issues: 2
1. No constraints specified (TIER 1)
2. No output format defined (TIER 1)

Recommendation: Add constraints (language, performance) and specify output format.
Estimated improvement: 4.2 to 8.5 (+4.3 points)
```
</example>

<example name="plugin-review-advisory">
**Input**:
```
/review --advisory [SKILL.md content]
```

**Orchestrator Advisory**:
```
Input Analysis Complete:
- Type: SKILL.md Plugin File
- Complexity: Medium (142 lines, 3 sections)
- Detected Concerns: Architecture, Prompt Engineering, Technical Standards

Recommended Profile: STANDARD REVIEW
Recommended Evaluators:
  1. Prompt Engineering (CRITICAL - checks instruction quality)
  2. Architecture (HIGH - validates plugin structure)
  3. Technical Standards (MEDIUM - encoding, format checks)
  4. Few-Shot (LOW - if examples present)

Estimated Time: 12-18 minutes

Options:
A) Proceed with Standard Review (recommended)
B) Run Comprehensive Review (adds Requirements, Code Gen, CoT)
C) Run Quick Review only (Prompt Eng + Security)
D) Custom selection

Your choice?
```

**User Response**: `A`

**Orchestrator**: "Executing Standard Review with 4 evaluators in parallel..."
</example>

<example name="code-focused-custom">
**Input**:
```
/review --profile=code --evaluators=pe,sec,code [Python code snippet]
```

**Orchestrator Decision**:
- Profile override: Code-Focused
- Evaluator override: Only PE, Security, Code Generation
- Mode: Automatic (no advisory flag)
- Custom configuration respected

**Execution**: Runs only the three specified evaluators, ignores profile defaults
</example>

## Edge Cases

<rules>
**Empty Input**:
Orchestrator responds: "Please provide content to review (prompt, code snippet, plugin file, architecture document, or requirements)"

**Unsupported Format**:
Orchestrator attempts best-effort classification, warns user if uncertain

**Timeout in Evaluator**:
Orchestrator continues with other evaluators, marks timed-out dimension as "incomplete"

**All Evaluators Return Errors**:
Orchestrator provides diagnostic information and suggests manual review

**Conflicting Recommendations**:
Orchestrator highlights conflicts, explains trade-offs, suggests balanced approach

**User Cancellation**:
If user cancels during advisory mode, Orchestrator saves partial analysis for later
</rules>

## Integration with Other Commands

The `/review` command can cache results for `/generate-plugin`:

```
User: /review [existing bad prompt]
Orchestrator: [Detailed analysis with Score 3.2/10]

User: /generate-plugin "Improve this prompt into a full plugin"
Generator: [Uses cached review insights to generate improved version]
```

## Performance Characteristics

**Quick Review**: 5-10 minutes, 2 evaluators
**Standard Review**: 10-20 minutes, 4-5 evaluators
**Comprehensive Review**: 20-40 minutes, 8 evaluators
**Custom Review**: Variable, depends on selection

**Token Usage** (estimated):
- Input analysis: ~500 tokens
- Per evaluator: ~2000-4000 tokens
- Synthesis: ~1000 tokens
- Total for Comprehensive: ~20,000-30,000 tokens

<constraints>
- Always delegate through Orchestrator (never call evaluators directly)
- In Advisory Mode: wait for user confirmation
- In Automatic Mode: show progress updates every 5 minutes
- For critical issues in TIER 1: stop and recommend fixes before further reviews
- All scores and recommendations must be research-backed
</constraints>
