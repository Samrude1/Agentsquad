---
description: Add unit tests to existing code
---

# Add Tests Workflow

## Step 1: Identify What to Test

Prioritize testing:
1. [ ] Critical business logic
2. [ ] Functions with complex calculations
3. [ ] API endpoints
4. [ ] User input handling
5. [ ] Error handling paths

**List functions/components to test.**

---

## Step 2: Set Up Testing Framework

**Python:**
// turbo
```bash
pip install pytest pytest-cov
```

**JavaScript/TypeScript:**
// turbo
```bash
npm install --save-dev jest @types/jest ts-jest
```

**React:**
// turbo
```bash
npm install --save-dev @testing-library/react @testing-library/jest-dom
```

---

## Step 3: Create Test Structure

```
project/
├── src/
│   └── utils.py (or .ts)
└── tests/
    └── test_utils.py (or utils.test.ts)
```

---

## Step 4: Write Unit Tests

**Python (pytest):**
```python
# tests/test_calculator.py
from src.calculator import add, multiply

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_multiply_by_zero():
    assert multiply(5, 0) == 0
```

**TypeScript (Jest):**
```typescript
// tests/calculator.test.ts
import { add, multiply } from '../src/calculator';

describe('Calculator', () => {
  test('adds positive numbers', () => {
    expect(add(2, 3)).toBe(5);
  });

  test('multiplies by zero', () => {
    expect(multiply(5, 0)).toBe(0);
  });
});
```

---

## Step 5: Test Edge Cases

Always test:
- [ ] Empty inputs
- [ ] Null/undefined values
- [ ] Boundary values (0, -1, max)
- [ ] Invalid inputs
- [ ] Error conditions

---

## Step 6: Test Async Code

**Python:**
```python
import pytest

@pytest.mark.asyncio
async def test_async_function():
    result = await my_async_function()
    assert result == expected
```

**JavaScript:**
```typescript
test('fetches data', async () => {
  const data = await fetchData();
  expect(data).toBeDefined();
});
```

---

## Step 7: Mock External Dependencies

**Python:**
```python
from unittest.mock import patch

@patch('module.external_api_call')
def test_with_mock(mock_api):
    mock_api.return_value = {'status': 'ok'}
    result = function_that_calls_api()
    assert result == expected
```

**JavaScript:**
```typescript
jest.mock('../api', () => ({
  fetchData: jest.fn(() => Promise.resolve({ data: 'mocked' }))
}));
```

---

## Step 8: Run Tests

// turbo
**Python:**
```bash
pytest -v --cov=src
```

**JavaScript:**
```bash
npm test -- --coverage
```

---

## Step 9: Check Coverage

Aim for:
- [ ] 80%+ line coverage for critical code
- [ ] 100% branch coverage for business logic
- [ ] All error paths tested

---

## Test Report

**Tests added:** X
**Coverage before:** Y%
**Coverage after:** Z%
**Critical paths covered:** [list]
