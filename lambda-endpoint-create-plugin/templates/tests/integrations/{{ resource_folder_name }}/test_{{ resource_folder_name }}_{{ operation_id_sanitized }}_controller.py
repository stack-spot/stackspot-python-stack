from fastapi.testclient import TestClient
from fastapi import status
from src.{{ resource_folder_name }}.{{ operation_id_sanitized }}.controller import app


client = TestClient(app)


def test_{{ method_sanitized }}_{{ resource_folder_name }}_{{ operation_id_sanitized }}():
    {% if method in ['POST', 'PUT'] %}
    response = client.{{ method_sanitized }}(
        "{{ uri_sanitized_for_test }}",
        json={"id_": 1})
    {% else %}
    response = client.{{ method_sanitized }}("{{ uri_sanitized_for_test }}")
    {% endif %}

    {% if method == 'POST' %}
    assert response.status_code == status.HTTP_201_CREATED
    {% else %}
    assert response.status_code == status.HTTP_200_OK
    {% endif %}

    {% if should_response_as_list %}
    assert response.json() == [
        {
            "id_": 1,
        },
        {
            "id_": 100,
        }
    ]
    {% else %}
    assert response.json() == {
        "id_": 20
    }
    {% endif %}
