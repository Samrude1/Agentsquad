from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from typing import Optional, Annotated
from backend.app.agents.sales.flow import run_sales_flow
from backend.app.agents.research.flow import run_deep_research
from backend.app.agents.meeting_prep.flow import run_meeting_prep
from backend.app.middleware.rate_limiter import rate_limit_middleware

app = FastAPI(title="Agent Squad API", version="1.1.0")

# Rate limiting middleware (applied first)
app.middleware("http")(rate_limit_middleware)

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

# Authentication Dependency
async def verify_pin_header(x_api_pin: Annotated[Optional[str], Header(alias="X-API-PIN")] = None):
    """
    Dependency to verify access. Supports both manual PIN and automatic Recruiter Token.
    """
    user_pin = os.getenv("APP_PIN", "0000")
    recruiter_token = os.getenv("RECRUITER_TOKEN", "portfolio_access")
    
    # Allow access if PIN matches either the user PIN or the recruiter token
    if x_api_pin and (x_api_pin == user_pin or x_api_pin == recruiter_token):
        return x_api_pin
        
    raise HTTPException(
        status_code=401, 
        detail="Unauthorized access. Use the official link or enter a valid PIN."
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

class AuthRequest(BaseModel):
    pin: str

# Endpoints
@app.post("/api/sales/draft", dependencies=[Depends(verify_pin_header)])
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

@app.post("/api/sales/send", dependencies=[Depends(verify_pin_header)])
async def send_endpoint(req: SendRequest):
    try:
        from backend.app.agents.sales.tools import _send_email_raw
        result = _send_email_raw(req.to_email, req.subject, req.html_body)
        if result.get("status") == "error":
            raise HTTPException(status_code=400, detail=result.get("message"))
        return result
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/research", dependencies=[Depends(verify_pin_header)])
async def research_endpoint(req: ResearchRequest):
    try:
        result = await run_deep_research(req.topic)
        return {"status": "success", "result": result}
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/meeting-prep", dependencies=[Depends(verify_pin_header)])
async def meeting_prep_endpoint(req: MeetingPrepRequest):
    try:
        result = await run_meeting_prep(req.topic)
        return {"status": "success", "result": result}
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/auth/verify")
async def verify_pin(req: AuthRequest):
    user_pin = os.getenv("APP_PIN", "0000")
    recruiter_token = os.getenv("RECRUITER_TOKEN", "portfolio_access")
    
    if req.pin == user_pin or req.pin == recruiter_token:
        return {"status": "success", "message": "Authenticated"}
    else:
        raise HTTPException(status_code=401, detail="Invalid PIN")


@app.get("/api/config/auth-enabled")
async def is_auth_enabled():
    # Authentication is now strictly enforced on all data endpoints.
    # We return True to ensure the frontend displays the login page.
    return {"enabled": True}

@app.get("/")
async def root():
    return {"message": "Smart Outreach Manager API", "version": "1.1"}

@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring."""
    return {"status": "healthy", "version": "1.1"}

