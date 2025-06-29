from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# -------------------------------
# User Schemas
# -------------------------------

class UserBase(BaseModel):
    name: str
    job_goal: Optional[str] = None
    industry: Optional[str] = None
    skills: List[str] = []

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: Optional[int] = None

    model_config = {
        "from_attributes": True
    }

# -------------------------------
# Job Schemas
# -------------------------------

class JobBase(BaseModel):
    title: str
    company: str
    description: str
    location: str

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: Optional[int] = None

    model_config = {
        "from_attributes": True
    }

# -------------------------------
# Action Schemas
# -------------------------------

class ActionBase(BaseModel):
    user_id: int
    action: str
    timestamp: datetime

class ActionCreate(ActionBase):
    pass

class Action(ActionBase):
    id: int

    model_config = {
        "from_attributes": True
    }

# -------------------------------
# Outcome Schemas
# -------------------------------

class OutcomeBase(BaseModel):
    user_id: int
    job_id: int
    outcome: str
    timestamp: datetime

class OutcomeCreate(OutcomeBase):
    pass

class Outcome(OutcomeBase):
    id: int

    model_config = {
        "from_attributes": True
    }

# -------------------------------
# Message Request Schema
# -------------------------------

class MessageRequest(BaseModel):
    recipient_name: str
    job: Job
    user: User
    tone: str

