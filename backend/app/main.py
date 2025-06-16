from fastapi import FastAPI
from app.routes.jobsearch import router as jobsearch_router

app = FastAPI()
app.include_router(jobsearch_router)
