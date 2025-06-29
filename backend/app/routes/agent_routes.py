from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List

from app.database import get_db
from app.schemas import (
    MessageRequest,
    ActionCreate,
    OutcomeCreate,
    Action,
    Outcome,
)
from app.services.ai_agent import generate_message as generate_ai_message
from app import crud

agent_router = APIRouter()

# Agent and planner
class SimplePlanner:
    def generate_plan(self, user_actions):
        if not user_actions:
            return {"steps": ["Start applying to jobs", "Update your resume"]}

        latest_action = user_actions[0].action.lower()

        if "follow-up" in latest_action:
            return {"steps": ["Schedule an informational interview", "Apply to a new job"]}
        elif "applied" in latest_action:
            return {"steps": ["Send follow-up to recruiter", "Research the company"]}
        else:
            return {"steps": ["Refine resume", "Reach out to network"]}

planner = SimplePlanner()

class SimpleAgent:
    def plan(self, actions):
        if not actions:
            return "Start applying to roles in your target field."
        latest = actions[0].action.lower()
        if "apply" in latest:
            return "Send follow-up messages to recruiters."
        if "follow-up" in latest:
            return "Expand job search to 2 more companies."
        return "Polish resume and update LinkedIn."

    def act(self, plan_text):
        return {"type": "next_step", "note": plan_text}

agent = SimpleAgent()

# ==========================
# ROUTES
# ==========================


@agent_router.get("/history/{user_id}", response_model=List[Action])
def get_user_history(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_actions(db, user_id)

@agent_router.get("/strategy/{user_id}")
def get_strategy(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "goals": [
            f"Apply to 5 {user.job_goal} roles",
            f"Follow up with companies in {user.industry}",
            "Attend 1 networking event",
            "Update LinkedIn profile"
        ]
    }

@agent_router.get("/plan/{user_id}")
def get_custom_plan(user_id: int, db: Session = Depends(get_db)):
    actions = crud.get_user_actions(db, user_id)
    return planner.generate_plan(actions)

@agent_router.get("/next_steps/{user_id}")
def get_next_steps(user_id: int, db: Session = Depends(get_db)):
    actions = crud.get_user_actions(db, user_id)
    return planner.generate_plan(actions)

@agent_router.post("/agent_tick")
def agent_tick(user_id: int, db: Session = Depends(get_db)):
    actions = crud.get_user_actions(db, user_id)
    plan = agent.plan(actions)
    action_result = agent.act(plan)
    action = ActionCreate(
        user_id=user_id,
        action=str(action_result),
        timestamp=datetime.utcnow()
    )
    crud.log_action(db, action)
    return {"thought": plan, "action": action_result}

@agent_router.post("/actions", response_model=Action)
def log_action(payload: ActionCreate, db: Session = Depends(get_db)):
    return crud.log_action(db, payload)

@agent_router.post("/follow_up")
def auto_follow_up(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    jobs = crud.get_jobs(db)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not jobs:
        raise HTTPException(status_code=404, detail="No jobs found")

    job = jobs[0]

    lead = MessageRequest(
        recipient_name=f"{job.company} Recruiter",
        job={
            "title": job.title,
            "company": job.company,
            "description": job.description,
            "location": job.location,
        },
        user={
            "name": user.name,
            "job_goal": user.job_goal,
            "industry": user.industry,
            "skills": user.skills,
        },
        tone="friendly"
    )

    # Include action history and the most recent outcome
    user_history = crud.get_user_actions(db, user.id)
    user_outcomes = crud.get_user_outcomes(db, user.id)
    latest_outcome = user_outcomes[0] if user_outcomes else None

    # Pass context to a generate_ai_message
    message = generate_ai_message(lead, history=user_history, outcome=latest_outcome)

    return {"follow_ups": [message]}


@agent_router.post("/generate_message")
def generate_message_route(payload: MessageRequest):
    try:
        message = generate_ai_message(payload)
        return {"message": message}
    except Exception as e:
        return {"error": str(e)}

@agent_router.post("/job_outcome", response_model=Outcome)
def report_job_outcome(payload: OutcomeCreate, db: Session = Depends(get_db)):
    return crud.create_outcome(db, payload)
