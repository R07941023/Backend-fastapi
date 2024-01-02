import sys, os
sys.path.append(os.getcwd())
from fastapi.testclient import TestClient
from src.main.python.main import app


client = TestClient(app)

def test_read_user():
    response = client.post("/appTest/users", json={"name": "john_doe"})
    assert response.json() == {'data': {'name': 'john_doe', 'uid': 'admin'}, 'info': 'welcome', 'statusCode': 200}


