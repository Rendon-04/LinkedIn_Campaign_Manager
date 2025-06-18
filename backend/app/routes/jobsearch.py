# app/routes/jobsearch.py
from fastapi import APIRouter
from typing import List
from app.data.mock_data import mock_jobs, mock_user
from app.schemas import Job, User

jobsearch_router = APIRouter()

@jobsearch_router.get("/jobs", response_model=List[Job])
def get_jobs():
    return mock_jobs

@jobsearch_router.get("/user", response_model=User)
def get_user():
    return mock_user
