# Use Case Recommendations

## Quick Decision Guide

### By Task Type

| Task | Best Model | Why |
|------|-----------|-----|
| Simple classification | Haiku 4.5 | Fast, cheap, accurate |
| Complex classification | Sonnet 4.5 | Better nuance handling |
| Data extraction (simple) | Haiku 4.5 | Speed and cost |
| Data extraction (complex) | GPT 5.1 (JSON) | Reliable structure |
| Code generation | Sonnet 4.5 | Best coding balance |
| Code review | Opus 4.5 | Thorough analysis |
| Creative writing | Opus 4.5 | Highest quality |
| Technical docs | Sonnet 4.5 | Good balance |
| Research synthesis | Opus 4.5 | Deep analysis |
| Image analysis | Gemini Pro / Opus | Best multimodal |
| High-volume ops | Haiku 4.5 | Cost efficiency |
| API integration | GPT 5.1 | Native functions |

### By Priority

| Priority | Recommended Model |
|----------|------------------|
| Maximum quality | Opus 4.5 |
| Best balance | Sonnet 4.5 |
| Fastest response | Haiku 4.5 |
| Lowest cost | Haiku 4.5 |
| Best for code | Sonnet 4.5 |
| Best multimodal | Gemini Pro 3.0 |
| Best function calling | GPT 5.1 |

## Detailed Use Case Analysis

### Software Development

#### Agentic Coding (Extended Development Sessions)
**Recommended: Claude Sonnet 4.5**

Why:
- Excellent parallel tool calling
- Great context awareness
- Strong instruction following
- Good balance of speed and quality

Alternative: Claude Opus 4.5 (for complex architecture decisions)

#### Code Generation
**Recommended: Claude Sonnet 4.5 or GPT 5.1 Codex**

Sonnet when:
- Part of larger agentic workflow
- Multi-file context matters
- Extended session needed

Codex when:
- Focused code generation
- OpenAI ecosystem
- Specific completion tasks

#### Code Review
**Recommended: Claude Opus 4.5**

Why:
- Deep understanding of implications
- Catches subtle issues
- Excellent at explaining concerns
- Can consider architectural impact

Alternative: Sonnet 4.5 (for routine reviews)

#### Debugging
**Recommended: Claude Sonnet 4.5**

Why:
- Fast iteration
- Good at tracing logic
- Can read and explore code
- Efficient for back-and-forth

#### Test Generation
**Recommended: Claude Sonnet 4.5**

Why:
- Understands testing patterns
- Generates comprehensive coverage
- Good at edge cases
- Efficient execution

### Data and Analysis

#### Complex Research Synthesis
**Recommended: Claude Opus 4.5**

Why:
- Best at integrating multiple sources
- Nuanced understanding
- Deep analytical capability
- Extended thinking for complex topics

#### Quick Data Analysis
**Recommended: Claude Sonnet 4.5**

Why:
- Fast execution
- Good at structured analysis
- Handles tables and data well
- Cost-effective for routine analysis

#### Simple Classification
**Recommended: Claude Haiku 4.5**

Why:
- Fastest response
- Lowest cost
- Accurate for clear categories
- Scales well for volume

#### Sentiment Analysis
**Recommended: Claude Haiku 4.5**

Why:
- Simple pattern recognition
- High volume capability
- Good accuracy
- Cost-effective

#### Data Extraction (Structured)
**Recommended: GPT 5.1 with JSON mode**

Why:
- Guaranteed valid JSON
- Reliable structure
- Good at following schemas
- Native format support

Alternative: Claude Sonnet 4.5 (with XML)

### Content and Creative

#### Long-Form Creative Writing
**Recommended: Claude Opus 4.5**

Why:
- Highest creative quality
- Distinctive voice
- Maintains coherence over length
- Best at avoiding generic output

#### Marketing Copy
**Recommended: Claude Sonnet 4.5**

Why:
- Good creative quality
- Fast turnaround
- Cost-effective for iterations
- Understands business context

#### Technical Documentation
**Recommended: Claude Sonnet 4.5**

Why:
- Understands code well
- Clear technical writing
- Good structure
- Efficient execution

#### Presentations and Slides
**Recommended: Claude Opus 4.5**

Why:
- Strong visual design sense
- Creates polished content
- Good at narrative structure
- Distinctive aesthetics

### Operations and Production

#### Customer Support Responses
**Recommended: Claude Sonnet 4.5**

Why:
- Good balance of quality and speed
- Understands context well
- Empathetic responses
- Handles complexity appropriately

Alternative: Haiku 4.5 (for simple, high-volume)

#### Ticket Routing/Triage
**Recommended: Claude Haiku 4.5**

Why:
- Fastest response
- Lowest cost
- Accurate for routing decisions
- Scales to high volume

#### Email Processing
**Recommended: Claude Haiku 4.5**

Why:
- Quick classification
- Cost-effective
- Handles volume well
- Good for simple extraction

### Multimodal Tasks

#### Image Understanding
**Recommended: Claude Opus 4.5 or Gemini Pro 3.0**

Opus when:
- Deep analysis needed
- Complex reasoning about images
- Quality matters most

Gemini when:
- Multiple images
- Video content included
- Context caching needed

#### Video Analysis
**Recommended: Gemini Pro 3.0**

Why:
- Native video support
- Frame-by-frame analysis
- Audio understanding
- Large context for video

#### Visual Q&A
**Recommended: Gemini Pro 3.0**

Why:
- Excellent image understanding
- Fast responses
- Good at specific questions
- Cost-effective for volume

### Special Scenarios

#### High-Volume Processing
**Recommended: Claude Haiku 4.5**

Why:
- Lowest cost per request
- Fastest response
- Scales well
- Good accuracy for simple tasks

Cost optimization:
- Process in batches
- Parallelize requests
- Use caching where possible

#### Repeated Context Queries
**Recommended: Gemini Pro 3.0**

Why:
- Native context caching
- Significant cost savings
- Reduced latency on cached content
- Good for document Q&A

#### API Integration
**Recommended: GPT 5.1**

Why:
- Excellent function calling
- Native JSON mode
- Reliable structured output
- Well-documented integration

Alternative: Claude Sonnet 4.5 (for tool-heavy tasks)

## Workflow Recommendations

### Multi-Model Workflows

#### Research Pipeline
```
1. Haiku 4.5: Quick relevance filtering
2. Sonnet 4.5: Detailed extraction
3. Opus 4.5: Synthesis and analysis
```

#### Content Pipeline
```
1. Sonnet 4.5: Draft creation
2. Opus 4.5: Quality editing
3. Haiku 4.5: Final proofreading
```

#### Support Pipeline
```
1. Haiku 4.5: Ticket routing
2. Sonnet 4.5: Response generation
3. Opus 4.5: Escalation handling
```

### Cost Optimization Patterns

#### Tiered Processing
```
Tier 1 (Haiku): Quick filter/classify
Tier 2 (Sonnet): Process if complex
Tier 3 (Opus): Escalate if critical
```

#### Caching Strategy
```
Gemini Pro: Cache repeated contexts
Haiku: Process simple queries on cache
Sonnet: Handle complex queries
```

## Decision Framework

### Step 1: Identify Core Requirement

| If you need... | Start with... |
|----------------|---------------|
| Maximum quality | Opus 4.5 |
| Fast + good quality | Sonnet 4.5 |
| Speed + low cost | Haiku 4.5 |
| Reliable structure | GPT 5.1 (JSON) |
| Multimodal | Gemini Pro |
| Best coding | Sonnet 4.5 |

### Step 2: Check Constraints

| Constraint | Adjustment |
|------------|------------|
| Budget tight | Downgrade to cheaper model |
| Speed critical | Use Haiku or parallelize |
| Quality critical | Use Opus |
| Volume high | Use Haiku + batching |
| Context large | Consider caching |

### Step 3: Test and Iterate

1. Start with recommended model
2. Test with representative samples
3. Adjust based on results
4. Consider model switching for edge cases

## Summary Table

| Scenario | Model | Confidence |
|----------|-------|------------|
| Complex research | Opus 4.5 | High |
| Agentic coding | Sonnet 4.5 | High |
| Simple classification | Haiku 4.5 | High |
| Structured extraction | GPT 5.1 | High |
| Image analysis | Gemini Pro / Opus | Medium |
| Creative writing | Opus 4.5 | High |
| High-volume ops | Haiku 4.5 | High |
| Balanced production | Sonnet 4.5 | High |
| Function calling | GPT 5.1 | High |
| Context caching | Gemini Pro | High |
