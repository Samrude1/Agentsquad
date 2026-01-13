---
description: Add API security (rate limiting) to AI projects
---

# API Security Workflow

This workflow adds rate limiting protection to AI projects. Use when the project has a paid AI API (OpenAI, Gemini, Anthropic).

## Step 1: Identify Architecture

Analyze the project and determine:
- [ ] Is this a Python backend (FastAPI/Flask)?
- [ ] Is this a Next.js API Route?
- [ ] Where are AI calls made?
- [ ] Is rate limiting already implemented?

**Report findings before proceeding.**

---

## Step 2: Python Backend (FastAPI)

If the project uses FastAPI:

// turbo
1. Add `slowapi` to `requirements.txt`

2. Add the following imports to `api.py` or equivalent:
```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
```

3. Initialize the limiter:
```python
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
```

4. Add decorators to all POST endpoints:
```python
@app.post("/endpoint")
@limiter.limit("5/minute")
@limiter.limit("50/day")
def endpoint(request: Request):
    ...
```

**NOTE:** Ensure `request: Request` is a parameter!

---

## Step 2 (Alternative): Next.js API Route

If the project uses Next.js:

### For Development (In-Memory):
```typescript
const rateLimitMap = new Map<string, { count: number; resetTime: number }>();

export async function POST(request: Request) {
  const ip = request.headers.get('x-forwarded-for') || 'unknown';
  const now = Date.now();
  const windowMs = 60 * 1000;
  const maxRequests = 5;

  const record = rateLimitMap.get(ip);
  if (record && now < record.resetTime) {
    if (record.count >= maxRequests) {
      return Response.json({ error: 'Too many requests' }, { status: 429 });
    }
    record.count++;
  } else {
    rateLimitMap.set(ip, { count: 1, resetTime: now + windowMs });
  }
  // Continue to AI call...
}
```

### For Production (Upstash Redis):
// turbo
1. Install: `npm install @upstash/ratelimit @upstash/redis`

2. Add to code:
```typescript
import { Ratelimit } from '@upstash/ratelimit';
import { Redis } from '@upstash/redis';

const ratelimit = new Ratelimit({
  redis: Redis.fromEnv(),
  limiter: Ratelimit.slidingWindow(5, '1 m'),
});
```

3. Add environment variables to Vercel:
   - `UPSTASH_REDIS_REST_URL`
   - `UPSTASH_REDIS_REST_TOKEN`

---

## Step 3: Check CORS

Ensure CORS is restricted:

**Python:**
```python
origins = [
    "http://localhost:3000",
    "https://your-site.vercel.app",
    # DO NOT use "*" in production!
]
```

**Next.js:** CORS is usually OK by default on the same domain.

---

## Step 4: Check .gitignore

Ensure the following are in .gitignore:
- [ ] `.env`
- [ ] `.env.local`
- [ ] `.env.*`

---

## Step 5: Deployment

Ensure environment variables are set:

**Render (Python):**
- `GEMINI_API_KEY` or `OPENAI_API_KEY`

**Vercel (Next.js):**
- API key (NOT with `NEXT_PUBLIC_` prefix!)
- If using Upstash: `UPSTASH_REDIS_REST_URL`, `UPSTASH_REDIS_REST_TOKEN`

---

## Final Checklist

- [ ] Rate limiting added (5/min + 50/day)
- [ ] CORS restricted to known domains
- [ ] .env files in .gitignore
- [ ] API keys in environment variables (not in code)
- [ ] Tested locally

---

## Additional Information

See full documentation:
`documents/api-security-guide.md`
