---
description: Get model recommendations for your specific use case
allowed-tools:
  - Task
  - AskUserQuestions
---

# Recommend Model Command

Use the **model-recommender** agent to help the user choose the best LLM for their task.

## Process

1. **Gather context**:
   - If arguments provided: `{{$ARGUMENTS}}`
   - Pass any task description or requirements to the agent

2. **Invoke the agent**:
   Use the Task tool with `subagent_type: "model-recommender"` and pass:
   - The task description (if provided)
   - Any constraints mentioned (speed, cost, quality)
   - Special requirements (vision, JSON mode, etc.)

3. **Present results**:
   The agent will ask clarifying questions via AskUserQuestion, then return:
   - Top 3 model recommendations with match scores
   - Trade-off comparisons
   - Decision guide for choosing between options
