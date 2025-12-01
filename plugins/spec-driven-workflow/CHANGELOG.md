# Changelog

All notable changes to the spec-driven-workflow plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.3.0] - 2025-01-30

### Added

#### Security Hardening
- **Input validation** for all commands using `$ARGUMENTS`
  - Path traversal protection (rejects `../`, `..\`)
  - Character sanitization (allows only `[a-z0-9-]`)
  - Length limits (1-50 characters for project names)
  - Reserved name protection
- **Secret detection** before git commits
  - Scans for API keys, tokens, credentials, private keys
  - User confirmation required before committing potential secrets
- **Template validation** in commands that use external templates
  - Graceful fallback to inline templates if files missing

#### Checkpoint/Resume Mechanism
- **Execution checkpoints** saved to `.specs/[project]/tasks/.checkpoint`
  - JSON format with wave, timestamps, and task status
  - Automatic save before execution and after each task
- **Resume capability** with `/spec-execute --resume`
  - Recovers from interrupted executions
  - Preserves progress on failures
- **Checkpoint cleanup** on successful wave completion

#### Prompt Engineering Improvements
- **XML tags** added throughout for structured parsing:
  - `<input_validation>` - Input validation rules
  - `<prerequisites>` - Command prerequisites
  - `<template_validation>` - Template existence checks
  - `<output_format>` / `<output_error>` - Output specifications
  - `<rules>` - Command constraints
  - `<thinking_instruction>` - Chain-of-thought activation
  - `<checkpoint_handling>` - Checkpoint management
  - `<secret_detection>` - Security scanning
  - `<git_operations>` - Git workflow
  - And many more domain-specific tags
- **Extended natural language triggers** in SKILL.md
  - Bug tracking triggers
  - Feature management triggers
  - Review triggers
  - Status/progress triggers
- **Project completion criteria** with measurable checklist
- **Glossary** of terms (Wave, Subagent, EARS, etc.)

#### Robustness Improvements
- **Robust ID generation** for bugs and features
  - Regex-based ID extraction
  - Handles non-sequential IDs
  - Fallback mechanisms for parse failures
- **Duplicate detection** for bugs and features
  - Title similarity comparison
  - User prompt before creating potential duplicates
- **Error handling** for missing/corrupted files
  - Graceful degradation with warnings
  - Helpful error messages with suggestions
- **Concurrent execution warning** in user confirmation
- **HEREDOC format** for multi-line git commit messages

#### Documentation
- **CHANGELOG.md** added for version history
- **Escalation protocol** added to task-orchestrator
  - When executors should escalate
  - BLOCKED status format
- **Review conflict resolution** documented
  - Handling for 2 PASS + 1 FAIL scenarios

### Changed
- Commands now use specific Bash tool permissions (e.g., `Bash(mkdir)` instead of `Bash(mkdir:*)`)
- task-orchestrator tools list refined for security
- spec-status.md metrics calculation converted from Python pseudocode to conceptual description
- SKILL.md description expanded to include bug tracking and feature management triggers

### Fixed
- Python pseudocode in spec-status.md replaced with structured `<metrics_calculation>` section
- Template file references now validated before use
- Auto-increment ID logic made robust against non-sequential IDs

### Security
- All `$ARGUMENTS` inputs now validated and sanitized
- Path traversal attacks prevented
- Secret scanning before git operations
- Restricted Bash wildcards in agent tool definitions

## [2.2.2] - Previous Release

### Features
- Multi-agent orchestration with 9 specialized subagents
- Wave-based task execution (max 4 parallel)
- EARS notation for requirements, bugs, features
- Review pipeline (requirements, architecture, code quality)
- Git integration with --git and --git-push flags
- Bug tracking with /spec-bug commands
- Feature management with /spec-feature commands
- Wave reports generation

---

## Migration Guide

### From 2.2.x to 2.3.0

No breaking changes. New features are additive.

**Recommended actions:**
1. Review the new input validation rules
2. Test the checkpoint/resume feature with `/spec-execute --resume`
3. Note the new concurrent execution warning during execution
4. Review the project completion criteria in SKILL.md

**New files created:**
- `.specs/[project]/tasks/.checkpoint` (automatic, during execution)
- `CHANGELOG.md` (this file)

**Updated files:**
- All command files (input validation, XML tags)
- SKILL.md (triggers, completion criteria, glossary)
- task-orchestrator.md (checkpoint management, escalation protocol)
