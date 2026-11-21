def test_register_user_success(client):
    response = client.post(
        "/api/auth/register",
        json={
            "username": "newtestuser",
            "email": "newtest@example.com",
            "password": "Test12345"
        }
    )

    assert response.status_code == 200
    assert response.json()["username"] == "newtestuser"
    assert response.json()["email"] == "newtest@example.com"
    assert "hashed_password" not in response.json()


def test_register_duplicate_email(client):
    user_data = {
        "username": "userone",
        "email": "duplicate@example.com",
        "password": "Test12345"
    }

    first_response = client.post(
        "/api/auth/register",
        json=user_data
    )

    second_response = client.post(
        "/api/auth/register",
        json={
            "username": "usertwo",
            "email": "duplicate@example.com",
            "password": "Test12345"
        }
    )

    assert first_response.status_code == 200
    assert second_response.status_code == 409


def test_register_duplicate_username(client):
    client.post(
        "/api/auth/register",
        json={
            "username": "sameuser",
            "email": "first@example.com",
            "password": "Test12345"
        }
    )

    response = client.post(
        "/api/auth/register",
        json={
            "username": "sameuser",
            "email": "second@example.com",
            "password": "Test12345"
        }
    )

    assert response.status_code == 409


def test_login_success(client):
    client.post(
        "/api/auth/register",
        json={
            "username": "loginuser",
            "email": "login@example.com",
            "password": "Test12345"
        }
    )

    response = client.post(
        "/api/auth/login",
        json={
            "email": "login@example.com",
            "password": "Test12345"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_login_wrong_password(client):
    client.post(
        "/api/auth/register",
        json={
            "username": "wrongpassuser",
            "email": "wrongpass@example.com",
            "password": "Test12345"
        }
    )

    response = client.post(
        "/api/auth/login",
        json={
            "email": "wrongpass@example.com",
            "password": "WrongPassword"
        }
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid email or password"


def test_login_unregistered_email(client):
    response = client.post(
        "/api/auth/login",
        json={
            "email": "unknown@example.com",
            "password": "Test12345"
        }
    )

    assert response.status_code == 401