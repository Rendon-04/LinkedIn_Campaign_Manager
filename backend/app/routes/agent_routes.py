# app/routes/agent_routes.py
from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from typing import List

from app.schemas import MessageRequest
from app.services.ai_agent import generate_message as generate_ai_message


agent_router = APIRouter()

# --- Strategy Route ---
@agent_router.get("/strategy")
def get_strategy():
    return {
        "goals": [
            "Apply to 5 jobs",
            "Follow up with 2 leads",
            "Attend 1 networking event",
            "Update LinkedIn profile"
        ]
    }

# --- Actions Route ---
class ActionRequest(BaseModel):
    user_id: int
    action: str
    timestamp: datetime

@agent_router.post("/actions")
def log_action(payload: ActionRequest):
    return {"status": "success", "message": "Action logged"}

# --- Next Steps Route ---
@agent_router.get("/next_steps")
def get_next_steps():
    return {
        "steps": [
            "Send follow-up message to recruiter",
            "Apply to 2 more jobs in your target industry",
            "Reach out to a connection working at your target company"
        ]
    }

# --- Message Generation Route ---
@agent_router.post("/generate_message")
def generate_message_route(payload: MessageRequest):
    try:
        message = generate_ai_message(payload)
        return {"message": message}
    except Exception as e:
        return {"error": str(e)}
