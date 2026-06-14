from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Word Embedding Demo API is running."


def test_similar_endpoint_valid_word():
    response = client.get("/similar?word=king")

    assert response.status_code == 200

    data = response.json()

    assert data["word"] == "king"
    assert len(data["similar_words"]) > 0


def test_similar_endpoint_invalid_word():
    response = client.get("/similar?word=qwertyasdfgh")

    assert response.status_code == 404