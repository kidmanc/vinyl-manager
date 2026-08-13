def test_register_user(client):
    resp = client.post(
        "/users/register",
        json={
            "username": "bob",
            "email": "bob@example.com",
            "password": "pass123",
        },
    )
    assert resp.status_code == 201
    data = resp.json()
    assert data["username"] == "bob"
    assert data["email"] == "bob@example.com"
    assert "id" in data


def test_register_duplicate_username(client):
    client.post(
        "/users/register",
        json={
            "username": "bob",
            "email": "bob@example.com",
            "password": "pass123",
        },
    )
    resp = client.post(
        "/users/register",
        json={
            "username": "bob",
            "email": "bob2@example.com",
            "password": "pass456",
        },
    )
    assert resp.status_code == 409
    assert "already taken" in resp.json()["detail"]


def test_login_success(client):
    client.post(
        "/users/register",
        json={
            "username": "bob",
            "email": "bob@example.com",
            "password": "pass123",
        },
    )
    resp = client.post(
        "/users/login",
        json={
            "username": "bob",
            "password": "pass123",
        },
    )
    assert resp.status_code == 200
    data = resp.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_register_validation_error(client):
    resp = client.post(
        "/users/register",
        json={
            "username": "",
            "email": "not-an-email",
            "password": "",
        },
    )
    assert resp.status_code == 422


def test_login_invalid_password(client):
    client.post(
        "/users/register",
        json={
            "username": "bob",
            "email": "bob@example.com",
            "password": "pass123",
        },
    )
    resp = client.post(
        "/users/login",
        json={
            "username": "bob",
            "password": "wrongpassword",
        },
    )
    assert resp.status_code == 401
