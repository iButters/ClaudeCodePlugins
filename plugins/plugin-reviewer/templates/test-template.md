# Test Template

**Used By**: Plugin generation examples (Example 6 - Migration Assistant)
**Purpose**: Standardized format for test files in generated plugins

---

## Test Suite: [Feature/Component Name]

**Test File**: [path/to/test.spec.js]
**Target File**: [path/to/implementation.js]
**Framework**: [Jest|Mocha|Pytest|etc.]
**Created**: [Date]

---

## Test Structure

```javascript
// Example structure for JavaScript/TypeScript
describe('[ComponentName]', () => {
  // Setup and teardown
  beforeEach(() => {
    // Initialize test fixtures
  });

  afterEach(() => {
    // Cleanup
  });

  // Unit tests grouped by functionality
  describe('Core Functionality', () => {
    it('should [expected behavior]', () => {
      // Arrange
      const input = [...];
      const expected = [...];

      // Act
      const result = functionUnderTest(input);

      // Assert
      expect(result).toEqual(expected);
    });
  });

  describe('Edge Cases', () => {
    it('should handle empty input', () => {
      expect(functionUnderTest([])).toEqual([]);
    });

    it('should handle null input', () => {
      expect(() => functionUnderTest(null)).toThrow();
    });

    it('should handle very large input', () => {
      const largeInput = Array(10000).fill('test');
      expect(() => functionUnderTest(largeInput)).not.toThrow();
    });
  });

  describe('Error Handling', () => {
    it('should throw error for invalid type', () => {
      expect(() => functionUnderTest('invalid')).toThrow(TypeError);
    });

    it('should provide meaningful error message', () => {
      expect(() => functionUnderTest('invalid'))
        .toThrow('Expected array, got string');
    });
  });

  describe('Performance', () => {
    it('should complete within time limit', () => {
      const startTime = Date.now();
      functionUnderTest(testInput);
      const elapsed = Date.now() - startTime;

      expect(elapsed).toBeLessThan(100); // 100ms limit
    });
  });
});
```

---

## Test Categories

### 1. Unit Tests (Happy Path)
Test basic functionality with valid inputs.

**Coverage Target**: 100% of public API

**Example**:
```javascript
it('should add two numbers correctly', () => {
  expect(add(2, 3)).toBe(5);
});
```

---

### 2. Edge Cases
Test boundary conditions and unusual inputs.

**Required Edge Cases**:
- [ ] Empty input ([], '', null, undefined)
- [ ] Minimum valid input (single element, zero, etc.)
- [ ] Maximum valid input (large arrays, max integers)
- [ ] Boundary values (0, -1, MAX_INT, MIN_INT)
- [ ] Special characters (in strings)
- [ ] Unicode/international input

**Example**:
```javascript
it('should handle empty array', () => {
  expect(processArray([])).toEqual([]);
});
```

---

### 3. Error Cases
Test invalid inputs and error handling.

**Required Error Cases**:
- [ ] Wrong type (string instead of number, etc.)
- [ ] Out of range values
- [ ] Missing required parameters
- [ ] Invalid state/preconditions

**Example**:
```javascript
it('should throw TypeError for string input', () => {
  expect(() => add('two', 3)).toThrow(TypeError);
});
```

---

### 4. Integration Tests
Test interaction with dependencies.

**Example**:
```javascript
it('should fetch and process data correctly', async () => {
  const mockAPI = jest.fn().mockResolvedValue({ data: [...] });
  const result = await fetchAndProcess(mockAPI);

  expect(mockAPI).toHaveBeenCalledTimes(1);
  expect(result).toMatchObject({ processed: true });
});
```

---

### 5. Performance Tests
Test time and space complexity.

**Performance Targets**:
- Time complexity: [O(n), O(log n), etc.]
- Space complexity: [O(1), O(n), etc.]
- Max execution time: [N ms]

**Example**:
```javascript
it('should complete large dataset in <1s', () => {
  const largeInput = generateLargeDataset(10000);
  const startTime = performance.now();

  processLargeDataset(largeInput);

  const elapsed = performance.now() - startTime;
  expect(elapsed).toBeLessThan(1000);
});
```

---

## Test Data

### Fixtures
```javascript
const VALID_INPUT = {
  id: 123,
  name: 'Test User',
  email: 'test@example.com'
};

const INVALID_INPUT = {
  id: 'not-a-number',
  name: '',
  email: 'invalid-email'
};

const EDGE_CASES = [
  { description: 'empty object', input: {} },
  { description: 'null values', input: { id: null, name: null } },
  { description: 'very long strings', input: { name: 'A'.repeat(10000) } }
];
```

---

## Mocks and Stubs

### API Mocks
```javascript
const mockAPISuccess = jest.fn().mockResolvedValue({
  status: 200,
  data: { result: 'success' }
});

const mockAPIFailure = jest.fn().mockRejectedValue(
  new Error('Network error')
);
```

### Database Mocks
```javascript
const mockDB = {
  query: jest.fn().mockResolvedValue([{ id: 1, name: 'Test' }]),
  insert: jest.fn().mockResolvedValue({ insertId: 42 }),
  update: jest.fn().mockResolvedValue({ affectedRows: 1 })
};
```

---

## Coverage Requirements

**Minimum Coverage Thresholds**:
- Statements: 80%
- Branches: 75%
- Functions: 90%
- Lines: 80%

**Coverage Report**:
```bash
npm run test:coverage
# or
pytest --cov=src --cov-report=html
```

---

## CI/CD Integration

**Pre-commit Hook**:
```bash
npm test -- --coverage --watchAll=false
```

**CI Pipeline**:
```yaml
test:
  script:
    - npm install
    - npm run test:ci
  coverage: '/All files[^|]*\|[^|]*\s+([\d\.]+)/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml
```

---

## Maintenance Notes

**When to Update Tests**:
- When functionality changes
- When bugs are discovered (add regression test)
- When edge cases are found
- When performance requirements change

**Test Smells to Avoid**:
- Tests depending on execution order
- Shared mutable state between tests
- Tests that test implementation, not behavior
- Overly complex test setup
- Tests without clear assertions

---

**Template Version**: 1.0
**Last Updated**: [Date]
**Maintained By**: QA/Engineering Team
