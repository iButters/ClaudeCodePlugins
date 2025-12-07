# GPT 5.1 Optimization Guide

## Overview

GPT 5.1 is OpenAI's flagship general-purpose model, offering strong capabilities across reasoning, function calling, and structured output. It excels at tasks requiring broad knowledge and reliable instruction following.

## Capabilities

### Strengths

| Capability | Rating | Notes |
|------------|--------|-------|
| General Reasoning | High | Broad knowledge base |
| Function Calling | Excellent | Native tool integration |
| JSON Mode | Excellent | Guaranteed structured output |
| Instruction Following | High | Reliable adherence |
| Knowledge Breadth | High | Extensive training data |
| API Integration | Excellent | Well-documented, stable |

### Ideal Use Cases

- General-purpose assistants
- Function/tool calling applications
- Structured data extraction (JSON mode)
- API integrations
- Customer-facing applications
- Question answering systems
- Content generation

### When NOT to Use GPT 5.1

- Specialized code generation (consider Codex)
- Extended autonomous coding (Claude Sonnet better)
- Complex multi-step research (Claude Opus better)
- Maximum speed required (smaller models)

## Key Optimizations

### 1. System Message Best Practices

Use the system message effectively:

```python
system_message = """
You are a [specific role] with expertise in [domain].
Your responsibilities:
1. [Responsibility 1]
2. [Responsibility 2]

Guidelines:
- [Guideline 1]
- [Guideline 2]

Output format: [Specify format]
"""
```

**Key principles:**
- Place persistent context in system message
- Keep task-specific content in user messages
- Be explicit about behavior and format

### 2. JSON Mode

Use JSON mode for reliable structured output:

```python
response = client.chat.completions.create(
    model="gpt-5.1",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": "You are a data extractor. Always respond with valid JSON."},
        {"role": "user", "content": "Extract key information from: [text]"}
    ]
)
```

**Important:** When using JSON mode, always mention "JSON" in the prompt.

### 3. Function Calling

Structure function definitions clearly:

```python
functions = [
    {
        "name": "get_weather",
        "description": "Get current weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City and state, e.g. San Francisco, CA"
                },
                "unit": {
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"]
                }
            },
            "required": ["location"]
        }
    }
]
```

**Best practices:**
- Clear, descriptive function names
- Detailed parameter descriptions
- Explicit enum values where applicable
- Required vs optional clearly marked

### 4. Clear Delimiters

Use consistent delimiters for multi-part prompts:

```
### CONTEXT ###
[Background information]

### TASK ###
[What to do]

### FORMAT ###
[Expected output structure]

### INPUT ###
[Data to process]
```

Or use XML-style:

```xml
<context>
[Background]
</context>

<task>
[Instructions]
</task>

<input>
[Data]
</input>
```

### 5. Temperature and Sampling

Adjust based on task type:

| Task Type | Temperature | Reason |
|-----------|-------------|--------|
| Factual/Extraction | 0.0-0.3 | Consistency |
| General tasks | 0.7 | Default balance |
| Creative writing | 0.8-1.0 | Variety |
| Brainstorming | 1.0+ | Maximum creativity |

### 6. Few-Shot Formatting

Format examples consistently:

```
User: [Example input 1]
Assistant: [Example output 1]

User: [Example input 2]
Assistant: [Example output 2]

User: [Actual input]
```

Or with explicit markers:

```
Example 1:
Input: [input]
Output: [output]

Example 2:
Input: [input]
Output: [output]

Now process:
Input: [actual input]
Output:
```

## Prompt Patterns for GPT 5.1

### Structured Extraction

```
System: You are a data extraction specialist. Extract information in JSON format.

User:
Extract the following fields from the text:
- company_name (string)
- founded_year (integer or null)
- industry (string)
- key_products (array of strings)

Text:
"""
[Document text]
"""

Respond with valid JSON only.
```

### Function Calling Pattern

```
System: You are a helpful assistant with access to external tools.
When you need information you don't have, use the appropriate function.
After receiving function results, synthesize them into a helpful response.

[Functions defined in API call]

User: [User's question requiring tool use]
```

### Analysis with Structure

```
System: You are an analyst who provides structured, actionable insights.

User:
Analyze the following data and provide:
1. Key findings (3-5 bullet points)
2. Trends identified
3. Recommendations

Data:
"""
[Data to analyze]
"""

Format your response with clear headings.
```

### Multi-Step Reasoning

```
System: You are a problem solver who shows your work.

User:
Solve this problem step by step:
[Problem statement]

Show your reasoning at each step before providing the final answer.
```

## Comparison with Claude Models

| Aspect | GPT 5.1 | Claude Sonnet 4.5 |
|--------|---------|------------------|
| Function calling | Excellent | Good |
| JSON mode | Native | Via prompting |
| Agentic coding | Good | Excellent |
| Extended work | Good | Excellent |
| System prompt | Standard | Powerful |
| Cost | Similar | Similar |

**Choose GPT 5.1 when:**
- Native function calling is priority
- JSON mode reliability needed
- OpenAI ecosystem integration
- Broad general knowledge required

**Choose Claude Sonnet when:**
- Agentic coding is primary use
- Extended autonomous work needed
- Parallel tool calling important
- Context awareness critical

## Context Window Management

### Efficient Use of Context

```
# Prioritize recent and relevant information
# Summarize older context when approaching limits
# Use explicit markers for important information

<important>
This information is critical for the task.
</important>

<background>
This provides context but is lower priority.
</background>
```

### Long Conversations

For extended conversations:
1. Summarize earlier turns periodically
2. Keep essential context in system message
3. Use explicit references to earlier points

## Cost and Performance

| Metric | GPT 5.1 |
|--------|---------|
| Context Window | 128K tokens |
| Speed | Fast |
| Pricing | Competitive |
| Reliability | High |

## Common Patterns

### Classification

```
System: You are a classifier. Classify items into exactly one category.

User:
Categories: [A, B, C, D]

Item to classify:
"""
[Content]
"""

Respond with only the category name.
```

### Summarization

```
System: You are a summarizer who creates concise, accurate summaries.

User:
Summarize the following in [X] sentences/words:
"""
[Content to summarize]
"""

Focus on: [key aspects to emphasize]
```

### Translation with Context

```
System: You are a professional translator specializing in [domain].

User:
Translate to [language], maintaining [tone/style]:
"""
[Text to translate]
"""

Context: [Additional context if relevant]
```

## Common Mistakes

### 1. Vague System Messages

```
# Bad
You are a helpful assistant.

# Good
You are a technical support specialist for [product].
You help users troubleshoot issues with [features].
Always ask clarifying questions before providing solutions.
Respond in a friendly, professional tone.
```

### 2. Not Using JSON Mode

```
# Risky: May not always produce valid JSON
Parse this into JSON: [data]

# Better: Use JSON mode in API call
response_format={"type": "json_object"}
And mention "JSON" in the prompt
```

### 3. Overloading Single Prompts

```
# Too much in one prompt
Analyze, summarize, translate, and format this document...

# Better: Chain of focused prompts
Prompt 1: Analyze → Output
Prompt 2: Summarize the analysis → Output
Prompt 3: Translate the summary → Final
```

## Quick Reference

**Optimize GPT 5.1 by:**
- Using system messages effectively
- Leveraging JSON mode for structure
- Defining clear function schemas
- Using consistent delimiters
- Adjusting temperature for task type
- Providing well-formatted examples

**Avoid:**
- Vague role definitions
- Expecting JSON without JSON mode
- Overloading single prompts
- Ignoring function calling capabilities

## Summary

GPT 5.1 excels at general-purpose tasks with strong function calling and structured output capabilities. Optimize by:
1. Using system messages for persistent context
2. Leveraging JSON mode for reliability
3. Defining clear function schemas
4. Using consistent formatting and delimiters
5. Matching temperature to task type
6. Breaking complex tasks into focused prompts

Use GPT 5.1 for general-purpose applications, especially those requiring reliable function calling and structured output.
