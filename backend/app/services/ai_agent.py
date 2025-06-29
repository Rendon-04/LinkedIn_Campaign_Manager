import os
from dotenv import load_dotenv
from openai import OpenAI
from app.schemas import MessageRequest


load_dotenv() 

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in environment")

client = OpenAI(api_key=api_key)

def generate_message(payload: MessageRequest, history=None, outcome=None):
    prompt = f"""
You are a helpful job search assistant helping {payload.user.name}, a {payload.user.job_goal}, connect with {payload.recipient_name} about a job at {payload.job.company}.
    
Job description: {payload.job.description}
User skills: {', '.join(payload.user.skills)}
Tone: {payload.tone}

"""
    if history:
        prompt += f"\nRecent user actions:\n" + "\n".join([f"- {a.action}" for a in history[:3]])

    if outcome:
        prompt += f"\nLast job outcome: {outcome.outcome}"

    prompt += "\n\nGenerate a short 3-4 sentence networking message that sounds natural and actionable."

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
