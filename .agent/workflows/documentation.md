---
description: Create comprehensive documentation for a project
---

# Documentation Workflow

## Step 1: Analyze Project

Understand the project:
- [ ] What does this project do?
- [ ] Who is the target audience?
- [ ] What are the main features?
- [ ] What tech stack is used?

---

## Step 2: Create/Update README.md

Structure:
```markdown
# Project Name

Brief description of what this project does.

## Features

- Feature 1
- Feature 2
- Feature 3

## Tech Stack

- Frontend: React/Next.js
- Backend: FastAPI/Node
- AI: OpenAI/Gemini
- Deployment: Vercel/Render

## Getting Started

### Prerequisites
- Node.js 18+ / Python 3.10+
- API keys for [services]

### Installation

1. Clone the repo
2. Install dependencies
3. Set up environment variables
4. Run the project

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `API_KEY` | OpenAI API key | Yes |
| `DATABASE_URL` | Database connection | No |

## Usage

[How to use the main features]

## API Reference

[If applicable, document endpoints]

## Deployment

[How to deploy to production]

## Contributing

[Contribution guidelines]

## License

[License info]
```

---

## Step 3: Document API Endpoints

For each endpoint:
```markdown
### POST /api/chat

Send a message to the AI agent.

**Request Body:**
```json
{
  "message": "string",
  "history": [{"role": "user", "content": "..."}]
}
```

**Response:**
```json
{
  "reply": "string"
}
```

**Errors:**
- 429: Rate limit exceeded
- 500: Server error
```

---

## Step 4: Add Inline Comments

Add comments to complex code:
```python
def calculate_score(items: list[Item]) -> float:
    """
    Calculate the total score for a list of items.
    
    Args:
        items: List of Item objects with 'value' and 'weight' attributes
        
    Returns:
        Weighted average score, or 0 if no items
        
    Example:
        >>> calculate_score([Item(value=10, weight=2)])
        10.0
    """
    # Implementation...
```

---

## Step 5: Create .env.example

```bash
# API Keys (required)
OPENAI_API_KEY=sk-your-key-here
GEMINI_API_KEY=AIza-your-key-here

# Database (optional)
DATABASE_URL=postgresql://user:pass@host:5432/db

# Configuration
NODE_ENV=development
DEBUG=false
```

---

## Step 6: Document Deployment

Create `DEPLOY.md` if complex:
- Step-by-step deployment instructions
- Environment variable setup
- Common issues and solutions
- Rollback procedures

---

## Step 7: Add CHANGELOG (Optional)

```markdown
# Changelog

## [1.0.0] - 2026-01-10

### Added
- Initial release
- AI chat feature
- Rate limiting

### Changed
- Updated to Gemini 2.0

### Fixed
- CORS configuration
```

---

## Documentation Checklist

- [ ] README.md is complete and up-to-date
- [ ] API endpoints documented
- [ ] Environment variables documented
- [ ] Installation steps work
- [ ] Complex code has comments
- [ ] .env.example exists
