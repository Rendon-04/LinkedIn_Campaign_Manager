# app/crud.py
from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_all_users(db: Session):
    return db.query(models.User).all()


def create_job(db: Session, job: schemas.JobCreate):
    db_job = models.Job(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def get_jobs(db: Session):
    return db.query(models.Job).all()

def get_job(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()

def log_action(db: Session, action: schemas.ActionCreate):
    db_action = models.Action(**action.dict())
    db.add(db_action)
    db.commit()
    db.refresh(db_action)
    return db_action

def get_user_actions(db: Session, user_id: int):
    return db.query(models.Action).filter(models.Action.user_id == user_id).order_by(models.Action.timestamp.desc()).all()

def create_outcome(db: Session, outcome: schemas.OutcomeCreate):
    db_outcome = models.Outcome(**outcome.dict())
    db.add(db_outcome)
    db.commit()
    db.refresh(db_outcome)
    return db_outcome

def get_user_outcomes(db: Session, user_id: int):
    return db.query(models.Outcome).filter(models.Outcome.user_id == user_id).order_by(models.Outcome.timestamp.desc()).all()

def delete_action(db: Session, action_id: int):
    action = db.query(models.Action).filter(models.Action.id == action_id).first()
    if action:
        db.delete(action)
        db.commit()
    return action

def update_action(db: Session, action_id: int, new_action: str):
    action = db.query(models.Action).filter(models.Action.id == action_id).first()
    if action:
        action.action = new_action
        db.commit()
        db.refresh(action)
    return action
