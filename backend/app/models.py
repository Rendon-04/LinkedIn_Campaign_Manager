from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, ARRAY
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    job_goal = Column(String)
    industry = Column(String)
    skills = Column(ARRAY(String))

    actions = relationship("Action", back_populates="user")
    outcomes = relationship("Outcome", back_populates="user")


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    company = Column(String)
    description = Column(Text)
    location = Column(String)

    outcomes = relationship("Outcome", back_populates="job")


class Action(Base):
    __tablename__ = "actions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    action = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="actions")


class Outcome(Base):
    __tablename__ = "job_outcomes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))
    outcome = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="outcomes")
    job = relationship("Job", back_populates="outcomes")
