# Prompt Troubleshooting Guide

## Diagnosis Framework

When a prompt isn't working as expected, follow this systematic approach:

1. **Identify the symptom** - What specifically is wrong?
2. **Diagnose the cause** - Why is this happening?
3. **Apply the fix** - What change will resolve it?
4. **Verify the solution** - Did it work?

## Common Problems and Solutions

### Problem 1: Inconsistent Outputs

**Symptoms:**
- Different formats across runs
- Varying levels of detail
- Unpredictable structure

**Diagnosis:**
- Missing or insufficient examples
- Ambiguous format instructions
- No output structure specification

**Solutions:**

1. **Add Examples (Most Effective)**
```xml
<examples>
  <example>
    <input>Sample input 1</input>
    <output>Exact format you want</output>
  </example>
  <example>
    <input>Sample input 2</input>
    <output>Same format, different content</output>
  </example>
</examples>
```

2. **Specify Format Explicitly**
```
Output format:
- First line: [Category]
- Second line: [One-sentence summary]
- Third line: [Key metric: X%]
```

3. **Add Role with Format Expectations**
```
You are a data analyst who always presents findings in exactly this format:
[Format specification]
```

### Problem 2: Wrong Focus or Priorities

**Symptoms:**
- Model emphasizes wrong aspects
- Key information missing
- Irrelevant details included

**Diagnosis:**
- Unclear success criteria
- Poor instruction ordering
- Missing priority indicators

**Solutions:**

1. **Clarify Success Criteria**
```
Success criteria:
- MUST include: [essential elements]
- SHOULD include: [important but optional]
- MUST NOT include: [what to avoid]
```

2. **Reorder by Priority**
```
In order of importance:
1. [Most critical task] - This is the primary goal
2. [Secondary task]
3. [Nice to have]
```

3. **Use Explicit Constraints**
```
<constraints>
Focus ONLY on security implications.
Ignore: performance, style, documentation.
</constraints>
```

### Problem 3: Missing Information

**Symptoms:**
- Incomplete responses
- Shallow analysis
- Key details omitted

**Diagnosis:**
- Insufficient instructions
- Assumed context not stated
- No detail level specified

**Solutions:**

1. **Be Explicit About Requirements**
```
Your response MUST include:
- At least 3 specific examples
- Quantitative data where available
- Action items with owners
```

2. **Specify Detail Level**
```
Provide a comprehensive analysis including:
- High-level summary (2-3 sentences)
- Detailed breakdown (3-5 paragraphs)
- Supporting evidence for each point
```

3. **Add Examples Showing Expected Detail**
```
<example>
Input: [Sample]
Output: [Response showing the level of detail expected]
</example>
```

### Problem 4: Overly Verbose Output

**Symptoms:**
- Responses too long
- Excessive preamble
- Repetitive content

**Diagnosis:**
- No length constraints
- No format specification
- Model defaulting to verbose

**Solutions:**

1. **Add Length Constraints**
```
Constraints:
- Maximum 200 words
- No introductory phrases
- Get straight to the answer
```

2. **Format for Brevity**
```
Respond with ONLY:
- Category: [one word]
- Reason: [one sentence]
```

3. **Model-Specific (Claude 4.x)**
```xml
<communication_style>
Be concise and direct. Skip unnecessary preamble.
Jump straight to the key points.
</communication_style>
```

### Problem 5: Complex Task Failing

**Symptoms:**
- Partial completion
- Errors in multi-step reasoning
- Lost context mid-task

**Diagnosis:**
- Task too complex for single prompt
- Missing structured thinking
- No intermediate verification

**Solutions:**

1. **Use Prompt Chaining**
```
Stage 1: Extract key facts
Stage 2: Analyze facts
Stage 3: Generate recommendations
```

2. **Add Chain of Thought**
```
Work through this step by step:
1. First, identify [X]
2. Then, analyze [Y]
3. Finally, conclude [Z]

Show your reasoning in <thinking> tags.
```

3. **Break Into Subtasks**
```
<task_1>
First, complete only this part: [subtask]
Output in <result_1> tags.
</task_1>

<task_2>
Using <result_1>, now: [next subtask]
</task_2>
```

### Problem 6: Domain-Specific Errors

**Symptoms:**
- Technical mistakes
- Wrong terminology
- Missing domain context

**Diagnosis:**
- No domain role specified
- Lacking domain examples
- Technical terms undefined

**Solutions:**

1. **Add Domain Role**
```
System: You are a senior [domain] expert with 15 years of experience in [specific areas].
You are familiar with [relevant standards, tools, practices].
```

2. **Provide Domain Examples**
```xml
<domain_examples>
In our industry, the standard approach is:
[Example of correct domain-specific output]
</domain_examples>
```

3. **Define Terminology**
```
<definitions>
- Term A: [definition in this context]
- Term B: [definition in this context]
</definitions>
```

### Problem 7: Format Not Followed

**Symptoms:**
- Ignoring requested structure
- Wrong output type
- Missing sections

**Diagnosis:**
- Format not clearly specified
- No examples of format
- Competing format signals

**Solutions:**

1. **Use XML Tags for Structure**
```
Structure your response as:
<summary>Brief overview</summary>
<details>Full analysis</details>
<recommendations>Action items</recommendations>
```

2. **Provide Format Examples**
```
Your response should look exactly like this:
---
Title: [Title]
Score: [X/10]
Summary: [One paragraph]
---
```

3. **For JSON (use JSON mode if available)**
```
Return valid JSON matching this schema:
{
  "category": "string",
  "confidence": "number 0-1",
  "reasoning": "string"
}
```

### Problem 8: Hallucinations

**Symptoms:**
- Made-up information
- Confident but wrong
- Invented citations

**Diagnosis:**
- No grounding instructions
- Asking about unknown topics
- No uncertainty acknowledgment

**Solutions:**

1. **Add Grounding Instructions**
```
Only use information from the provided context.
If information is not available, say "Information not provided."
Never make up facts, citations, or data.
```

2. **Request Uncertainty**
```
If you're not certain, indicate your confidence level.
Distinguish between:
- Facts from the document
- Your inferences
- Speculation
```

3. **For Claude Opus (specific optimization)**
```xml
<investigate_before_answering>
Never speculate about code or information you haven't verified.
Read relevant files before making claims.
</investigate_before_answering>
```

## Quick Diagnosis Table

| Symptom | Likely Cause | Quick Fix |
|---------|--------------|-----------|
| Inconsistent format | No examples | Add 3-5 examples |
| Wrong focus | Unclear priorities | Explicit success criteria |
| Too brief | No detail specification | Request specific depth |
| Too verbose | No constraints | Add word limits |
| Task incomplete | Too complex | Break into steps |
| Wrong terminology | No domain context | Add role/definitions |
| Made-up info | No grounding | Add verification rules |
| Wrong structure | Format unclear | Use XML structure |

## Model-Specific Troubleshooting

### Claude 4.x Issues

| Problem | Solution |
|---------|----------|
| Not implementing (just suggesting) | Add "implement, don't suggest" |
| Over-engineering | Add simplicity constraints |
| Skipping code exploration | Add "read before proposing" |
| Test fixation | Add general solution focus |

### GPT 5.1 Issues

| Problem | Solution |
|---------|----------|
| JSON invalid | Use JSON mode in API |
| Functions not called | Check function definitions |
| Wrong temperature effects | Adjust temperature setting |

### Haiku Issues

| Problem | Solution |
|---------|----------|
| Quality too low | Upgrade to Sonnet |
| Complex task failing | Task too hard for Haiku |
| Nuance missed | Add explicit examples |

## Debugging Process

### Step 1: Isolate the Problem
```
Test with minimal prompt
Add components one by one
Identify which addition causes issues
```

### Step 2: Compare Expected vs Actual
```
Expected output: [What you wanted]
Actual output: [What you got]
Gap: [Specific differences]
```

### Step 3: Apply Targeted Fix
```
Based on gap, apply relevant solution from this guide
Change ONE thing at a time
Re-test after each change
```

### Step 4: Verify and Document
```
Confirm fix works across multiple inputs
Test edge cases
Document the solution for future reference
```

## When to Change Models

Consider switching models if:

| Situation | Action |
|-----------|--------|
| Quality consistently too low | Upgrade (Haiku → Sonnet → Opus) |
| Cost too high for quality needed | Downgrade if acceptable |
| Task fundamentally too complex | Use Opus or chain prompts |
| Speed critical and quality okay | Use faster model |
| Multimodal needed | Use Gemini Pro or Opus |

## Prevention Best Practices

1. **Always include examples** - Prevent format inconsistency
2. **Define success explicitly** - Prevent wrong focus
3. **Specify constraints** - Prevent verbosity issues
4. **Add domain context** - Prevent technical errors
5. **Request verification** - Prevent hallucinations
6. **Match model to task** - Prevent capability issues
