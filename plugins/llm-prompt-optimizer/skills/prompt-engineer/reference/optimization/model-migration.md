# Model Migration Guide

## Overview

This guide covers adapting prompts when switching between LLM models. Each model family has different strengths, behaviors, and optimal prompting patterns.

## Migration Principles

### 1. Understand the Differences

Before migrating, understand key differences:
- System prompt handling
- Instruction following precision
- Output format tendencies
- Special features (JSON mode, thinking, etc.)

### 2. Test Incrementally

Don't migrate blind:
1. Test with representative examples
2. Compare outputs carefully
3. Adjust prompts based on results
4. Verify edge cases

### 3. Leverage New Capabilities

Each model may offer unique features:
- Claude: Extended thinking, parallel tools
- GPT: JSON mode, function calling
- Gemini: Context caching, multimodal

## Claude → GPT Migration

### System Prompt Differences

**Claude:**
- System prompt sets persistent context
- Strong behavioral influence
- Works well with XML in system prompt

**GPT:**
- System message similarly used
- May need more explicit instruction
- JSON mode for structured output

### Prompt Adjustments

| Claude Pattern | GPT Equivalent |
|---------------|----------------|
| XML tags | Markdown headers or ### delimiters |
| Extended thinking | Request step-by-step reasoning |
| `<thinking>` tags | "Think step by step before answering" |
| Parallel tool calls | Function calling |

### Example Migration

**Claude Version:**
```xml
<context>
You're analyzing customer feedback data.
</context>

<task>
Classify each feedback item into categories.
</task>

<output_format>
Return as structured analysis.
</output_format>
```

**GPT Version:**
```
### CONTEXT ###
You're analyzing customer feedback data.

### TASK ###
Classify each feedback item into categories.

### OUTPUT FORMAT ###
Return as JSON with this structure:
{"category": "...", "sentiment": "...", "summary": "..."}
```

### Key Adjustments

1. **Replace XML with delimiters** - GPT works well with `###` sections
2. **Add JSON mode** - Use `response_format={"type": "json_object"}`
3. **Explicit instruction following** - Be even more explicit
4. **Temperature adjustment** - May need different temperature

## GPT → Claude Migration

### Leveraging Claude Strengths

**Gains when moving to Claude:**
- Better agentic capabilities
- Larger context window (200K)
- Extended thinking (Opus)
- More natural conversation

### Prompt Adjustments

| GPT Pattern | Claude Equivalent |
|------------|-------------------|
| JSON mode | XML tags + format specification |
| Function calling | Native tool use |
| `###` delimiters | XML tags (optional, both work) |
| System message | System prompt (similar) |

### Example Migration

**GPT Version:**
```
System: You are a helpful assistant that always responds in JSON.

User:
### INPUT ###
[Data to process]

### TASK ###
Extract key entities and their relationships.

Return valid JSON.
```

**Claude Version:**
```xml
System: You are an expert data analyst.

User:
<input>
[Data to process]
</input>

<task>
Extract key entities and their relationships.
</task>

<output_format>
Structure your response as:
<entities>List of entities</entities>
<relationships>List of relationships</relationships>
</output_format>
```

### Key Adjustments

1. **XML tags optional** - Claude handles both XML and markdown
2. **More explicit for 4.x** - Claude 4.x follows instructions precisely
3. **Leverage context** - Can use full 200K context
4. **Add thinking guidance** - For complex tasks

## Claude → Gemini Migration

### Key Differences

**Gemini Strengths:**
- Native multimodal
- Context caching
- Search grounding
- Video support

**Adjustments Needed:**
- Explicit formatting instructions
- Clear structure specification
- Consider caching opportunities

### Example Migration

**Claude Version:**
```xml
<context>
Analyze this document for key insights.
</context>

<document>
[Document content]
</document>

<task>
Extract main themes and recommendations.
</task>
```

**Gemini Version:**
```
## Context
Analyze this document for key insights.

## Document
[Document content]

## Task
Extract main themes and recommendations.

## Output Format
1. **Main Themes** (bulleted list)
2. **Key Findings** (numbered list)
3. **Recommendations** (numbered list)

Use clear markdown formatting as shown.
```

### Key Adjustments

1. **Explicit formatting** - Gemini benefits from format examples
2. **Consider caching** - Cache repeated context
3. **Multimodal opportunities** - Add images/video if relevant
4. **Search grounding** - For current information

## Gemini → Claude Migration

### Leveraging Claude Capabilities

**Gains when moving to Claude:**
- Deeper reasoning (especially Opus)
- Better code understanding
- Extended thinking
- Stronger agentic behavior

### Example Migration

**Gemini Version:**
```
Analyze this image and document together:
[IMAGE]
[DOCUMENT]

Provide a comprehensive analysis.
```

**Claude Version:**
```xml
<context>
Analyze the provided image and document together.
</context>

<task>
Provide a comprehensive analysis covering:
1. Visual elements in the image
2. Key points from the document
3. Connections between image and text
4. Overall insights
</task>

<quality>
Be thorough and specific. Reference specific visual elements
and document sections in your analysis.
</quality>
```

## Cross-Family Migration Checklist

### Before Migration

- [ ] Identify source model's unique features used
- [ ] Identify target model's unique features to leverage
- [ ] Prepare test cases with expected outputs
- [ ] Plan for capability differences

### During Migration

- [ ] Adjust prompt structure (XML vs markdown vs delimiters)
- [ ] Update format specifications
- [ ] Modify special instructions (thinking, JSON, etc.)
- [ ] Adjust for precision differences

### After Migration

- [ ] Test with representative inputs
- [ ] Compare output quality
- [ ] Verify edge case handling
- [ ] Document any quality differences

## Common Migration Issues

### Issue: Format Inconsistency

**Cause:** Different default formatting tendencies

**Solution:**
- Add explicit format examples
- Use structured output features (JSON mode)
- Provide more format detail in prompt

### Issue: Quality Difference

**Cause:** Models have different capability levels

**Solution:**
- Match task complexity to model capability
- Adjust expectations appropriately
- Consider prompt chaining for complex tasks

### Issue: Missing Features

**Cause:** Target model lacks source feature

**Solution:**
- Find equivalent capability
- Adjust prompt to work without feature
- Consider if migration is appropriate

### Issue: Different Behavior

**Cause:** Models interpret instructions differently

**Solution:**
- Be more explicit in instructions
- Test and adjust iteratively
- Document behavioral differences

## Model-Specific Migration Tips

### Migrating TO Claude 4.x

- Be extremely explicit (more than before)
- Request "above and beyond" if desired
- Provide context for better understanding
- Watch example quality carefully

### Migrating TO GPT

- Use JSON mode for structured output
- Define functions clearly
- Use consistent delimiters
- Adjust temperature for task

### Migrating TO Gemini

- Leverage multimodal where possible
- Use context caching for repeated queries
- Be explicit about formatting
- Consider search grounding

## Quick Reference

| From | To | Key Changes |
|------|-----|-------------|
| Claude → GPT | Add JSON mode, use ### delimiters |
| GPT → Claude | Can use XML, leverage larger context |
| Claude → Gemini | Explicit formatting, consider caching |
| Gemini → Claude | Can use XML, leverage thinking |
| Any → Haiku | Simplify, shorten, focus on essentials |
| Haiku → Any | Can add complexity, detail |

## Summary

Successful migration requires:
1. Understanding model differences
2. Adjusting prompt patterns appropriately
3. Testing thoroughly with representative cases
4. Leveraging unique capabilities of target model
5. Documenting quality differences for future reference
