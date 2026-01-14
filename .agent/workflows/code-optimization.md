---
description: Optimize codebase for minimalism, readability, and Pythonic elegance.
---

1. **Analyze for Bloat**
   - Identify redundant functions, unused imports, or duplicate logic (e.g., separate tools doing the same thing).
   - Look for "boilerplate" that can be simplified with modern Python patterns or built-in functions.

2. **Enforce Modularity**
   - Ensure specific logic is isolated in its own domain (e.g., agents in `backend/app/agents/`, core logic in `backend/app/core/`).
   - If a file exceeds ~150 lines, evaluate splitting it into smaller, focused modules.

3. **Pythonic Refinement**
   - Use list comprehensions, `asyncio.gather` for parallel flows, and type hinting.
   - Favor "Explicit over Implicit" but keep instructions and code blocks short.

4. **Minimalist UX/UI Check**
   - On the frontend: Ensure variables are named clearly and components are stateless where possible.
   - On the backend: Keep API endpoints simple (e.g., `run_flow` -> `result`).

5. **Readability Audit**
   - Simplify complex nested `if/else` blocks into guard clauses.
   - Remove "noise" comments that explain *what* the code does (let the clean code explain itself); use comments only for *why* if non-obvious.

6. **Implementation**
   - Make the smallest possible changes that deliver the maximum improvement.
   - Always verify that functionality remains 100% intact after optimization.
