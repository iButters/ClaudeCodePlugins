# Classification Prompt Examples

## Simple Classification

### Support Ticket Categorization

**Optimized for: Claude Haiku 4.5 / Any fast model**

```xml
<task>
Classify the support ticket into exactly one category.
</task>

<categories>
- billing: Payment issues, charges, refunds, invoices
- technical: Bugs, errors, feature issues, performance
- account: Login, password, profile, settings
- general: Questions, feedback, other inquiries
</categories>

<examples>
  <example>
    <ticket>I was charged twice for my subscription this month</ticket>
    <category>billing</category>
  </example>
  <example>
    <ticket>The app crashes when I try to upload a file</ticket>
    <category>technical</category>
  </example>
  <example>
    <ticket>How do I change my email address?</ticket>
    <category>account</category>
  </example>
  <example>
    <ticket>Do you offer student discounts?</ticket>
    <category>general</category>
  </example>
</examples>

<ticket>
{{TICKET_CONTENT}}
</ticket>

<output>
Respond with only the category name, nothing else.
</output>
```

---

## Multi-Label Classification

### Content Tagging

**Optimized for: Claude Sonnet 4.5**

```xml
<task>
Assign all applicable tags to this article. An article may have multiple tags.
</task>

<available_tags>
- technology: Software, hardware, AI, digital tools
- business: Companies, markets, finance, strategy
- science: Research, discoveries, academic studies
- health: Medical, wellness, fitness
- politics: Government, policy, elections
- entertainment: Movies, music, games, celebrities
</available_tags>

<examples>
  <example>
    <article>Apple announces new AI features for iPhone using on-device processing</article>
    <tags>technology, business</tags>
  </example>
  <example>
    <article>New study links regular exercise to improved cognitive function in elderly</article>
    <tags>science, health</tags>
  </example>
  <example>
    <article>Congress debates new regulations for social media companies</article>
    <tags>politics, technology, business</tags>
  </example>
</examples>

<article>
{{ARTICLE_CONTENT}}
</article>

<output_format>
Return comma-separated tags. Include only tags that clearly apply.
If none apply, return "uncategorized".
</output_format>
```

---

## Sentiment Analysis

### Customer Feedback Sentiment

**Optimized for: Claude Haiku 4.5**

```xml
<task>
Classify the sentiment of customer feedback.
</task>

<sentiment_scale>
- positive: Happy, satisfied, praising, recommending
- neutral: Factual, mixed, neither positive nor negative
- negative: Unhappy, complaining, criticizing
</sentiment_scale>

<examples>
  <example>
    <feedback>Absolutely love this product! Best purchase I've made all year.</feedback>
    <sentiment>positive</sentiment>
  </example>
  <example>
    <feedback>It works as described. Nothing special but does the job.</feedback>
    <sentiment>neutral</sentiment>
  </example>
  <example>
    <feedback>Complete waste of money. Broke after two days.</feedback>
    <sentiment>negative</sentiment>
  </example>
  <example>
    <feedback>The design is nice but the quality could be better for this price.</feedback>
    <sentiment>neutral</sentiment>
  </example>
</examples>

<feedback>
{{FEEDBACK_TEXT}}
</feedback>

Output only: positive, neutral, or negative
```

---

## Priority/Urgency Classification

### Ticket Priority Assignment

**Optimized for: Claude Sonnet 4.5**

```xml
<role>
You are a support triage specialist who accurately assesses ticket urgency.
</role>

<task>
Assign a priority level to the support ticket based on business impact and urgency.
</task>

<priority_levels>
- critical: System down, data loss, security breach, blocking multiple users
- high: Major feature broken, significant user impact, workaround difficult
- medium: Feature issue with workaround, moderate user impact
- low: Minor issue, cosmetic, feature request, how-to question
</priority_levels>

<examples>
  <example>
    <ticket>URGENT: Our entire team of 50 people cannot log in. We have a client demo in 2 hours!</ticket>
    <priority>critical</priority>
    <reasoning>Multiple users blocked, time-sensitive business impact</reasoning>
  </example>
  <example>
    <ticket>The export function is broken. I can't download my reports.</ticket>
    <priority>high</priority>
    <reasoning>Core feature broken, likely blocking work, no easy workaround</reasoning>
  </example>
  <example>
    <ticket>Search is slow, taking 5-10 seconds. It used to be faster.</ticket>
    <priority>medium</priority>
    <reasoning>Degraded experience but feature works, not blocking</reasoning>
  </example>
  <example>
    <ticket>Can you add dark mode to the mobile app?</ticket>
    <priority>low</priority>
    <reasoning>Feature request, not a current issue</reasoning>
  </example>
</examples>

<ticket>
{{TICKET_CONTENT}}
</ticket>

<output_format>
priority: [critical/high/medium/low]
reasoning: [one sentence explaining why]
</output_format>
```

---

## Intent Classification

### Chatbot Intent Detection

**Optimized for: Claude Haiku 4.5**

```xml
<task>
Identify the user's primary intent from their message.
</task>

<intents>
- greeting: Hello, hi, starting conversation
- question: Asking for information
- complaint: Expressing dissatisfaction
- request: Asking for action/change
- purchase: Buying intent
- cancel: Wanting to end service
- other: Doesn't fit other categories
</intents>

<examples>
  <example>
    <message>Hi there!</message>
    <intent>greeting</intent>
  </example>
  <example>
    <message>What are your business hours?</message>
    <intent>question</intent>
  </example>
  <example>
    <message>This is ridiculous, I've been waiting for a week!</message>
    <intent>complaint</intent>
  </example>
  <example>
    <message>Can you update my shipping address?</message>
    <intent>request</intent>
  </example>
  <example>
    <message>I'd like to order 3 units of the Pro version</message>
    <intent>purchase</intent>
  </example>
  <example>
    <message>I want to close my account</message>
    <intent>cancel</intent>
  </example>
</examples>

<message>
{{USER_MESSAGE}}
</message>

Output only the intent name.
```

---

## Binary Classification

### Spam Detection

**Optimized for: Claude Haiku 4.5**

```
Classify as spam or not_spam:

Examples:
"Congratulations! You've won $1,000,000! Click here to claim!" → spam
"Your package has been shipped. Track it here: [legitimate URL]" → not_spam
"Make $5000/day working from home! No experience needed!" → spam
"Meeting reminder: Team sync at 3pm today" → not_spam
"Hot singles in your area want to meet you!" → spam

Message: {{MESSAGE}}

Output only: spam or not_spam
```

---

## Hierarchical Classification

### Product Categorization

**Optimized for: Claude Sonnet 4.5**

```xml
<task>
Classify the product into category and subcategory.
</task>

<taxonomy>
electronics:
  - smartphones
  - laptops
  - accessories
  - audio

clothing:
  - mens
  - womens
  - kids
  - accessories

home:
  - furniture
  - kitchen
  - decor
  - garden
</taxonomy>

<examples>
  <example>
    <product>Apple AirPods Pro - Wireless Earbuds with Noise Cancellation</product>
    <category>electronics</category>
    <subcategory>audio</subcategory>
  </example>
  <example>
    <product>Men's Slim Fit Cotton Dress Shirt - Blue</product>
    <category>clothing</category>
    <subcategory>mens</subcategory>
  </example>
  <example>
    <product>Stainless Steel Kitchen Knife Set - 8 Pieces</product>
    <category>home</category>
    <subcategory>kitchen</subcategory>
  </example>
</examples>

<product>
{{PRODUCT_DESCRIPTION}}
</product>

<output_format>
{
  "category": "...",
  "subcategory": "..."
}
</output_format>
```

---

## Best Practices for Classification Prompts

### 1. Clear Category Definitions
Always define what each category means, not just list names.

### 2. Representative Examples
Include examples that cover:
- Typical cases for each category
- Edge cases / boundary decisions
- Similar items that go to different categories

### 3. Consistent Format
Keep example format identical to expected output.

### 4. Single Output Instruction
End with clear instruction: "Output only: [format]"

### 5. Model Selection
- **Haiku**: Simple binary/multi-class, high volume
- **Sonnet**: Nuanced classification, multiple factors
- **Opus**: Complex reasoning about categories
