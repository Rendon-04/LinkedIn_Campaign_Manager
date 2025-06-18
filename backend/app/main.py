# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.jobsearch import jobsearch_router
from app.routes.agent_routes import agent_router

app = FastAPI()

# CORS setup for frontend dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all routes
app.include_router(jobsearch_router)
app.include_router(agent_router)
