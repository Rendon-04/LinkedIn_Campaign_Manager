from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.jobsearch import jobsearch_router
from app.routes.agent_routes import agent_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(jobsearch_router)
app.include_router(agent_router)
