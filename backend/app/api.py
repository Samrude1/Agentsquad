from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.app.agents.sales.flow import run_sales_flow
from backend.app.agents.research.flow import run_deep_research

app = FastAPI(title="Smart Outreach Manager API")

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request models
class SalesRequest(BaseModel):
    contact_name: str = ""  # Optional if company-only
    company_name: str
    prospect_email: str
    sender_name: str
    product_description: str

class SendRequest(BaseModel):
    to_email: str
    subject: str
    html_body: str

class ResearchRequest(BaseModel):
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
        print(f"DEBUG: api endpoint result = {result}")
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
        return result
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

@app.get("/")
async def root():
    return {"message": "Smart Outreach Manager API", "version": "1.0"}
