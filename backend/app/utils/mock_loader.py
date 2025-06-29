from app.database import SessionLocal
from app.models import User, Job, Action, Outcome
from datetime import datetime, timedelta

def load_mock_data():
    db = SessionLocal()

    # Check if data already exists
    if db.query(User).first():
        print("Mock data already exists. Skipping insert.")
        db.close()
        return

    # Mock user
    user = User(
        id=1,
        name="Ivan Rendon",
        job_goal="Software Engineer",
        industry="Information Technology",
        skills=["Python", "React", "SQL", "FastAPI"]
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    print(f"User inserted with ID: {user.id}")

    # Mock jobs
    job1 = Job(
        id=1,
        title="Backend Engineer",
        company="TechWave",
        description="Looking for a Python backend engineer with FastAPI experience.",
        location="Remote"
    )

    job2 = Job(
        id=2,
        title="Full Stack Developer",
        company="LinkedIn",
        description="LinkedIn REACH Apprenticeship",
        location="San Francisco, CA"
    )

    db.add_all([job1, job2])
    db.commit()
    db.refresh(job1)
    db.refresh(job2)
    print(f"Jobs inserted with IDs: {job1.id}, {job2.id}")

    # Mock actions
    actions = [
        Action(
            user_id=user.id,
            action="Applied to Backend Engineer at TechWave",
            timestamp=datetime.utcnow() - timedelta(days=3)
        ),
        Action(
            user_id=user.id,
            action="Sent follow-up email to TechWave recruiter",
            timestamp=datetime.utcnow() - timedelta(days=2)
        ),
        Action(
            user_id=user.id,
            action="Attended virtual networking event",
            timestamp=datetime.utcnow() - timedelta(days=1)
        )
    ]
    db.add_all(actions)
    db.commit()
    print("✅ Mock actions inserted.")

    # Mock outcomes
    outcomes = [
        Outcome(
            user_id=user.id,
            job_id=job1.id,
            outcome="rejected",
            timestamp=datetime.utcnow() - timedelta(days=1)
        ),
        Outcome(
            user_id=user.id,
            job_id=job2.id,
            outcome="interview_scheduled",
            timestamp=datetime.utcnow()
        )
    ]
    db.add_all(outcomes)
    db.commit()
    print("Mock outcomes inserted.")

    db.close()
    print("Mock data loaded successfully.")
