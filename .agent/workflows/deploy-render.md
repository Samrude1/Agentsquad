---
description: Deploy Python FastAPI backend to Render.com
---

# Deploy to Render Workflow

## Step 1: Verify Project Structure

Check that the project has:
- [ ] `requirements.txt` with all dependencies
- [ ] `api.py` or `main.py` as entry point
- [ ] `.gitignore` with `.env` files excluded

---

## Step 2: Verify requirements.txt

// turbo
Ensure these are present (if using FastAPI + AI):
```
fastapi
uvicorn[standard]
pydantic
python-dotenv
openai  # or google-generativeai
requests
slowapi  # for rate limiting
```

---

## Step 3: Create/Update .gitignore

Ensure these are in `.gitignore`:
```
.env
.env.local
.env.*
__pycache__/
*.py[cod]
venv/
.venv/
```

---

## Step 4: Render Configuration

Provide this information for Render setup:

**Build Command:**
```
pip install -r requirements.txt
```

**Start Command:**
```
python -m uvicorn api:app --host 0.0.0.0 --port $PORT
```

**Environment Variables needed:**
- List all env vars from `.env` that need to be set in Render

---

## Step 5: Push to GitHub

// turbo
1. `git add .`
2. `git commit -m "Prepare for Render deployment"`
3. `git push origin main`

---

## Step 6: Post-Deployment Checklist

After Render deploys, verify:
- [ ] Health endpoint returns OK (`GET /`)
- [ ] API endpoints work
- [ ] Environment variables are set
- [ ] Logs show no errors

---

## Common Issues

| Issue | Solution |
|-------|----------|
| `uvicorn: command not found` | Use `python -m uvicorn` in start command |
| `ModuleNotFoundError` | Check requirements.txt has all deps |
| `500 Internal Server Error` | Check Render logs for details |
| `CORS error` | Add frontend domain to origins list |
