from pydantic import BaseModel
from typing import List

class Job(BaseModel):
    title: str
    company: str
    description: str
    location: str

class User(BaseModel):
    name: str
    job_goal: str
    industry: str
    skills: List[str]

class MessageRequest(BaseModel):
    recipient_name: str
    job: Job
    user: User
    tone: str
