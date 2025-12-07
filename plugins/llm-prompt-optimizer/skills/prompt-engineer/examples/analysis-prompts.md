# Analysis Prompt Examples

## Data Analysis

### Sales Performance Analysis

**Optimized for: Claude Sonnet 4.5**

```xml
<role>
You are a data analyst specializing in sales performance metrics.
</role>

<context>
We're analyzing Q4 sales data for a SaaS company.
Leadership needs actionable insights for the board meeting.
</context>

<data>
{{SALES_DATA}}
</data>

<task>
Analyze the sales data and provide insights.
</task>

<analysis_framework>
1. Overview: Key metrics summary
2. Trends: Quarter-over-quarter patterns
3. Segments: Performance by region/product/channel
4. Anomalies: Unusual patterns or outliers
5. Recommendations: Actionable next steps
</analysis_framework>

<output_format>
## Executive Summary
[2-3 sentence overview]

## Key Metrics
| Metric | Value | vs. Last Quarter |
[Table format]

## Trends
[Bullet points with supporting data]

## Segment Analysis
[Key insights by segment]

## Recommendations
[Numbered, actionable items]
</output_format>

<constraints>
- Focus on actionable insights
- Support all claims with data
- Keep executive summary under 100 words
</constraints>
```

---

## Document Analysis

### Contract Review

**Optimized for: Claude Opus 4.5**

```xml
<role>
You are a legal analyst reviewing contracts for potential issues.
</role>

<task>
Review the contract and identify key terms, risks, and recommendations.
</task>

<contract>
{{CONTRACT_TEXT}}
</contract>

<analysis_areas>
1. Key Terms: Important dates, amounts, obligations
2. Risk Areas: Liability, indemnification, termination clauses
3. Non-Standard Terms: Unusual provisions to note
4. Missing Elements: Standard clauses that are absent
5. Recommendations: Suggested modifications
</analysis_areas>

<output_format>
## Contract Summary
- Parties: [Names]
- Effective Date: [Date]
- Term: [Duration]
- Value: [Amount if applicable]

## Key Terms
[Important provisions in plain language]

## Risk Assessment
| Risk Area | Severity | Details |
[Table format]

## Recommendations
[Specific suggested changes or questions to raise]

## Questions for Legal
[Items requiring legal counsel review]
</output_format>

<constraints>
- This is analysis, not legal advice
- Flag items needing attorney review
- Focus on business-relevant issues
</constraints>
```

---

## Competitive Analysis

### Competitor Comparison

**Optimized for: Claude Opus 4.5**

```xml
<context>
We're a B2B SaaS company evaluating our market position.
Need analysis for strategic planning session.
</context>

<task>
Analyze competitors based on the provided information.
</task>

<our_product>
{{OUR_PRODUCT_INFO}}
</our_product>

<competitor_data>
{{COMPETITOR_DATA}}
</competitor_data>

<analysis_framework>
1. Feature Comparison: Core capabilities matrix
2. Pricing Analysis: Value positioning
3. Market Position: Target segments and share
4. Strengths/Weaknesses: SWOT elements
5. Differentiation: Our unique advantages
6. Threats: Competitive risks to address
7. Opportunities: Gaps we can exploit
</analysis_framework>

<output_format>
## Market Overview
[Current landscape summary]

## Feature Comparison Matrix
| Feature | Us | Competitor A | Competitor B |
[Detailed comparison]

## Pricing Analysis
[Value positioning analysis]

## Competitive Position
### Our Strengths
### Our Weaknesses
### Competitive Threats
### Market Opportunities

## Strategic Recommendations
[Prioritized action items]
</output_format>
```

---

## Technical Analysis

### System Architecture Review

**Optimized for: Claude Opus 4.5**

```xml
<role>
You are a senior solutions architect reviewing system designs.
</role>

<context>
The engineering team has proposed a new microservices architecture.
We need an objective assessment before proceeding.
</context>

<architecture>
{{ARCHITECTURE_DIAGRAM_OR_DESCRIPTION}}
</architecture>

<requirements>
{{SYSTEM_REQUIREMENTS}}
</requirements>

<analysis_areas>
1. Requirements Alignment: Does it meet stated needs?
2. Scalability: Can it handle growth projections?
3. Reliability: Single points of failure, redundancy
4. Security: Authentication, data protection, compliance
5. Maintainability: Complexity, developer experience
6. Cost: Infrastructure and operational costs
7. Trade-offs: What's sacrificed for the benefits?
</analysis_areas>

<output_format>
## Architecture Summary
[Brief description of proposed architecture]

## Requirements Analysis
| Requirement | Addressed? | Details |
[Matrix]

## Strengths
[What the architecture does well]

## Concerns
| Concern | Severity | Recommendation |
[Table]

## Risk Assessment
[Key risks and mitigations]

## Recommendations
[Specific improvements or alternatives]

## Questions for Team
[Clarifications needed]
</output_format>
```

---

## Research Synthesis

### Literature Review

**Optimized for: Claude Opus 4.5**

```xml
<context>
Synthesizing research on [topic] for a comprehensive understanding.
</context>

<sources>
{{RESEARCH_SOURCES}}
</sources>

<task>
Synthesize the research into a coherent analysis.
</task>

<synthesis_framework>
1. Common Findings: What do sources agree on?
2. Contradictions: Where do sources disagree?
3. Gaps: What's not adequately addressed?
4. Methodological Notes: How was research conducted?
5. Implications: What does this mean in practice?
</synthesis_framework>

<output_format>
## Overview
[Topic introduction and scope]

## Key Findings
[Synthesized themes with source citations]

### Theme 1: [Name]
[Analysis with evidence]

### Theme 2: [Name]
[Analysis with evidence]

## Points of Disagreement
[Conflicting findings and possible reasons]

## Research Gaps
[Areas needing further study]

## Conclusions
[Summary of current understanding]

## Practical Implications
[How to apply these findings]
</output_format>
```

---

## Financial Analysis

### Investment Analysis

**Optimized for: Claude Opus 4.5**

```xml
<role>
You are a financial analyst evaluating investment opportunities.
</role>

<company_data>
{{FINANCIAL_DATA}}
</company_data>

<task>
Analyze the company's financial health and investment potential.
</task>

<analysis_framework>
1. Financial Health: Key ratios and metrics
2. Growth Trends: Revenue and profit trajectory
3. Competitive Position: Market context
4. Risk Factors: Financial and business risks
5. Valuation: Fair value assessment
6. Recommendation: Investment thesis
</analysis_framework>

<output_format>
## Company Overview
[Brief description]

## Financial Metrics
| Metric | Current | Industry Avg | Assessment |
[Key ratios]

## Growth Analysis
[Trend analysis with data]

## Risk Assessment
| Risk | Probability | Impact | Mitigation |
[Table]

## Valuation
[Fair value analysis]

## Investment Recommendation
[Clear recommendation with rationale]

## Disclaimer
This is analysis for informational purposes, not financial advice.
</output_format>
```

---

## Diagnostic Analysis

### Problem Root Cause

**Optimized for: Claude Sonnet 4.5**

```xml
<context>
We're experiencing [problem] and need to identify root causes.
</context>

<problem_description>
{{PROBLEM_DETAILS}}
</problem_description>

<available_data>
{{LOGS_METRICS_REPORTS}}
</available_data>

<task>
Perform root cause analysis on the problem.
</task>

<analysis_method>
Use the 5 Whys technique combined with evidence review.
</analysis_method>

<output_format>
## Problem Statement
[Clear description of the issue]

## Impact Assessment
- Scope: [Who/what is affected]
- Severity: [How serious]
- Duration: [How long ongoing]

## Evidence Review
[What the data shows]

## Root Cause Analysis
### Why 1: [First level cause]
### Why 2: [Deeper cause]
### Why 3: [Even deeper]
### Why 4: [Underlying cause]
### Why 5: [Root cause]

## Root Cause(s) Identified
[Clear statement of root cause(s)]

## Recommended Solutions
| Solution | Effort | Impact | Priority |
[Table]

## Prevention
[How to prevent recurrence]
</output_format>
```

---

## Best Practices for Analysis Prompts

### 1. Define the Role/Expertise
What perspective should the analysis take?

### 2. Provide Complete Context
Background, constraints, purpose of analysis.

### 3. Use Analysis Frameworks
Give structure to the thinking process.

### 4. Specify Output Format
Exactly how results should be presented.

### 5. Request Evidence
"Support claims with data from the provided information."

### 6. Define Scope
What to include, what to exclude.

### 7. Model Selection
- **Opus 4.5**: Complex synthesis, nuanced analysis
- **Sonnet 4.5**: Structured analysis, clear frameworks
- **Haiku 4.5**: Quick metrics extraction
