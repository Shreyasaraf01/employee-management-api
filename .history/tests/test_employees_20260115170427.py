def test_create_employee(auth_headers):
    from fastapi.testclient import TestClient
    from app.main import app

    client = TestClient(app)

    response = client.post(
        "/api/employees/",
        json={
            "name": "John Doe",
            "email": "john.doe@test.com",
            "department": "IT",
            "role": "Engineer",
            "salary": 60000,
        },
        headers=auth_headers,
    )

    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"


def test_get_employees(auth_headers):
    from fastapi.testclient import TestClient
    from app.main import app

    client = TestClient(app)

    response = client.get("/api/employees/", headers=auth_headers)

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_employee_by_id(auth_headers):
    from fastapi.testclient import TestClient
    from app.main import app

    client = TestClient(app)

    response = client.get("/api/employees/1", headers=auth_headers)

    assert response.status_code in [200, 404]


def test_update_employee(auth_headers):
    from fastapi.testclient import TestClient
    from app.main import app

    client = TestClient(app)

    response = client.put(
        "/api/employees/1",
        json={"role": "Senior Engineer"},
        headers=auth_headers,
    )

    assert response.status_code in [200, 404]


def test_delete_employee(auth_headers):
    from fastapi.testclient import TestClient
    from app.main import app

    response = client.delete("/api/employees/1", headers=auth_headers)

    assert response.status_code in [204, 404]
