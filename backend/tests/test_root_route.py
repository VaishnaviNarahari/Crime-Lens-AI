from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root_route_returns_successful_html_response():
    response = client.get("/")

    assert response.status_code == 200
    assert response.text
