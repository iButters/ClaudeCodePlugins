# Few-Shot Optimization - Practical Guide

**Used By**:
- `agents/few-shot-evaluator.md` (Example count, quality, ordering, and diversity analysis)
- `skills/plugin-reviewer/SKILL.md` (Example structure and progression guidance)

---

Few-shot learning improves LLM performance through examples. The quality and number of examples are critical, but ordering is just as important as count.

## Optimal Example Counts by Task Type

| Task Type        | Optimal Count | Accuracy Gain | Rationale                                 |
|------------------|---------------|---------------|-------------------------------------------|
| Code Generation  | 4-6 examples  | +8-12%        | Balance between context and overhead      |
| Code Analysis    | 3-4 examples  | +5-8%         | Pattern recognition needs fewer examples  |
| Refactoring      | 2-3 examples  | +6-10%        | Before/after transforms are self-explanatory |
| Test Generation  | 4-5 examples  | +7-9%         | Structural consistency matters            |
| Debugging        | 1-2 examples (or zero-shot) | Variable | Too many examples can confuse         |

**Important:** More examples are not always better. Above seven examples, diminishing returns set in because token overhead exceeds the benefit.

## PERO Strategy (Priming Example Reordering)

The order of examples has a surprisingly large impact on performance. PERO says: **order examples from easy to hard (Easy -> Hard)**.

### Why PERO works

LLMs learn from examples while reading the prompt. If examples are ordered from simple to complex, the model can build patterns incrementally. This improves accuracy by **5-10% compared to random ordering**.

### Complexity Score Calculation

To order examples objectively by complexity, use this algorithm:

```
Complexity Score =
  (Lines of Code * 0.3) +
  (Conditionals * 2.0) +
  (Try/Except Blocks * 3.0) +
  (Classes * 5.0) +
  (Nesting Depth * 1.5)
```

**Example:**
```python
# Example A: 5 LOC, 1 if, 0 try/except, 0 classes, nesting 1
Score = (5 * 0.3) + (1 * 2.0) + 0 + 0 + (1 * 1.5) = 5.0

# Example B: 12 LOC, 3 if, 1 try/except, 0 classes, nesting 2
Score = (12 * 0.3) + (3 * 2.0) + (1 * 3.0) + 0 + (2 * 1.5) = 15.6

# Example C: 8 LOC, 2 if, 0 try/except, 0 classes, nesting 1
Score = (8 * 0.3) + (2 * 2.0) + 0 + 0 + (1 * 1.5) = 8.9
```

**Correct PERO order:** A (5.0) -> C (8.9) -> B (15.6)

## Example Quality Criteria

Good few-shot examples meet these criteria.

### 1. Completeness
Each example should include:
- **Input:** clear specification of the task
- **Output:** complete, correct solution
- **Explanation (optional):** why this approach works

```
Incomplete:
Example: Write a function to reverse a string
def reverse_string(s): ...

Complete:
Example: Write a function to reverse a string
def reverse_string(s: str) -> str:
    """Reverse a string using slicing."""
    return s[::-1]
```

### 2. Diversity
Examples should cover different aspects of the task:

```python
# Example 1: Basic case (simple string)
reverse_string("hello") -> "olleh"

# Example 2: Edge case (empty string)
reverse_string("") -> ""

# Example 3: Edge case (single character)
reverse_string("a") -> "a"

# Example 4: Complex case (special characters)
reverse_string("Hello, World!") -> "!dlroW ,olleH"
```

### 3. Consistency
All examples should use the same style and conventions:

```
Inconsistent:
Example 1: camelCase naming
Example 2: snake_case naming
Example 3: No type hints
Example 4: Full type hints

Consistent:
All examples use snake_case, type hints, docstrings
```

## Practical Templates

### Template 1: Code Generation

```
Generate a [language] function that [task description].

Example 1 (Basic):
Task: Sum two numbers
def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b

Example 2 (Edge Cases):
Task: Sum a list of numbers (handle empty list)
def sum_list(numbers: list[int]) -> int:
    """Return sum of all numbers in list, 0 for empty list."""
    return sum(numbers) if numbers else 0

Example 3 (Error Handling):
Task: Divide two numbers (handle division by zero)
def divide(a: float, b: float) -> float:
    """Divide a by b, raise ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

Example 4 (Complex):
Task: [Your complex task]
[Let the LLM generate based on the progression]
```

### Template 2: Refactoring

```
Refactor this code to improve [specific aspect].

Example 1 (Simple - Extract Variable):
Before:
if user.age >= 18 and user.country == "US" and user.verified:
    grant_access()

After:
is_adult = user.age >= 18
is_us_user = user.country == "US"
if is_adult and is_us_user and user.verified:
    grant_access()

Example 2 (Medium - Extract Function):
Before:
result = []
for item in items:
    if item.price < 100:
        result.append(item)
return result

After:
def is_affordable(item):
    return item.price < 100

return [item for item in items if is_affordable(item)]

Now refactor: [Your code]
```

## Anti-Patterns (avoid these)

**1. Too many similar examples**
- Five examples that all show the same simple case
- Better: one simple, one edge case, one error case, one complex case

**2. Wrong ordering**
- Complex -> Medium -> Simple (reverse PERO)
- Random ordering
- Use Simple -> Medium -> Complex (PERO)

**3. Inconsistent quality**
- Example 1 has tests, Example 2 does not
- Example 1 follows best practices, Example 2 has code smells
- Make all examples consistently high quality

**4. Overly generic examples**
- Examples too far from the actual task
- Use examples directly relevant to the task

## Debugging Note

If few-shot does not help or hurts performance, try:
1. **Zero-shot instead** - sometimes examples confuse more than they help
2. **Fewer examples** - 2-3 instead of 5-6
3. **Better ordering** - check PERO compliance
4. **More diverse examples** - cover more aspects

For debugging tasks, research shows zero-shot is often better than few-shot.
