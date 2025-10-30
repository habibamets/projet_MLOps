from main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_predict_ok():
    payload = {
        "sepal_length": 4.3,
        "sepal_width": 3.0,
        "petal_length": 1.3,
        "petal_width": 0.2
    }
    r = client.post("/predict", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert "predicted_class" in data
    assert isinstance(data["predicted_class"], int)
    assert "metadata" in data

def test_health():
    r = client.get("/")
    assert r.status_code == 200
    assert "message" in r.json()
