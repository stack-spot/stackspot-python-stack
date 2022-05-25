from fastapi.testclient import TestClient

from src.user.controller import app

client = TestClient(app)


def test_post_user():
    response = client.post(
        "/user/",
        json={"id_": 1, "name": "John Doe", "age": 33})
    assert response.status_code == 200
    assert response.json() == {
        "id_": 1,
        "name": "John Doe",
        "age": 33
    }


def test_post_user_error_invalid_age():
    response = client.post(
        "/user/",
        json={"id_": 1, "name": "John Doe", "age": 150})
    assert response.status_code == 422
    assert response.json() == {'detail': [{'ctx': {'limit_value': 130},
                                           'loc': ['body', 'age'],
                                           'msg': 'ensure this value is less than 130',
                                           'type': 'value_error.number.not_lt'}]}


def test_delete_user():
    response = client.delete("/user/1")
    assert response.status_code == 200
    assert response.json() == "User 1 deleted!"


def test_delete_user_error_not_found():
    response = client.delete("/user/3")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "User not found"
    }
