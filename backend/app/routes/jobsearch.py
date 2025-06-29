# app/routes/jobsearch.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas import User


from app.database import get_db
from app.schemas import Job
from app import crud

jobsearch_router = APIRouter()

@jobsearch_router.get("/jobs", response_model=List[Job])
def get_jobs(db: Session = Depends(get_db)):
    return crud.get_jobs(db)

@jobsearch_router.get("/user/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user