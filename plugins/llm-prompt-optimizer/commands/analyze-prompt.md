---
description: Analyze a prompt and get detailed feedback without modification
allowed-tools:
  - Task
  - Read
---

# Analyze Prompt Command

Use the **prompt-analyzer** agent to evaluate the user's prompt and provide a quality score.

## Process

1. **Get the prompt**:
   - If arguments provided: `{{$ARGUMENTS}}`
   - If a file path is given: Read the file using the Read tool
   - If no prompt available: The agent will report an error

2. **Invoke the agent**:
   Use the Task tool with `subagent_type: "prompt-analyzer"` and pass:
   - The prompt to analyze
   - Target model (if known)

3. **Present results**:
   The agent returns a detailed analysis report including:
   - Quality score (0-100)
   - Breakdown by category (Clarity, Context, Structure, Output Spec, Techniques, Model Fit)
   - Strengths and issues with severity ratings
   - Suggestions for improvement (without implementing them)
