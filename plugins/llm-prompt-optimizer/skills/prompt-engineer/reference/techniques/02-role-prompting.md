# Role Prompting

## Overview

Role prompting assigns a specific persona, expertise, or perspective to the model via the system prompt. This technique enhances domain-specific performance by establishing context, expertise level, and behavioral expectations.

## When to Use Role Prompting

Apply role prompting when:
- Domain expertise would improve response quality
- Specific communication style is required
- Consistent persona across multiple interactions needed
- Task requires specialized knowledge perspective
- Professional or technical context matters

## Core Principles

### 1. System Prompt vs User Message

**System Prompt (Role Definition):**
- Persistent context across the conversation
- Establishes expertise, constraints, and behavior
- Defines who the model is for this session

**User Message (Task Instructions):**
- Specific task to accomplish
- Variable content and inputs
- Situational instructions

```python
# Correct: Role in system, task in user
system = "You are a senior security engineer with 15 years of experience in application security."

user = "Review this code for SQL injection vulnerabilities: [code]"
```

### 2. Be Specific About Expertise

**Generic (Less Effective):**
```
You are a helpful assistant.
```

**Specific (More Effective):**
```
You are a senior backend engineer specializing in Python and PostgreSQL,
with deep experience in API design and database optimization. You have
10 years of production experience at high-traffic SaaS companies.
```

### 3. Include Relevant Context

Add context that shapes responses:

```
You are a financial analyst at a Fortune 500 company. You:
- Analyze quarterly earnings reports
- Prepare executive summaries for the C-suite
- Focus on actionable insights over raw data
- Use conservative estimates and flag uncertainties
```

## Role Definition Patterns

### Expert Role

```
You are a [specific title] with expertise in [domain areas].
You have [years] of experience in [context].
Your specializations include [specific skills].
```

**Example:**
```
You are a machine learning engineer specializing in NLP and transformer architectures.
You have 8 years of experience deploying production ML systems at scale.
Your specializations include text classification, entity extraction, and LLM fine-tuning.
```

### Advisor Role

```
You are a [type] advisor for [audience].
Your goal is to help them [objective].
You communicate in a [style] manner, focusing on [priorities].
```

**Example:**
```
You are a technical writing advisor for software developers.
Your goal is to help them write clear, concise documentation.
You communicate in a direct, practical manner, focusing on readability and maintainability.
```

### Reviewer Role

```
You are a [type] reviewer with high standards for [criteria].
You provide constructive feedback that is [characteristics].
You focus on [priority areas] while being [tone].
```

**Example:**
```
You are a code reviewer with high standards for security and maintainability.
You provide constructive feedback that is specific and actionable.
You focus on potential vulnerabilities and architectural issues while being respectful.
```

## Domain-Specific Role Templates

### Software Engineering

```
You are a senior software engineer with expertise in [languages/frameworks].
You follow best practices for [coding standards, testing, documentation].
You prioritize [performance, security, maintainability, readability].
When reviewing code, you focus on [specific concerns].
When writing code, you follow [conventions].
```

### Data Analysis

```
You are a data analyst with expertise in [tools/methods].
You work with [data types] and specialize in [analysis types].
You prioritize [accuracy, clarity, actionable insights].
You present findings with appropriate caveats and confidence levels.
```

### Creative Writing

```
You are a [type of writer] with a distinctive voice characterized by [traits].
You specialize in [genres/formats].
Your writing prioritizes [qualities: clarity, engagement, emotional impact].
You adapt your style based on [audience, purpose, medium].
```

### Customer Support

```
You are a customer support specialist for [product/service].
You are knowledgeable about [product features, common issues, policies].
You communicate with [empathy, clarity, professionalism].
You prioritize [resolution, customer satisfaction, efficiency].
```

## Combining Role with Constraints

### Add Behavioral Constraints

```
You are a medical information specialist.

IMPORTANT CONSTRAINTS:
- Never provide diagnosis or treatment recommendations
- Always recommend consulting a healthcare provider for medical decisions
- Cite sources when discussing medical information
- Clearly distinguish between general information and medical advice
```

### Add Output Constraints

```
You are a technical documentation writer.

OUTPUT REQUIREMENTS:
- Use clear, jargon-free language where possible
- Define technical terms on first use
- Include code examples for all procedures
- Structure content with clear headings
```

### Add Knowledge Boundaries

```
You are a legal research assistant specializing in US contract law.

BOUNDARIES:
- Provide information, not legal advice
- Focus on general principles, not case-specific guidance
- Recommend consulting an attorney for specific situations
- Acknowledge when questions fall outside your expertise
```

## Model-Specific Considerations

### Claude Models

Claude responds exceptionally well to role prompting. Key optimizations:

- Be explicit about the role's expertise level
- Include relevant context that shapes perspective
- Define communication style explicitly
- For Claude 4.x: Avoid overly aggressive role emphasis

```
You are a senior Python developer with 10 years of experience.
You write clean, well-documented code following PEP 8 guidelines.
You prefer practical solutions over theoretical perfection.
```

### GPT Models

GPT models also benefit from role prompting:

- System messages are the appropriate place for role definition
- Clear, structured role descriptions work best
- Consider adding explicit instruction-following guidance

```
You are an expert data scientist.
Follow these guidelines:
- Explain concepts at the appropriate technical level
- Show code with clear comments
- Validate assumptions before proceeding
```

### Gemini Models

Gemini uses similar patterns:

- Clear role definition in system instruction
- Explicit about expertise and constraints
- May benefit from more explicit formatting guidance

## Common Mistakes

### 1. Role Too Generic

```
# Too vague
You are a helpful assistant who knows about technology.

# Better
You are a DevOps engineer specializing in Kubernetes and AWS, with experience
in CI/CD pipelines and infrastructure as code.
```

### 2. Role Contradicts Task

```
# Contradiction: Lawyer role but asking for code
System: You are a corporate lawyer specializing in M&A transactions.
User: Write a Python function to sort a list.

# Better: Match role to task
System: You are a Python developer specializing in algorithm optimization.
User: Write an efficient function to sort a list.
```

### 3. Mixing Role and Task

```
# Wrong: Task in system prompt
System: You are a translator. Translate the following text to French: [text]

# Right: Role in system, task in user
System: You are a professional translator fluent in English and French.
User: Translate the following text to French: [text]
```

### 4. Overly Complex Role

```
# Too much information dilutes focus
System: You are a software engineer who also does data science, knows about
finance, has experience in healthcare, speaks 5 languages, and is an
expert in machine learning, web development, mobile apps, embedded systems...

# Better: Focused expertise
System: You are a backend engineer specializing in Python APIs and PostgreSQL.
```

## Integration with Other Techniques

### Role + XML Tags

```
System: You are a senior code reviewer focusing on security.

User:
<review_context>
This is a financial application handling sensitive user data.
</review_context>

<code>
[code to review]
</code>

<focus_areas>
- Authentication and authorization
- Data validation
- SQL injection prevention
</focus_areas>
```

### Role + Chain of Thought

```
System: You are a detective solving logical puzzles.
Think through each problem methodically, considering all evidence.

User: A witness claims they saw the suspect at 3pm, but the security
footage shows the office was empty. What conclusions can we draw?

Show your reasoning step by step before reaching your conclusion.
```

### Role + Examples

```
System: You are a customer support agent for TechCorp.

User:
Here are examples of good responses:

Example 1:
Customer: My subscription isn't working.
Response: I understand how frustrating that can be. Let me help you get
this resolved right away. Could you tell me the email address associated
with your account?

Now respond to this customer inquiry:
Customer: I can't log into my account.
```

## Effective Role Components

| Component | Purpose | Example |
|-----------|---------|---------|
| Title/Position | Establishes expertise level | "Senior software architect" |
| Domain | Focuses knowledge area | "specializing in distributed systems" |
| Experience | Adds credibility | "with 15 years of production experience" |
| Context | Shapes perspective | "at a high-growth startup" |
| Style | Defines communication | "who explains concepts clearly" |
| Constraints | Sets boundaries | "focusing on practical solutions" |

## Quick Reference

**Do:**
- Put role in system prompt, tasks in user messages
- Be specific about expertise and context
- Match role to the actual task
- Include relevant constraints and style guidance
- Keep role focused on most relevant expertise

**Don't:**
- Use vague, generic role descriptions
- Mix role definition with task instructions
- Create contradictory role-task combinations
- Overload with too many areas of expertise
- Forget to align role with domain needs

## Summary

Role prompting establishes expertise and context that shapes model responses. Effective roles are:
- Specific about expertise area
- Relevant to the task at hand
- Placed in the system prompt
- Combined with clear constraints
- Focused rather than overly broad

Use role prompting to get responses that reflect domain expertise and appropriate communication style.
