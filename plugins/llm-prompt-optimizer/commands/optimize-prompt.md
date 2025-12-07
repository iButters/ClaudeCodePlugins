---
description: Optimize an existing prompt for better LLM performance
allowed-tools:
  - Task
  - Read
---

# Optimize Prompt Command

Use the **prompt-optimizer** agent to improve the user's prompt.

## Process

1. **Get the prompt**:
   - If arguments provided: `{{$ARGUMENTS}}`
   - If a file path is given: Read the file using the Read tool
   - If no prompt available: The agent will ask for it

2. **Invoke the agent**:
   Use the Task tool with `subagent_type: "prompt-optimizer"` and pass:
   - The prompt to optimize
   - Target model (if known)
   - Problems the user is experiencing (if any)

3. **Present results**:
   The agent returns a fully optimized prompt with explanations.
