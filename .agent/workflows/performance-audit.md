---
description: Analyze and optimize application performance
---

# Performance Audit Workflow

## Step 1: Identify Performance Issues

Ask the user:
- [ ] What feels slow?
- [ ] When does it slow down?
- [ ] First load or ongoing usage?
- [ ] Which pages/features?

---

## Step 2: Frontend Performance

### Check Bundle Size
// turbo
```bash
npm run build
```
Look at bundle sizes. Large bundles (>500KB) need optimization.

### Check for:
- [ ] Large images not optimized
- [ ] Unused dependencies
- [ ] No code splitting
- [ ] No lazy loading

### React-Specific:
- [ ] Unnecessary re-renders (use React DevTools Profiler)
- [ ] Missing `useMemo`/`useCallback` on expensive operations
- [ ] Missing `key` props causing full list re-renders

---

## Step 3: API Performance

### Check Response Times
- [ ] API calls taking >500ms
- [ ] Large payloads (>100KB)
- [ ] Too many API calls

### Optimize:
- [ ] Add caching
- [ ] Reduce payload size
- [ ] Batch requests
- [ ] Add pagination

---

## Step 4: Database Performance (if applicable)

### Check for:
- [ ] N+1 queries
- [ ] Missing indexes
- [ ] Large table scans
- [ ] No connection pooling

---

## Step 5: Frontend Optimizations

### Image Optimization
```jsx
// Use Next.js Image component
import Image from 'next/image';
<Image src="/photo.jpg" width={500} height={300} loading="lazy" />
```

### Code Splitting
```jsx
// Lazy load components
import dynamic from 'next/dynamic';
const HeavyComponent = dynamic(() => import('./HeavyComponent'), {
  loading: () => <p>Loading...</p>
});
```

### Memoization
```jsx
const expensiveValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
const memoizedCallback = useCallback(() => doSomething(a), [a]);
```

---

## Step 6: Backend Optimizations

### Python/FastAPI:
```python
# Add caching
from functools import lru_cache

@lru_cache(maxsize=100)
def expensive_computation(param):
    ...

# Use async properly
async def endpoint():
    results = await asyncio.gather(
        fetch_data_1(),
        fetch_data_2(),
    )
    return results
```

### Add Response Caching Headers:
```python
from fastapi import Response

@app.get("/data")
def get_data(response: Response):
    response.headers["Cache-Control"] = "max-age=3600"
    return data
```

---

## Step 7: Measure Improvement

Before and after metrics:
- [ ] Initial load time
- [ ] Time to Interactive (TTI)
- [ ] API response times
- [ ] Bundle size

---

## Performance Report

**Issues Found:**
1. [Issue] - [Impact]
2. [Issue] - [Impact]

**Optimizations Applied:**
1. [Change] - [Improvement]
2. [Change] - [Improvement]

**Results:**
- Load time: X → Y ms (Z% improvement)
- Bundle size: X → Y KB
- API response: X → Y ms
