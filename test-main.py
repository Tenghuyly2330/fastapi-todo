from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "FastApi CI/CD App"
    }