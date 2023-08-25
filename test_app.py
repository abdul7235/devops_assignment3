import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_hello_message():
    request_data = {
        "name": "Alice",
        "age": 30,
        "location": "RWP"
    }
    response = client.post("/hello_message/", json=request_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Alice"}
