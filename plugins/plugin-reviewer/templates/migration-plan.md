# Migration Plan Template

**Used By**: Plugin generation examples (Example 6 - Migration Assistant)
**Purpose**: Standardized format for documenting migration plans in generated plugins

---

## Migration Overview

**Source Framework**: [e.g., React Class Components]
**Target Framework**: [e.g., React Hooks]
**Migration Type**: [Full|Incremental|Selective]
**Estimated Complexity**: [Low|Medium|High|Very High]

---

## Scope Analysis

### Files in Scope
Total files to migrate: [N]

| File Path | Current Lines | Complexity Score | Priority | Estimated Effort |
|-----------|---------------|------------------|----------|------------------|
| [path/to/file.js] | [N] | [1-10] | [High\|Med\|Low] | [Hours] |
| [...] | | | | |

### Files Out of Scope
Files excluded from migration (with rationale):
- [file1.js]: Already using target framework
- [file2.js]: Third-party dependency, will be replaced

---

## Migration Phases

### Phase 1: Preparation (Estimated: [N] hours)
**Goal**: Set up infrastructure and safety checks

**Tasks**:
1. Create feature branch: `migration/[framework-name]`
2. Set up backup/rollback mechanism
3. Install target framework dependencies
4. Configure linting/type checking for new patterns
5. Create test baseline (all tests must pass)

**Success Criteria**:
- [ ] All existing tests pass
- [ ] Build succeeds without warnings
- [ ] Dependencies installed and verified

---

### Phase 2: Incremental Migration (Estimated: [N] hours)
**Goal**: Migrate files one-by-one with validation

**Approach**: [Bottom-up|Top-down|Critical-path-first]

**Iteration Pattern per File**:
1. Migrate file to target framework
2. Run targeted tests for that file
3. Run full test suite
4. Manual smoke test
5. If all pass -> commit, else -> rollback and retry

**File Order** (by dependency graph):
1. [file1] (no dependencies, leaf node)
2. [file2] (depends on file1)
3. [...]

**Success Criteria per File**:
- [ ] File compiles/transpiles successfully
- [ ] All unit tests pass
- [ ] No regression in other files
- [ ] Code review approved

---

### Phase 3: Validation (Estimated: [N] hours)
**Goal**: Comprehensive testing and quality assurance

**Validation Checklist**:
- [ ] All unit tests pass (target: 100% pass rate)
- [ ] Integration tests pass
- [ ] End-to-end tests pass
- [ ] Performance benchmarks within 10% of baseline
- [ ] No new linting errors
- [ ] Type coverage maintained or improved
- [ ] Bundle size within 5% of baseline
- [ ] Manual QA completed

**Rollback Triggers**:
- Test pass rate <95%
- Performance degradation >15%
- Critical bugs introduced
- Security vulnerabilities detected

---

### Phase 4: Cleanup (Estimated: [N] hours)
**Goal**: Remove old framework artifacts

**Tasks**:
1. Remove deprecated framework dependencies
2. Delete unused utility functions
3. Update documentation
4. Remove compatibility shims
5. Final code review

**Success Criteria**:
- [ ] No references to old framework in codebase
- [ ] Documentation updated
- [ ] README reflects new stack
- [ ] CHANGELOG updated with migration notes

---

## Risk Assessment

### High Risks
| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| [Breaking changes in core files] | High | Medium | [Comprehensive test coverage before migration] |
| [...] | | | |

### Medium Risks
| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| [...] | | | |

---

## Rollback Strategy

**Backup Locations**:
- Git branch: `backup/pre-migration-[timestamp]`
- Tagged commit: `v[version]-pre-migration`
- Local backup: `backups/[timestamp]/`

**Rollback Procedure**:
1. Identify failure point (which file/phase)
2. Revert git to last known good commit
3. Restore dependencies from package-lock backup
4. Verify rollback with full test suite
5. Document failure reason for retry

**Maximum Rollback Time**: [N] minutes

---

## Communication Plan

**Stakeholders**:
- Engineering Team: [Daily standups with migration status]
- QA Team: [Test plan review before Phase 3]
- Product Team: [Feature freeze communication]

**Status Updates**:
- Daily: Progress dashboard (files migrated / total)
- Weekly: Risk assessment update
- Blockers: Immediate escalation via [channel]

---

## Success Metrics

**Quantitative**:
- Migration completion: [N]% of files migrated
- Test coverage: Maintained at [N]%
- Performance: Within [N]% of baseline
- Bundle size: Within [N]% of baseline

**Qualitative**:
- Code maintainability improved
- Developer experience improved
- Tech debt reduced

---

**Plan Created**: [Date]
**Last Updated**: [Date]
**Plan Owner**: [Name/Team]
**Approved By**: [Name/Role]
