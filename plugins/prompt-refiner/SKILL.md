---
name: prompt-refiner
description: "Systematic prompt optimization using established prompt engineering frameworks. Use when: (1) User invokes /refine for quick optimization, (2) User invokes /refine-interactive for guided refinement with clarifying questions, (3) User asks to improve, optimize, or enhance a prompt for AI/LLM use."
---

# Prompt Refiner

Optimize prompts through systematic analysis using established prompt engineering principles.

## Commands

### `/refine <prompt>` — Quick Optimization
Analyze and optimize the prompt directly. Auto-detect context from content.

### `/refine-interactive <prompt>` — Guided Refinement
Ask 2-4 targeted clarifying questions first, then optimize based on gathered context.

## Workflow

### Step 1: Analyze Input Prompt

Run the prompt through each diagnostic:

| Check | Question |
|-------|----------|
| Specificity | Are there vague terms like "good", "better", "some"? |
| Context | Is background/domain information provided? |
| Objective | Is the goal explicitly stated? |
| Role | Is a persona/expertise level assigned? |
| Format | Is output structure specified? |
| Constraints | Are length, style, or scope limits set? |
| Audience | Is the target reader/user identified? |

### Step 2: Identify Issues

Common weaknesses to detect and fix:

**Vagueness** → Add specific details, quantities, examples
**Missing context** → Infer and add domain/background
**No role** → Add "You are a [expert type]" or "Act as..."
**Unclear format** → Specify output structure (list, paragraphs, JSON, etc.)
**No constraints** → Add length, scope, or style limits
**Ambiguous objective** → Restate goal explicitly
**Buried instructions** → Move critical constraints to the beginning

### Step 3: Apply Enhancements

Select techniques based on prompt type:

**For reasoning/analysis tasks:**
- Add "Think step by step" or "Break this down into steps"
- Request explanation of reasoning

**For creative tasks:**
- Add style/tone guidance
- Include constraints to focus creativity

**For technical tasks:**
- Add precision requirements
- Specify error handling expectations

**For all prompts:**
- Use positive instructions ("do X") over negative ("don't do Y")
- Put most critical instructions first (primacy effect)
- Add delimiters for multi-part prompts

### Step 4: Output

Return **only** the refined prompt in a markdown code block:

```
[Refined prompt here]
```

No explanations. No commentary. Just the improved prompt.

## Interactive Mode Questions

For `/refine-interactive`, ask 2-4 questions from this pool:

- What specific outcome do you need from this prompt?
- Who is the target audience for the output?
- What format should the output take? (list, paragraphs, code, etc.)
- What tone or style is appropriate? (formal, casual, technical, etc.)
- Are there any constraints? (length, scope, things to avoid)
- What context or background should the AI know?

Select questions based on what's missing from the prompt. Skip questions where answers are obvious from the prompt content.

## Reference

For detailed frameworks and techniques, see `references/techniques.md`.
