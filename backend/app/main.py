from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.routes.jobsearch import jobsearch_router
from app.routes.agent_routes import agent_router
from app.utils.mock_loader import load_mock_data  

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 LinkedIn Agent API starting...")
    load_mock_data()
    yield
    print("🛑 Shutting down API.")

app = FastAPI(
    title="LinkedIn Agent API",
    description="An AI-powered job search assistant inspired by LinkedIn",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(jobsearch_router, prefix="/jobsearch", tags=["Job Search"])
app.include_router(agent_router, prefix="/agent", tags=["AI Agent"])
