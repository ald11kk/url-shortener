from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_short_url():
    payload = {"url": "https://www.python.org"}
    response = client.post("/shorten", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert "short_code" in data
    assert "short_url" in data
    assert data["short_url"].endswith(data["short_code"])

def test_redirect_to_original_url():
    original_url = "https://www.google.com/"
    create_res = client.post("/shorten", json={"url": original_url})
    code = create_res.json()["short_code"]
    
    response = client.get(f"/{code}", follow_redirects=False)
    
    assert response.status_code in [301, 307]
    assert response.headers["location"] == original_url

def test_non_existent_code_returns_404():
    response = client.get("/thiscode-does-not-exist")
    assert response.status_code == 404