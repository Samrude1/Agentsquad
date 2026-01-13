---
description: Clean up git history and branches
---

# Git Cleanup Workflow

## Step 1: Check Current State

// turbo
```bash
git status
git branch -a
git log --oneline -20
```

**Report:**
- Current branch
- Number of local branches
- Number of remote branches
- Recent commits

---

## Step 2: Remove Merged Branches

// turbo
List merged branches:
```bash
git branch --merged main
```

Delete merged local branches:
```bash
git branch -d branch-name
```

---

## Step 3: Remove Stale Remote Branches

// turbo
Prune remote references:
```bash
git remote prune origin
```

---

## Step 4: Clean Untracked Files (Careful!)

Preview what would be deleted:
```bash
git clean -n
```

Remove untracked files (if confirmed):
```bash
git clean -fd
```

⚠️ **Only run if user confirms!**

---

## Step 5: Squash Commits (Before PR)

If there are many small commits to squash:

```bash
git rebase -i HEAD~N  # N = number of commits to squash
```

In the editor:
- Keep first commit as `pick`
- Change others to `squash` or `s`
- Save and edit the combined message

---

## Step 6: Fix Last Commit Message

// turbo
```bash
git commit --amend -m "New commit message"
```

---

## Step 7: Update .gitignore

Ensure these are ignored:
```
# Dependencies
node_modules/
venv/
.venv/

# Environment
.env
.env.local
.env.*

# Build outputs
.next/
dist/
build/
__pycache__/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```

---

## Step 8: Remove Files from Git History (Nuclear Option)

If a secret was accidentally committed:
```bash
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch PATH/TO/FILE" \
  --prune-empty --tag-name-filter cat -- --all
```

⚠️ **This rewrites history! Only use if absolutely necessary.**

---

## Step 9: Push Cleaned State

// turbo
```bash
git push origin main --force-with-lease
```

⚠️ Force push only if you've rewritten history!

---

## Git Cleanup Checklist

- [ ] Merged branches deleted
- [ ] Remote pruned
- [ ] Commits squashed (if needed)
- [ ] .gitignore is complete
- [ ] No secrets in history
- [ ] Clean working directory
