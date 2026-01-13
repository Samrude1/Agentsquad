---
description: Systematic approach to debugging errors
---

# Debug Errors Workflow

## Step 1: Understand the Error

Gather information:
- [ ] What is the exact error message?
- [ ] What file and line number?
- [ ] What was the user doing when it happened?
- [ ] Is it reproducible?

**Paste the full error/stack trace.**

---

## Step 2: Check the Logs

Look at relevant logs:
- [ ] Browser console (frontend)
- [ ] Terminal output (backend)
- [ ] Render/Vercel logs (production)
- [ ] Network tab (API calls)

**Report what the logs show.**

---

## Step 3: Reproduce the Issue

Try to reproduce:
- [ ] Same input/action
- [ ] Same environment (dev/prod)
- [ ] Same user state

**Can you reproduce? Yes/No**

---

## Step 4: Isolate the Problem

Narrow down the cause:
- [ ] Comment out code sections
- [ ] Add console.log/print statements
- [ ] Test with simpler inputs
- [ ] Check if issue is in frontend or backend

**Where is the issue? (file/function)**

---

## Step 5: Check Common Causes

**JavaScript/TypeScript:**
- [ ] Undefined/null values
- [ ] Async/await missing
- [ ] Wrong import/export
- [ ] TypeScript type mismatch

**Python:**
- [ ] IndentationError
- [ ] Missing dependencies
- [ ] Wrong variable scope
- [ ] Async not awaited

**API/Network:**
- [ ] Wrong URL
- [ ] CORS issue
- [ ] Missing headers
- [ ] Rate limit exceeded

**Environment:**
- [ ] Missing env variable
- [ ] Wrong env variable value
- [ ] Different behavior dev vs prod

---

## Step 6: Implement Fix

Once cause is found:
1. Write the fix
2. Test locally
3. Verify error is gone
4. Check for side effects

---

## Step 7: Prevent Recurrence

After fixing:
- [ ] Add error handling if missing
- [ ] Add validation if input issue
- [ ] Add logging for future debugging
- [ ] Consider adding a test

---

## Debug Report

**Error:** [description]
**Cause:** [root cause]
**Fix:** [what was changed]
**Prevention:** [how to prevent in future]
