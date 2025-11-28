# Implementation Plan

## Overview

**Project:** [PROJECT_NAME]
**Total Tasks:** [TOTAL]
**Waves:** [WAVE_COUNT]
**Created:** [DATE]
**Last Updated:** [DATE]

## Progress

| Wave | Description | Total | ✅ | 🔄 | ⬜ | ❌ |
|------|-------------|-------|----|----|----|----|
| 1 | Foundation | 0 | 0 | 0 | 0 | 0 |
| 2 | Core Features | 0 | 0 | 0 | 0 | 0 |
| 3 | Integration | 0 | 0 | 0 | 0 | 0 |

**Overall Progress:** 0/[TOTAL] (0%)

```
[░░░░░░░░░░░░░░░░░░░░] 0%
```

## Dependency Graph

```
Wave 1: T1, T2, T3 (parallel, no dependencies)
    ↓
Wave 2: T4, T5, T6 (parallel, depends on Wave 1)
    ↓
Wave 3: T7, T8 (parallel, depends on Wave 2)
```

## Wave Files

| Wave | File | Status | Tasks |
|------|------|--------|-------|
| 1 | [wave-1.md](wave-1.md) | ⬜ Pending | T1, T2, T3 |
| 2 | [wave-2.md](wave-2.md) | ⬜ Blocked | T4, T5, T6 |
| 3 | [wave-3.md](wave-3.md) | ⬜ Blocked | T7, T8 |

## Task Index

| ID | Task | Type | Wave | Status | Effort |
|----|------|------|------|--------|--------|
| T1 | [Task Name] | database | 1 | ⬜ | M |
| T2 | [Task Name] | backend | 1 | ⬜ | L |
| T3 | [Task Name] | frontend | 1 | ⬜ | M |
| T4 | [Task Name] | backend | 2 | ⬜ | L |
| T5 | [Task Name] | frontend | 2 | ⬜ | M |
| T6 | [Task Name] | test | 2 | ⬜ | S |
| T7 | [Task Name] | backend | 3 | ⬜ | L |
| T8 | [Task Name] | docs | 3 | ⬜ | S |

## Requirements Traceability

| Requirement | Tasks | Status |
|-------------|-------|--------|
| R1 | T1, T4, T7 | ⬜ |
| R2 | T2, T5, T7 | ⬜ |
| R3 | T3, T5, T8 | ⬜ |

## Effort Summary

| Size | Count | Description |
|------|-------|-------------|
| S | 0 | < 1 hour |
| M | 0 | 1-4 hours |
| L | 0 | 4-8 hours |
| XL | 0 | 1-2 days |

**Total Estimated Effort:** [X] hours

## Execution Notes

- Maximum 4 parallel tasks per wave (token budget)
- Review required after each task completion
- Update this index after any status change
- Wave N+1 blocked until Wave N complete

## Quick Commands

```
/spec-status              # View current progress
/spec-execute             # Execute next pending wave
/spec-execute wave 2      # Execute specific wave
/spec-execute T5          # Execute specific task
/spec-review T5           # Review specific task
```
