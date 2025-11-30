# plugin-reviewer

Multi‑agent review system for Claude Code plugins, prompts, and code, based on scientifically grounded quality criteria across multiple dimensions.

> **TL;DR:** Use this plugin when you want a structured, research‑backed quality review of a plugin, prompt, or code snippet, or when you want to generate/improve a plugin to hit specific quality targets.

---

## Overview

- **Category:** Quality assurance, review, plugin generation
- **Primary goal:** Evaluate and improve Claude Code plugins and prompts along dimensions like prompt engineering, architecture, security, and technical standards.
- **Typical use cases:**
  - Reviewing an existing Claude Code plugin (SKILLs, commands, agents, references)
  - Evaluating prompt quality (action verbs, constraints, specificity)
  - Assessing security risks and vulnerability patterns in generated code
  - Optimizing few‑shot examples and chain‑of‑thought strategies
  - Generating a new plugin from high‑level requirements and validating it
- **Requirements:** Claude Code with this plugin installed; access to the plugin or content you want to review (e.g. SKILL.md, command files, code snippets).

---

## Installation

### Via Claude Code Marketplace

```bash
/plugin marketplace add <MARKETPLACE-NAME>
/plugin install plugin-reviewer@<MARKETPLACE-NAME>
```

After installation, new commands such as `/review`, `/improve-to-target`, and `/generate-plugin` become available within Claude Code.

---

## Commands

### `/review`

Run a multi‑dimensional quality analysis on a prompt, plugin file, or code.

```bash
/review [input]
/review --advisory [input]
/review --profile=standard [input]
/review --evaluators=pe,sec [input]
```

- **Automatic mode (default):** Detects content type (prompt, SKILL.md, command, code), chooses a review profile (quick, standard, comprehensive, code‑focused), and runs the appropriate evaluators.
- **Advisory mode (`--advisory`):** Recommends a review profile and evaluator set, asks you to confirm before running.
- **Profiles:** `quick`, `standard`, `comprehensive`, `code`.
- **Evaluators:** `pe` (prompt), `sec` (security), `fs` (few‑shot), `cot` (chain‑of‑thought), `arch` (architecture), `tech` (technical standards).

Output is a structured report with:
- Overall score (0–10)
- Per‑dimension scores
- Critical/Major/Minor issues
- Suggested fixes and expected score improvements
- Cross‑dimensional insights and an actionable roadmap

### `/improve-to-target`

Iteratively improve a prompt or plugin to reach a target quality score.

Typical usage:

```bash
/improve-to-target "target-score=8.5" [prompt-or-plugin-content]
```

The command:
- Runs an initial review to establish baseline score
- Identifies weakest dimensions
- Proposes improvements and rewrites
- Re‑evaluates until the target score (or limit) is reached

### `/generate-plugin`

Generate a new Claude Code plugin from high‑level requirements.

Example:

```bash
/generate-plugin "Create a plugin that helps migrate a legacy React app to React hooks and TypeScript"
```

The command:
- Asks 3–5 clarifying questions (scope, safety constraints, test needs, etc.)
- Proposes a plugin structure (skills, commands, agents, references, templates)
- Generates a complete plugin according to TIER 1–5 quality criteria
- Optionally runs an internal review pass on the generated plugin

---

## Typical Workflows

### Workflow 1: Reviewing an existing plugin

1. Collect the plugin files you want to analyze (`SKILL.md`, command files, agent specs, references).
2. Run:
   ```bash
   /review --advisory [SKILL.md or plugin folder content]
   ```
3. In advisory mode, choose the suggested profile (e.g. Standard or Comprehensive).
4. Study the report:
   - Overall score and per‑dimension scores
   - Critical and Major issues
   - Recommended changes (with estimated score improvements)
5. Apply the suggested changes to the plugin and optionally re‑run `/review` to verify improvement.

### Workflow 2: Improving a prompt to a target score

1. Provide the prompt you use for a plugin, command, or complex task.
2. Run:
   ```bash
   /improve-to-target "target-score=8.5" "your current prompt here"
   ```
3. Follow the suggested rewrites and constraints.
4. Use the improved prompt in your plugin or workflow.

### Workflow 3: Generating a new plugin

1. Describe what you want the plugin to do (domain, tasks, constraints).
2. Run:
   ```bash
   /generate-plugin "High-level description of the plugin"
   ```
3. Answer the clarifying questions about goals, safety, and environment.
4. Review the proposed plugin structure and code.
5. Optionally, call `/review` on the generated plugin to confirm quality.

---

## Architecture & Agents

The plugin uses multiple specialized agents, coordinated by orchestrators:

- **Review orchestrator:** Analyzes input, chooses review profile, configures evaluators, runs them (often in parallel), then synthesizes the final report.
- **Improvement orchestrator:** Drives iterative improvement toward a target score.
- **Specialized evaluators:**  
  - Prompt engineering evaluator  
  - Architecture and plugin‑architecture evaluators  
  - Few‑shot evaluator  
  - Chain‑of‑thought evaluator  
  - Security evaluator (OWASP/CWE patterns)  
  - Technical standards evaluator  

Each evaluator focuses on a subset of scientifically validated quality dimensions and returns scores, issues, and recommendations.

---

## Configuration

No mandatory configuration beyond enabling the plugin.

Example `.claude/settings.json`:

```json
{
  "enabledPlugins": [
    "plugin-reviewer@<MARKETPLACE-NAME>"
  ]
}
```

Internally, the plugin uses:
- Research‑backed scoring scales (0–10)
- Timeouts and execution limits per evaluator
- Profiles that control which evaluators run and how long they can run

---

## Directory & Project Structure

```text
plugins/plugin-reviewer/
├─ .claude-plugin/
│  └─ plugin.json                 # Plugin metadata (name, version, description, keywords, license)
├─ agents/                        # Specialized reviewer and orchestrator agents
│  ├─ architecture-evaluator.md
│  ├─ plugin-architecture-evaluator.md
│  ├─ prompt-engineering-evaluator.md
│  ├─ security-evaluator.md
│  ├─ few-shot-evaluator.md
│  ├─ cot-evaluator.md
│  ├─ technical-standards-evaluator.md
│  └─ review-orchestrator.md
├─ commands/                      # Entry points for users
│  ├─ review.md                   # Main multi-dimensional review command
│  ├─ improve-to-target.md        # Target-score improvement command
│  └─ generate-plugin.md          # Plugin generation command
├─ references/
│  ├─ quality-framework.md        # Quality dimensions, scoring, research basis
│  ├─ cot-strategies.md           # Chain-of-thought related strategies
│  ├─ few-shot-optimization.md    # Example ordering and few-shot design
│  └─ vulnerability-patterns.md   # Common security pitfalls and mitigation patterns
└─ skills/
   └─ plugin-reviewer/
      └─ SKILL.md                 # Core skill defining behavior and quality framework
```

The `SKILL.md` file contains the TIER 1–5 quality framework, research citations, and detailed rules used by the agents and commands.

---

## Best Practices & Tips

- Use `/review` on SKILL.md and command files before sharing a plugin with others.
- Combine `/review` with `/improve-to-target` to gradually push an existing plugin toward higher quality.
- When generating a new plugin, answer clarifying questions concretely—this directly improves the resulting design.
- Use the per‑dimension sections of the report as a checklist when editing your plugin or prompt.

Good prompts:
- “Review this SKILL.md for a Claude plugin and propose specific improvements to reach at least 8.5/10 overall.”
- “Help me design a plugin for X; then generate it and run a review to validate quality.”

---

## Troubleshooting

- **Problem:** Review takes too long or feels overkill.  
  **Fix:** Use `/review --profile=quick [input]` for a lighter pass or narrow the evaluator set via `--evaluators=pe,sec`.

- **Problem:** Results seem generic.  
  **Fix:** Provide the full context (SKILL.md, key commands, and any example prompts) and specify what you care about most (e.g. “focus on security”).

- **Problem:** It suggests changes but doesn’t show concrete rewrites.  
  **Fix:** Ask explicitly for “rewritten SKILL.md sections” or “revised prompt text” and/or use `/improve-to-target`.

---

## Versioning, Maintenance & Compatibility

- **Current version:** `1.4.0`
- **Focus:** Claude Code plugin ecosystem, prompt engineering, and code generation workflows.
- **Breaking changes:** See repository history or a future `CHANGELOG.md` for details as the quality framework evolves.

---

## License & Contribution

- **License:** MIT (see `plugins/plugin-reviewer/.claude-plugin/plugin.json` and repo `LICENSE`).
- **Contributions:** You can propose new evaluators, dimensions, or research‑based improvements by contributing to this plugin’s repository.
- **Contact/Support:** Use the issue tracker or discussions of the main Claude Code marketplace repo that includes this plugin.

