# Validation Checklist Template

**Used By**: Plugin generation examples (Example 6 - Migration Assistant)
**Purpose**: Comprehensive quality validation checklist for generated plugins and migrated code

---

## Validation Checklist for: [Plugin/Feature Name]

**Validation Date**: [Date]
**Validator**: [Name]
**Version/Commit**: [Hash or Version Number]
**Environment**: [Development|Staging|Production]

---

## 1. Functional Validation

### Core Functionality
- [ ] All primary features work as specified
- [ ] All user-facing commands execute successfully
- [ ] All agent delegations complete within timeout
- [ ] Output format matches specifications

### Feature Completeness
- [ ] All requirements from specification implemented
- [ ] All acceptance criteria met
- [ ] All user stories satisfied
- [ ] No critical features missing

### Regression Testing
- [ ] All previously working features still work
- [ ] No unintended behavior changes
- [ ] Backward compatibility maintained (if required)

**Notes**:
```
[Document any functional issues found]
```

---

## 2. Code Quality

### TIER 1: Prompt Engineering (for plugins)
- [ ] All instructions use specific action verbs (Analyze, Create, Review, etc.)
- [ ] Target specificity ≥8/10 (specific file/function references)
- [ ] All 5 constraint categories defined (Performance, Scope, Format, Complexity, Domain)
- [ ] Output format specified with schema
- [ ] Success criteria measurable and objective

**Score**: [X/10]

### TIER 2: Claude-Specific Optimization
- [ ] XML tags properly structured (<role>, <capabilities>, <constraints>, etc.)
- [ ] Chain-of-thought decomposition appropriate for complexity
  - Simple tasks: 2-3 steps
  - Medium: 3-5 steps
  - Complex: 5-7 steps
  - Very complex: 7-9 steps
- [ ] Few-shot examples follow PERO ordering (Easy → Medium → Hard)
- [ ] Example count appropriate for task type (Code gen: 4-6, Analysis: 3-4)

**Score**: [X/10]

### Code Standards (for generated code)
- [ ] Follows language-specific style guide (PEP 8, ESLint, etc.)
- [ ] No linting errors
- [ ] No compiler warnings
- [ ] Proper indentation and formatting
- [ ] Meaningful variable/function names
- [ ] Adequate code comments where needed
- [ ] No dead code or unused imports

**Linting Report**:
```
[Paste linting results]
```

---

## 3. Security Validation

### OWASP Top-5 for LLM-Generated Code
- [ ] **CWE-89 (SQL Injection)**: All database queries use parameterized queries
- [ ] **CWE-78 (Command Injection)**: No user input in shell commands, use subprocess.run() with array
- [ ] **CWE-22 (Path Traversal)**: File paths validated against directory traversal attacks
- [ ] **CWE-338 (Weak Random)**: Cryptographic random (secrets module) for security-sensitive operations
- [ ] **CWE-327 (Weak Crypto)**: No MD5/SHA1 for passwords, use bcrypt/argon2

### Input Validation
- [ ] All user input validated
- [ ] Type checking enforced
- [ ] Range checking where applicable
- [ ] Sanitization for special characters
- [ ] XSS prevention (for web output)

### Authentication & Authorization
- [ ] Authentication implemented correctly
- [ ] Authorization checks in place
- [ ] Session management secure
- [ ] No hardcoded credentials
- [ ] API keys stored securely (environment variables)

### Data Protection
- [ ] Sensitive data encrypted at rest
- [ ] Sensitive data encrypted in transit (HTTPS/TLS)
- [ ] No sensitive data in logs
- [ ] PII handling compliant with regulations

**Security Score**: [Pass/Fail]
**Critical Vulnerabilities**: [N]
**Major Vulnerabilities**: [N]

---

## 4. Performance Validation

### Response Time
- [ ] Average response time ≤ [N ms]
- [ ] P95 response time ≤ [N ms]
- [ ] P99 response time ≤ [N ms]
- [ ] No timeouts under normal load

### Resource Usage
- [ ] Memory usage ≤ [N MB] steady state
- [ ] CPU usage ≤ [N%] average
- [ ] Disk I/O within acceptable range
- [ ] Network bandwidth efficient

### Scalability
- [ ] Handles expected load (concurrent users/requests)
- [ ] Degrades gracefully under overload
- [ ] No memory leaks detected
- [ ] Connection pooling optimized

**Performance Benchmarks**:
```
Test 1: [Description]
- Result: [N ms]
- Target: [N ms]
- Status: [Pass/Fail]

Test 2: [...]
```

---

## 5. Test Coverage

### Unit Tests
- [ ] Statement coverage ≥ 80%
- [ ] Branch coverage ≥ 75%
- [ ] Function coverage ≥ 90%
- [ ] All tests pass

### Integration Tests
- [ ] All integration points tested
- [ ] API contracts verified
- [ ] Database interactions tested
- [ ] All tests pass

### End-to-End Tests
- [ ] Critical user flows tested
- [ ] Error scenarios tested
- [ ] All tests pass

**Coverage Report**:
```
Statements: [X]%
Branches: [X]%
Functions: [X]%
Lines: [X]%
```

---

## 6. Documentation Validation

### Code Documentation
- [ ] README.md present and complete
- [ ] Installation instructions clear
- [ ] Usage examples provided
- [ ] API documentation complete (if applicable)
- [ ] Inline code comments where needed

### Plugin-Specific Documentation
- [ ] SKILL.md follows YAML frontmatter format
- [ ] All commands documented with examples
- [ ] All agents have proper role definitions
- [ ] Cross-references valid (all mentioned files exist)
- [ ] No broken links

### User Documentation
- [ ] User guide available
- [ ] Common errors documented
- [ ] FAQ section (if needed)
- [ ] Troubleshooting guide

**Documentation Score**: [Complete/Partial/Incomplete]

---

## 7. Architecture Validation

### TIER 3: Plugin Architecture (for plugins)
- [ ] File structure follows conventions
  - skills/[name]/SKILL.md
  - commands/[name].md
  - agents/[name].md
  - references/[name].md
- [ ] Header hierarchy valid (no skipped levels)
- [ ] Cross-file references correct
- [ ] Command structure consistent
- [ ] Agent delegation rules clear

### Design Patterns
- [ ] Appropriate design patterns used
- [ ] Separation of concerns maintained
- [ ] DRY principle followed
- [ ] SOLID principles respected (if OOP)
- [ ] No circular dependencies

### Scalability
- [ ] Architecture supports future growth
- [ ] Modular and extensible
- [ ] Configuration externalized
- [ ] No hard-coded limits

**Architecture Score**: [X/10]

---

## 8. Dependencies Validation

### Dependency Security
- [ ] No known security vulnerabilities (npm audit / safety check)
- [ ] All dependencies up to date (or outdated ones documented)
- [ ] License compatibility verified
- [ ] No unnecessary dependencies

### Dependency Management
- [ ] Lock file present (package-lock.json, Pipfile.lock, etc.)
- [ ] Version pinning appropriate
- [ ] Peer dependencies satisfied
- [ ] Dev dependencies separated from production

**Vulnerability Scan**:
```bash
npm audit
# or
safety check
```

---

## 9. Build & Deployment

### Build Process
- [ ] Clean build succeeds without errors
- [ ] Build produces expected artifacts
- [ ] Build time acceptable (< [N] minutes)
- [ ] Source maps generated (if applicable)

### Deployment Readiness
- [ ] Environment variables documented
- [ ] Configuration templates provided
- [ ] Database migrations ready (if applicable)
- [ ] Rollback procedure documented

### CI/CD Pipeline
- [ ] All CI checks pass
- [ ] Automated tests run successfully
- [ ] Static analysis passes
- [ ] Docker image builds (if containerized)

**Build Status**: [Pass/Fail]

---

## 10. Compliance & Standards

### TIER 4: Technical Standards (for plugins)
- [ ] UTF-8 encoding without BOM
- [ ] LF line endings (Unix-style)
- [ ] Files ≤ 500 lines
- [ ] Model configuration specified where needed

### Industry Standards
- [ ] Follows relevant industry standards (REST, OAuth, etc.)
- [ ] Accessibility standards met (if applicable - WCAG)
- [ ] Internationalization support (if required)
- [ ] Data privacy regulations complied with (GDPR, CCPA)

### Internal Standards
- [ ] Coding standards followed
- [ ] Naming conventions consistent
- [ ] Commit message format followed
- [ ] PR template used

**Compliance Status**: [Compliant/Non-Compliant]

---

## Overall Assessment

### Validation Summary

| Category | Status | Score | Blocker Issues |
|----------|--------|-------|----------------|
| Functional | [Pass/Fail] | - | [N] |
| Code Quality | [Pass/Fail] | [X/10] | [N] |
| Security | [Pass/Fail] | - | [N] |
| Performance | [Pass/Fail] | - | [N] |
| Tests | [Pass/Fail] | [X%] | [N] |
| Documentation | [Pass/Fail] | - | [N] |
| Architecture | [Pass/Fail] | [X/10] | [N] |
| Dependencies | [Pass/Fail] | - | [N] |
| Build/Deploy | [Pass/Fail] | - | [N] |
| Compliance | [Pass/Fail] | - | [N] |

**Overall Status**: [Ready for Production / Needs Revision / Blocked]

**Overall Quality Score**: [X.X/10]

---

## Critical Issues (Must Fix Before Production)

1. **[Issue Title]**
   - Category: [Functional/Security/Performance/etc.]
   - Severity: CRITICAL
   - Description: [...]
   - Impact: [...]
   - Recommended Fix: [...]

---

## Major Issues (Should Fix)

1. **[Issue Title]**
   - Category: [...]
   - Severity: MAJOR
   - Description: [...]
   - Impact: [...]
   - Recommended Fix: [...]

---

## Minor Issues (Nice to Have)

1. **[Issue Title]**
   - Category: [...]
   - Severity: MINOR
   - Description: [...]
   - Impact: [...]
   - Recommended Fix: [...]

---

## Recommendations

**For Immediate Action**:
1. [...]
2. [...]

**For Future Iterations**:
1. [...]
2. [...]

---

## Sign-Off

**Validated By**: [Name]
**Role**: [Title]
**Date**: [Date]
**Signature**: [Digital Signature or Approval Link]

**Status**: [Approved for Production / Conditional Approval / Rejected]

---

**Checklist Version**: 1.0
**Last Updated**: [Date]
**Based On**: TIER 1-5 Quality Framework, OWASP 2024, CWE Top-5
