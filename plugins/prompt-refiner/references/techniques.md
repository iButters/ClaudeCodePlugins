# Prompt Engineering Techniques Reference

## Frameworks

### COSTAR Framework
Structure prompts with six components:
- **C**ontext: Background information for the task
- **O**bjective: Clear goal of what to accomplish
- **S**tyle: Writing style (academic, conversational, technical)
- **T**one: Emotional quality (formal, friendly, urgent)
- **A**udience: Who will read/use the output
- **R**esponse: Output format (list, JSON, paragraphs)

### RISEN Framework
- **R**ole: Define the AI's expertise/persona
- **I**nstructions: Clear task description
- **S**teps: Break down into actionable steps
- **E**xpectation: Define success criteria
- **N**arrowing: Add constraints and focus

### APE Framework (Simple tasks)
- **A**ction: What to do
- **P**urpose: Why
- **E**xpectation: What output looks like

## Core Techniques

### Chain-of-Thought (CoT)
Add reasoning triggers for complex tasks:
- "Think step by step"
- "Break this down into steps"
- "Explain your reasoning"
- "Walk through this systematically"

### Few-Shot Prompting
Include 1-3 examples when:
- Format is specific or unusual
- Domain has specialized conventions
- Pattern recognition needed

Example structure:
```
Here are examples of the format I need:

Input: [example 1 input]
Output: [example 1 output]

Input: [example 2 input]
Output: [example 2 output]

Now do this:
Input: [actual request]
```

### Role/Persona Assignment
Improves expertise alignment:
- "You are an expert [domain] specialist..."
- "Act as a senior [role] with 10 years experience..."
- "As a [profession], provide..."

## Enhancement Patterns

### Specificity Upgrades
| Vague | Specific |
|-------|----------|
| "Write something about X" | "Write a 500-word explanation of X focusing on Y" |
| "Make it good" | "Use professional tone with concrete examples" |
| "A few examples" | "Provide exactly 3 examples" |
| "Recent developments" | "Developments from the past 6 months" |

### Structure Templates

**For explanations:**
```
Explain [topic] in [length].
Structure: [format requirements]
Audience: [who will read this]
Focus on: [key aspects]
```

**For analysis:**
```
Analyze [subject] considering [factors].
Provide:
1. [First component]
2. [Second component]
3. [Conclusion/recommendation]
```

**For creative:**
```
Create [type of content] about [subject].
Style: [tone/voice]
Length: [constraints]
Include: [required elements]
Avoid: [things to exclude]
```

## Common Fixes

### Problem: Generic responses
→ Add specific context, constraints, and examples

### Problem: Wrong format
→ Explicitly state output structure

### Problem: Too long/short
→ Add word/sentence count limits

### Problem: Wrong tone
→ Specify audience and formality level

### Problem: Missing key points
→ List required elements explicitly

### Problem: Scattered logic
→ Add "Think step by step" for reasoning tasks
