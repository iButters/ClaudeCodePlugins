# GPT 5.1 Codex Optimization Guide

## Overview

GPT 5.1 Codex is OpenAI's code-specialized model variant, optimized for code generation, understanding, debugging, and transformation tasks. It excels at producing high-quality code across multiple programming languages.

## Capabilities

### Strengths

| Capability | Rating | Notes |
|------------|--------|-------|
| Code Generation | Excellent | Multiple languages |
| Code Understanding | Excellent | Complex codebases |
| Debugging | High | Identifies issues effectively |
| Code Completion | Excellent | Context-aware suggestions |
| Language Coverage | Broad | Python, JS, TS, Go, Rust, etc. |
| API Integration | High | Standard OpenAI API |

### Ideal Use Cases

- Code generation from requirements
- Code completion and suggestions
- Bug identification and fixes
- Code refactoring
- Test generation
- Documentation generation
- Code translation between languages
- Algorithm implementation

### When NOT to Use Codex

- Non-code tasks (use GPT 5.1)
- Complex architectural decisions (consider Claude Opus)
- Extended agentic coding sessions (consider Claude Sonnet)
- Tasks requiring deep reasoning beyond code

## Key Optimizations

### 1. Clear Context and Requirements

Provide complete context for the code task:

```
Language: Python 3.11
Framework: FastAPI
Task: Create an endpoint for user authentication

Requirements:
- Accept email and password in request body
- Validate input using Pydantic
- Check credentials against database
- Return JWT token on success
- Return appropriate error on failure

Existing patterns in codebase:
- Use SQLAlchemy for DB access
- JWT tokens use HS256 algorithm
- Error responses use standard ErrorResponse model
```

### 2. Specify Language and Framework

Always be explicit about the technology stack:

```
# Good: Explicit specification
Language: TypeScript
Runtime: Node.js 20
Framework: Express.js
Database: PostgreSQL with Prisma ORM

# Bad: Vague
Write some backend code to handle users.
```

### 3. Provide Type Information

Include type signatures and interfaces:

```typescript
// Provide this context:
interface User {
  id: string;
  email: string;
  name: string;
  createdAt: Date;
}

interface CreateUserInput {
  email: string;
  password: string;
  name: string;
}

// Then request:
Implement the createUser function that takes CreateUserInput
and returns Promise<User>. Include validation and error handling.
```

### 4. Show Existing Patterns

Reference existing code patterns:

```
Existing validation pattern in the codebase:

```python
def validate_email(email: str) -> str:
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        raise ValidationError("Invalid email format")
    return email.lower()
```

Follow this pattern to implement validate_phone().
```

### 5. Request Specific Output

Be clear about what you want:

```
Generate:
1. The function implementation
2. Type hints for all parameters and return value
3. Docstring with usage examples
4. Unit tests (using pytest)

Do NOT include:
- Unnecessary imports (assume standard library available)
- Verbose comments for obvious code
- Alternative implementations
```

### 6. Include Test Cases

Provide test cases for better code generation:

```
Implement a function that:
- Takes a list of integers
- Returns the longest increasing subsequence

Test cases:
- [10, 9, 2, 5, 3, 7, 101, 18] → [2, 3, 7, 101] (length 4)
- [0, 1, 0, 3, 2, 3] → [0, 1, 2, 3] (length 4)
- [7, 7, 7, 7] → [7] (length 1)
```

## Prompt Patterns for Codex

### Code Generation

```
Language: [Language]
Framework: [Framework if applicable]

Task:
[Clear description of what to implement]

Requirements:
1. [Requirement 1]
2. [Requirement 2]
3. [Requirement 3]

Constraints:
- [Constraint 1]
- [Constraint 2]

Example usage:
```
[How the code should be used]
```
```

### Debugging

```
Language: [Language]

The following code has a bug:
```[language]
[Code with bug]
```

Expected behavior:
[What it should do]

Actual behavior:
[What it actually does / error message]

Identify the bug and provide the corrected code.
```

### Code Review

```
Review this code for:
- Bugs and logic errors
- Performance issues
- Security vulnerabilities
- Best practice violations
- Missing error handling

```[language]
[Code to review]
```

Provide specific line numbers and recommendations for each issue.
```

### Refactoring

```
Refactor this code to:
- [Goal 1: e.g., improve readability]
- [Goal 2: e.g., reduce complexity]
- [Goal 3: e.g., add type hints]

Original code:
```[language]
[Code to refactor]
```

Maintain the same functionality. Explain changes made.
```

### Test Generation

```
Generate comprehensive tests for:

```[language]
[Function or class to test]
```

Requirements:
- Use [testing framework: pytest/jest/etc.]
- Cover happy path
- Cover edge cases
- Cover error conditions
- Include boundary tests

Expected test file structure:
- Descriptive test names
- Arrange-Act-Assert pattern
- Minimal setup/fixtures
```

### Documentation

```
Generate documentation for:

```[language]
[Code to document]
```

Include:
- Module/function docstrings
- Parameter descriptions with types
- Return value descriptions
- Usage examples
- Edge case notes
```

## Language-Specific Tips

### Python

```
Use modern Python features:
- Type hints (Python 3.9+ syntax)
- Dataclasses or Pydantic models
- asyncio for I/O operations
- Context managers where appropriate

Follow PEP 8 conventions.
```

### TypeScript

```
Use strict TypeScript:
- Explicit types, avoid 'any'
- Interfaces for data structures
- Proper error types
- Async/await over callbacks

Follow project tsconfig.json settings.
```

### JavaScript

```
Use modern ES features:
- const/let, no var
- Arrow functions for callbacks
- Destructuring where cleaner
- Optional chaining (?.)
- Nullish coalescing (??)
```

### Go

```
Follow Go conventions:
- Effective Go guidelines
- Error wrapping with context
- Interface-based design
- Standard project layout
```

## Comparison with Claude Sonnet

| Aspect | GPT 5.1 Codex | Claude Sonnet 4.5 |
|--------|--------------|------------------|
| Code generation | Excellent | Excellent |
| Multi-file work | Good | Excellent |
| Agentic coding | Good | Excellent |
| Context length | 128K | 200K |
| Tool integration | Function calling | Native tools |
| Long sessions | Good | Excellent |

**Choose Codex when:**
- Focused code generation tasks
- OpenAI ecosystem integration
- Standard code completion needs
- Shorter, bounded tasks

**Choose Claude Sonnet when:**
- Extended agentic sessions
- Multi-file refactoring
- Complex codebase navigation
- Long-running development tasks

## Cost and Performance

| Metric | Value |
|--------|-------|
| Context Window | 128K tokens |
| Speed | Fast |
| Code Quality | High |
| Language Coverage | Broad |

## Common Mistakes

### 1. Insufficient Context

```
# Bad: Missing context
Write a sorting function.

# Good: Full context
Language: Python 3.11
Write a function that sorts a list of dictionaries by a specified key.
Support ascending and descending order.
Include type hints and handle the case where the key doesn't exist.
```

### 2. Vague Requirements

```
# Bad
Make this code better.

# Good
Refactor this code to:
1. Reduce cyclomatic complexity (currently 15, target <10)
2. Extract repeated logic into helper functions
3. Add comprehensive error handling
4. Improve variable names for clarity
```

### 3. Missing Language Specification

```
# Bad
Write a function to validate email.

# Good
Language: TypeScript
Runtime: Node.js
Write a function validateEmail(email: string): boolean
that validates email format using a regex pattern.
Include JSDoc comments.
```

### 4. Not Providing Examples

```
# Better results with examples
Implement a rate limiter that:
- Allows 100 requests per minute per user
- Uses sliding window algorithm

Example behavior:
- User makes 100 requests in first 30 seconds: all allowed
- User makes request at 31 seconds: blocked
- User makes request at 61 seconds: allowed (window slides)
```

## Quick Reference

**Optimize Codex by:**
- Specifying language and framework explicitly
- Providing type information and interfaces
- Including test cases and examples
- Showing existing code patterns
- Being specific about output requirements
- Including relevant context only

**Avoid:**
- Vague task descriptions
- Missing language/framework info
- Assuming context is understood
- Requesting too many things at once
- Ignoring type safety

## Summary

GPT 5.1 Codex excels at focused code generation tasks. Optimize by:
1. Always specify language, framework, and version
2. Provide complete context and requirements
3. Include type information and interfaces
4. Show existing patterns to follow
5. Provide test cases for better results
6. Be specific about output format

Use Codex for code generation, completion, debugging, and focused development tasks where you need high-quality code output.
