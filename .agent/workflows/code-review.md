---
description: Perform comprehensive code review before PR or deployment
---

# Code Review Workflow

## Step 1: Security Check

Scan for security issues:
- [ ] No API keys/secrets in code
- [ ] No hardcoded passwords
- [ ] .env files in .gitignore
- [ ] Input validation on user inputs
- [ ] SQL injection prevention (if applicable)
- [ ] XSS prevention (if applicable)

**Report any issues found.**

---

## Step 2: Performance Check

Look for performance issues:
- [ ] No unnecessary re-renders (React)
- [ ] No N+1 queries (database)
- [ ] Large files chunked/lazy loaded
- [ ] Proper caching used
- [ ] No blocking operations in async code

---

## Step 3: Code Quality

Check code quality:
- [ ] Functions are small and focused
- [ ] Clear variable/function names
- [ ] No dead code
- [ ] Consistent formatting
- [ ] DRY (Don't Repeat Yourself)
- [ ] Proper error handling

---

## Step 4: Best Practices

Verify best practices:

**Python:**
- [ ] Type hints used
- [ ] Docstrings present
- [ ] Virtual environment used

**JavaScript/TypeScript:**
- [ ] TypeScript types defined
- [ ] No `any` types (unless necessary)
- [ ] Async/await used properly

**React:**
- [ ] Components are functional
- [ ] Hooks used correctly
- [ ] Keys on list items
- [ ] No prop drilling (use context if needed)

---

## Step 5: Documentation

Check documentation:
- [ ] README is up to date
- [ ] Complex functions have comments
- [ ] API endpoints documented
- [ ] Environment variables documented

---

## Step 6: Testing

Verify tests:
- [ ] Critical paths have tests
- [ ] Tests pass
- [ ] Edge cases covered

---

## Review Report

Provide a summary:

**Critical Issues:** (must fix before deploy)
- ...

**Recommended Improvements:** (nice to have)
- ...

**Good Practices Found:** (positive feedback)
- ...
