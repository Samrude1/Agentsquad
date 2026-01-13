---
description: Deploy Next.js frontend to Vercel
---

# Deploy to Vercel Workflow

## Step 1: Verify Project Structure

Check that the project has:
- [ ] `package.json` with correct scripts
- [ ] `next.config.js` or `next.config.ts`
- [ ] `.gitignore` with node_modules and .env excluded

---

## Step 2: Check Environment Variables

List all environment variables the project needs:

**Server-side only (secure):**
- `OPENAI_API_KEY`
- `GEMINI_API_KEY`
- Database URLs, etc.

**Client-side (public):**
- `NEXT_PUBLIC_API_URL` (backend URL)
- Other public config

⚠️ **NEVER put API keys in NEXT_PUBLIC_ variables!**

---

## Step 3: Verify .gitignore

Ensure these are in `.gitignore`:
```
node_modules/
.next/
.env
.env.local
.env*.local
```

---

## Step 4: Test Build Locally

// turbo
```bash
npm run build
```

Fix any build errors before deploying.

---

## Step 5: Push to GitHub

// turbo
1. `git add .`
2. `git commit -m "Prepare for Vercel deployment"`
3. `git push origin main`

---

## Step 6: Vercel Configuration

Provide this information:

**Framework Preset:** Next.js (auto-detected)

**Environment Variables to set in Vercel:**
- List each variable and its purpose
- Mark which are sensitive (API keys)

---

## Step 7: Post-Deployment Checklist

After Vercel deploys, verify:
- [ ] Site loads correctly
- [ ] API routes work (if any)
- [ ] Environment variables are set
- [ ] No console errors

---

## Common Issues

| Issue | Solution |
|-------|----------|
| Build fails | Check `npm run build` locally |
| API route 500 | Check Vercel function logs |
| Env var undefined | Verify set in Vercel dashboard |
| CORS error | Check API allows Vercel domain |
