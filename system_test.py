# Import TestClient
from fastapi.testclient import TestClient
from main import app

# Create test client with application context
client = TestClient(app)

def test_main():
    response = client.get("/items?name=rock")
    assert response.status_code == 200
    assert response.json() == {"name": "rock",
                               "quantity": 100}