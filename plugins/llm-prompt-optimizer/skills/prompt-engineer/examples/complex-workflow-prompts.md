# Complex Workflow Prompt Examples

## Multi-Stage Research

### Market Research Pipeline

**Stage 1: Information Gathering**
**Model: Claude Sonnet 4.5**

```xml
<task>
Gather information about the target market.
</task>

<topic>
{{MARKET_TOPIC}}
</topic>

<gather>
1. Market size and growth trends
2. Key players and market share
3. Customer segments
4. Pricing models observed
5. Recent developments
</gather>

<output>
<findings>
[Raw information organized by category]
</findings>
<sources>
[Where information came from]
</sources>
<confidence>
[High/Medium/Low for each category]
</confidence>
</output>
```

**Stage 2: Analysis**
**Model: Claude Opus 4.5**

```xml
<task>
Analyze the gathered market research.
</task>

<input>
{{STAGE_1_OUTPUT}}
</input>

<analyze>
1. Identify patterns and trends
2. Assess competitive dynamics
3. Find market gaps and opportunities
4. Evaluate barriers to entry
5. Highlight risks and uncertainties
</analyze>

<output>
<analysis>
[Structured analysis by theme]
</analysis>
<insights>
[Key takeaways]
</insights>
<questions>
[Areas needing more research]
</questions>
</output>
```

**Stage 3: Strategic Recommendations**
**Model: Claude Opus 4.5**

```xml
<task>
Generate strategic recommendations based on analysis.
</task>

<input>
{{STAGE_2_OUTPUT}}
</input>

<synthesize>
1. Core strategic options
2. Recommended approach
3. Implementation considerations
4. Risk mitigation strategies
5. Success metrics
</synthesize>

<output_format>
## Executive Summary
[One paragraph]

## Strategic Options
[3-4 options with pros/cons]

## Recommended Approach
[Detailed recommendation with rationale]

## Implementation Roadmap
[High-level phases]

## Key Risks and Mitigations
[Table format]
</output_format>
```

---

## Document Processing Pipeline

### Contract Analysis Workflow

**Stage 1: Extraction**
**Model: Claude Haiku 4.5**

```xml
<task>
Extract structured information from the contract.
</task>

<contract>
{{CONTRACT_TEXT}}
</contract>

<extract>
- parties: [Names of all parties]
- effective_date: [Date]
- term: [Duration]
- value: [Total value if specified]
- key_dates: [List of important dates]
- key_obligations: [List of main obligations per party]
</extract>

<output>
JSON format matching the extraction schema.
</output>
```

**Stage 2: Risk Assessment**
**Model: Claude Sonnet 4.5**

```xml
<task>
Assess risks in the contract.
</task>

<contract>
{{CONTRACT_TEXT}}
</contract>

<extracted_data>
{{STAGE_1_OUTPUT}}
</extracted_data>

<assess>
For each risk area, evaluate:
- Liability and indemnification clauses
- Termination provisions
- Intellectual property rights
- Confidentiality obligations
- Limitation of liability
- Force majeure provisions
</assess>

<output>
<risks>
  <risk>
    <area>[Risk area]</area>
    <severity>High/Medium/Low</severity>
    <clause_reference>[Section number]</clause_reference>
    <issue>[What the concern is]</issue>
    <recommendation>[What to do about it]</recommendation>
  </risk>
  <!-- More risks -->
</risks>
</output>
```

**Stage 3: Summary and Recommendations**
**Model: Claude Opus 4.5**

```xml
<task>
Create executive summary with recommendations.
</task>

<extracted_data>
{{STAGE_1_OUTPUT}}
</extracted_data>

<risk_assessment>
{{STAGE_2_OUTPUT}}
</risk_assessment>

<contract>
{{CONTRACT_TEXT}}
</contract>

<synthesize>
1. Overall contract assessment
2. Key terms summary
3. Risk summary with priorities
4. Recommended actions before signing
5. Suggested modifications
</synthesize>

<output_format>
## Contract Summary
[One paragraph overview]

## Key Terms
[Table of essential terms]

## Risk Assessment
| Risk | Severity | Recommendation |
[Priority-ordered table]

## Recommended Actions
[Numbered list, most important first]

## Suggested Contract Modifications
[Specific language changes to propose]

## Questions for Legal Review
[Items requiring attorney input]
</output_format>
```

---

## Code Development Workflow

### Feature Implementation Pipeline

**Stage 1: Requirements Analysis**
**Model: Claude Sonnet 4.5**

```xml
<task>
Analyze the feature request and create technical requirements.
</task>

<feature_request>
{{FEATURE_REQUEST}}
</feature_request>

<codebase_context>
{{RELEVANT_CODE_CONTEXT}}
</codebase_context>

<analyze>
1. Functional requirements (what it must do)
2. Non-functional requirements (performance, security)
3. Technical constraints
4. Integration points with existing code
5. Testing requirements
</analyze>

<output>
<requirements>
  <functional>
    [List of must-haves]
  </functional>
  <nonfunctional>
    [Performance, security, etc.]
  </nonfunctional>
  <constraints>
    [Technical limitations]
  </constraints>
  <integrations>
    [Files/modules affected]
  </integrations>
  <tests>
    [Test scenarios needed]
  </tests>
</requirements>
<questions>
[Clarifications needed before proceeding]
</questions>
</output>
```

**Stage 2: Design**
**Model: Claude Opus 4.5**

```xml
<task>
Design the implementation approach.
</task>

<requirements>
{{STAGE_1_OUTPUT}}
</requirements>

<codebase_context>
{{RELEVANT_CODE_CONTEXT}}
</codebase_context>

<design>
1. High-level approach
2. Component breakdown
3. API/interface design
4. Data model changes (if any)
5. Integration strategy
6. Testing strategy
</design>

<output>
<design_doc>
## Approach Overview
[Summary of implementation strategy]

## Components
[List of components/modules to create/modify]

## API Design
[Interfaces, function signatures]

## Data Model
[Schema changes if any]

## Integration Plan
[How it connects to existing code]

## Testing Plan
[Types of tests, coverage targets]

## Risks and Mitigations
[Potential issues and how to address]
</design_doc>
</output>
```

**Stage 3: Implementation**
**Model: Claude Sonnet 4.5**

```xml
<task>
Implement the feature based on the design.
</task>

<design>
{{STAGE_2_OUTPUT}}
</design>

<codebase_context>
{{RELEVANT_CODE_CONTEXT}}
</codebase_context>

<implement>
Following the design:
1. Create/modify each component
2. Follow existing code patterns
3. Add appropriate tests
4. Update documentation
</implement>

<constraints>
- Don't add unnecessary abstractions
- Follow existing style conventions
- Handle edge cases identified in requirements
- Keep changes focused on the feature
</constraints>

<output>
For each file:
<file path="...">
[Complete file content or diff]
</file>
</output>
```

---

## Content Creation Workflow

### Article Production Pipeline

**Stage 1: Research and Outline**
**Model: Claude Sonnet 4.5**

```xml
<task>
Research the topic and create a detailed outline.
</task>

<topic>
{{ARTICLE_TOPIC}}
</topic>

<target_audience>
{{AUDIENCE_DESCRIPTION}}
</target_audience>

<research>
1. Key points to cover
2. Supporting data/evidence
3. Expert perspectives to include
4. Common questions to address
5. Unique angles to explore
</research>

<output>
<research_notes>
[Key findings organized by theme]
</research_notes>
<outline>
## [Working Title]

### Introduction
[Hook and thesis]

### Section 1: [Topic]
- Point A
- Point B
- Supporting evidence

### Section 2: [Topic]
[Structure continues]

### Conclusion
[Key takeaways]
</outline>
<sources>
[References to cite]
</sources>
</output>
```

**Stage 2: Draft**
**Model: Claude Opus 4.5**

```xml
<task>
Write the first draft based on the outline.
</task>

<outline>
{{STAGE_1_OUTLINE}}
</outline>

<research_notes>
{{STAGE_1_RESEARCH}}
</research_notes>

<write>
Create a complete first draft that:
1. Follows the outline structure
2. Incorporates research naturally
3. Maintains consistent voice
4. Hits target length
</write>

<requirements>
- Length: {{TARGET_LENGTH}}
- Tone: {{TONE_DESCRIPTION}}
- Each section should transition smoothly
- Include specific examples and data
</requirements>

<output>
[Complete draft with all sections]
</output>
```

**Stage 3: Edit**
**Model: Claude Opus 4.5**

```xml
<task>
Edit the draft for quality and clarity.
</task>

<draft>
{{STAGE_2_DRAFT}}
</draft>

<edit_for>
1. Clarity: Is every sentence clear?
2. Concision: Remove unnecessary words
3. Flow: Do paragraphs connect well?
4. Accuracy: Are facts correct?
5. Engagement: Is it interesting throughout?
6. Grammar: Fix any errors
</edit_for>

<constraints>
- Preserve the author's voice
- Keep structural changes minimal unless necessary
- Focus on strengthening, not rewriting
</constraints>

<output>
<edited_draft>
[Improved version]
</edited_draft>
<changes_summary>
[What was changed and why]
</changes_summary>
</output>
```

---

## Decision-Making Workflow

### Strategic Decision Analysis

**Stage 1: Option Generation**
**Model: Claude Sonnet 4.5**

```xml
<task>
Generate strategic options for the decision.
</task>

<decision_context>
{{SITUATION_DESCRIPTION}}
</decision_context>

<constraints>
{{CONSTRAINTS_AND_REQUIREMENTS}}
</constraints>

<generate>
Create 4-5 distinct strategic options:
- Include conservative and bold approaches
- Consider short-term and long-term
- Include a "do nothing" baseline
- Each should be genuinely different
</generate>

<output>
<options>
  <option id="1">
    <name>[Short name]</name>
    <description>[What this option entails]</description>
    <key_actions>[Main steps required]</key_actions>
  </option>
  <!-- More options -->
</options>
</output>
```

**Stage 2: Option Evaluation**
**Model: Claude Opus 4.5**

```xml
<task>
Evaluate each option against criteria.
</task>

<options>
{{STAGE_1_OPTIONS}}
</options>

<evaluation_criteria>
{{CRITERIA_LIST}}
</evaluation_criteria>

<evaluate>
For each option, assess:
1. How well it meets each criterion
2. Key risks and mitigations
3. Resource requirements
4. Timeline implications
5. Second-order effects
</evaluate>

<output>
<evaluations>
  <option id="1">
    <criteria_scores>
      <criterion name="...">
        <score>1-5</score>
        <reasoning>[Why this score]</reasoning>
      </criterion>
    </criteria_scores>
    <risks>[Key risks]</risks>
    <resources>[What's needed]</resources>
    <timeline>[Expected duration]</timeline>
  </option>
</evaluations>
<comparison_matrix>
[Options vs criteria matrix]
</comparison_matrix>
</output>
```

**Stage 3: Recommendation**
**Model: Claude Opus 4.5**

```xml
<task>
Synthesize analysis into a recommendation.
</task>

<options>
{{STAGE_1_OPTIONS}}
</options>

<evaluations>
{{STAGE_2_EVALUATIONS}}
</evaluations>

<synthesize>
1. Weight the criteria
2. Consider risk tolerance
3. Account for implementation realities
4. Identify the best path forward
</synthesize>

<output_format>
## Recommendation Summary
[One paragraph with the recommended option]

## Why This Option
[Key reasons for the recommendation]

## Comparison to Alternatives
[Why not the other options]

## Implementation Considerations
[What to keep in mind]

## Key Success Factors
[What must go right]

## Monitoring and Adjustment
[How to track progress and adapt]
</output_format>
```

---

## Best Practices for Workflow Prompts

### 1. Clear Stage Boundaries
Each stage should have:
- Defined input
- Specific task
- Structured output

### 2. Appropriate Model Selection
- **Haiku**: Extraction, classification, simple transforms
- **Sonnet**: Analysis, generation, most tasks
- **Opus**: Synthesis, complex reasoning, final output

### 3. State Preservation
Explicitly pass outputs between stages in structured format.

### 4. Validation Points
Consider adding validation between stages:
- Is output complete?
- Does it meet quality standards?
- Are there errors to address?

### 5. Error Handling
Define what happens if a stage fails or produces incomplete output.

### 6. Parallel Opportunities
Identify stages that can run in parallel to save time.
