# Spec-Driven Workflow - GitHub Copilot Chat Edition

Transform feature ideas into structured, testable requirements using EARS (Easy Approach to Requirements Syntax) notation.

## 📋 Overview

This is the GitHub Copilot Chat version of the Spec-Driven Workflow plugin. It guides you through:
- Writing structured requirements with EARS notation
- Creating clear, testable acceptance criteria
- Covering normal flows, edge cases, and errors
- Organizing requirements by category
- Including non-functional requirements
- Ensuring every requirement is verifiable

## 🎯 EARS Notation

EARS (Easy Approach to Requirements Syntax) provides six patterns for writing clear, unambiguous requirements:

### 1. **Ubiquitous** (Always True)
```
THE [System] SHALL [behavior]
```
**Example**: THE System SHALL encrypt all passwords using bcrypt

### 2. **Event-Driven** (Triggered)
```
WHEN [event] THE [System] SHALL [response]
```
**Example**: WHEN a user submits the login form THE System SHALL validate credentials

### 3. **State-Driven** (Ongoing)
```
WHILE [state] THE [System] SHALL [behavior]
```
**Example**: WHILE the user is authenticated THE System SHALL display the dashboard

### 4. **Optional Feature**
```
WHERE [feature] THE [System] SHALL [behavior]
```
**Example**: WHERE two-factor authentication is enabled THE System SHALL require a verification code

### 5. **Error Handling**
```
IF [condition] THEN THE [System] SHALL [response]
```
**Example**: IF the password is incorrect THEN THE System SHALL display an error message

### 6. **Complex** (Combined)
```
WHILE [state] WHEN [event] THE [System] SHALL [response]
```
**Example**: WHILE the cart is not empty WHEN the user clicks checkout THE System SHALL navigate to payment

## 🚀 Installation

### Copy to Your Project

```bash
cp -r .github /path/to/your/project/
```

The instructions automatically activate when you mention requirements, specifications, or EARS notation.

## 💡 Features

### Automatic Expert Guidance

When working on requirements, GitHub Copilot automatically applies EARS notation best practices:

**Just ask**:
- "Generate requirements for user authentication"
- "Create EARS requirements for this feature"
- "Write acceptance criteria for the shopping cart"
- "What requirements do I need for password reset?"

### Requirements Engineer Chat Mode

For intensive requirements work, use the specialized chat mode:

```
@workspace use chatmode requirements-engineer
```

This mode:
- ✅ Asks clarifying questions about the feature
- ✅ Identifies functional and non-functional requirements
- ✅ Organizes requirements by category
- ✅ Writes each requirement in strict EARS notation
- ✅ Covers normal flows, edge cases, and errors
- ✅ Ensures every requirement is testable

## 📐 EARS Strict Rules

When writing requirements, MUST follow:

1. **Keywords are UPPERCASE**: WHEN, THE, SHALL, IF, THEN, WHILE, WHERE
2. **Only "SHALL"**: Never "should", "must", or "will"
3. **Never lowercase "the system"**: Always "THE System" or "THE API"
4. **One behavior per requirement**: Don't combine multiple actions
5. **Be specific**: Avoid vague terms ("appropriate", "quickly", "properly")
6. **Cover errors**: Use IF/THEN for edge cases and error scenarios
7. **Testable**: Every requirement must be verifiable

## 📝 Requirements Document Structure

Complete requirements documents include:

```markdown
# Requirements Document - [Feature Name]

## Introduction
[Brief description, purpose, business value]

## Scope
### In Scope
- [What is included]

### Out of Scope
- [What is NOT included]

## Requirements

### Functional Requirements

#### FR-1: [Category]
**Acceptance Criteria:**
1. THE System SHALL [behavior]
2. WHEN [event] THE System SHALL [response]
3. IF [error] THEN THE System SHALL [handling]

### Non-Functional Requirements

#### NFR-1: Performance
- Response times, throughput, capacity

#### NFR-2: Security
- Authentication, encryption, data protection

#### NFR-3: Reliability
- Uptime, backups, disaster recovery

## Dependencies
[External systems, prerequisites]

## Acceptance Testing
[How requirements will be validated]
```

## 🎨 Common Requirement Categories

### Authentication & Authorization
```
THE System SHALL hash passwords using bcrypt with cost factor 12
WHEN a user provides valid credentials THE System SHALL create a session token
IF the session expires THEN THE System SHALL redirect to the login page
WHERE MFA is enabled THE System SHALL require two-factor authentication
```

### Data Validation
```
THE System SHALL validate email addresses using RFC 5322 format
WHEN a user submits a form THE System SHALL validate all required fields
IF validation fails THEN THE System SHALL display specific error messages
```

### API Operations
```
THE API SHALL return JSON responses with appropriate HTTP status codes
WHEN a POST request creates a resource THE API SHALL return 201 Created
IF the request is unauthorized THEN THE API SHALL return 401 Unauthorized
```

### User Interface
```
THE UI SHALL display loading indicators during async operations
WHEN data is loading THE UI SHALL disable form submit buttons
IF an error occurs THEN THE UI SHALL display a user-friendly error message
```

### File Operations
```
THE System SHALL support file uploads up to 10MB
WHEN a file is uploaded THE System SHALL validate the file type
IF the file is invalid THEN THE System SHALL reject the upload with an error
```

## ❌ Bad vs ✅ Good Requirements

### Bad Examples (Vague, untestable)
```
❌ The system should handle errors appropriately
❌ Users must be able to login quickly
❌ The application will provide good performance
❌ Data should be stored securely
```

### Good Examples (Specific, testable, EARS format)
```
✅ IF an error occurs THEN THE System SHALL display an error message with specific details
✅ WHEN a user submits credentials THE System SHALL respond within 500ms
✅ THE System SHALL return API responses within 200ms for 1000 concurrent users
✅ THE System SHALL encrypt data at rest using AES-256
```

## 🎯 Usage Scenarios

### Scenario 1: New Feature Requirements

**You**: "I need requirements for a user profile feature where users can update their information"

**Copilot** (with this guidance): Will generate:
- Complete requirements document with EARS notation
- Organized by category (Display, Editing, Validation, etc.)
- Functional requirements with acceptance criteria
- Non-functional requirements (performance, security, usability)
- Error handling for all edge cases
- Dependencies and testing approach

### Scenario 2: Review Existing Requirements

**You**: "Review these requirements: 'Users should be able to reset their password'"

**Copilot**: Will identify issues:
- Uses "should" instead of "SHALL"
- Missing EARS pattern keywords
- Too vague (no specifics on process)
- No error handling
- No validation requirements

Then provide corrected version with proper EARS notation.

### Scenario 3: Expand Partial Requirements

**You**: "Expand this requirement: 'THE System SHALL authenticate users'"

**Copilot**: Will expand into:
- Multiple specific requirements
- Normal flow requirements
- Error handling (invalid credentials, locked accounts)
- State management (sessions, tokens)
- Non-functional requirements (performance, security)

### Scenario 4: Using Chat Mode

**You**:
```
@workspace use chatmode requirements-engineer
Generate requirements for a shopping cart feature
```

**Copilot** (in Requirements Engineer mode): Will:
1. Ask clarifying questions (payment integration? guest checkout? wishlist?)
2. Organize into categories (Cart Management, Checkout, Persistence)
3. Write complete EARS requirements for each category
4. Include non-functional requirements
5. Cover all edge cases and error scenarios
6. Provide acceptance testing approach

## 📊 Quality Checklist

Before finalizing requirements, verify:

- [ ] All keywords (WHEN, THE, SHALL, IF, THEN, WHILE, WHERE) are UPPERCASE
- [ ] Every requirement uses "SHALL" (never "should", "must", or "will")
- [ ] Each requirement is testable and specific
- [ ] Error cases are covered with IF/THEN statements
- [ ] Edge cases are addressed
- [ ] No vague terms ("appropriate", "quickly", "properly")
- [ ] Each requirement specifies a single behavior
- [ ] Requirements are organized by category
- [ ] Non-functional requirements (performance, security) are included
- [ ] Dependencies and prerequisites are listed
- [ ] Acceptance testing approach is defined

## 💡 Pro Tips

1. **Start with questions**: Ask Copilot to help you understand what requirements you need
2. **Think errors first**: Error cases often reveal missing requirements
3. **Be specific**: Provide context about the domain, users, and constraints
4. **Request examples**: "Show me EARS examples for [feature]"
5. **Iterate**: Ask Copilot to review and improve your requirements
6. **Use chat mode**: For complex features, use `requirements-engineer` chat mode
7. **Mention non-functionals**: Explicitly ask about performance, security, usability

## 🔧 Example Interactions

### Simple Generation
```
Generate EARS requirements for password reset functionality
```

### With Context
```
Create requirements for an e-commerce checkout process.
Include payment integration, address validation, and inventory checking.
Use EARS notation.
```

### Review Request
```
Review these requirements and convert to EARS format:
- Users can create accounts
- Passwords must be secure
- The system should send confirmation emails
```

### Using Chat Mode
```
@workspace use chatmode requirements-engineer
I'm building a task management app. Users need to:
- Create, edit, delete tasks
- Set due dates and priorities  
- Organize tasks into projects
- Share tasks with team members

Generate complete requirements.
```

## 📁 File Structure

```
.github/
├── copilot-instructions.md              # Main EARS guidance
├── chatmodes/
│   └── requirements-engineer.md         # Specialized requirements mode
└── README-COPILOT.md                   # This file
```

## 🆚 Differences from Claude Code Version

| Feature | Claude Code | GitHub Copilot Chat |
|---------|-------------|---------------------|
| **Commands** | `/spec-init`, `/spec-requirements` | Natural language requests |
| **Agents** | Automatic agent triggering | Chat mode activation |
| **File Creation** | Creates `.specs/` directory | Generates requirements text |
| **Workflow** | Multi-step with commands | Single request or chat mode |
| **Integration** | Claude Code IDE | VS Code, Visual Studio |

## 🚦 Getting Started

1. **Copy files to your project**:
   ```bash
   cp -r .github /path/to/your/project/
   ```

2. **Start generating requirements**:
   ```
   Generate EARS requirements for [your feature]
   ```

3. **Or use chat mode for guided process**:
   ```
   @workspace use chatmode requirements-engineer
   ```

4. **Iterate and refine**:
   ```
   Review these requirements and add error handling
   Add performance requirements for this feature
   ```

## 🐛 Troubleshooting

**Requirements don't follow EARS format**:
- Explicitly mention "using EARS notation" in your request
- Reference specific patterns: "use WHEN/THEN pattern"
- Use the requirements-engineer chat mode

**Missing error cases**:
- Ask explicitly: "Add error handling requirements"
- Mention: "Include IF/THEN statements for edge cases"

**Too vague**:
- Provide more context about the feature
- Mention specific constraints or requirements
- Ask for "specific, testable requirements"

**Want specific structure**:
- Request: "Generate a complete requirements document"
- Reference sections: "Include non-functional requirements"

## 📄 License

MIT License - Same as the original Claude Code plugin

---

**Write Better Requirements with EARS! 📋✅**
