import uuid
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_employee(auth_headers):
    unique_email = f"john_{uuid.uuid4().hex}@test.com"

    response = client.post(
        "/api/employees/",
        json={
            "name": "John Doe",
            "email": unique_email,
            "department": "IT",
            "role": "Engineer",
            "salary": 60000,
        },
        headers=auth_headers,
    )

    assert response.status_code == 201
    assert response.json()["email"] == unique_email


def test_get_employees(auth_headers):
    response = client.get("/api/employees/", headers=auth_headers)

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_employee_by_id(auth_headers):
    response = client.get("/api/employees/1", headers=auth_headers)

    assert response.status_code in [200, 404]


def test_update_employee(auth_headers):
    response = client.put(
        "/api/employees/1",
        json={"role": "Senior Engineer"},
        headers=auth_headers,
    )

    assert response.status_code in [200, 404]


def test_delete_employee(auth_headers):
    response = client.delete("/api/employees/1", headers=auth_headers)

    assert response.status_code in [204, 404]
