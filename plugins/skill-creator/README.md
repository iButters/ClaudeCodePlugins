# skill-creator

Guided workflow for designing, implementing, and packaging high‑quality skills that extend Claude’s capabilities with specialized knowledge, workflows, and tools.

> **TL;DR:** Use this plugin when you want Claude to help you design or refine a SKILL (with SKILL.md, scripts, references, and assets) that another Claude instance can use effectively.

---

## Overview

- **Category:** Skill design, workflow engineering, developer tooling
- **Primary goal:** Help you create concise, effective, and reusable skills that encode domain knowledge, workflows, and tools for Claude.
- **Typical use cases:**
  - Designing a new skill from scratch (with SKILL.md and supporting files)
  - Updating an existing skill to be more concise, robust, or focused
  - Structuring scripts, references, and assets for a complex domain
  - Validating and packaging a skill into a distributable `.skill` file
- **Requirements:** Python environment for running the helper scripts in `scripts/`, and a project where you want to use or distribute skills.

---

## Installation

### Via Claude Code Marketplace

```bash
/plugin marketplace add <MARKETPLACE-NAME>
/plugin install skill-creator@<MARKETPLACE-NAME>
```

After installation, Claude can draw on the Skill Creator guidance whenever you ask about creating or improving skills.

### Manual script usage (optional)

If you want to use the helper scripts directly:

1. Ensure Python is installed and available on your PATH.
2. From the `plugins/skill-creator` directory, run the scripts in `scripts/` as described below.

---

## Quick Start

1. Decide what your skill should do (domain, workflows, tools).
2. Ask Claude, e.g.:

```text
Use the skill-creator guidance.
Help me design a skill for managing our internal QA workflows, including SKILL.md, scripts, and references.
```

3. Use the plugin’s recommendations to:
   - Define a clear, trigger‑oriented `description` in SKILL.md frontmatter.
   - Keep instructions concise, focusing on non‑obvious, domain‑specific knowledge.
   - Decide which scripts, references, and assets to bundle.
4. When you’re ready, use the helper scripts to initialize, validate, and package the skill.

---

## Core Concepts

### What is a Skill?

Skills are modular packages that extend Claude’s capabilities by providing:

- **Specialized workflows** – multi‑step procedures for specific domains.
- **Tool integrations** – instructions for structured interaction with files, APIs, CLIs, etc.
- **Domain expertise** – company‑ or domain‑specific knowledge and rules.
- **Bundled resources** – scripts, references, and assets for repetitive or complex tasks.

Think of a Skill as an “onboarding guide + toolkit” that makes Claude behave like a specialist in a particular area.

### Concise is Key

The plugin emphasizes:

- Keeping SKILL.md focused on what Claude truly needs to know.
- Avoiding duplication between SKILL.md and reference files.
- Preferring examples and templates over long prose where possible.

---

## Typical Workflows

### Workflow 1: Creating a new skill

1. **Define the goal and triggers**  
   Describe what the skill should do and when it should activate.
2. **Run the initializer script** (optional but recommended)  
   Use `scripts/init_skill.py` to scaffold the directory structure and a template SKILL.md.
3. **Fill in SKILL.md**  
   - Add clear `name` and `description` frontmatter.  
   - Write concise instructions and workflows in the body.
4. **Add resources**  
   - Place deterministic code in `scripts/`.  
   - Put detailed documentation in `references/`.  
   - Store any templates or assets in `assets/` (if you add such a directory).
5. **Validate and package**  
   - Run `scripts/quick_validate.py` or `scripts/package_skill.py` to check structure and content.  
   - Package to a `.skill` file for distribution.

### Workflow 2: Improving an existing skill

1. Show Claude your current SKILL.md and any important references.
2. Ask it to:
   - Reduce redundant explanations.
   - Move detailed content into references.
   - Clarify triggers and “when to use” in the `description`.
3. Apply the suggested changes and re‑run validation/packaging.

---

## Helper Scripts

The plugin ships with Python scripts to automate common tasks:

- `scripts/init_skill.py`  
  Scaffolds a new skill directory with:
  - A SKILL.md template with YAML frontmatter and TODOs
  - Example `scripts/`, `references/`, and `assets/` structure

- `scripts/quick_validate.py`  
  Performs a lightweight validation on a skill:
  - Checks YAML frontmatter, naming conventions, directory layout
  - Highlights missing or inconsistent fields

- `scripts/package_skill.py`  
  Validates and packages a skill into a `.skill` file:
  - Validates the skill (frontmatter, structure, references)
  - Produces `<skill-name>.skill` (a zip archive with `.skill` extension)

Example usage:

```bash
python scripts/init_skill.py my-new-skill --path ./skills
python scripts/quick_validate.py ./skills/my-new-skill
python scripts/package_skill.py ./skills/my-new-skill ./dist
```

---

## Directory & Project Structure

```text
plugins/skill-creator/
├─ .claude-plugin/
│  └─ plugin.json         # Plugin metadata (name, version, description, license)
├─ SKILL.md               # Main Skill Creator instructions for Claude
├─ references/            # Design patterns and workflow guidance
│  ├─ output-patterns.md  # Examples of good output formats and templates
│  └─ workflows.md        # Patterns for multi-step skill workflows
└─ scripts/               # Helper scripts for skill authors
   ├─ init_skill.py       # Initialize a new skill folder with templates
   ├─ package_skill.py    # Validate and package a skill into a .skill file
   └─ quick_validate.py   # Lightweight validation of a skill’s structure
```

`SKILL.md` contains the detailed design principles and step‑by‑step guidance that Claude follows when acting as a Skill Creator.

---

## Best Practices & Tips

- Treat the skill as something another Claude instance will read and follow; write instructions for “future Claude”, not for yourself.
- Make the `description` field in SKILL.md frontmatter explicit about:
  - What the skill does
  - When it should be used
  - Which inputs or file types are relevant
- Move dense, detailed content (schemas, policies, long examples) into `references/` and reference them from SKILL.md.
- Use scripts for repetitive or fragile operations (e.g. transformations, conversions) rather than embedding such logic in prompts.

Good prompts:
- “Using the Skill Creator guidance, help me design a skill for our internal incident response process.”
- “Review this SKILL.md and suggest how to make it more concise and effective.”

---

## Troubleshooting

- **Problem:** Skill doesn’t seem to trigger when expected.  
  **Fix:** Make the `description` frontmatter more explicit about when it should be used and what signals (file types, phrases, tasks) should trigger it.

- **Problem:** Skills feel too verbose or consume too many tokens.  
  **Fix:** Use the principles from Skill Creator to move detail into references and keep SKILL.md focused on workflows and non‑obvious knowledge.

- **Problem:** Packaging fails.  
  **Fix:** Run `scripts/quick_validate.py` to see what’s missing or inconsistent (frontmatter, naming, structure) and fix the reported issues before packaging again.

---

## Versioning, Maintenance & Compatibility

- **Current version:** `1.0.0`
- **License:** Apache‑2.0 (see `plugins/skill-creator/LICENSE.txt` and `.claude-plugin/plugin.json`).
- **Evolution:** As Anthropic’s skill design guidelines evolve, this plugin can be updated to reflect new patterns and best practices.

---

## License & Contribution

- **License:** Apache‑2.0 (Skill Creator content and scripts follow the license in `LICENSE.txt`).
- **Contributions:** You can extend the references and scripts, or adapt the patterns for your own organization’s skill libraries.
- **Support:** For questions about Skill design as a concept, refer to Anthropic’s official documentation and examples, or open issues in the repository that ships this plugin.

