import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analyze_invalid_file():
    files = {"file": ("test.txt", b"test content", "text/plain")}
    response = client.post("/api/v1/documents/analyze", files=files)
    assert response.status_code == 400
    assert "Only PDF files are allowed" in response.json()["detail"]