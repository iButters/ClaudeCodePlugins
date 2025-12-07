# Code Generation Prompt Examples

## Function Generation

### Python Function with Type Hints

**Optimized for: Claude Sonnet 4.5 / GPT 5.1 Codex**

```xml
<task>
Create a Python function with the specified behavior.
</task>

<requirements>
Function: validate_email
Purpose: Validate if a string is a properly formatted email address

Requirements:
1. Accept a single string parameter
2. Return True if valid email format, False otherwise
3. Use regex for validation
4. Handle edge cases (empty string, None, etc.)
</requirements>

<specifications>
- Python 3.11+
- Include type hints for all parameters and return value
- Include docstring with description and examples
- Follow PEP 8 style guide
</specifications>

<test_cases>
- validate_email("user@example.com") → True
- validate_email("invalid-email") → False
- validate_email("user.name+tag@domain.co.uk") → True
- validate_email("") → False
- validate_email(None) → False (handle gracefully)
</test_cases>

<output>
Provide only the function code, no explanations.
</output>
```

---

## API Endpoint Generation

### REST API Endpoint

**Optimized for: Claude Sonnet 4.5**

```xml
<context>
Framework: FastAPI
Database: SQLAlchemy with PostgreSQL
Auth: JWT tokens
Existing patterns: See examples below
</context>

<task>
Create an API endpoint for user profile updates.
</task>

<requirements>
- Endpoint: PUT /api/v1/users/{user_id}/profile
- Authentication required
- Only user can update their own profile
- Accept: display_name, bio, avatar_url (all optional)
- Validate: bio max 500 chars, avatar_url must be valid URL
- Return: Updated user profile
</requirements>

<existing_pattern>
```python
@router.get("/users/{user_id}")
async def get_user(
    user_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
) -> UserResponse:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse.from_orm(user)
```
</existing_pattern>

<output>
Provide:
1. Pydantic model for request body
2. Endpoint function
3. Any helper functions needed
</output>
```

---

## Class Generation

### TypeScript Class

**Optimized for: GPT 5.1 Codex**

```
Language: TypeScript
Runtime: Node.js 20

Create a class with the following specification:

Class: CacheManager<T>

Purpose: In-memory cache with TTL support

Constructor:
- defaultTtl: number (milliseconds, default 60000)

Methods:
- set(key: string, value: T, ttl?: number): void
- get(key: string): T | undefined
- has(key: string): boolean
- delete(key: string): boolean
- clear(): void
- size(): number

Requirements:
- Generic type T for cached values
- Automatic cleanup of expired entries
- Thread-safe for async operations
- Memory efficient (don't store expired entries)

Include:
- JSDoc comments for all public methods
- Private helper methods as needed
- Type definitions for internal structures

Example usage:
```typescript
const cache = new CacheManager<User>(30000);
cache.set("user:123", user);
const cached = cache.get("user:123"); // User | undefined
```
```

---

## Test Generation

### Unit Tests

**Optimized for: Claude Sonnet 4.5**

```xml
<task>
Generate comprehensive unit tests for the provided function.
</task>

<function>
```python
def calculate_discount(price: float, discount_percent: float, max_discount: float = None) -> float:
    """
    Calculate the discounted price.

    Args:
        price: Original price (must be >= 0)
        discount_percent: Discount percentage (0-100)
        max_discount: Maximum discount amount (optional)

    Returns:
        Final price after discount

    Raises:
        ValueError: If price < 0 or discount_percent not in 0-100
    """
    if price < 0:
        raise ValueError("Price cannot be negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")

    discount = price * (discount_percent / 100)
    if max_discount is not None and discount > max_discount:
        discount = max_discount

    return round(price - discount, 2)
```
</function>

<testing_requirements>
- Framework: pytest
- Coverage: All branches and edge cases
- Organization: Grouped by functionality
- Naming: test_[scenario]_[expected_result]
</testing_requirements>

<test_categories>
1. Happy path tests
2. Edge cases (zero, max values)
3. Error cases (invalid inputs)
4. Boundary tests
5. max_discount parameter tests
</test_categories>

<output>
Complete pytest test file with all test cases.
</output>
```

---

## Refactoring

### Code Improvement

**Optimized for: Claude Opus 4.5**

```xml
<task>
Refactor this code to improve quality while maintaining functionality.
</task>

<code>
```python
def process_data(data):
    result = []
    for i in range(len(data)):
        if data[i]['status'] == 'active':
            item = {}
            item['name'] = data[i]['name'].upper()
            item['email'] = data[i]['email'].lower()
            if data[i]['age'] >= 18:
                item['adult'] = True
            else:
                item['adult'] = False
            item['score'] = data[i]['points'] / data[i]['max_points'] * 100
            result.append(item)
    return result
```
</code>

<goals>
1. Improve readability
2. Use Pythonic patterns
3. Add type hints
4. Handle potential errors
5. Improve performance if possible
</goals>

<constraints>
- Maintain same input/output behavior
- Keep it simple (no unnecessary abstractions)
- Compatible with Python 3.9+
</constraints>

<output>
1. Refactored code
2. Brief explanation of changes
</output>
```

---

## Algorithm Implementation

### Data Structure Implementation

**Optimized for: Claude Sonnet 4.5 / GPT 5.1 Codex**

```xml
<task>
Implement a Least Recently Used (LRU) Cache.
</task>

<specifications>
Language: Python 3.11+
Class name: LRUCache

Constructor:
- capacity: int (maximum number of items)

Methods:
- get(key: str) -> Any | None
  - Returns value if exists, None otherwise
  - Marks key as recently used

- put(key: str, value: Any) -> None
  - Adds or updates key-value pair
  - Evicts least recently used if at capacity

Performance requirements:
- get: O(1)
- put: O(1)
</specifications>

<test_cases>
cache = LRUCache(2)
cache.put("a", 1)
cache.put("b", 2)
cache.get("a")      # Returns 1, "a" is now most recent
cache.put("c", 3)   # Evicts "b" (least recently used)
cache.get("b")      # Returns None
cache.get("a")      # Returns 1
cache.get("c")      # Returns 3
</test_cases>

<hints>
Consider using: OrderedDict, or combination of dict + doubly linked list
</hints>

<output>
Complete implementation with:
1. Class code
2. Brief complexity analysis
</output>
```

---

## Database Query Generation

### SQL Query

**Optimized for: Claude Sonnet 4.5**

```xml
<schema>
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    created_at TIMESTAMP DEFAULT NOW(),
    subscription_tier VARCHAR(50)
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    amount DECIMAL(10,2),
    status VARCHAR(50),
    created_at TIMESTAMP DEFAULT NOW()
);
```
</schema>

<task>
Write a SQL query to find the top 10 users by total order value
in the last 30 days, including only completed orders.
</task>

<requirements>
- Include: user_id, email, total_order_value, order_count
- Only completed orders (status = 'completed')
- Only orders from last 30 days
- Order by total value descending
- Limit to top 10
</requirements>

<output>
PostgreSQL query, optimized for performance.
</output>
```

---

## Best Practices for Code Generation Prompts

### 1. Specify Language and Version
Always state: `Language: Python 3.11+` or `TypeScript 5.x`

### 2. Provide Context
Include framework, existing patterns, related code.

### 3. Define Clear Requirements
- What it should do (functionality)
- How it should behave (edge cases)
- How it should look (style, patterns)

### 4. Include Test Cases
Examples of input/output help ensure correctness.

### 5. Show Existing Patterns
If code should match existing style, provide examples.

### 6. Specify Output Format
```
Provide:
1. Main code
2. Tests (optional)
3. Brief explanation (optional)
```

### 7. Model Selection
- **Sonnet 4.5**: Agentic coding, multi-file, production code
- **Codex**: Focused generation, completions
- **Opus 4.5**: Architecture decisions, complex algorithms
- **Haiku 4.5**: Simple transformations, formatting
