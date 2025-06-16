from fastapi import APIRouter
from app.schemas import MessageRequest
from app.services.ai_agent import generate_message

router = APIRouter()

@router.post("/generate_message")
def get_message(payload: MessageRequest):
    message =  generate_message(payload)
    return {"message": message}

