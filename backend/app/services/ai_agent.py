import os
from dotenv import load_dotenv
from openai import OpenAI
from app.schemas import MessageRequest


load_dotenv() 

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in environment")

client = OpenAI(api_key=api_key)


def generate_message(payload: MessageRequest):
    prompt = f"""
    You are a job search assistant. Help {payload.user.name}, a {payload.user.job_goal}, write a {payload.tone.lower()} networking message to {payload.recipient_name} about the job at {payload.job.company}.

    Job description: {payload.job.description}
    User skills: {', '.join(payload.user.skills)}

    Generate a 3-4 sentence outreach message.
    """

    response = client.chat.completions.create(model="gpt-4",
    messages=[
        {"role": "user", "content": prompt}
    ])

    return response.choices[0].message.content