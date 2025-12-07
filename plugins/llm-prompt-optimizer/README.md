# LLM Prompt Optimizer

A comprehensive Claude Code plugin for prompt engineering across multiple LLM models. Optimize prompts, create new ones from scratch, and get model recommendations through interactive dialog.

## Supported Models

- **Claude Opus 4.5** - Complex reasoning, creative excellence
- **Claude Sonnet 4.5** - Balanced quality/speed, agentic coding
- **Claude Haiku 4.5** - Fast, cost-effective, simple tasks
- **GPT 5.1** - General-purpose, function calling, JSON mode
- **GPT 5.1 Codex** - Code-specialized variant
- **Gemini Pro 3.0** - Multimodal, context caching

## Features

### Commands

| Command | Description |
|---------|-------------|
| `/optimize-prompt` | Analyze and improve an existing prompt |
| `/create-prompt` | Create a new prompt from requirements |
| `/recommend-model` | Get model recommendations for your use case |
| `/analyze-prompt` | Get detailed prompt analysis without modifications |

### Agents

| Agent | Trigger Phrases |
|-------|-----------------|
| `prompt-optimizer` | "optimize this prompt", "improve prompt", "fix my prompt" |
| `prompt-architect` | "create a prompt for", "design a prompt", "build a prompt" |
| `model-recommender` | "which model should I use", "recommend a model", "GPT vs Claude" |

### Skill

The `prompt-engineer` skill provides deep knowledge about:
- 6 core prompt engineering techniques
- Model-specific optimizations for all 6 supported models
- Optimization checklists and troubleshooting guides
- Real-world prompt examples across categories

## Installation

Add this plugin to your Claude Code project:

```bash
# From project root
cp -r llm-prompt-optimizer ~/.claude/plugins/
```

Or add the path to your `.claude/plugins` configuration.

## Usage Examples

### Optimize an Existing Prompt

```
/optimize-prompt
```

Then paste your prompt or provide a file path. The optimizer will:
1. Analyze your prompt against quality criteria
2. Identify issues and missing techniques
3. Apply model-specific optimizations
4. Deliver an improved version with explanations

### Create a New Prompt

```
/create-prompt
```

Answer a few questions about your task, and receive:
- A complete, ready-to-use prompt
- Technique explanations
- Usage instructions
- Testing recommendations

### Get Model Recommendations

```
/recommend-model
```

Through interactive dialog, describe your:
- Task type (code, analysis, creative, etc.)
- Priority (speed, quality, cost, balance)
- Context size needs
- Special requirements

Receive ranked model recommendations with trade-offs.

### Analyze Without Changing

```
/analyze-prompt
```

Get a detailed quality report including:
- Score breakdown (clarity, context, structure, etc.)
- Strengths and weaknesses
- Missing techniques
- Model-specific observations

## Prompt Engineering Techniques

The plugin teaches and applies these core techniques:

| Technique | Best For |
|-----------|----------|
| **XML Tags** | Structured prompts with 3+ components |
| **Role Prompting** | Tasks requiring domain expertise |
| **Clear & Direct** | All prompts (baseline technique) |
| **Multishot Prompting** | Format consistency, style matching |
| **Chain of Thought** | Complex reasoning, accuracy |
| **Prompt Chaining** | Multi-stage workflows |

## Model Selection Guide

Quick reference for model selection:

| Use Case | Recommended Model |
|----------|-------------------|
| Agentic coding | Claude Sonnet 4.5 |
| Complex research | Claude Opus 4.5 |
| High-volume processing | Claude Haiku 4.5 |
| Function calling | GPT 5.1 |
| Code generation | GPT 5.1 Codex or Sonnet 4.5 |
| Multimodal tasks | Gemini Pro 3.0 or Opus 4.5 |
| Context caching | Gemini Pro 3.0 |

## Directory Structure

```
llm-prompt-optimizer/
├── .claude-plugin/
│   └── plugin.json
├── agents/
│   ├── model-recommender.md
│   ├── prompt-architect.md
│   └── prompt-optimizer.md
├── commands/
│   ├── analyze-prompt.md
│   ├── create-prompt.md
│   ├── optimize-prompt.md
│   └── recommend-model.md
├── skills/
│   └── prompt-engineer/
│       ├── SKILL.md
│       ├── examples/
│       │   ├── analysis-prompts.md
│       │   ├── classification-prompts.md
│       │   ├── code-generation-prompts.md
│       │   ├── complex-workflow-prompts.md
│       │   └── creative-prompts.md
│       └── reference/
│           ├── comparisons/
│           ├── models/
│           ├── optimization/
│           └── techniques/
└── README.md
```

## License

MIT
