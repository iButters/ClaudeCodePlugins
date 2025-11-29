# Plugin Generator

Creates high-quality Claude Code plugins from natural language descriptions and validates them through specialized review agents.

## Features

This plugin provides a **skill-based workflow** for creating and validating Claude Code plugins:

- **Natural Language to Plugin** - Convert ideas into complete plugin structures
- **Multi-Agent Review System** - Validate plugins through 4 specialized agents
- **Quality Criteria Enforcement** - Ensure plugins meet LLM instruction best practices
- **Template Library** - Reusable templates for Skills, Commands, and Agents
- **Automated Scoring** - Objective quality assessment with actionable feedback

## When to Use

Activate this skill when you want to:

1. Create a new plugin or skill from scratch
2. Get implementation help for a plugin idea
3. Quality-check existing plugin files
4. Receive feedback on instruction markdown files
5. Understand quality criteria for LLM instructions

## Contents

### Main Skill
- `SKILL.md` - Core workflow and decision trees

### Review Agents
- `agents/structure-agent.md` - Frontmatter, headers, syntax validation
- `agents/content-agent.md` - Completeness, specificity, examples
- `agents/clarity-agent.md` - Ambiguity detection, readability
- `agents/consistency-agent.md` - Terminology, cross-file consistency
- `agents/synthesis-agent.md` - Aggregates review results into prioritized reports

### Reference Documentation
- `references/quality-criteria.md` - Comprehensive quality standards
- `references/markdown-types.md` - Requirements per file type
- `references/examples/` - High-quality example files

### Templates
- `templates/skill-template.md` - SKILL.md boilerplate
- `templates/command-template.md` - Command file structure
- `templates/agent-template.md` - Agent definition template

## Workflow

### 1. Requirements Analysis
Extract core functionality, trigger scenarios, and required resources from user description.

### 2. Structure Planning
Determine required file types based on:
- **Commands**: User-triggerable actions with parameters
- **Agents**: Specialized sub-tasks with own logic
- **References**: Extensive documentation
- **Templates**: Reusable structures

### 3. Generation
Create all files adhering to quality criteria from `references/quality-criteria.md`.

### 4. Parallel Review
Run 4 specialist reviews simultaneously:
- Structure Review
- Content Review
- Clarity Review
- Consistency Review

### 5. Synthesis
Aggregate review results into prioritized report via synthesis agent.

### 6. Iteration
Refine plugin based on review feedback.

## Quality Scoring

| Score | Status | Action |
|-------|--------|--------|
| 4.5-5.0 | ✅ Excellent | Release without changes |
| 4.0-4.4 | ✅ Good | Release with optional improvements |
| 3.5-3.9 | ⚠️ Acceptable | Revision recommended |
| 2.5-3.4 | ⚠️ Deficient | Revision required |
| 0-2.4 | ❌ Insufficient | Fundamental redesign needed |

**Category Weighting:**
- Structure: 15%
- Content: 35%
- Clarity: 30%
- Consistency: 20%

## Example: Plugin Creation

**User Request:**
"I need a plugin that helps me write Git commit messages."

**Analysis:**
- Core functionality: Commit message generation
- Triggers: Describing code changes, preparing commits
- Required files: SKILL.md, 1 Command, 1 Reference

**Generated Structure:**
```
commit-helper/
├── SKILL.md
├── .claude/commands/
│   └── generate-commit.md
└── references/
    └── conventional-commits.md
```

## Installation

This plugin is part of the claude-code-plugins marketplace. Install via:

```bash
claude plugin add plugin-generator --source ./plugins/plugin-generator
```

## License

MIT
