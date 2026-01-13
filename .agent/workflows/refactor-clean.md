---
description: Clean up and refactor messy code
---

# Refactor & Clean Workflow

## Step 1: Identify Problem Areas

Scan the codebase for:
- [ ] Functions longer than 50 lines
- [ ] Deeply nested code (>3 levels)
- [ ] Repeated code blocks
- [ ] Poor naming
- [ ] Dead/unused code
- [ ] TODO/FIXME comments

**List files that need refactoring.**

---

## Step 2: Remove Dead Code

Find and remove:
- [ ] Unused imports
- [ ] Unused variables
- [ ] Commented-out code blocks
- [ ] Unused functions
- [ ] Unreachable code

// turbo
Use linter to identify unused code.

---

## Step 3: Improve Naming

Rename for clarity:

**Bad → Good:**
- `x` → `userCount`
- `data` → `apiResponse`
- `handle` → `handleFormSubmit`
- `process` → `validateUserInput`

---

## Step 4: Extract Functions

Break large functions into smaller ones:

**Before:**
```python
def process_order(order):
    # 50 lines of validation
    # 30 lines of calculation
    # 20 lines of saving
    pass
```

**After:**
```python
def process_order(order):
    validated = validate_order(order)
    calculated = calculate_totals(validated)
    return save_order(calculated)
```

---

## Step 5: Remove Duplication (DRY)

Find repeated patterns and extract:
- [ ] Helper functions
- [ ] Shared utilities
- [ ] Constants
- [ ] Reusable components (React)

---

## Step 6: Simplify Logic

Reduce complexity:

**Flatten nested conditionals:**
```python
# Before
if a:
    if b:
        if c:
            do_thing()

# After (early returns)
if not a: return
if not b: return
if not c: return
do_thing()
```

---

## Step 7: Add Type Hints (Python) / Types (TypeScript)

Add types where missing:
```python
def calculate_total(items: list[Item], discount: float) -> float:
    ...
```

```typescript
function calculateTotal(items: Item[], discount: number): number {
    ...
}
```

---

## Step 8: Format and Lint

// turbo
Run formatters and linters:

**Python:**
```bash
black .
isort .
flake8 .
```

**JavaScript/TypeScript:**
```bash
npm run lint
npm run format
```

---

## Step 9: Test After Refactoring

Verify nothing is broken:
- [ ] Run existing tests
- [ ] Manual testing of key features
- [ ] Check for regressions

---

## Refactoring Report

**Files changed:** [list]
**Improvements made:**
- Removed X lines of dead code
- Extracted Y helper functions
- Improved naming in Z places
- Reduced nesting in N functions
