# Plugin Generation Examples

**Used By**:
- `skills/plugin-reviewer/SKILL.md` (referenced in Examples section)
- `commands/generate-plugin.md` (plugin generation workflow)
- `agents/review-orchestrator.md` (complexity assessment)

---

This document contains detailed examples of plugin generation ordered by complexity (PERO strategy: Easy -> Medium -> Hard). The examples demonstrate the full range of plugin architectures from simple SKILL-only plugins to complex multi-agent orchestration systems.

## Complexity Scoring

Examples are ordered using this complexity calculation:
```python
complexity_score = (
    file_count * 10 +                    # Number of files
    command_count * 8 +                  # Commands
    agent_count * 12 +                   # Agents (highest weight)
    reference_count * 5 +                # References
    template_count * 5                   # Templates
)
```

---

## Example 3: API Documentation Generator (SKILL + commands + agents + references)

**Complexity Score**: ~58 (Medium)

<example name="api-documentation-plugin">
<input>
"I need a plugin that generates API documentation from code."
</input>

<clarifying_questions>
1. Which programming languages should be supported?
2. Which documentation format do you prefer? (OpenAPI/Swagger, Markdown, HTML)
3. Should automatic tests be created for the generated docs?
4. Are there specific code annotation standards? (JSDoc, docstrings, etc.)
5. Does the plugin need review functions for code quality?
</clarifying_questions>

<generated_structure>
```text
api-doc-generator/
|-- SKILL.md
|-- .claude/commands/
|   |-- generate-api-docs.md
|   |-- validate-annotations.md
|   `-- review-api-design.md
|-- agents/
|   |-- openapi-generator.md
|   |-- annotation-parser.md
|   `-- api-design-reviewer.md
`-- references/
    |-- openapi-3.1-spec.md
    |-- rest-api-best-practices.md
    `-- annotation-standards.md
```
</generated_structure>

<quality_scores>
- Prompt Engineering: 9.6/10 (Specific verbs, clear constraints)
- Architecture: 9.0/10 (Clean separation of concerns)
- Technical Standards: 9.8/10 (Follows OpenAPI 3.1 spec)
- Overall: 9.4/10 (Excellent - production ready)
</quality_scores>
</example>

---

## Example 4: Database Schema Migration Plugin (SKILL + commands + agents + references with validation)

**Complexity Score**: ~68 (Medium-High)

<example name="database-migration-plugin">
<input>
"I need a plugin that helps generate and validate database schema migrations safely."
</input>

<clarifying_questions>
1. Which database systems should be supported? (PostgreSQL, MySQL, SQLite)
2. Should migrations be reversible (up/down scripts)?
3. Do you need automatic migration testing?
4. Should the plugin check for breaking changes?
5. Which migration framework? (Alembic, Flyway, custom)
</clarifying_questions>

<generated_structure>
```text
db-migration-helper/
|-- skills/
|   `-- db-migration/
|       `-- SKILL.md
|-- commands/
|   |-- generate-migration.md
|   |-- validate-migration.md
|   |-- review-schema-changes.md
|   `-- rollback-plan.md
|-- agents/
|   |-- migration-generator.md
|   |-- breaking-change-detector.md
|   |-- schema-validator.md
|   `-- rollback-planner.md
`-- references/
    |-- sql-best-practices.md
    |-- breaking-changes-patterns.md
    `-- migration-safety-checklist.md
```
</generated_structure>

<architecture_notes>
- **Validation pipeline**: schema-validator checks migrations before generation
- **Breaking change detection**: dedicated agent analyzes schema diffs for compatibility issues
- **Rollback safety**: rollback-planner generates down migrations with data preservation strategies
- **Multi-database support**: reference files contain DB-specific patterns
</architecture_notes>

<quality_scores>
- Prompt Engineering: 9.4/10 (Clear constraints, specific validation rules)
- Architecture: 9.2/10 (Good separation of validation and generation)
- Security: 9.6/10 (SQL injection prevention, data loss protection)
- Technical Standards: 9.4/10 (Follows migration framework conventions)
- Overall: 9.4/10 (Excellent - production ready)
</quality_scores>

<rationale>
**Complexity Level**: Medium-High (~68)
- 4 commands (more than Example 3's 3)
- 4 specialized agents (no orchestrator pattern, sequential workflow)
- 3 references with validation rules
- Database-specific safety considerations increase complexity
- Multiple validation stages but simpler than multi-agent orchestration
</rationale>
</example>

---

## Example 5: Multi-Agent Code Reviewer (SKILL + commands + multiple agents)

**Complexity Score**: ~74 (High)

<example name="code-reviewer-multi-agent">
<input>
"Build a plugin that reviews code for security, performance, and maintainability issues."
</input>

<clarifying_questions>
1. Which languages should be supported?
2. Should it auto-fix issues or just report them?
3. Do you want parallel review execution for speed?
4. Should it integrate with CI/CD pipelines?
5. What severity levels do you need? (Critical/Major/Minor)
</clarifying_questions>

<generated_structure>
```text
code-reviewer/
|-- skills/
|   `-- code-reviewer/
|       `-- SKILL.md
|-- commands/
|   |-- review-full.md
|   `-- review-diff.md
`-- agents/
    |-- security-reviewer.md
    |-- performance-reviewer.md
    |-- maintainability-reviewer.md
    `-- review-orchestrator.md
```
</generated_structure>

<architecture_notes>
- **Orchestrator pattern**: `review-orchestrator` spawns three specialized agents in parallel
- **Tool access**: each agent has read, grep, and glob tools for analysis
- **Aggregation**: orchestrator synthesizes findings by severity
- **Reference integration**: agents must read corresponding reference files before scoring
</architecture_notes>

<quality_scores>
- Prompt Engineering: 9.6/10 (Excellent agent role definitions)
- Architecture: 9.8/10 (Clean orchestrator pattern, parallel execution)
- Chain-of-Thought: 9.2/10 (Five-step review process per agent)
- Security: 9.6/10 (OWASP Top-10 integration)
- Overall: 9.6/10 (Excellent - production ready)
</quality_scores>
</example>

---

## Example 6: Full-Featured Migration Assistant (complete plugin)

**Complexity Score**: ~82 (Very High)

<example name="migration-assistant-complete">
<input>
"I need a comprehensive plugin for migrating legacy codebases to modern frameworks with safety checks, test generation, and rollback capabilities."
</input>

<clarifying_questions>
1. Which migration paths? (React Class -> Hooks, Python 2 -> 3, etc.)
2. Should it generate tests for migrated code automatically?
3. Do you need incremental migration support (file-by-file)?
4. Should it create backup/rollback points?
5. Do you want validation against type systems (TypeScript, mypy)?
</clarifying_questions>

<generated_structure>
```text
migration-assistant/
|-- skills/
|   `-- migration-assistant/
|       `-- SKILL.md
|-- commands/
|   |-- plan-migration.md
|   |-- execute-migration.md
|   |-- generate-migration-tests.md
|   |-- validate-migration.md
|   `-- rollback.md
|-- agents/
|   |-- migration-planner.md
|   |-- code-transformer.md
|   |-- test-generator.md
|   |-- safety-validator.md
|   `-- migration-orchestrator.md
|-- references/
|   |-- react-migration-patterns.md
|   |-- python2to3-gotchas.md
|   |-- type-system-validation.md
|   `-- rollback-strategies.md
`-- templates/
    |-- migration-plan.md
    |-- test-template.md
    `-- validation-checklist.md
```
</generated_structure>

<complexity_notes>
- **Five commands**: full workflow coverage from planning to rollback
- **Five agents**: specialized for each phase (plan, transform, test, validate, orchestrate)
- **Four references**: domain knowledge for common migration paths
- **Three templates**: standardized output formats
- **Orchestrator coordination**: migration-orchestrator coordinates sequential execution with checkpoints
- **Safety first**: safety-validator runs on every transformation before commit
</complexity_notes>

<workflow_example>
1. `/plan-migration [directory]` -> analyzes codebase, generates migration plan
2. `/execute-migration --file-by-file` -> transforms code incrementally with checkpoints
3. `/generate-migration-tests` -> creates tests for migrated code
4. `/validate-migration` -> runs type checks, tests, security scans
5. If validation fails -> `/rollback` restores last checkpoint
</workflow_example>

<quality_scores>
- Prompt Engineering: 9.8/10 (Specific verbs, clear constraints, measurable criteria)
- Architecture: 9.8/10 (Excellent separation of concerns, orchestrator pattern)
- Few-Shot: 9.6/10 (Six migration examples covering common patterns)
- Chain-of-Thought: 9.8/10 (Seven to nine steps per migration phase)
- Security: 9.4/10 (Validation gates, rollback safety)
- Technical Standards: 9.8/10 (Proper templates, type system integration)
- Overall: 9.7/10 (Excellent - enterprise production ready)
</quality_scores>

<rationale>
This example demonstrates maximum plugin complexity while maintaining quality. It shows:
- Complete file type coverage (SKILL, commands, agents, references, templates)
- Advanced orchestration patterns with checkpoints
- Safety-first design with validation gates
- Comprehensive documentation following all TIER 1-5 standards
</rationale>
</example>

---

## Usage Guidelines

**When to use each example level:**

- **Example 3 (Medium)**: Plugins with 3+ commands, 3+ agents, reference documentation
- **Example 4 (Medium-High)**: Plugins requiring validation pipelines and safety checks
- **Example 5 (High)**: Multi-dimensional analysis with orchestrator pattern
- **Example 6 (Very High)**: Enterprise-grade plugins with templates and complete workflows

**Complexity assessment formula** from Example 6:
```python
complexity_score = (
    len(files) * 10 +
    len(commands) * 8 +
    len(agents) * 12 +
    len(references) * 5 +
    len(templates) * 5
)
```

See `quality-framework.md` for TIER 1-5 quality criteria applied in all examples.
