# Claude Sonnet 4.5 Optimization Guide

## Overview

Claude Sonnet 4.5 is the balanced workhorse of the Claude family—fast, capable, and cost-effective. It excels at agentic coding, production applications, and tasks requiring a good balance of speed and quality.

## Capabilities

### Strengths

| Capability | Rating | Notes |
|------------|--------|-------|
| Agentic Coding | Excellent | Best-in-class for coding agents |
| Instruction Following | Excellent | Highly precise |
| Parallel Tool Calling | Excellent | Aggressive parallelization |
| Context Awareness | Excellent | Tracks token budget |
| Speed | Fast | 3x faster than Opus |
| Code Quality | High | Production-ready output |
| Long Context | Good | 200K tokens |
| Cost Efficiency | Good | $3 input / $15 output per million |

### Ideal Use Cases

- Agentic coding and development workflows
- Production application backends
- Balanced quality/speed workloads
- Multi-file operations
- API integrations with tools
- General-purpose work

### When NOT to Use Sonnet

- Highest-end creative work (use Opus)
- Simple classification at scale (use Haiku)
- Maximum speed required (use Haiku)
- Complex research synthesis (consider Opus)

## Key Optimizations

### 1. Explicit Instruction Following

Sonnet 4.5 follows instructions precisely. Be extremely explicit:

```xml
<!-- Too vague -->
Create an analytics dashboard.

<!-- Explicit (better) -->
Create an analytics dashboard. Include as many relevant features and
interactions as possible. Go beyond the basics to create a fully-featured
implementation with:
- Real-time data visualization
- Interactive filtering
- Export functionality
- Responsive design
- Smooth animations
```

### 2. Context and Motivation

Provide context to help Sonnet understand goals:

```xml
<context>
We're building a customer support tool for a SaaS company with 10,000+ users.
Response time is critical, and we need to prioritize high-urgency issues.
The support team consists of 5 people handling 200+ tickets daily.
</context>

<task>
Design a ticket classification system that helps route tickets efficiently.
</task>
```

### 3. Default to Action

Sonnet follows instructions precisely—if you say "suggest," it will suggest rather than implement.

**For proactive implementation:**

```xml
<default_to_action>
By default, implement changes rather than only suggesting them. If intent is
unclear, infer the most useful likely action and proceed, using tools to
discover any missing details instead of guessing. Try to infer whether a tool
call is intended and act accordingly.
</default_to_action>
```

**For cautious approach:**

```xml
<do_not_act_before_instructions>
Do not jump into implementation unless clearly instructed to make changes.
When intent is ambiguous, default to providing information, doing research,
and providing recommendations rather than taking action. Only proceed with
edits when explicitly requested.
</do_not_act_before_instructions>
```

### 4. Parallel Tool Calling

Sonnet is aggressive about parallel operations. This is usually good but can be controlled:

**Maximize parallelism:**

```xml
<use_parallel_tool_calls>
If you intend to call multiple tools and there are no dependencies between
them, make all independent calls in parallel. Prioritize calling tools
simultaneously whenever possible. For example, when reading 3 files, run 3
tool calls in parallel. Maximize parallel tool calls for speed and efficiency.

However, if some tool calls depend on previous calls to inform parameters,
do NOT call these in parallel—call them sequentially. Never use placeholders
or guess missing parameters.
</use_parallel_tool_calls>
```

**Reduce parallelism:**

```
Execute operations sequentially with brief pauses between each step to
ensure stability.
```

### 5. Context Management

Sonnet tracks its token budget. For long tasks:

```xml
<context_management>
Your context window will be automatically compacted as it approaches its limit,
allowing you to continue working indefinitely. Therefore, do not stop tasks
early due to token budget concerns. As you approach your token budget limit,
save your current progress and state to memory before the context window
refreshes. Always be persistent and autonomous—complete tasks fully, even if
the end of your budget is approaching. Never artificially stop any task early.
</context_management>
```

### 6. Communication Style

Sonnet is concise and may skip verbal summaries after tool use.

**For more visibility:**

```
After completing a task that involves tool use, provide a quick summary
of the work you've done.
```

### 7. Avoiding Test Fixation

Sonnet can focus too heavily on making tests pass at the expense of general solutions:

```xml
<general_solution_focus>
Write a high-quality, general-purpose solution using standard tools.
Do not create helper scripts or workarounds. Implement a solution that
works correctly for all valid inputs, not just the test cases.

Do not hard-code values or create solutions that only work for specific
test inputs. Implement the actual logic that solves the problem generally.

Focus on understanding requirements and implementing the correct algorithm.
Tests verify correctness—they don't define the solution. If tests are
incorrect, inform me rather than working around them.
</general_solution_focus>
```

### 8. Format Control

Sonnet may produce more markdown than desired. To reduce:

```xml
<avoid_excessive_markdown>
When writing reports, documents, or explanations, write in clear, flowing
prose using complete paragraphs. Reserve markdown for inline code, code
blocks, and simple headings. Avoid using **bold** and *italics*.

DO NOT use ordered or unordered lists unless:
a) presenting truly discrete items where list format is best, or
b) the user explicitly requests a list

Instead of bullets, incorporate items naturally into sentences. Your goal
is readable, flowing text that guides the reader through ideas naturally.
</avoid_excessive_markdown>
```

## Prompt Patterns for Sonnet

### Agentic Coding

```xml
<coding_task>
[Description of what needs to be built/changed]
</coding_task>

<approach>
1. First, explore the relevant code to understand existing patterns
2. Implement changes following existing conventions
3. Test your implementation
4. Clean up any temporary files created
</approach>

<constraints>
- Follow existing code style
- Don't add unnecessary abstractions
- Keep changes focused on the task
</constraints>
```

### Multi-File Operations

```xml
<task>
Refactor the authentication system across multiple files.
</task>

<files_to_modify>
- src/auth/login.ts
- src/auth/session.ts
- src/middleware/auth.ts
</files_to_modify>

<approach>
Read all files in parallel to understand the current implementation.
Then apply changes systematically, maintaining consistency across files.
</approach>
```

### Production API Work

```xml
<api_task>
Create a RESTful API endpoint for [functionality].
</api_task>

<requirements>
- Follow existing API patterns in the codebase
- Include proper error handling
- Add input validation
- Write tests
- Update API documentation
</requirements>

<quality_standards>
- Production-ready code
- Clear error messages
- Proper status codes
- Consistent with existing endpoints
</quality_standards>
```

### Balanced Analysis

```xml
<analysis_task>
Evaluate [topic] considering practical implications.
</analysis_task>

<approach>
1. Gather relevant information efficiently
2. Focus on actionable insights
3. Provide clear recommendations
4. Note key trade-offs
</approach>

<output>
- Keep response focused and practical
- Prioritize actionable information
- Include specific next steps
</output>
```

## State Tracking Across Sessions

### For Multi-Context Workflows

```xml
<state_management>
Use structured formats for test results and task status.
Use unstructured text for progress notes.
Use git for state tracking across sessions.
Focus on incremental progress—a few things at a time.
</state_management>
```

### Starting Fresh Sessions

```
You are continuing work on [project]. Review these files to understand state:
- progress.txt - Current status
- tests.json - Test results
- git log - Recent changes

Run integration tests before implementing new features.
```

## Cost and Performance

| Metric | Value |
|--------|-------|
| Input | $3/million tokens |
| Output | $15/million tokens |
| Context Window | 200K tokens |
| Speed | Fast (3x Opus) |
| Quality | High |

### Cost vs Opus

- 5x cheaper on input
- 5x cheaper on output
- 3x faster
- 95% of quality for most tasks

## When to Choose Sonnet

| Task Type | Choose Sonnet? |
|-----------|----------------|
| Agentic coding | Yes (best choice) |
| Production code | Yes |
| Multi-file refactoring | Yes |
| API development | Yes |
| General analysis | Yes |
| Complex research | Consider Opus |
| Highest-quality creative | Consider Opus |
| Simple classification | Consider Haiku |

## Quick Reference

**Optimize Sonnet by:**
- Being extremely explicit about requirements
- Providing context and motivation
- Controlling action vs suggestion behavior
- Leveraging parallel tool calling
- Managing context for long tasks
- Preventing test fixation

**Avoid:**
- Vague instructions (Sonnet takes them literally)
- Expecting "above and beyond" without asking
- Ignoring its parallel tool capabilities
- Using for simple tasks where Haiku suffices

## Summary

Claude Sonnet 4.5 is the optimal choice for most development and production work. Optimize by:
1. Being extremely explicit about what you want
2. Providing context for better understanding
3. Controlling tool usage behavior explicitly
4. Leveraging parallel operations
5. Managing context for long-running tasks
6. Focusing on general solutions, not test-specific ones

Use Sonnet for balanced quality-speed-cost workloads and agentic development.
