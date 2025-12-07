# Multishot Prompting (Few-Shot Learning)

## Overview

Multishot prompting provides examples that demonstrate the desired input-output pattern. This technique dramatically improves consistency, format adherence, and quality—especially for nuanced or ambiguous tasks.

## When to Use Multishot Prompting

Apply multishot prompting when:
- Output format consistency is critical
- Task involves subjective judgment
- Style or tone must be specific
- Classification categories need clarification
- Complex transformations are required
- Zero-shot produces inconsistent results

## Impact

Well-designed examples typically improve:
- **Format consistency**: 40-60%
- **Style adherence**: 50-70%
- **Classification accuracy**: 20-40%
- **Edge case handling**: Significant when examples cover them

## Core Principles

### 1. Examples Teach by Demonstration

Examples show what you want more effectively than descriptions:

```
# Description alone (less effective)
Classify customer feedback as positive, negative, or neutral.
Consider the overall sentiment, not just individual words.

# With examples (much more effective)
Classify customer feedback as positive, negative, or neutral.

Examples:
Input: "The product works, but I expected more for the price."
Output: neutral

Input: "Absolutely love it! Best purchase I've made all year!"
Output: positive

Input: "Complete waste of money. It broke after two days."
Output: negative

Now classify: "It's okay, nothing special but gets the job done."
```

### 2. Quality Over Quantity

3-5 well-chosen examples beat 10 mediocre ones:

- Cover the most common cases
- Include at least one edge case
- Show the exact format you want
- Demonstrate nuances in judgment

### 3. Diversity Matters

Examples should cover different scenarios:

```
# Good: Diverse examples
Example 1: Short positive review → positive
Example 2: Long mixed review with complaints → neutral
Example 3: Short angry complaint → negative
Example 4: Sarcastic "positive" → negative (edge case)
Example 5: Technical issue report without emotion → neutral

# Bad: Homogeneous examples
Example 1: "Great product!" → positive
Example 2: "Love it!" → positive
Example 3: "Amazing!" → positive
(All same category, all same style)
```

## Example Structures

### Basic Input-Output Format

```
<examples>
  <example>
    <input>The quarterly sales exceeded projections by 15%.</input>
    <output>positive business development</output>
  </example>
  <example>
    <input>Two key engineers resigned this month.</input>
    <output>negative personnel change</output>
  </example>
</examples>
```

### With Reasoning (Improved Transparency)

```
<examples>
  <example>
    <input>The product arrived damaged but customer service was helpful.</input>
    <sentiment>neutral</sentiment>
    <reasoning>Negative experience with product balanced by positive service</reasoning>
  </example>
</examples>
```

### Multi-Part Output

```
<examples>
  <example>
    <email>Hi, can you send the report by Friday?</email>
    <response>
      <priority>medium</priority>
      <category>request</category>
      <action_required>send report</action_required>
      <deadline>Friday</deadline>
    </response>
  </example>
</examples>
```

## How Many Examples?

| Task Type | Recommended Examples | Reason |
|-----------|---------------------|--------|
| Simple classification | 3-4 | One per category + edge case |
| Complex classification | 5-7 | Cover nuances and boundaries |
| Format transformation | 2-3 | Show the pattern clearly |
| Style matching | 3-5 | Establish consistent voice |
| Subjective judgment | 5+ | Calibrate the decision boundary |

## Selecting Good Examples

### Criteria for Strong Examples

1. **Representative**: Cover common scenarios
2. **Diverse**: Different types, lengths, styles
3. **Boundary-defining**: Show edge cases
4. **Consistent**: All follow the same rules
5. **Clear**: Unambiguous classification

### Example Selection Process

1. Identify the main categories/outputs
2. Select 1-2 clear examples for each
3. Identify potential edge cases
4. Add examples for tricky boundaries
5. Review for consistency and diversity

## Common Patterns

### Classification with Multiple Categories

```
Classify support tickets into: billing, technical, account, other

<examples>
<example>
<ticket>I was charged twice for my subscription</ticket>
<category>billing</category>
</example>

<example>
<ticket>The app crashes when I try to upload files</ticket>
<category>technical</category>
</example>

<example>
<ticket>How do I change my email address?</ticket>
<category>account</category>
</example>

<example>
<ticket>Do you offer discounts for non-profits?</ticket>
<category>other</category>
</example>
</examples>
```

### Format Transformation

```
Convert informal notes to formal meeting minutes.

<examples>
<example>
<notes>talked about Q3 goals, john wants to increase sales 20%,
mary thinks we need more marketing budget</notes>
<minutes>
## Meeting Minutes

### Q3 Goals Discussion
- John proposed a 20% sales increase target
- Mary recommended expanding the marketing budget

### Action Items
- [Pending] Define specific Q3 targets
</minutes>
</example>
</examples>
```

### Tone/Style Matching

```
Rewrite corporate messages in a friendly, casual tone.

<examples>
<example>
<corporate>Please be advised that system maintenance will occur
on Saturday from 2:00 AM to 6:00 AM EST.</corporate>
<casual>Heads up! We're doing some system updates this Saturday
between 2-6 AM EST. Things might be a bit slow during that time.</casual>
</example>

<example>
<corporate>We regret to inform you that your request has been denied.</corporate>
<casual>Sorry, but we weren't able to approve your request this time.</casual>
</example>
</examples>
```

### Structured Extraction

```
Extract key information from job postings.

<examples>
<example>
<posting>
Senior Software Engineer - Remote
TechCorp is looking for an experienced developer with 5+ years in Python.
Salary: $150k-180k. Must have experience with AWS and PostgreSQL.
</posting>
<extracted>
{
  "title": "Senior Software Engineer",
  "location": "Remote",
  "company": "TechCorp",
  "experience": "5+ years",
  "skills": ["Python", "AWS", "PostgreSQL"],
  "salary_range": "$150k-180k"
}
</extracted>
</example>
</examples>
```

## Edge Cases and Boundaries

### Handling Ambiguous Cases

Include examples that show how to handle ambiguity:

```
<example>
<input>This is fine I guess</input>
<output>neutral</output>
<note>Mild sentiment defaults to neutral when truly ambiguous</note>
</example>
```

### Showing Boundaries

Demonstrate where categories split:

```
# These show the boundary between urgent and normal
<example>
<ticket>System is completely down, no one can work</ticket>
<priority>urgent</priority>
</example>

<example>
<ticket>System is slow but still functional</ticket>
<priority>normal</priority>
</example>
```

## Model-Specific Considerations

### Claude Models

Claude 4.x pays very close attention to examples:

- Examples strongly influence output format
- If examples are verbose, output will be verbose
- Include examples that match your desired style exactly
- Quality of examples directly affects quality of output

### GPT Models

GPT responds well to few-shot prompting:

- Consistent format across examples helps
- JSON examples work especially well with JSON mode
- Clear input-output pairing is important

### Gemini Models

Gemini benefits from clear examples:

- Explicit format demonstration helps
- Works well with structured examples

## Common Mistakes

### 1. Inconsistent Examples

```
# Wrong: Different formats
Example 1: positive
Example 2: POSITIVE
Example 3: Positive sentiment

# Right: Consistent format
Example 1: positive
Example 2: negative
Example 3: neutral
```

### 2. Examples Don't Match Instructions

```
# Wrong: Instructions say 3 categories, examples show 4
Instructions: Classify as positive, negative, or neutral
Example output: somewhat_positive  # Not in the categories!
```

### 3. Missing Edge Cases

```
# Only showing clear-cut examples
Example: "I love this!" → positive
Example: "I hate this!" → negative
# What about: "I love the design but hate the price"?
```

### 4. Too Few Examples for Complex Tasks

```
# One example for multi-category classification
Example: Technical issue → technical
# Doesn't show billing, account, or other categories
```

## Integration with Other Techniques

### With XML Tags

```xml
<task>
Classify customer feedback by department.
</task>

<examples>
  <example>
    <feedback>The checkout process was confusing</feedback>
    <department>product</department>
  </example>
  <example>
    <feedback>I was overcharged $20</feedback>
    <department>billing</department>
  </example>
</examples>

<input>
[Customer feedback to classify]
</input>
```

### With Chain of Thought

```xml
<examples>
  <example>
    <input>Is 847 divisible by 7?</input>
    <thinking>
    847 ÷ 7 = 121
    121 × 7 = 847 ✓
    </thinking>
    <answer>Yes, 847 is divisible by 7</answer>
  </example>
</examples>
```

### With Role Prompting

```
System: You are a legal document analyst.

Examples of how to summarize contract clauses:

<example>
<clause>Party A shall indemnify and hold harmless Party B...</clause>
<summary>A must protect B from legal claims</summary>
</example>
```

## Quick Reference

| Scenario | Examples Needed | Focus |
|----------|-----------------|-------|
| Binary classification | 2-3 | Clear contrast |
| Multi-class (3-5 classes) | 4-6 | One+ per class |
| Subjective judgment | 5-7 | Boundary cases |
| Format transformation | 2-4 | Pattern clarity |
| Style matching | 3-5 | Voice consistency |

## Summary

Multishot prompting uses examples to:
- Demonstrate desired output format
- Show classification boundaries
- Establish style and tone
- Handle edge cases
- Improve consistency

For best results:
- Use 3-5 high-quality, diverse examples
- Cover edge cases and boundaries
- Keep format consistent across examples
- Match example style to desired output
- Include reasoning when helpful
