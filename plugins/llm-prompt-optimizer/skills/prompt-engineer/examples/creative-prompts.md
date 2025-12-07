# Creative Writing Prompt Examples

## Long-Form Content

### Blog Post Generation

**Optimized for: Claude Opus 4.5**

```xml
<context>
Writing for a technology company's blog.
Audience: Technical decision-makers (CTOs, Engineering Managers)
Voice: Authoritative but approachable, not overly casual
</context>

<topic>
The future of AI-assisted software development
</topic>

<task>
Write a comprehensive blog post that provides genuine insight and value.
</task>

<structure>
1. Hook: Compelling opening that addresses reader pain points
2. Context: Current state of AI in development
3. Body: 3-4 key insights with supporting evidence
4. Practical: How readers can apply this
5. Conclusion: Forward-looking perspective
</structure>

<requirements>
- Length: 1,500-2,000 words
- Include: 2-3 specific examples or case studies
- Tone: Thought leadership, not sales pitch
- Avoid: Buzzwords, hype, generic statements
</requirements>

<quality_standards>
- Every paragraph adds new value
- Claims supported by reasoning or evidence
- Practical takeaways, not just theory
- Distinctive perspective, not generic content
</quality_standards>
```

---

## Marketing Copy

### Product Description

**Optimized for: Claude Sonnet 4.5**

```xml
<product>
Name: CloudSync Pro
Category: Enterprise file synchronization software
Key features:
- End-to-end encryption
- Real-time collaboration
- 99.99% uptime SLA
- SOC 2 Type II certified
Target: IT administrators at mid-size companies
</product>

<task>
Write a product description for the website landing page.
</task>

<requirements>
- Opening: Problem/pain point hook
- Middle: Key benefits (not just features)
- End: Clear call-to-action
- Length: 150-200 words
- Tone: Professional, trustworthy, confident
</requirements>

<examples_of_tone>
Good: "Secure your team's files without sacrificing productivity."
Avoid: "THE BEST file sync solution EVER!!!"
</examples_of_tone>

<output>
Primary description paragraph + 3 bullet points highlighting key benefits.
</output>
```

---

## Email Sequences

### Onboarding Email Series

**Optimized for: Claude Sonnet 4.5**

```xml
<context>
Product: Project management SaaS
Trigger: User signed up for free trial
Goal: Convert to paid subscription
</context>

<task>
Create a 5-email onboarding sequence.
</task>

<email_sequence>
Email 1 (Day 0): Welcome + quick start
Email 2 (Day 2): Key feature highlight
Email 3 (Day 5): Success story/case study
Email 4 (Day 10): Address common concerns
Email 5 (Day 13): Trial ending + offer
</email_sequence>

<requirements_per_email>
- Subject line (under 50 chars, no clickbait)
- Preview text (50-100 chars)
- Body (100-200 words)
- Single clear CTA
- P.S. line (optional but encouraged)
</requirements_per_email>

<tone>
Helpful, not pushy. Educational, not salesy.
Build relationship, not just convert.
</tone>

<output_format>
For each email:
---
**Email [X]: [Purpose]**
Subject: [subject line]
Preview: [preview text]

[Body content]

CTA: [Button text]
---
</output_format>
```

---

## Technical Documentation

### API Documentation

**Optimized for: Claude Sonnet 4.5**

```xml
<api_details>
Endpoint: POST /api/v1/users/authenticate
Purpose: Authenticate user and return access token
Request body: { email: string, password: string }
Response: { token: string, expires_at: ISO8601 }
Errors: 400 (invalid input), 401 (bad credentials), 429 (rate limited)
</api_details>

<task>
Write complete API documentation for this endpoint.
</task>

<documentation_format>
## Endpoint Name

**Description**: [Clear explanation]

### Request

**Method**: [HTTP method]
**URL**: [Full path]
**Authentication**: [Required or not]

**Headers**:
| Header | Required | Description |
[Table]

**Body Parameters**:
| Parameter | Type | Required | Description |
[Table]

### Response

**Success Response (200)**:
```json
[Example response]
```

**Error Responses**:
| Status | Code | Description |
[Table for each error]

### Examples

**cURL**:
```bash
[Example request]
```

**Response**:
```json
[Example response]
```

### Notes
[Any important considerations]
</documentation_format>
```

---

## Storytelling

### Case Study

**Optimized for: Claude Opus 4.5**

```xml
<source_information>
Company: TechStartup Inc.
Challenge: Slow deployment cycles (2 weeks average)
Solution: Implemented our CI/CD platform
Results: Reduced to 2 hours, 10x more deployments per month
Quote from CTO: "It transformed how we ship software."
</source_information>

<task>
Create a compelling case study that tells a story.
</task>

<structure>
1. **The Challenge** (Setting the scene, stakes)
2. **The Search** (Why they needed a solution)
3. **The Solution** (How they found and implemented us)
4. **The Transformation** (Results with specific metrics)
5. **The Future** (What's next for them)
</structure>

<requirements>
- Length: 600-800 words
- Include: Direct quotes (can create realistic ones)
- Metrics: Highlight specific numbers
- Narrative: Tell a story, not just list facts
- Balance: Genuine, not an advertisement
</requirements>

<tone>
Journalistic storytelling. Let the customer be the hero.
We're the guide that helped them succeed.
</tone>
```

---

## Social Media

### LinkedIn Post Series

**Optimized for: Claude Sonnet 4.5**

```xml
<topic>
Leadership lessons from scaling a startup
</topic>

<context>
Author: CEO of a Series B startup
Audience: Other founders, executives, professionals
Platform: LinkedIn
Goal: Thought leadership, engagement, brand building
</context>

<task>
Create 5 LinkedIn posts as a content series.
</task>

<post_structure>
- Hook: First 2-3 lines that grab attention
- Story/insight: The main content
- Lesson: Key takeaway
- Engagement: Question or CTA
- Hashtags: 3-5 relevant ones
</post_structure>

<requirements>
- Length: 150-250 words each
- Format: Use line breaks for readability
- Tone: Authentic, vulnerable, insightful
- Include: At least one specific story per post
- Avoid: Obvious humble-brags, generic advice
</requirements>

<series_themes>
1. A mistake that taught me the most
2. The hardest decision I made
3. What I wish I knew earlier
4. How I handle failure
5. Advice I'd give my past self
</series_themes>
```

---

## Creative Fiction

### Short Story Opening

**Optimized for: Claude Opus 4.5**

```xml
<specifications>
Genre: Science fiction
Length: 500-word opening
Theme: Human connection in a digital age
Setting: Near future (2045)
Mood: Contemplative, slightly melancholic
</specifications>

<task>
Write the opening of a short story that hooks the reader.
</task>

<requirements>
- Start in media res (in the middle of action/scene)
- Introduce protagonist through behavior, not description
- Hint at larger conflict without explaining it
- Use sensory details to establish setting
- End the excerpt with a hook
</requirements>

<avoid>
- Info dumps
- Cliché openings ("It was a dark and stormy night")
- Overexplanation of technology
- Generic character names/descriptions
</avoid>

<style_guidance>
- Prose: Literary but accessible
- Perspective: Close third person
- Sentences: Varied length, some short and punchy
- Show, don't tell
</style_guidance>
```

---

## Presentation Content

### Slide Deck Narrative

**Optimized for: Claude Opus 4.5**

```xml
<presentation_context>
Purpose: Series A fundraising pitch
Audience: Venture capital partners
Length: 10-12 slides
Company: B2B SaaS for HR automation
</presentation_context>

<task>
Create the narrative flow and key content for each slide.
</task>

<slide_structure>
Slide 1: Hook/Vision
Slide 2: Problem
Slide 3: Solution
Slide 4: Product demo highlights
Slide 5: Business model
Slide 6: Market size
Slide 7: Traction/metrics
Slide 8: Competition
Slide 9: Team
Slide 10: Financial projections
Slide 11: Ask
Slide 12: Contact
</slide_structure>

<output_format>
For each slide:
---
**Slide [X]: [Title]**
Main message: [One sentence]
Key points:
- [Point 1]
- [Point 2]
Supporting data: [If applicable]
Transition to next: [Connection]
---
</output_format>

<requirements>
- Each slide = one clear message
- Narrative builds throughout
- Balance vision with evidence
- End with clear, compelling ask
</requirements>
```

---

## Best Practices for Creative Prompts

### 1. Define Voice and Tone
"Authoritative but approachable" is more useful than "professional."

### 2. Provide Context
Who's the audience? What's the goal? What's the medium?

### 3. Show Examples of Style
Good/avoid examples calibrate expectations.

### 4. Structure the Output
Give clear frameworks, especially for longer content.

### 5. Specify Length
Word counts help ensure appropriate depth.

### 6. Emphasize Quality Standards
"Every paragraph adds value" prevents filler.

### 7. Model Selection
- **Opus 4.5**: Highest creative quality, distinctive voice
- **Sonnet 4.5**: Good creative output, faster iterations
- **Haiku 4.5**: Quick drafts, simple copy
