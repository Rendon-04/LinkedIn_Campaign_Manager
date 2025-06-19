from fastapi.testclient import TestClient
from app.main import app
from app.data.mock_data import mock_user, mock_jobs

client = TestClient(app)

def test_generate_message_route():
    payload = {
        "recipient_name": "Alicia Patel",
        "tone": "Professional",
        "user": mock_user,
        "job": mock_jobs[0]
    }

    response = client.post("/generate_message", json=payload)
    print(response.json())

    assert response.status_code == 200
    assert "message" in response.json()
    assert isinstance(response.json()["message"], str)
    assert len(response.json()["message"]) > 0
