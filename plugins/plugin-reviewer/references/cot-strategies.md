# Chain-of-Thought Strategies - Practical Guide

**Used By**:
- `agents/cot-evaluator.md` (CoT presence detection, step count optimization, type classification)
- `agents/review-orchestrator.md` (Multi-phase workflow orchestration)
- `skills/plugin-reviewer/SKILL.md` (Workflow structuring and step decomposition)

---

Chain-of-thought (CoT) prompting guides LLMs through stepwise reasoning. The right CoT strategy and optimal step count depend on task complexity.

## When to Use CoT

CoT is especially valuable for tasks that require multi-stage reasoning. Simple lookups or direct answers do not benefit, but complex problems that need decomposition, intermediate steps, or logical deduction show major gains.

**Use CoT for:**
- Multi-step reasoning (e.g., math problems, algorithms)
- Complex code generation with many constraints
- Architecture decisions that weigh trade-offs
- Debugging where hypotheses must be tested
- Requirements analysis where multiple aspects must be considered

**Use zero-shot for:**
- Simple fact queries
- Single-step transformations
- Template-based generation
- Simple code completion

## Optimal Step Counts by Complexity

Research shows a clear correlation between task complexity and optimal step count. Each additional step costs roughly 8-10% more tokens (Sonnet 4.5 optimized) but brings 3-5% additional accuracy.

| Complexity   | Optimal Steps | Token Overhead | Accuracy Gain | Example Tasks                           |
|--------------|---------------|----------------|---------------|-----------------------------------------|
| Simple       | 2-3 steps     | +16-20%        | +5-8%         | Simple validation, basic transformations|
| Medium       | 3-5 steps     | +32-40%        | +10-15%       | Standard code generation, refactoring   |
| Complex      | 5-7 steps     | +48-60%        | +15-20%       | Multi-constraint code, architecture design |
| Very Complex | 7-9 steps     | +64-80%        | +18-25%       | System design, security analysis        |

**Cost-benefit:** For simple tasks the overhead is rarely worth it. For complex tasks, the ROI is clearly positive.

## Standard Chain-of-Thought

The simplest form just asks the LLM to think step by step:

```
Task: Write a function that finds the second largest number in a list.

Think step by step:
1. What edge cases need handling?
2. What algorithm should we use?
3. How do we implement it?

Then write the code.
```

This produces generic steps that are often not optimally structured. For better results, use specialized CoT variants.

## Structured Chain-of-Thought (for code tasks)

Structured CoT explicitly integrates programming-structure concepts into the reasoning steps. Instead of generic steps, it uses domain-specific categories.

**Template for code generation:**
```
Generate a [language] function that [task description].

Analyze step-by-step with this structure:

INITIALIZATION:
- What variables or state need to be initialized?
- What are the initial conditions?

ITERATION:
- How will we traverse the data?
- What loop structure is appropriate?

COMPARISON/COMPUTATION:
- What comparisons or calculations are needed in each step?
- How do we track the result?

EDGE CASES:
- What special cases need handling?
- What could go wrong?

RETURN:
- What do we return?
- In what format?

Now implement the function based on this analysis.
```

**Example in action:**
```
Task: Find the second largest number in a list.

INITIALIZATION:
- Need to track the largest and second_largest
- Initialize both to None or negative infinity

ITERATION:
- Loop through all numbers in the list
- Single pass is sufficient (O(n))

COMPARISON/COMPUTATION:
- For each number:
  - If larger than current largest: second_largest = largest, largest = current
  - Else if larger than second_largest: second_largest = current

EDGE CASES:
- Empty list -> return None
- Single element -> return None (no second largest)
- All identical -> return None or that value (design choice)
- Fewer than two unique values -> return None

RETURN:
- Return second_largest (could be None)

Implementation:
def second_largest(numbers: list[int]) -> int | None:
    if len(numbers) < 2:
        return None
    
    largest = second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_largest if second_largest != float('-inf') else None
```

**Improvement over standard CoT:** Pass@1 improves by roughly 14% through structured decomposition.

## Semantic Chain-of-Thought (for refactoring)

Semantic CoT incorporates code semantics, data flow, and control flow into the reasoning steps. This is especially valuable for refactoring and architecture decisions.

**Template for refactoring:**
```
Refactor this code to improve [specific aspect].

Analyze the semantics step-by-step:

DATA FLOW:
- What data flows from input to output?
- Are there unnecessary transformations?
- Can we simplify the data pipeline?

CONTROL FLOW:
- In what order are statements executed?
- Are there unnecessary branches?
- Can we reduce cyclomatic complexity?

INVARIANTS:
- What conditions must always be true?
- Can we make implicit invariants explicit?
- Are there hidden assumptions?

ABSTRACTIONS:
- What abstractions can be extracted?
- What responsibilities can be separated?
- What patterns emerge?

Now perform the refactoring based on this analysis.
```

**Example:**
```
Original Code:
def process_users(users):
    result = []
    for user in users:
        if user.age >= 18:
            if user.country == "US":
                if user.verified:
                    result.append(user)
    return result

DATA FLOW:
Input: list of users -> filter chain -> output: list of eligible users
The data only flows one way, good. No mutations.

CONTROL FLOW:
Three nested conditionals create complexity (CC = 4)
Each condition is independent and could be combined
Sequential filtering would be clearer

INVARIANTS:
All users in result must satisfy: age >= 18 AND country == "US" AND verified
This invariant should be explicit

ABSTRACTIONS:
The filtering logic can be extracted into a predicate function
The concept of "eligible user" is implicit but important

Refactored:
def is_eligible_user(user) -> bool:
    """Check if user is eligible (18+, US, verified)."""
    return user.age >= 18 and user.country == "US" and user.verified

def process_users(users):
    """Return all eligible users."""
    return [user for user in users if is_eligible_user(user)]
```

## Progressive CoT (for very complex tasks)

For very complex tasks with seven to nine steps, a progressive strategy is effective, where each step builds on the previous one.

**Template:**
```
[Complex Task Description]

Let's solve this progressively:

STEP 1 - Problem Decomposition:
Break the problem into independent sub-problems.

STEP 2 - Constraint Analysis:
Identify all constraints and requirements.

STEP 3 - Approach Selection:
Evaluate different approaches and select the best.

STEP 4 - High-Level Design:
Sketch the overall structure.

STEP 5 - Detailed Design:
Design each component in detail.

STEP 6 - Edge Case Planning:
Identify all edge cases and how to handle them.

STEP 7 - Implementation:
Write the code with all considerations.

STEP 8 - Verification:
Check against constraints and requirements.

[Optional STEP 9 - Optimization:
Identify optimization opportunities.]
```

This approach is especially valuable for system design, security-critical code, or complex algorithms.

## Anti-Patterns (avoid these)

**Too many steps for simple tasks:**
A simple "reverse a string" does not need seven steps. That wastes tokens without value.

**Too few steps for complex tasks:**
A complex algorithm with only "Step 1: Think about it, Step 2: Write code" is too shallow.

**Generic steps without structure:**
"Step 1: Understand the problem, Step 2: Think of solution, Step 3: Implement" is not better than no CoT.

**Repeating steps:**
If multiple steps ask the same thing, the structure is poorly chosen.

## Practical Tips

**For code generation:** use Structured CoT with INITIALIZATION -> ITERATION -> COMPARISON -> EDGE CASES -> RETURN

**For refactoring:** use Semantic CoT with DATA FLOW -> CONTROL FLOW -> INVARIANTS -> ABSTRACTIONS

**For debugging:** use Hypothesis-Testing CoT with OBSERVE -> HYPOTHESIZE -> TEST -> CONCLUDE

**For architecture:** use Progressive CoT with Decomposition -> Constraints -> Approaches -> Design -> Verification

**Quick check if CoT helps:**
Run the same task once with and once without CoT. If the difference is minimal, you probably do not need CoT for this task type.

## Debugging CoT

If CoT does not deliver expected improvements:

1. **Check step count:** too many or too few steps?
2. **Check structure:** are the steps logically building or arbitrary?
3. **Check relevance:** are the steps task-specific or too generic?
4. **Compare strategies:** maybe standard CoT is better for your task than structured CoT?
5. **Consider zero-shot:** sometimes no CoT is better than a poorly structured CoT.
