# Chain of Thought Prompting

## Overview

Chain of Thought (CoT) prompting instructs the model to show its reasoning process before providing a final answer. This technique significantly improves accuracy on complex reasoning tasks by making the thinking process explicit and structured.

## When to Use Chain of Thought

Apply CoT when:
- Task requires multi-step reasoning
- Mathematical or logical calculations needed
- Complex analysis with multiple factors
- Decision-making with trade-offs
- Problem-solving that benefits from decomposition
- Verification of reasoning is important

## Impact

CoT typically improves:
- **Math problems**: 30-50% accuracy increase
- **Logic puzzles**: 40-60% accuracy increase
- **Complex analysis**: Significant quality improvement
- **Consistency**: More reliable outputs

## Core Principles

### 1. Explicit Thinking

Ask the model to show its work:

```
# Without CoT (may skip steps, make errors)
What is 23 × 47?

# With CoT (more accurate)
Calculate 23 × 47. Show your work step by step before giving
the final answer.
```

### 2. Structured Reasoning

Provide a framework for thinking:

```
Analyze this business decision using these steps:
1. List the key factors to consider
2. Evaluate each option against these factors
3. Identify risks and trade-offs
4. Make a recommendation with reasoning
```

### 3. Separate Thinking from Answer

Use clear markers:

```
First, work through this problem in <thinking> tags.
Then provide your final answer in <answer> tags.
```

## CoT Patterns

### Basic Pattern

```
[Problem statement]

Think through this step by step:
1. First, identify...
2. Then, consider...
3. Finally, conclude...

Show your reasoning before giving your answer.
```

### XML-Structured Pattern

```xml
<problem>
[Problem to solve]
</problem>

<instructions>
Think through this carefully. Show your reasoning in
<thinking> tags, then provide your answer in <answer> tags.
</instructions>
```

### Guided Reasoning Pattern

```
Analyze this situation using the following framework:

<analysis_steps>
1. What are the key facts?
2. What assumptions are we making?
3. What are the possible outcomes?
4. What is the most likely scenario?
5. What is the recommended action?
</analysis_steps>

Work through each step before concluding.
```

## Task-Specific CoT Templates

### Mathematical Reasoning

```
Solve this problem step by step:

<problem>
A store offers 20% off, then an additional 10% off the sale price.
If the original price is $80, what is the final price?
</problem>

Show your calculations:
1. Calculate the first discount
2. Calculate the price after first discount
3. Calculate the second discount
4. Calculate the final price

Then provide your final answer.
```

### Logical Analysis

```
<scenario>
If all programmers drink coffee, and some coffee drinkers are night owls,
can we conclude that some programmers are night owls?
</scenario>

Analyze this logic problem:
1. State the given premises clearly
2. Identify what can and cannot be concluded
3. Explain why the conclusion is valid or invalid
4. Provide your final answer
```

### Code Debugging

```
<code>
def calculate_average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)
</code>

<bug_report>
Returns ZeroDivisionError for empty lists
</bug_report>

Debug this code step by step:
1. Trace through the code with an empty list
2. Identify where the error occurs
3. Explain why it happens
4. Propose a fix
5. Show the corrected code
```

### Decision Analysis

```
<decision>
Should we migrate from PostgreSQL to MongoDB for our e-commerce application?
</decision>

<context>
- 10M users, 1M daily active
- Current performance issues with complex queries
- Team has PostgreSQL expertise
- Some data is highly relational, some is document-like
</context>

Analyze this decision:
1. List pros of migrating to MongoDB
2. List cons of migrating to MongoDB
3. Consider the current team expertise
4. Evaluate the data model fit
5. Assess migration risks
6. Make a recommendation with clear reasoning
```

### Research Synthesis

```
<research_question>
What are the main causes of employee turnover in tech companies?
</research_question>

<sources>
[Multiple research summaries]
</sources>

Synthesize this research:
1. Identify common themes across sources
2. Note any conflicting findings
3. Evaluate the strength of evidence
4. Draw conclusions supported by the data
5. Identify gaps in the research
```

## Zero-Shot vs Few-Shot CoT

### Zero-Shot CoT

Simply instruct to think step by step:

```
Solve this problem. Think step by step before answering.

[Problem]
```

### Few-Shot CoT

Provide examples of the reasoning process:

```
<example>
<problem>If a train travels 60 mph for 2.5 hours, how far does it go?</problem>
<thinking>
Distance = Speed × Time
Speed = 60 mph
Time = 2.5 hours
Distance = 60 × 2.5 = 150 miles
</thinking>
<answer>150 miles</answer>
</example>

Now solve: If a car travels 45 mph for 3 hours, how far does it go?
```

## Model-Specific Considerations

### Claude Models

Claude 4.x offers extended thinking capabilities:

- Use `<thinking>` tags to encourage structured reasoning
- After tool use, prompt for reflection on results
- Leverage thinking for multi-step planning

```
After receiving tool results, carefully reflect on their quality and
determine optimal next steps before proceeding. Use your thinking to
plan and iterate based on this new information.
```

**Important for Claude Opus 4.5**: When extended thinking is disabled, avoid the word "think" and variants. Use alternatives:
- "consider"
- "analyze"
- "evaluate"
- "reason through"

### GPT Models

GPT responds well to CoT:

- "Let's think step by step" is a classic trigger
- Structured templates work well
- Can combine with JSON mode for formatted output

### Gemini Models

Gemini supports chain of thought:

- Explicit step instructions help
- Clear output format specification

## When NOT to Use CoT

CoT adds tokens and latency. Skip it for:
- Simple factual questions
- Direct translations
- Basic classifications (use examples instead)
- Format conversions
- Tasks where speed is critical

```
# CoT unnecessary
What is the capital of France?

# CoT helpful
Which European capital would be best for a tech startup
considering talent, costs, and regulatory environment?
```

## Structured Output from CoT

### Separating Reasoning from Answer

```xml
<problem>
Should this PR be approved?
</problem>

<instructions>
1. Analyze the code changes in <analysis> tags
2. List any concerns in <concerns> tags
3. Provide your verdict in <verdict> tags
4. Explain in <explanation> tags
</instructions>
```

### Confidence Levels

```
Analyze this legal question. In your response:
1. Work through the relevant considerations
2. Rate your confidence (high/medium/low)
3. Explain what additional information would help

Format:
<reasoning>[Your analysis]</reasoning>
<confidence>[high/medium/low]</confidence>
<answer>[Your conclusion]</answer>
<limitations>[What you're uncertain about]</limitations>
```

## Common Mistakes

### 1. Asking to "Think" Without Structure

```
# Too vague
Think about this problem.

# Better
Work through this problem using these steps:
1. Identify the given information
2. Determine what we need to find
3. Apply the relevant formula
4. Calculate the answer
5. Verify by checking
```

### 2. Not Separating Reasoning from Answer

```
# Confusing output
The answer is 42 because first we... and then... so 42.

# Clear separation
<thinking>First we... then we...</thinking>
<answer>42</answer>
```

### 3. Overusing CoT for Simple Tasks

```
# Overkill
Think step by step about what 2 + 2 equals.

# Just ask
What is 2 + 2?
```

## Integration with Other Techniques

### With Examples (Few-Shot CoT)

```xml
<examples>
  <example>
    <problem>Is 91 prime?</problem>
    <thinking>
    Check divisibility:
    91 ÷ 7 = 13
    91 = 7 × 13
    91 has factors other than 1 and itself
    </thinking>
    <answer>No, 91 is not prime</answer>
  </example>
</examples>

Now solve: Is 97 prime?
```

### With Role Prompting

```
System: You are a financial analyst who always shows your work.

User: Should I invest in Company X given these financials?

Show your analysis step by step:
1. Evaluate the revenue trends
2. Analyze the profit margins
3. Consider the debt levels
4. Compare to industry benchmarks
5. Provide your recommendation
```

### With Prompt Chaining

Use CoT within each step of a chain:

```
Step 1: Analyze the problem (with reasoning)
Step 2: Generate solutions (with reasoning)
Step 3: Evaluate solutions (with reasoning)
Step 4: Make recommendation (with reasoning)
```

## Quick Reference

| Task Type | CoT Approach |
|-----------|--------------|
| Math problems | Show calculations step by step |
| Logic puzzles | Trace through premises to conclusion |
| Decisions | List factors, evaluate, conclude |
| Debugging | Trace execution, identify issue, fix |
| Analysis | Break down, examine parts, synthesize |

## Summary

Chain of Thought prompting:
- Makes reasoning explicit and verifiable
- Improves accuracy on complex tasks
- Reduces errors in multi-step problems
- Enables confidence assessment

Best practices:
- Use structured thinking frameworks
- Separate reasoning from final answer
- Provide examples for complex reasoning patterns
- Match depth of reasoning to task complexity
- Skip for simple, factual tasks
