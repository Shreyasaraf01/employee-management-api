def test_login_success():
    from fastapi.testclient import TestClient
    from app.main import app

    client = TestClient(app)

    response = client.post(
        "/api/auth/login",
        data={"username": "admin", "password": "admin123"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_login_failure():
    from fastapi.testclient import TestClient
    from app.main import app

    client = TestClient(app)

    response = client.post(
        "/api/auth/login",
        data={"username": "wrong", "password": "wrong"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    assert response.status_code == 401
