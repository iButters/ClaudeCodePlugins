# .NET Development Plugin

Expert guidance for .NET development with Domain-Driven Design, SOLID principles, and modern C# practices.

## Features

This plugin provides **auto-activating skills** that guide Claude when working with .NET code:

- **Domain-Driven Design** patterns (Aggregates, Value Objects, Domain Events)
- **SOLID principles** application
- **ASP.NET Core REST API** best practices
- **Entity Framework Core** patterns
- **Testing strategies** (Unit, Integration, API tests)
- **C# coding conventions** (naming, nullability, formatting)

## When It Activates

The skill automatically activates when you're working with:

- C# code files (`.cs`)
- .NET project files (`.csproj`, `.sln`)
- ASP.NET Core applications
- Domain-Driven Design implementations
- REST API development
- Entity Framework Core
- Unit/integration testing in .NET

## Contents

### Main Skill
- `skills/dotnet-development/SKILL.md` - Core guidelines and workflow

### Reference Documentation
- `references/ddd-patterns.md` - Aggregates, Value Objects, Domain Events, Specifications
- `references/api-patterns.md` - Validation, Error Handling, Versioning, Auth, Performance
- `references/testing-patterns.md` - Test naming, categories, mocking, coverage

## Key Patterns

### Implementation Workflow

1. **Analysis Phase** - Identify domain concepts, layers, SOLID alignment
2. **Architecture Review** - Validate aggregate boundaries, dependencies
3. **Implementation** - Apply C# best practices, async/await, DI
4. **Testing** - Write tests with `MethodName_Condition_ExpectedResult` naming

### Layer Responsibilities

| Layer | Responsibility |
|-------|---------------|
| Domain | Business logic, aggregates, value objects, domain events |
| Application | Orchestration, validation, DTOs, use cases |
| Infrastructure | Persistence, external services, repositories |
| API | HTTP endpoints, controllers, minimal APIs |

### C# Conventions

- **PascalCase**: Types, methods, public members
- **camelCase**: Private fields, local variables
- **File-scoped namespaces**
- **Nullable reference types enabled**
- **Pattern matching preferred**

## Installation

```bash
/plugin install dotnet-development@YOUR_MARKETPLACE
```

## Usage

Simply work on .NET code and the skill will automatically guide Claude with:

- Proper aggregate design
- SOLID-compliant class structure
- RESTful API patterns
- Comprehensive test strategies

## Example

When you ask Claude to implement a feature in a .NET project, it will:

1. Analyze domain concepts involved
2. Design aggregates with proper boundaries
3. Implement with DDD patterns
4. Add appropriate tests
5. Follow C# conventions throughout

## License

MIT
