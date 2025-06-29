import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.main import app
from app.database import get_db, SessionLocal
from app import crud, schemas

client = TestClient(app)


@pytest.fixture(scope="module")
def db():
    """Yields a session and rolls back changes after tests."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.rollback()
        db.close()


@pytest.fixture(scope="module")
def test_user_and_jobs(db: Session):
    # Create user
    user_data = schemas.UserCreate(
        name="Ivan Rendon",
        job_goal="Software Engineer",
        industry="Information Technology",
        skills=["Python", "React", "SQL", "FastAPI"]
    )
    user = crud.create_user(db, user_data)

    # Create jobs
    job1_data = schemas.JobCreate(
        title="Backend Engineer",
        company="TechWave",
        description="Looking for Python backend engineer with FastAPI experience.",
        location="Remote"
    )
    job2_data = schemas.JobCreate(
        title="Full Stack Developer",
        company="LinkedIn",
        description="LinkedIn REACH Apprenticeship",
        location="San Francisco, CA"
    )

    job1 = crud.create_job(db, job1_data)
    job2 = crud.create_job(db, job2_data)

    return user, [job1, job2]
print("Ttest_user_and_jobs passed")


def test_generate_message_route(test_user_and_jobs):
    user, jobs = test_user_and_jobs

    payload = {
        "recipient_name": f"{jobs[0].company} Recruiter",
        "tone": "Friendly",
        "user": {
            "id": user.id,
            "name": user.name,
            "job_goal": user.job_goal,
            "industry": user.industry,
            "skills": user.skills,
        },
        "job": {
            "id": jobs[0].id,
            "title": jobs[0].title,
            "company": jobs[0].company,
            "description": jobs[0].description,
            "location": jobs[0].location,
        }
    }

    response = client.post("/agent/generate_message", json=payload)
    print(response.json())

    assert response.status_code == 200
    assert "message" in response.json()
    assert isinstance(response.json()["message"], str)
    assert len(response.json()["message"]) > 0
print("test_generate_message_route passed")

def test_strategy_route(test_user_and_jobs):
    user, _ = test_user_and_jobs

    response = client.get(f"/agent/strategy/{user.id}")
    assert response.status_code == 200
    data = response.json()
    assert "goals" in data
    assert isinstance(data["goals"], list)
print("test_strategy_route passed")

def test_next_steps_route(test_user_and_jobs):
    user, _ = test_user_and_jobs

    response = client.get(f"/agent/next_steps/{user.id}")
    assert response.status_code == 200
    data = response.json()
    assert "steps" in data
    assert isinstance(data["steps"], list)
print("test_next_steps_route passed")

def test_user_history_empty(test_user_and_jobs):
    user, _ = test_user_and_jobs

    response = client.get(f"/agent/history/{user.id}")
    assert response.status_code == 200
    assert response.json() == []
print("test_user_history_empty passed")

def test_jobsearch_routes(test_user_and_jobs):
    user, jobs = test_user_and_jobs

    # Test /jobs
    response = client.get("/jobsearch/jobs")
    assert response.status_code == 200
    job_list = response.json()
    assert isinstance(job_list, list)
    assert any(j["title"] == jobs[0].title for j in job_list)

    # Test /user/{user_id}
    response = client.get(f"/jobsearch/user/{user.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == user.name
print("test_jobsearch_routes passed")