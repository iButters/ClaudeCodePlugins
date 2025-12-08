# LLM Prompt Optimizer - GitHub Copilot Chat Edition

A comprehensive GitHub Copilot Chat extension for prompt engineering across multiple LLM models. Optimize prompts, analyze quality, and get expert model recommendations.

## 📋 Overview

This is the GitHub Copilot Chat version of the LLM Prompt Optimizer plugin. It provides expert guidance for:
- Analyzing prompt quality with detailed scoring
- Optimizing existing prompts for better performance
- Recommending the best LLM model for your specific use case
- Applying model-specific optimizations

## 🎯 Supported Models

- **Claude Opus 4.5** - Complex reasoning, creative excellence (200K context)
- **Claude Sonnet 4.5** - Balanced quality/speed, agentic coding (200K context)
- **Claude Haiku 4.5** - Fast, cost-effective, simple tasks (200K context)
- **GPT 5.1** - General-purpose, function calling, JSON mode (128K context)
- **GPT 5.1 Codex** - Code-specialized variant (128K context)
- **Gemini Pro 3.0** - Multimodal, context caching (2M context)

## 🚀 Installation

### Option 1: Copy to Your Repository

Copy the `.github` directory to your repository:

```bash
cp -r .github /path/to/your/project/
```

### Option 2: Use as Template

Use this as a template for your own prompt engineering workflows.

## 💡 Features

### 1. **Repository-Wide Prompt Engineering Guidance**

The main `.github/copilot-instructions.md` file provides comprehensive prompt engineering knowledge that's automatically available in all Copilot Chat conversations within this repository.

**Automatic activation** - No special commands needed! Just start chatting with Copilot about:
- "How can I improve this prompt?"
- "Which LLM model should I use for this task?"
- "Analyze the quality of this prompt"

### 2. **Specialized Chat Modes**

Three expert chat modes for specific tasks:

#### **Prompt Optimizer** (`@workspace /chatmode prompt-optimizer`)
Systematically improves existing prompts:
- Analyzes current quality with scoring (0-100)
- Identifies specific weaknesses by severity
- Applies appropriate prompt engineering techniques
- Adds model-specific optimizations
- Explains all changes with rationale

**When to use**: When you have a prompt that needs improvement or isn't performing well.

**Example**:
```
@workspace use chatmode prompt-optimizer
I have this prompt that gives inconsistent results: "Summarize the document"
```

#### **Prompt Analyzer** (`@workspace /chatmode prompt-analyzer`)
Evaluates prompt quality without modification:
- Provides detailed quality scoring across 6 criteria
- Identifies strengths and weaknesses
- Suggests improvements (without implementing)
- Detects missing techniques
- Categorizes issues by severity

**When to use**: When you want to understand prompt quality or get a diagnostic report.

**Example**:
```
@workspace use chatmode prompt-analyzer
Analyze this prompt: "Write a function to process user data from CSV"
```

#### **Model Recommender** (`@workspace /chatmode model-recommender`)
Helps choose the optimal LLM model:
- Gathers requirements systematically
- Scores models against your specific needs
- Provides top 3 recommendations with trade-offs
- Includes cost estimates
- Offers clear decision guidance

**When to use**: When choosing which LLM model to use for a task.

**Example**:
```
@workspace use chatmode model-recommender
I need to process thousands of customer support tickets daily for categorization
```

## 📚 Prompt Engineering Techniques

The system teaches and applies these core techniques:

### 1. **XML Tags** (Structured Prompts)
Use XML-style tags for prompts with 3+ components:
```xml
<role>You are an expert developer</role>
<task>Create a Python function</task>
<requirements>
- Validate input
- Handle errors
</requirements>
```

### 2. **Role Prompting**
Assign specific expertise:
```
You are a senior software architect with expertise in distributed systems...
```

### 3. **Be Clear and Direct**
State tasks explicitly, use precise language, specify exact outputs.

### 4. **Multishot Prompting**
Provide 2-5 examples demonstrating format and style.

### 5. **Chain of Thought**
Request step-by-step reasoning:
```
Let's think through this step by step...
Show your reasoning before the final answer...
```

### 6. **Prompt Chaining**
Break complex tasks into sequential prompts where each output feeds the next.

## 📊 Prompt Quality Scoring

All prompts are evaluated on a 0-100 scale across:

| Category | Points | Evaluates |
|----------|--------|-----------|
| **Clarity** | 25 | Task explicit? Instructions unambiguous? |
| **Context** | 20 | Background provided? Domain clear? |
| **Structure** | 20 | Well-organized? Logical? XML tags? |
| **Output Spec** | 15 | Format specified? Length expectations? |
| **Techniques** | 10 | Appropriate techniques applied? |
| **Model Fit** | 10 | Right model? Model-specific optimizations? |

**Score Interpretation**:
- **90-100**: Excellent - Ready for production
- **80-89**: Good - Minor improvements possible
- **70-79**: Adequate - Some issues to address
- **60-69**: Needs Work - Significant gaps
- **Below 60**: Poor - Major revision needed

## 🎨 Usage Examples

### Example 1: Optimize a Weak Prompt

**Before**:
```
Write some code to process user data.
```

**Using Copilot Chat with Prompt Optimizer**:
```
@workspace use chatmode prompt-optimizer
Optimize this prompt: "Write some code to process user data"
```

**After**:
```xml
<role>You are an expert Python developer specializing in data processing.</role>

<task>
Create a Python function that processes user data from a CSV file.
</task>

<requirements>
- Read user data from CSV file
- Validate email addresses using regex
- Filter users with valid emails
- Return list of validated user dictionaries
- Handle file not found errors gracefully
</requirements>

<output_format>
Provide:
1. Complete, documented Python function
2. Example usage
3. Error handling explanation
</output_format>

<constraints>
- Use only Python standard library
- Function must be testable
- Include type hints
</constraints>
```

### Example 2: Analyze Prompt Quality

```
@workspace use chatmode prompt-analyzer
Analyze this prompt: "Create a REST API endpoint for user management"
```

The analyzer will provide:
- Numerical scores across all criteria
- Specific strengths and weaknesses
- Missing elements
- Technique recommendations
- Priority fixes to reach 90+ score

### Example 3: Choose the Right Model

```
@workspace use chatmode model-recommender
I'm building a code generation feature that needs to handle complex refactoring tasks. 
Quality is more important than speed, but I want to keep costs reasonable.
```

The recommender will:
- Ask clarifying questions about volume and requirements
- Score each model against your needs
- Provide top 3 recommendations with trade-offs
- Include cost estimates
- Give clear decision guidance

## 🔄 Model-Specific Optimizations

### Claude Opus 4.5
- Leverage extensive context and examples
- Use for complex reasoning and creative tasks
- Take advantage of 200K context window

### Claude Sonnet 4.5
- Balance detail with efficiency
- Optimize for tool use and agentic coding
- Structure for multi-step workflows

### Claude Haiku 4.5
- Simplify and streamline prompts
- Focus on single, clear tasks
- Minimize unnecessary context

### GPT 5.1/Codex
- Use system messages for context
- Leverage function calling
- Specify JSON mode for structured output

### Gemini Pro 3.0
- Leverage massive 2M context window
- Use context caching for repeated prefixes
- Optimize for multimodal inputs

## 🎯 Model Selection Guide

Quick reference:

| Use Case | Recommended Model | Why |
|----------|-------------------|-----|
| Agentic coding | Claude Sonnet 4.5 | Best balance for dev work |
| Complex research | Claude Opus 4.5 | Superior reasoning |
| High-volume processing | Claude Haiku 4.5 | Fastest, cheapest |
| Function calling | GPT 5.1 | Strong structured output |
| Code generation | GPT 5.1 Codex or Sonnet 4.5 | Code-specialized |
| Multimodal tasks | Gemini Pro 3.0 or Opus 4.5 | Image/video support |
| Long documents | Gemini Pro 3.0 | 2M context |

## 📁 File Structure

```
.github/
├── copilot-instructions.md          # Main prompt engineering guidance
├── chatmodes/
│   ├── prompt-optimizer.md          # Systematic prompt improvement
│   ├── prompt-analyzer.md           # Quality analysis and scoring
│   └── model-recommender.md         # Model selection guidance
└── README-COPILOT.md               # This file
```

## 🆚 Differences from Claude Code Version

This GitHub Copilot Chat version differs from the original Claude Code plugin:

| Feature | Claude Code | GitHub Copilot Chat |
|---------|-------------|---------------------|
| **Commands** | Slash commands (`/optimize-prompt`) | Chat modes and natural language |
| **Agents** | Automatic agent triggering | Manual chat mode selection |
| **Skills** | Separate skill files | Integrated in instructions |
| **Activation** | Plugin installation | Copy `.github` directory |
| **Integration** | Claude Code IDE | VS Code, Visual Studio, etc. |

## 🚦 Getting Started

1. **Copy files to your repository**:
   ```bash
   cp -r .github /path/to/your/project/
   ```

2. **Start using immediately** - Just chat with Copilot:
   ```
   How can I improve this prompt for better consistency?
   ```

3. **Use specialized chat modes for specific tasks**:
   ```
   @workspace use chatmode prompt-optimizer
   @workspace use chatmode prompt-analyzer
   @workspace use chatmode model-recommender
   ```

4. **Reference the guidance** - The system automatically provides context from the instructions.

## 💡 Tips and Best Practices

1. **Start with Analysis**: Use Prompt Analyzer to understand current quality before optimizing
2. **Be Specific**: When asking for help, provide the actual prompt text
3. **Include Context**: Mention the target model and use case
4. **Iterate**: Test optimized prompts and refine based on results
5. **Choose Wisely**: Use Model Recommender early to avoid costly model mismatches

## 🐛 Troubleshooting

**Copilot isn't using the instructions**:
- Ensure `.github/copilot-instructions.md` is in your repository root
- Try explicitly mentioning "use the prompt engineering guidance"

**Chat mode not activating**:
- Use the exact syntax: `@workspace use chatmode [mode-name]`
- Make sure the chat mode file exists in `.github/chatmodes/`

**Responses feel generic**:
- Provide more context about your specific use case
- Include the actual prompt you want help with
- Mention the target LLM model

## 📄 License

MIT License - Same as the original Claude Code plugin

## 🤝 Contributing

This is a conversion of the Claude Code plugin. For improvements or issues:
1. Test changes in your own repository
2. Submit feedback or PRs to the original repository
3. Share your optimizations with the community

## 📞 Support

- Original Claude Code Plugin: See main repository
- GitHub Copilot Chat: [Official Documentation](https://docs.github.com/en/copilot)
- Custom Instructions Guide: [GitHub Docs](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot)

---

**Happy Prompt Engineering! 🎉**
