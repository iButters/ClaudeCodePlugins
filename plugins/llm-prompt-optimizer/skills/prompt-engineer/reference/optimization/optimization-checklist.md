# Prompt Optimization Checklist

## Pre-Submission Checklist

Use this checklist before finalizing any prompt. Each section should score "Yes" or have a documented reason for exception.

## 1. Clarity

### Context
- [ ] Is the purpose of the prompt clear?
- [ ] Is background information provided?
- [ ] Is the intended audience/use case stated?
- [ ] Are relevant constraints mentioned?

### Instructions
- [ ] Is the main task explicitly stated?
- [ ] Are sub-tasks clearly identified?
- [ ] Is the scope defined (what's included/excluded)?
- [ ] Are priorities clear if multiple things requested?

### Format
- [ ] Is the output format specified?
- [ ] Is length/depth defined?
- [ ] Is structure clear (list, paragraphs, table)?
- [ ] Are required components mentioned?

### Success Criteria
- [ ] Would you know if the response is good?
- [ ] Are quality standards defined?
- [ ] Are examples of what you want provided?
- [ ] Are common mistakes/pitfalls mentioned?

## 2. Technique Application

### XML Tags
- [ ] Are tags used when prompt has 3+ components?
- [ ] Are tags properly nested and closed?
- [ ] Are tag names semantic and descriptive?
- [ ] Is information organized logically within tags?

### Role Prompting
- [ ] Is role in system prompt (not user message)?
- [ ] Is role specific to the domain?
- [ ] Does role include relevant context?
- [ ] Is role appropriate for the task?

### Examples (Multishot)
- [ ] Are 3-5 examples provided (when needed)?
- [ ] Do examples cover diverse scenarios?
- [ ] Are examples in consistent format?
- [ ] Do examples show edge cases?

### Chain of Thought
- [ ] Is step-by-step reasoning requested (when beneficial)?
- [ ] Is thinking separated from answer?
- [ ] Is thinking structure provided if needed?
- [ ] Is reasoning depth appropriate for task?

### Prompt Chaining
- [ ] Are complex tasks broken into stages?
- [ ] Are handoffs between stages clear?
- [ ] Is each stage single-purpose?
- [ ] Is validation between stages planned?

## 3. Model-Specific Optimization

### For Claude Opus 4.5
- [ ] Is over-engineering prevention included?
- [ ] Is code exploration encouraged?
- [ ] Is extended thinking leveraged?
- [ ] Are vision capabilities utilized (if relevant)?

### For Claude Sonnet 4.5
- [ ] Are instructions extremely explicit?
- [ ] Is action vs suggestion behavior controlled?
- [ ] Is parallel tool calling considered?
- [ ] Is test fixation prevention included (if coding)?

### For Claude Haiku 4.5
- [ ] Is prompt concise?
- [ ] Is context minimized to essentials?
- [ ] Is output format simple and clear?
- [ ] Is task appropriately simple?

### For GPT 5.1
- [ ] Is system message used effectively?
- [ ] Is JSON mode enabled (if structured output)?
- [ ] Are function definitions clear?
- [ ] Is temperature appropriate?

### For GPT 5.1 Codex
- [ ] Is language/framework specified?
- [ ] Are type definitions provided?
- [ ] Is existing code pattern shown?
- [ ] Are test cases included?

### For Gemini Pro 3.0
- [ ] Is multimodal utilized (if applicable)?
- [ ] Is context caching considered?
- [ ] Is formatting explicit?
- [ ] Is search grounding used (if current info needed)?

## 4. Common Issues Prevention

### Consistency
- [ ] Will output format be consistent across runs?
- [ ] Are ambiguous terms defined?
- [ ] Are boundaries between categories clear?
- [ ] Is the prompt deterministic enough?

### Completeness
- [ ] Is all necessary information provided?
- [ ] Are edge cases addressed?
- [ ] Is error handling specified?
- [ ] Are fallback behaviors defined?

### Quality
- [ ] Is output length appropriate?
- [ ] Is detail level specified?
- [ ] Are quality standards defined?
- [ ] Is verification method identified?

## 5. Testing Readiness

### Test Cases
- [ ] Can you test with sample inputs?
- [ ] Do you have expected outputs to compare?
- [ ] Are edge cases identified for testing?
- [ ] Is success measurable?

### Iteration Plan
- [ ] Do you know what to change if results are poor?
- [ ] Are potential failure modes identified?
- [ ] Is the prompt modifiable?
- [ ] Is feedback collection planned?

## Quick Validation

### Essential Checks (Must Pass)
1. **Clear task**: Would someone else understand what to do?
2. **Complete context**: Is all necessary background provided?
3. **Defined output**: Is expected format specified?
4. **Appropriate techniques**: Are chosen techniques justified?

### Quality Checks (Should Pass)
1. **Examples**: Are examples provided when format matters?
2. **Model-specific**: Are model optimizations applied?
3. **Edge cases**: Are unusual scenarios addressed?
4. **Testing**: Can results be validated?

## Scoring Guide

| Score | Meaning | Action |
|-------|---------|--------|
| 90-100% | Production ready | Deploy |
| 70-89% | Good but improvable | Minor adjustments |
| 50-69% | Needs work | Significant revision |
| <50% | Major issues | Redesign |

## Common Fixes

| Issue | Quick Fix |
|-------|-----------|
| Inconsistent format | Add examples |
| Missing information | Improve context |
| Wrong focus | Clarify success criteria |
| Too verbose | Add length constraints |
| Too brief | Request more detail |
| Errors in reasoning | Add chain of thought |
| Complex task failing | Use prompt chaining |

## Final Review Questions

Before submitting, ask:

1. **Clarity**: Would a new team member understand this prompt?
2. **Completeness**: Is anything important missing?
3. **Appropriateness**: Is the technique/model match correct?
4. **Testability**: Can I verify if this works?
5. **Maintainability**: Can this be improved later?

## Checklist Summary

```
□ Context: Purpose, background, audience, constraints
□ Instructions: Task, sub-tasks, scope, priorities
□ Format: Output structure, length, components
□ Criteria: Success definition, quality standards
□ Techniques: XML, role, examples, CoT, chaining
□ Model-specific: Appropriate optimizations applied
□ Prevention: Consistency, completeness, quality
□ Testing: Sample inputs, expected outputs, edge cases
```
