from fastapi.testclient import TestClient

from src.book.controller import app

client = TestClient(app)


def test_get_by_id():
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json() == {
        "id_": 1,
        "name": "The War of Art",
        "author": "Sun Tzu",
        "image_url": None
    }


def test_get_by_id_not_found():
    response = client.get("/books/3")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Book not found"
    }
