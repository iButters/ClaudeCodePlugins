# Prompt Chaining

## Overview

Prompt chaining breaks complex tasks into sequential subtasks, where each prompt's output feeds into the next. This technique manages complexity, improves quality, and enables sophisticated multi-stage workflows.

## When to Use Prompt Chaining

Apply prompt chaining when:
- Task has distinct stages or phases
- Single prompt would be too complex
- Different expertise needed at each stage
- Quality control needed between stages
- Task requires iteration or refinement
- Output of one step is input to another

## Impact

Prompt chaining provides:
- **Quality**: Each stage can be optimized independently
- **Reliability**: Errors contained to single stage
- **Flexibility**: Stages can use different models
- **Control**: Human review possible between stages
- **Debugging**: Problems isolated to specific step

## Core Principles

### 1. Single Responsibility per Prompt

Each prompt should do one thing well:

```
# Bad: Too much in one prompt
"Research the topic, write an outline, draft the article,
edit for style, add citations, format for publication"

# Good: Chain of focused prompts
Prompt 1: Research key points
Prompt 2: Create outline from research
Prompt 3: Draft article from outline
Prompt 4: Edit for style
Prompt 5: Add citations and format
```

### 2. Clear Handoffs

Define what passes between stages:

```xml
<stage_1_output>
- Key finding 1: [content]
- Key finding 2: [content]
- Key finding 3: [content]
</stage_1_output>

<stage_2_input>
Using the research above, create a structured outline:
[Instructions for outline]
</stage_2_input>
```

### 3. Validation Between Stages

Check output quality before proceeding:

```
After each stage, verify:
- Output meets stage requirements
- Format is correct for next stage
- No critical errors or omissions
- Quality threshold is met
```

## Chain Design Patterns

### Linear Chain

Simple sequential processing:

```
[Input] → [Stage 1] → [Stage 2] → [Stage 3] → [Output]

Example:
Document → Extract Facts → Analyze Facts → Generate Summary → Final Report
```

### Parallel-Then-Merge

Process multiple aspects simultaneously, then combine:

```
           ┌→ [Technical Analysis] ─┐
[Input] ───┼→ [Business Analysis] ──┼→ [Merge] → [Output]
           └→ [Risk Analysis] ──────┘

Example:
Product Idea → [Technical Feasibility]   ┐
            → [Market Analysis]          ├→ [Combined Assessment]
            → [Cost Estimation]          ┘
```

### Iterative Refinement

Cycle through improvement stages:

```
[Draft] → [Review] → [Revise] → [Review] → [Final]
              ↑          │
              └──────────┘ (if issues found)
```

### Hierarchical Chain

Break down, process, recombine:

```
[Document] → [Split into Sections]
                   │
         ┌─────────┼─────────┐
         ↓         ↓         ↓
    [Analyze 1] [Analyze 2] [Analyze 3]
         │         │         │
         └─────────┼─────────┘
                   ↓
           [Synthesize All]
                   ↓
              [Final Report]
```

## Common Chain Templates

### Research and Synthesis Chain

```
Stage 1: Information Gathering
Input: Research question
Task: Search and collect relevant information
Output: Raw findings with sources

Stage 2: Analysis
Input: Raw findings
Task: Identify themes, patterns, contradictions
Output: Analyzed findings with insights

Stage 3: Synthesis
Input: Analyzed findings
Task: Create coherent narrative
Output: Synthesized report

Stage 4: Executive Summary
Input: Full report
Task: Distill key points for executives
Output: One-page summary
```

### Code Development Chain

```
Stage 1: Requirements Analysis
Input: Feature request
Task: Extract technical requirements
Output: Technical specification

Stage 2: Architecture Design
Input: Technical specification
Task: Design component structure
Output: Architecture document

Stage 3: Implementation
Input: Architecture document
Task: Write code
Output: Code files

Stage 4: Testing
Input: Code files
Task: Generate and run tests
Output: Test results

Stage 5: Documentation
Input: Code + Architecture
Task: Write documentation
Output: README and API docs
```

### Content Creation Chain

```
Stage 1: Outline
Input: Topic and audience
Task: Create structured outline
Output: Detailed outline

Stage 2: Draft
Input: Outline
Task: Write first draft
Output: Complete draft

Stage 3: Edit
Input: Draft
Task: Edit for clarity and style
Output: Edited draft

Stage 4: Review
Input: Edited draft
Task: Check facts, grammar, flow
Output: Review notes

Stage 5: Final Polish
Input: Edited draft + Review notes
Task: Apply final corrections
Output: Publication-ready content
```

### Decision Analysis Chain

```
Stage 1: Problem Definition
Input: Situation description
Task: Clarify the decision to be made
Output: Clear problem statement + criteria

Stage 2: Option Generation
Input: Problem statement
Task: Generate possible solutions
Output: List of options

Stage 3: Evaluation
Input: Options + Criteria
Task: Evaluate each option against criteria
Output: Evaluation matrix

Stage 4: Risk Assessment
Input: Top options
Task: Identify risks for each
Output: Risk analysis

Stage 5: Recommendation
Input: Evaluation + Risks
Task: Make final recommendation
Output: Decision with reasoning
```

## Implementing Chains

### Using XML for Handoffs

```xml
<!-- Stage 1 Output -->
<research_output>
  <finding id="1">
    <topic>Market size</topic>
    <content>The market is valued at $5B...</content>
    <source>Industry Report 2024</source>
  </finding>
  <finding id="2">
    <!-- More findings -->
  </finding>
</research_output>

<!-- Stage 2 Input -->
<stage_2_instructions>
Using the research findings above, identify the three most
significant market trends. For each trend:
1. Name the trend
2. Summarize the supporting evidence
3. Assess its impact (high/medium/low)
</stage_2_instructions>
```

### State Management

Track what's been done and what's needed:

```xml
<chain_state>
  <completed_stages>
    <stage name="research" status="complete"/>
    <stage name="analysis" status="complete"/>
  </completed_stages>
  <current_stage name="synthesis"/>
  <pending_stages>
    <stage name="review"/>
    <stage name="final"/>
  </pending_stages>
</chain_state>

<current_input>
[Output from previous stage]
</current_input>

<current_task>
[Instructions for current stage]
</current_task>
```

### Error Handling

Plan for failures at each stage:

```xml
<stage_validation>
  <required_elements>
    - At least 3 findings
    - Each finding has a source
    - No contradictions in data
  </required_elements>

  <on_failure>
    If validation fails:
    1. Identify the missing or incorrect elements
    2. Request correction or additional research
    3. Re-run stage with corrections
  </on_failure>
</stage_validation>
```

## Model Selection for Chains

Different stages may benefit from different models:

| Stage Type | Recommended Model | Reason |
|------------|------------------|--------|
| Research/Analysis | Opus 4.5 | Deep reasoning |
| Code Generation | Sonnet 4.5 or Codex | Coding strength |
| Quick Classification | Haiku 4.5 | Speed, cost |
| Creative Writing | Opus 4.5 | Quality |
| Data Extraction | Haiku 4.5 | Simple, fast |
| Final Review | Opus 4.5 | Thoroughness |

## Optimization Strategies

### Parallel Processing

Run independent stages simultaneously:

```
Instead of:
A → B → C → D (sequential, slow)

When B and C don't depend on each other:
A → [B, C in parallel] → D (faster)
```

### Early Filtering

Reduce work for later stages:

```
Stage 1: Quick filter (Haiku) - remove obviously irrelevant items
Stage 2: Detailed analysis (Sonnet) - only on filtered items
Stage 3: Deep review (Opus) - only on top candidates
```

### Checkpointing

Save state for long chains:

```
After each stage:
1. Save output to file/database
2. Record chain state
3. Enable restart from any point
```

## Common Mistakes

### 1. Stages Too Large

```
# Bad: Stage does too much
Stage 1: Research, analyze, outline, and draft the article

# Good: Focused stages
Stage 1: Research key points
Stage 2: Analyze and prioritize findings
Stage 3: Create outline
Stage 4: Write draft
```

### 2. Poor Handoff Design

```
# Bad: Unclear what passes between stages
Stage 1 output: "The research is done"

# Good: Structured handoff
Stage 1 output:
<findings>
  <finding>Specific content with details</finding>
  <finding>Another specific finding</finding>
</findings>
```

### 3. No Validation

```
# Bad: Just chain outputs together
output_1 → input_2 → output_2 → input_3

# Good: Validate between stages
output_1 → validate → input_2 → validate → input_3
```

### 4. Unnecessary Chaining

```
# Overkill for simple task
Chain for "What is 2 + 2?":
Stage 1: Parse the numbers
Stage 2: Identify the operation
Stage 3: Perform calculation
Stage 4: Format result

# Just ask directly
"What is 2 + 2?"
```

## Integration with Other Techniques

### Chain + CoT

Use chain of thought within each stage:

```
Stage 2: Analysis

<instructions>
Analyze the research findings step by step:
1. First, identify the main themes
2. Then, look for patterns across themes
3. Next, note any contradictions
4. Finally, draw preliminary conclusions

Show your reasoning in <thinking> tags.
</instructions>
```

### Chain + Examples

Provide examples for complex stages:

```
Stage 3: Create executive summary

<examples>
<example>
<full_report>
[Long report about market expansion]
</full_report>
<executive_summary>
Key Finding: Market opportunity of $50M identified
Recommendation: Expand to APAC region
Timeline: Q3 2025
Risk: Medium (competitive pressure)
</executive_summary>
</example>
</examples>

Now create an executive summary for:
[Current report]
```

### Chain + Role Prompting

Use different roles for different stages:

```
Stage 1:
Role: "You are a research analyst gathering data"

Stage 2:
Role: "You are a strategic advisor synthesizing findings"

Stage 3:
Role: "You are an executive communication specialist"
```

## Quick Reference

| Chain Type | Use When | Example |
|------------|----------|---------|
| Linear | Sequential processing | Draft → Edit → Review |
| Parallel | Independent analysis | Tech + Business + Risk |
| Iterative | Refinement needed | Write → Review → Revise |
| Hierarchical | Break down and combine | Analyze sections → Synthesize |

## Summary

Prompt chaining:
- Breaks complex tasks into manageable stages
- Enables quality control between stages
- Allows different models for different needs
- Improves reliability and debugability

Best practices:
- Single responsibility per stage
- Clear, structured handoffs
- Validation between stages
- Match model to stage requirements
- Only chain when complexity warrants it
