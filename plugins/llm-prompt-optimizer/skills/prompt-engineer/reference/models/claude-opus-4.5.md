# Claude Opus 4.5 Optimization Guide

## Overview

Claude Opus 4.5 is Anthropic's most capable model, excelling at complex reasoning, research synthesis, creative work, and sophisticated analysis. It offers the highest quality output but at higher cost and slower speed compared to other Claude models.

## Capabilities

### Strengths

| Capability | Rating | Notes |
|------------|--------|-------|
| Complex Reasoning | Excellent | Multi-step, nuanced analysis |
| Research Synthesis | Excellent | Integrates multiple sources |
| Creative Writing | Excellent | High-quality, distinctive output |
| Vision/Multimodal | Excellent | Enhanced with crop tool |
| Code Quality | Excellent | Sophisticated architecture |
| Long Context | Excellent | 200K tokens, great utilization |
| Extended Thinking | Excellent | Deep reflection capability |
| Subagent Orchestration | Excellent | Native delegation |

### Ideal Use Cases

- Complex research and analysis projects
- High-quality creative content generation
- Sophisticated multi-step reasoning
- Image understanding and analysis
- Long-horizon autonomous tasks
- Executive-level document creation
- Architecture and design decisions

### When NOT to Use Opus

- Simple classification tasks (use Haiku)
- High-volume, cost-sensitive workloads (use Haiku)
- Speed-critical applications (use Sonnet or Haiku)
- Routine code generation (use Sonnet)
- Budget-constrained projects

## Key Optimizations

### 1. Avoiding Over-Engineering

Opus has a tendency to create extra files, add unnecessary abstractions, or build in flexibility that wasn't requested.

**Add this to prompts:**

```xml
<avoid_over_engineering>
Avoid over-engineering. Only make changes that are directly requested or
clearly necessary. Keep solutions simple and focused.

Don't add features, refactor code, or make "improvements" beyond what was asked.
A bug fix doesn't need surrounding code cleaned up. A simple feature doesn't
need extra configurability.

Don't add error handling, fallbacks, or validation for scenarios that can't
happen. Trust internal code and framework guarantees. Only validate at system
boundaries (user input, external APIs).

Don't create helpers, utilities, or abstractions for one-time operations.
Don't design for hypothetical future requirements. The right amount of
complexity is the minimum needed for the current task.
</avoid_over_engineering>
```

### 2. Encouraging Code Exploration

Opus can be overly conservative when exploring code, sometimes proposing solutions without looking at the codebase.

**Add this to prompts:**

```xml
<explore_code_thoroughly>
ALWAYS read and understand relevant files before proposing code edits. Do not
speculate about code you have not inspected. If a file is referenced, you MUST
open and inspect it before explaining or proposing fixes. Be rigorous and
persistent in searching code for key facts. Thoroughly review the style,
conventions, and abstractions of the codebase before implementing.
</explore_code_thoroughly>
```

### 3. Minimizing Hallucinations

Opus already has good factual grounding, but this can be enhanced:

```xml
<investigate_before_answering>
Never speculate about code you have not opened. If a specific file is referenced,
you MUST read the file before answering. Make sure to investigate and read
relevant files BEFORE answering questions about the codebase. Never make claims
about code before investigating. Give grounded, hallucination-free answers.
</investigate_before_answering>
```

### 4. Leveraging Extended Thinking

Use Opus's thinking capabilities for reflection:

```
After receiving tool results, carefully reflect on their quality and determine
optimal next steps before proceeding. Use your thinking to plan and iterate
based on this new information, and then take the best next action.
```

**Important:** When extended thinking is disabled, avoid the word "think" and variants. Use:
- "consider"
- "analyze"
- "evaluate"
- "reflect on"
- "reason through"

### 5. Vision Capabilities

Opus has improved vision. For better performance:

```xml
<vision_approach>
When analyzing images, consider using a crop tool or skill to zoom in on
relevant regions. Breaking down complex images into focused areas improves
accuracy significantly.
</vision_approach>
```

### 6. Subagent Orchestration

Opus naturally delegates to subagents when beneficial. To adjust:

**More conservative:**
```
Only delegate to subagents when the task clearly benefits from a separate
agent with a new context window.
```

**Let it orchestrate naturally:**
(No special instruction needed—Opus does this well by default)

## Prompt Patterns for Opus

### Research and Synthesis

```xml
<context>
You are conducting deep research on [topic] for [audience].
This requires synthesizing multiple perspectives and sources.
</context>

<research_approach>
Search for information systematically. As you gather data, develop
competing hypotheses. Track confidence levels in your findings.
Regularly self-critique your approach and plan. Update research notes
to persist information and provide transparency. Break down complex
questions systematically.
</research_approach>

<output_requirements>
Provide a comprehensive analysis that:
- Integrates multiple perspectives
- Acknowledges uncertainty where appropriate
- Offers actionable insights
- Includes supporting evidence
</output_requirements>
```

### Complex Analysis

```xml
<task>
Analyze [complex topic] considering multiple dimensions.
</task>

<analysis_framework>
1. Identify key factors and stakeholders
2. Examine relationships and dependencies
3. Consider second-order effects
4. Evaluate trade-offs explicitly
5. Provide weighted recommendations
</analysis_framework>

<quality_standards>
- Depth over superficiality
- Acknowledge complexity and nuance
- Support conclusions with reasoning
- Consider counterarguments
</quality_standards>
```

### Creative Excellence

```xml
<creative_brief>
Create [content type] that is distinctive and high-quality.
</creative_brief>

<creative_guidance>
Focus on:
- Original perspective, not generic approaches
- Distinctive voice and style
- Depth and substance over surface appeal
- Thoughtful structure and pacing
</creative_guidance>

<avoid>
- Generic, predictable patterns
- Clichéd approaches
- Superficial treatment of complex topics
</avoid>
```

### Architecture and Design

```xml
<design_task>
Design a [system/architecture] for [requirements].
</design_task>

<design_principles>
- Favor simplicity over premature optimization
- Consider maintainability and extensibility
- Evaluate trade-offs explicitly
- Document key decisions and rationale
</design_principles>

<constraints>
[Specific constraints and requirements]
</constraints>
```

## Multi-Context Window Workflows

For long projects spanning multiple sessions:

### First Context Window

Set up the framework:
- Write tests in structured format (e.g., tests.json)
- Create setup scripts (e.g., init.sh)
- Establish state tracking files

### Subsequent Windows

Start fresh with clear instructions:
```
Review progress.txt, tests.json, and git logs.
Run through integration tests before implementing new features.
Continue from where previous session ended.
```

### State Management

```xml
<state_tracking>
Use structured formats (JSON) for test results and task status.
Use unstructured text for progress notes.
Use git for checkpointing and state recovery.
Focus on incremental progress—a few things at a time.
</state_tracking>
```

## Communication Style

Opus provides fact-based, direct communication:
- More grounded and less self-celebratory
- Focuses on actual accomplishments
- May skip summaries for efficiency

**If you want more visibility:**
```
After completing tool operations, provide a quick summary of the work done.
```

## Cost and Performance

| Metric | Value |
|--------|-------|
| Input | $15/million tokens |
| Output | $75/million tokens |
| Context Window | 200K tokens |
| Speed | Slowest Claude model |
| Quality | Highest Claude model |

### Cost Optimization

- Use Opus for quality-critical stages
- Delegate simple tasks to Sonnet/Haiku
- Cache common operations where possible
- Consider prompt length optimization

## When to Choose Opus Over Sonnet

| Scenario | Choose Opus |
|----------|-------------|
| Research requiring synthesis | Yes |
| Complex architectural decisions | Yes |
| High-stakes creative content | Yes |
| Deep analysis with nuance | Yes |
| Multi-step autonomous work | Yes |
| Routine coding tasks | No (use Sonnet) |
| Simple Q&A | No (use Haiku) |
| Cost-sensitive projects | No |

## Quick Reference

**Optimize Opus by:**
- Adding over-engineering prevention
- Encouraging code exploration
- Leveraging thinking capabilities
- Using structured research approaches
- Managing multi-window workflows

**Avoid:**
- Using for simple tasks
- Ignoring its tendency to over-build
- Skipping code exploration guidance
- Wasting tokens on verbose prompts

## Summary

Claude Opus 4.5 delivers the highest quality output for complex tasks. Optimize by:
1. Preventing over-engineering with explicit constraints
2. Encouraging thorough code exploration
3. Leveraging extended thinking for reflection
4. Using structured approaches for research
5. Managing long-horizon projects with state tracking

Use Opus when quality matters most and the task justifies the cost.
