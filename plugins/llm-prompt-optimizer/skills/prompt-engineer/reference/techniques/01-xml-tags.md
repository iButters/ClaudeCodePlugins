# XML Tags for Prompt Structure

## Overview

XML tags provide clear visual and semantic separation of prompt components. They help LLMs parse complex prompts reliably and maintain consistent output formats.

## When to Use XML Tags

Apply XML tags when:
- Prompt has 3+ distinct components
- Structured output format is required
- Clear separation between context, instructions, and data needed
- Examples need to be clearly delineated
- Multi-part input needs organization

## Core Tag Patterns

### Basic Structure

```xml
<context>
Background information, purpose, and constraints.
</context>

<instructions>
Clear, numbered steps for the task.
</instructions>

<input>
The actual data or content to process.
</input>

<output_format>
Specification of expected output structure.
</output_format>
```

### With Examples

```xml
<context>
[Background and purpose]
</context>

<instructions>
[Task description]
</instructions>

<examples>
  <example>
    <input>[Sample input]</input>
    <output>[Expected output]</output>
  </example>
  <example>
    <input>[Another input]</input>
    <output>[Another output]</output>
  </example>
</examples>

<input>
[Actual input to process]
</input>
```

### With Role Definition

```xml
<role>
You are a [specific expertise] with experience in [domain].
Your responsibilities include [key tasks].
</role>

<context>
[Background information]
</context>

<task>
[Specific task to accomplish]
</task>
```

## Best Practices

### 1. Use Semantic Tag Names

Choose tag names that describe content purpose:

```xml
<!-- Good: Semantic and clear -->
<customer_query>...</customer_query>
<response_guidelines>...</response_guidelines>
<urgency_criteria>...</urgency_criteria>

<!-- Avoid: Generic or unclear -->
<text1>...</text1>
<section>...</section>
<data>...</data>
```

### 2. Maintain Consistent Hierarchy

Nest tags logically:

```xml
<examples>
  <example id="1">
    <scenario>Customer complaint about billing</scenario>
    <classification>billing</classification>
    <urgency>medium</urgency>
  </example>
</examples>
```

### 3. Separate Data from Instructions

Keep instructions and data clearly separated:

```xml
<instructions>
Analyze the code for security vulnerabilities.
Focus on: SQL injection, XSS, authentication issues.
</instructions>

<code_to_analyze>
[Actual code here - clearly separated from instructions]
</code_to_analyze>
```

### 4. Use for Output Specification

Define expected output structure:

```xml
<output_format>
Respond with JSON in this exact structure:
{
  "classification": "category_name",
  "confidence": 0.0-1.0,
  "reasoning": "brief explanation"
}
</output_format>
```

## Common Tag Patterns by Use Case

### Classification Tasks

```xml
<classification_criteria>
- Category A: [definition]
- Category B: [definition]
- Category C: [definition]
</classification_criteria>

<examples>
  <example>
    <input>Sample text</input>
    <category>Category A</category>
  </example>
</examples>

<item_to_classify>
[Content to classify]
</item_to_classify>
```

### Analysis Tasks

```xml
<analysis_framework>
Examine the following aspects:
1. [Aspect 1]
2. [Aspect 2]
3. [Aspect 3]
</analysis_framework>

<document>
[Document to analyze]
</document>

<output_requirements>
Provide:
- Summary of findings
- Key insights
- Recommendations
</output_requirements>
```

### Code Review Tasks

```xml
<review_criteria>
Focus on:
- Security vulnerabilities
- Performance issues
- Code style violations
- Logic errors
</review_criteria>

<code>
[Code to review]
</code>

<output_format>
For each issue found:
- Line number
- Issue type
- Severity (critical/high/medium/low)
- Recommendation
</output_format>
```

## Model-Specific Considerations

### Claude Models

- Claude handles XML naturally without special configuration
- Complex nested structures work well
- Use semantic tag names for best results

### GPT Models

- GPT also parses XML reliably
- Consider combining with JSON mode for structured output
- Keep nesting depth reasonable (3-4 levels max)

### Gemini Models

- XML works but consider explicit format instructions
- Combine with clear output specification

## Common Mistakes to Avoid

### 1. Unclosed Tags

```xml
<!-- Wrong -->
<instructions>
Do the following tasks:
<task>Task 1</task>
<task>Task 2
</instructions>

<!-- Correct -->
<instructions>
<task>Task 1</task>
<task>Task 2</task>
</instructions>
```

### 2. Inconsistent Tag Usage

```xml
<!-- Wrong: Mixing conventions -->
<Input>...</Input>
<output>...</output>
<EXAMPLE>...</EXAMPLE>

<!-- Correct: Consistent lowercase -->
<input>...</input>
<output>...</output>
<example>...</example>
```

### 3. Overusing Tags

Simple prompts don't need XML structure. Only add tags when they improve clarity:

```xml
<!-- Overkill for simple task -->
<task>
<instruction>
<action>Tell me a joke</action>
</instruction>
</task>

<!-- Better: Just ask directly -->
Tell me a joke.
```

## Integration with Other Techniques

### With Chain of Thought

```xml
<instructions>
Analyze this problem step by step.
</instructions>

<problem>
[Problem statement]
</problem>

<thinking_format>
Show your reasoning in <thinking> tags.
Provide final answer in <answer> tags.
</thinking_format>
```

### With Examples (Multishot)

```xml
<task_description>
Classify customer support tickets by urgency.
</task_description>

<examples>
  <example>
    <ticket>My account was hacked!</ticket>
    <urgency>critical</urgency>
    <reasoning>Security breach requires immediate action</reasoning>
  </example>
  <example>
    <ticket>How do I change my password?</ticket>
    <urgency>low</urgency>
    <reasoning>Standard how-to question, not time-sensitive</reasoning>
  </example>
</examples>

<ticket_to_classify>
[New ticket]
</ticket_to_classify>
```

## Quick Reference

| Tag | Purpose | Common Usage |
|-----|---------|--------------|
| `<context>` | Background information | Always useful for complex tasks |
| `<instructions>` | Task specification | Core of most prompts |
| `<input>` | Data to process | Separates data from instructions |
| `<output_format>` | Expected response structure | Ensures consistent format |
| `<examples>` | Demonstration cases | Multishot prompting |
| `<thinking>` | Reasoning process | Chain of thought |
| `<answer>` | Final response | Separates reasoning from output |

## Summary

XML tags are powerful for organizing complex prompts. Use them to:
- Clearly separate prompt components
- Define expected output structure
- Organize examples systematically
- Guide the model through multi-part tasks

Start simple and add structure as complexity grows. Match tag usage to actual need.
