# Generate Plugin Command

**Purpose**: Interactively create a new Claude Code plugin through systematic requirements analysis and generation based on the TIER 1-5 quality criteria.

**Trigger**: The user wants to create a new plugin or describes functionality that should be implemented as a plugin.

## Workflow

### Phase 1: Requirements Analysis

Ask the user 3-5 structured questions to understand the requirements:

<question_framework>
**Core Functionality:**
1. What is the primary goal of the plugin? (Describe in one sentence)
2. What specific actions should the plugin be able to perform?

**Trigger Scenarios:**
3. In which situations will the user use the plugin?
4. Are there specific commands the user should be able to execute?

**Constraints & Standards:**
5. Are there technical requirements? (Programming languages, frameworks, APIs)
6. Are there security or compliance requirements?
7. Are there performance requirements? (Latency, throughput, memory usage, response time)

**Complexity:**
8. Is this a simple plugin (<100 lines SKILL.md) or complex (>5 files)?
9. Are specialized sub-agents needed?
</question_framework>

<rules>
- Ask a maximum of 5 questions at once
- Wait for user response before proceeding
- For vague answers: request clarification with an example
- Document all answers in structured form
</rules>

### Phase 2: Structure Planning

Based on the answers, decide which files need to be created.

**Decision Tree:**

```
Number of expected user actions?
|-- 0-1: Only SKILL.md
|-- 2-4: SKILL.md + commands
`-- 5+: SKILL.md + commands + agents

Logic complexity?
|-- Simple: Inline in commands
|-- Medium: Separate agents
`-- Complex: Agents + references

Extensive specs/standards?
|-- Yes: references folder
`-- No: Inline documentation

Recurring output formats?
|-- Yes: templates folder
`-- No: Inline specification
```

**Output Format:**
```markdown
Planned Structure:
[plugin-name]/
|-- SKILL.md
|-- .claude/commands/
|   `-- [list commands]
|-- agents/ [optional]
|   `-- [list agents]
|-- references/ [optional]
|   `-- [list references]
`-- templates/ [optional]
    `-- [list templates]

Rationale:
- [Why these files?]
- [Which alternatives were rejected?]
```

Wait for user confirmation before proceeding to generation.

### Phase 3: Generation

Generate all files sequentially following the quality criteria:

<generation_rules>
**SKILL.md Generation:**
1. Frontmatter with complete description (100-500 characters)
2. <role> tag immediately after title
3. Workflow section with 3-7 numbered steps
4. <constraints> tag with specific limitations
5. <quality_requirements> if specialized standards apply
6. Cross-references to all other files

**Command Generation:**
Per command:
1. Define purpose and trigger clearly
2. Specify input parameters with type and validation
3. Output format with concrete example
4. <rules> tag for execution logic
5. At least 1 complete example (Input -> Output)

**Agent Generation:**
Per agent:
1. <role> with specific expertise
2. <capabilities> list (3-7 items)
3. <constraints> for scope limitation
4. <output_format> with XML schema
5. <delegation_rules> if sub-agents are possible

**Reference Generation:**
Per reference:
1. <specification> tag for standards
2. Structured by categories
3. At least 3 concrete examples
4. Links to external sources (if available)
</generation_rules>

**Quality Gates During Generation:**
- Every file: Action verb in every instruction (TIER 1)
- SKILL.md: Score >=8.0 in structure review
- Commands: Output format specified
- Agents: <role>, <capabilities>, <constraints> present

### Phase 4: Initial Review

Automatically perform the following quick checks:

```markdown
Quick Quality Check:
Yes/No SKILL.md: Frontmatter complete
Yes/No SKILL.md: <role> and <constraints> tags present
Yes/No Commands: Output format for each command
Yes/No Agents: All mandatory tags (<role>, <capabilities>, <constraints>)
Yes/No All files: Imperative form throughout
Yes/No All files: No vague qualifiers ("some", "etc.")
Yes/No Cross-references: All mentioned files exist

Critical Issues: [Count]
Major Issues: [Count]
Minor Issues: [Count]
```

For more than two critical issues: automatically revise.

### Phase 5: User Presentation

Present the result in structured form:

```markdown
## Generated Plugin: [Name]

### Structure
[Directory tree]

### Quality Assessment
- Prompt Engineering: [Score/10] - [Brief rationale]
- Architecture: [Score/10] - [Brief rationale]
- Technical Standards: [Score/10] - [Brief rationale]
- Overall: [Score/10]

### Next Steps
1. [Optional] Run `/review` for comprehensive analysis
2. [Optional] Run security review if code generation is involved
3. Test the plugin with a concrete use case
4. Iterate based on feedback

Do you want to:
A) Use the plugin as is
B) Revise specific aspects
C) Run a comprehensive review
```

## Output Format

<output_schema>
Phase 1 Output:
```markdown
## Requirements Analysis: [Plugin Name]

**Core Functionality:**
- Primary goal: [...]
- Specific actions: [...]

**Trigger Scenarios:**
- [Scenario 1]
- [Scenario 2]

**Constraints:**
- Technical: [...]
- Security: [...]
- Performance: [...]

**Complexity:** [Simple|Medium|Complex]
```

Phase 2 Output:
```markdown
## Structure Planning

[Directory tree with rationale]
```

Phases 3-5: see above
</output_schema>

## Example

<example>
**User Input:**
"I need a plugin for Git commit messages."

**Questions:**
1. What standard should the commit messages follow? (Conventional Commits, Angular, custom standard, or freeform)
2. Should the plugin automatically analyze the Git diff or expect manual description?
3. Should different commit types be supported? (feat, fix, docs, style, refactor, test, chore)
4. Does the plugin need validation functions?
5. Should there be integration with Git hooks?

**User Answers:**
1. Conventional Commits
2. Automatic diff analysis
3. Yes, all standard types
4. Yes, format validation
5. No, only message generation

**Generated Structure:**
```
commit-message-generator/
|-- SKILL.md
|-- .claude/commands/
|   |-- generate-commit-msg.md
|   `-- validate-commit-msg.md
|-- agents/
|   `-- diff-analyzer.md
`-- references/
    `-- conventional-commits-spec.md
```

**Quality Score:** 9.2/10 (Excellent)
</example>

<example>
**User Input:**
"Create a plugin that is both fast AND comprehensive for code analysis."

**Questions:**
1. Which is more important: speed or thoroughness? (For example, is this for CI/CD where speed matters, or for deep audits where comprehensiveness matters?)
2. Are there specific analysis types you need? (Security, performance, maintainability, style)
3. What is an acceptable timeout? (<30 seconds for fast, <5 minutes for comprehensive)
4. Should the plugin have different modes? (Quick mode vs. Deep mode)

**User Answers:**
1. Prefer thoroughness, but CI/CD integration would be nice
2. All four types (security, performance, maintainability, style)
3. <2 minutes for CI/CD, no limit for deep analysis
4. Yes, two modes would be ideal

**Conflict Resolution:**
The requirements "fast" and "comprehensive" conflict. Solution:
- Default mode: **Standard Review** (~1-2 minutes, covers critical issues)
- Flag `--quick`: **Quick Review** (~30 seconds, only security + basic checks)
- Flag `--deep`: **Comprehensive Review** (no timeout, all dimensions)

**Generated Structure:**
```
code-analyzer/
|-- SKILL.md
|-- .claude/commands/
|   |-- analyze.md (with --quick, --deep flags)
|   `-- analyze-diff.md
|-- agents/
|   |-- security-analyzer.md
|   |-- performance-analyzer.md
|   |-- maintainability-analyzer.md
|   `-- style-analyzer.md
`-- references/
    |-- analysis-profiles.md (documents trade-offs)
    `-- performance-benchmarks.md
```

**Trade-offs Documented in SKILL.md:**
- Quick mode: 30s, 70% issue detection
- Standard mode: 1-2min, 90% issue detection (recommended for CI/CD)
- Deep mode: No limit, 98% issue detection (for audits)

**Quality Score:** 9.4/10 (Excellent - demonstrates conflict resolution pattern)
</example>

<example>
**User Input:**
"Generate a plugin with three commands in the agents/ folder."

**Error Detection:**
Commands belong in `.claude/commands/`, not `agents/`. Agents are specialized sub-agents used by commands.

**Clarification Questions:**
1. Did you mean three **commands** (user-facing actions) or three **agents** (background processors)?
2. If commands: What should each command do?
3. If agents: Which command will call them, and what is their specialization?

**User Clarification:**
"I want three commands: analyze, fix, and validate."

**Corrected Structure:**
```
code-quality-plugin/
|-- SKILL.md
|-- .claude/commands/
|   |-- analyze.md
|   |-- fix.md
|   `-- validate.md
```

**Explanation Provided:**
"I've created three **commands** in `.claude/commands/` (the correct location). Commands are user-facing actions triggered by `/analyze`, `/fix`, `/validate`. If you need background processing agents, those would go in `agents/` and be called by commands."

**Quality Score:** 8.8/10 (Good - demonstrates error correction and user education)
</example>

<constraints>
- Maximum 500 lines per generated file
- Do not automatically create README.md or CHANGELOG.md
- When uncertain: ask instead of assuming
- All generated files must be UTF-8 encoded
</constraints>
