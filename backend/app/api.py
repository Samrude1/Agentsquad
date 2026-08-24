from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import logging
from typing import Optional
from backend.app.agents.sales.flow import run_sales_flow
from backend.app.agents.research.flow import run_deep_research
from backend.app.agents.meeting_prep.flow import run_meeting_prep
from backend.app.middleware.rate_limiter import rate_limit_middleware

logger = logging.getLogger(__name__)

app = FastAPI(title="Agent Squad API", version="1.2.0")

# Rate limiting middleware (applied first)
app.middleware("http")(rate_limit_middleware)

# Security Headers Middleware
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response

# CORS for frontend - supports both local and production
allowed_origins = [
    "http://localhost:5173",  # Local development
    "http://localhost:4173",  # Local preview
]

# Add production frontend URL if set
if production_url := os.getenv("FRONTEND_URL"):
    allowed_origins.append(production_url)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request models
class SalesRequest(BaseModel):
    contact_name: Optional[str] = ""
    company_name: Optional[str] = ""
    prospect_email: str
    sender_name: str
    product_description: str

class SendRequest(BaseModel):
    to_email: str
    subject: str
    html_body: str

class ResearchRequest(BaseModel):
    topic: str

class MeetingPrepRequest(BaseModel):
    topic: str

# Endpoints
@app.post("/api/sales/draft")
async def sales_endpoint(req: SalesRequest):
    try:
        result = await run_sales_flow(
            req.contact_name,
            req.company_name,
            req.sender_name,
            req.product_description,
            req.prospect_email
        )
        return {"status": "success", "draft": result}
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/sales/send")
async def send_endpoint(req: SendRequest):
    try:
        from backend.app.agents.sales.tools import _send_email_raw
        result = _send_email_raw(req.to_email, req.subject, req.html_body)
        if result.get("status") == "error":
            raise HTTPException(status_code=400, detail=result.get("message"))
        return result
    except HTTPException:
        raise
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/research")
async def research_endpoint(req: ResearchRequest):
    try:
        result = await run_deep_research(req.topic)
        return {"status": "success", "result": result}
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/meeting-prep")
async def meeting_prep_endpoint(req: MeetingPrepRequest):
    try:
        result = await run_meeting_prep(req.topic)
        return {"status": "success", "result": result}
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/config/auth-enabled")
async def is_auth_enabled():
    """Returns false for frictionless public portfolio demo mode."""
    return {"enabled": False}

@app.get("/")
async def root():
    return {"message": "Smart Outreach Manager API", "version": "1.2"}

@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring."""
    return {"status": "healthy", "version": "1.2"}

