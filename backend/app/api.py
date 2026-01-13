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
    prospect_name: str
    prospect_email: str
    sender_name: str
    product_description: str

class ResearchRequest(BaseModel):
    topic: str

# Endpoints
@app.post("/api/sales")
async def sales_endpoint(req: SalesRequest):
    try:
        result = await run_sales_flow(
            req.prospect_name, 
            req.sender_name,
            req.product_description,
            req.prospect_email
        )
        return {"status": "success", "result": str(result)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/research")
async def research_endpoint(req: ResearchRequest):
    try:
        result = await run_deep_research(req.topic)
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Smart Outreach Manager API", "version": "1.0"}
