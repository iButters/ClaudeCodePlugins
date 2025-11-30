# dotnet-development

Expert guidance for modern .NET development with Domain-Driven Design, SOLID principles, ASP.NET Core APIs, and testing best practices.

> **TL;DR:** Use this plugin whenever you want Claude to behave like a senior .NET architect and reviewer for C# code, projects, and APIs.

---

## Overview

- **Category:** Backend development, architecture, and testing for .NET/C#
- **Primary goal:** Help you design and implement maintainable, testable, domain-driven .NET applications.
- **Typical use cases:**
  - Reviewing and improving C# code and .NET architectures
  - Designing aggregates, bounded contexts, and domain models
  - Implementing REST APIs with ASP.NET Core and EF Core
  - Creating or improving test suites (unit, integration, API)
  - Refactoring legacy .NET projects toward modern patterns
- **Requirements:** Claude Desktop / Claude Code with this marketplace installed; any existing .NET solution (`.sln`) or project (`.csproj`) you want to work on.

---

## Installation

### Via Claude Code Marketplace

```bash
/plugin marketplace add <MARKETPLACE-NAME>
/plugin install dotnet-development@<MARKETPLACE-NAME>
```

After installation, Claude gains a dedicated `.NET Development` skill that it can activate whenever you open C#/.NET files or ask .NET-related questions.

### Manual installation (optional)

If you are using this repository directly:

1. Clone the repo containing this plugin.
2. Ensure the `dotnet-development` folder lives under your Claude marketplace `plugins/` directory.
3. Restart Claude so it can pick up the new plugin metadata from `.claude-plugin/plugin.json`.

---

## Quick Start

1. Open a .NET project in your IDE and start a Claude Code session in the repo root.
2. Describe what you want, for example:
   - “Review my domain model for the ordering context.”
   - “Help me design an aggregate for booking reservations.”
3. Paste the relevant C# files or ask Claude to inspect them (using your usual tooling).
4. Ask for a concrete output:
   - “Propose a refactored version that follows DDD and SOLID.”
   - “Design a REST API controller and minimal API endpoints for this service.”
   - “Generate a set of unit tests and integration tests for this service.”

Example prompt:

```text
Use the dotnet-development skill.
Review my `Order` aggregate and propose improvements for DDD, SOLID, and testability.
```

Claude will then apply the patterns and checklists from this plugin when suggesting designs and code.

---

## Feature Overview

- **DDD guidance:** Aggregates, entities, value objects, domain events, bounded contexts.
- **Layered architecture:** Clear separation between Domain, Application, and Infrastructure layers.
- **API patterns:** RESTful controllers and minimal APIs with proper status codes and problem details.
- **Testing strategy:** Naming conventions, test categories, mocking strategies, and coverage focus.
- **C# conventions:** Naming, formatting, nullability, async/await, dependency injection.
- **Security and robustness:** Input validation, error handling, and consistent exception patterns.

---

## Typical Workflows

### Workflow 1: Designing a new domain model

1. Describe your business domain and main entities.
2. Ask Claude to propose bounded contexts and aggregates.
3. Review the suggested domain model and iterate.
4. Let Claude generate sample aggregate classes and domain events.
5. Add tests to validate key business rules.

### Workflow 2: Building an API around an existing domain

1. Show Claude your domain layer (aggregate roots, entities, value objects).
2. Ask it to design application services around those aggregates.
3. Generate REST controllers or minimal APIs following the recommended patterns.
4. Add API tests (integration tests) and adjust infrastructure (EF Core, repositories).

### Workflow 3: Improving an existing .NET service

1. Provide Claude with one or more service classes, controllers, or repositories.
2. Ask for an analysis focusing on SOLID, separation of concerns, and testability.
3. Apply the proposed refactors (e.g., extract domain logic from controllers into aggregates).
4. Generate or refine tests to protect against regressions.

---

## Configuration

This plugin is skill-based and requires no special configuration beyond being enabled.

Example `.claude/settings.json`:

```json
{
  "enabledPlugins": [
    "dotnet-development@<MARKETPLACE-NAME>"
  ]
}
```

Claude automatically triggers the skill when:
- You work with `.cs`, `.csproj`, `.sln`, or ASP.NET Core projects.
- You describe tasks related to DDD, SOLID, REST APIs, or testing in .NET.

---

## Directory & Project Structure

```text
plugins/dotnet-development/
├─ .claude-plugin/
│  └─ plugin.json           # Plugin metadata (name, description, keywords, license)
├─ references/              # Deep-dive reference guides
│  ├─ api-patterns.md       # REST, validation, error handling, versioning
│  ├─ ddd-patterns.md       # Aggregates, bounded contexts, domain events
│  └─ testing-patterns.md   # Unit/integration testing, mocking, coverage
└─ skills/
   └─ dotnet-development/
      └─ SKILL.md           # Main .NET development skill instructions
```

The `SKILL.md` file contains the detailed workflow, examples, and checklists that Claude uses internally when acting as a .NET expert.

---

## Best Practices & Tips

- Start by explaining your domain and constraints, not just showing code.
- Ask for diagrams or conceptual models before asking for full implementations.
- Use this plugin together with code navigation tools (like Serena MCP) to target specific files and symbols.
- When refactoring, ask Claude to:
  - Propose a refactor plan.
  - Show a small, focused diff (one class or method at a time).
  - Generate tests before and after refactoring when possible.

Good prompts:
- “Given this domain description, propose aggregates and value objects.”
- “Refactor this service to follow CQRS and improve testability.”

---

## Troubleshooting

- **Problem:** Suggestions feel generic and not particularly “.NET-aware”.  
  **Fix:** Explicitly mention that Claude should use the `dotnet-development` skill and provide concrete C# files or domain descriptions.

- **Problem:** Claude mixes concerns (domain logic in controllers, etc.).  
  **Fix:** Ask it to re-check the design against the layered architecture described in the `.NET Development` skill and `ddd-patterns.md`.

- **Problem:** Not enough focus on tests.  
  **Fix:** Ask specifically for a testing plan and example test files guided by `testing-patterns.md`.

---

## Versioning, Maintenance & Compatibility

- **Current version:** `1.0.0`
- **Tested with:** Modern .NET (6+), ASP.NET Core, and C# language features.
- **Breaking changes:** See the git history or repository changelog for evolution of patterns and references.

---

## License & Contribution

- **License:** MIT (see `plugins/dotnet-development/.claude-plugin/plugin.json` and repository `LICENSE`).
- **Contributions:** Propose new patterns, examples, or corrections via pull requests or issues in the parent repository.
- **Contact/Support:** Use the issue tracker or discussions of the main Claude Code marketplace repo where this plugin is hosted.
