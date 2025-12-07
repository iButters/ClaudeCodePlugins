# Claude Haiku 4.5 Optimization Guide

## Overview

Claude Haiku 4.5 is the speed and efficiency champion of the Claude family. It delivers fast responses at low cost while maintaining good quality for straightforward tasks. Ideal for high-volume, latency-sensitive applications.

## Capabilities

### Strengths

| Capability | Rating | Notes |
|------------|--------|-------|
| Speed | Excellent | Fastest Claude model |
| Cost Efficiency | Excellent | Lowest cost per token |
| Instruction Following | Good | Reliable for clear tasks |
| Classification | Good | Accurate categorization |
| Simple Transforms | Good | Quick data processing |
| Latency | Excellent | Sub-second responses |

### Ideal Use Cases

- Classification and categorization
- Simple data extraction
- High-volume processing
- Latency-critical applications
- Cost-sensitive workloads
- Quick question answering
- Simple text transformations
- Triage and routing

### When NOT to Use Haiku

- Complex reasoning tasks (use Sonnet/Opus)
- Creative writing requiring nuance (use Opus)
- Multi-step analysis (use Sonnet/Opus)
- Sophisticated code generation (use Sonnet)
- Tasks requiring deep context (use Sonnet/Opus)

## Key Optimizations

### 1. Keep Prompts Concise

Token efficiency is critical with Haiku. Minimize prompt length:

```xml
<!-- Too verbose for Haiku -->
I would like you to please analyze the following customer feedback
and determine whether the sentiment expressed by the customer is
positive, negative, or neutral. Please consider the overall tone,
specific words used, and the context of the feedback.

<!-- Concise (better for Haiku) -->
Classify sentiment as positive, negative, or neutral:
"[feedback text]"
```

### 2. Clear, Direct Instructions

Haiku performs best with straightforward instructions:

```
# Good: Direct and clear
Extract the email address from this text: [text]

# Good: Simple format
Classify as: spam, promotion, important, or other
Email: [email content]

# Not ideal: Complex multi-step
First analyze the text, then determine if it's formal or informal,
then extract key entities, then...
```

### 3. Use Examples for Consistency

A few examples help Haiku maintain consistency:

```xml
<task>
Categorize support tickets.
</task>

<examples>
"My account was charged twice" → billing
"App crashes on startup" → technical
"How do I reset password" → account
</examples>

<input>
"I can't access my subscription"
</input>
```

### 4. Minimize Context

Only include necessary information:

```
# Too much context for Haiku
Here's the entire document with all sections...
[2000 words of context]
Now extract the date.

# Better: Focused context
Extract the meeting date from:
"Team sync scheduled for March 15, 2025 at 2pm"
```

### 5. Structured Output Specification

Be explicit about output format:

```xml
<input>
[Customer message]
</input>

<output_format>
category: [billing|technical|account|other]
priority: [high|medium|low]
</output_format>
```

### 6. Binary and Simple Decisions

Haiku excels at clear-cut decisions:

```
Is this message spam? Answer only "yes" or "no":
[message]
```

## Prompt Patterns for Haiku

### Classification

```xml
<task>
Classify the following item into exactly one category.
</task>

<categories>
- billing: Payment, charges, invoices
- technical: Bugs, errors, features
- account: Login, password, settings
- other: Everything else
</categories>

<input>
[Content to classify]
</input>

<output>
Return only the category name, nothing else.
</output>
```

### Data Extraction

```xml
<task>
Extract the following fields from the text.
</task>

<fields>
- name (string or null)
- email (string or null)
- phone (string or null)
</fields>

<text>
[Text to extract from]
</text>

<format>
JSON: {"name": "...", "email": "...", "phone": "..."}
</format>
```

### Quick Q&A

```
Answer briefly (1-2 sentences max):
Q: [Question]
```

### Sentiment Analysis

```
Rate sentiment: positive, neutral, or negative
Text: "[text]"
Rating:
```

### Routing/Triage

```xml
<task>
Route this request to the appropriate department.
</task>

<departments>
sales, support, billing, other
</departments>

<request>
[Customer request]
</request>

<output>
Department name only.
</output>
```

### Simple Transformation

```
Convert to title case:
Input: [text]
Output:
```

## Batch Processing Patterns

### High-Volume Classification

For processing many items:

```python
# Process in batches for efficiency
prompt = """
Classify each item. Return one category per line.

Categories: A, B, C

Items:
1. [item1]
2. [item2]
3. [item3]
...
"""
```

### Parallel Processing

Haiku's low cost makes parallel processing viable:

```
# Run multiple Haiku calls in parallel rather than
# one complex Sonnet call when tasks are independent
```

## Cost and Performance

| Metric | Value |
|--------|-------|
| Input | $0.80/million tokens |
| Output | $4/million tokens |
| Speed | Fastest |
| Latency | Sub-second |
| Quality | Good for simple tasks |

### Cost Comparison

| Model | Input Cost | Output Cost | Speed |
|-------|-----------|-------------|-------|
| Haiku | $0.80/M | $4/M | Fastest |
| Sonnet | $3/M | $15/M | Fast |
| Opus | $15/M | $75/M | Slow |

Haiku is ~4x cheaper than Sonnet and ~19x cheaper than Opus.

## When to Choose Haiku

| Task Type | Use Haiku? |
|-----------|------------|
| Simple classification | Yes |
| Data extraction (simple) | Yes |
| Sentiment analysis | Yes |
| Routing/triage | Yes |
| Quick Q&A | Yes |
| High-volume processing | Yes |
| Complex reasoning | No (use Sonnet/Opus) |
| Creative writing | No (use Opus) |
| Multi-step analysis | No (use Sonnet) |
| Code generation | No (use Sonnet) |

## Optimization Strategies

### 1. Pre-Filter with Haiku

Use Haiku as a first-pass filter:

```
Step 1: Haiku classifies incoming items (fast, cheap)
Step 2: Only complex items go to Sonnet (quality where needed)
```

### 2. Batch Similar Tasks

Group similar items for processing:

```
Process these 10 similar items together:
[items]
Return classifications one per line.
```

### 3. Cache Common Responses

For repeated patterns, cache Haiku responses to avoid redundant calls.

### 4. Simplify Complex Tasks

Break complex tasks into Haiku-sized pieces:

```
Instead of: "Analyze, summarize, and recommend"
Do:
- Haiku: Extract key facts
- Haiku: Classify importance
- Sonnet: Synthesize and recommend
```

## Common Mistakes

### 1. Overloading with Complexity

```
# Bad: Too complex for Haiku
Analyze this research paper, identify the methodology,
evaluate the statistical approach, and provide a critique.

# Better: Simple, focused task
What is the main methodology used? (experimental/observational/review)
```

### 2. Verbose Prompts

```
# Bad: Wastes tokens
I would like you to kindly help me by determining whether
the following piece of text contains any mention of...

# Better: Concise
Does this text mention pricing? yes/no:
```

### 3. Expecting Nuanced Output

```
# Bad: Requires nuance Haiku may miss
Write a thoughtful, balanced analysis of...

# Better: Structured output
List 3 pros and 3 cons of [topic]:
```

## Quick Reference

**Optimize Haiku by:**
- Keeping prompts short and direct
- Using clear, simple instructions
- Providing 2-3 examples for consistency
- Minimizing context to essentials
- Specifying exact output format
- Focusing on single, clear tasks

**Avoid:**
- Complex multi-step reasoning
- Verbose prompt text
- Tasks requiring nuanced judgment
- Long-form content generation
- Deep contextual understanding

## Summary

Claude Haiku 4.5 is optimal for high-speed, high-volume, cost-sensitive workloads. Optimize by:
1. Keeping prompts concise and direct
2. Using clear examples for consistency
3. Minimizing context to essentials
4. Specifying exact output formats
5. Batching similar tasks
6. Using as a pre-filter before heavier models

Use Haiku for classification, extraction, routing, and any task where speed and cost matter more than sophistication.
