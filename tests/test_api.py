from pathlib import Path

from fastapi.testclient import TestClient
from app.main import app
from app.tools.doc_generator import create_document

client = TestClient(app)


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_agent_endpoint():
    response = client.post(
        "/agent",
        json={"prompt": "Create a summary report"},
    )
    assert response.status_code == 200
    assert response.json()["status"] == "completed"


def test_document_generation_creates_docx_file():
    output_path = create_document("Sample content", title="Workflow Test")
    assert Path(output_path).exists()
    assert Path(output_path).suffix == ".docx"
