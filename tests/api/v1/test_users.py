from fastapi.testclient import TestClient
from app.core import settings

def test_create_user(client: TestClient) -> None:
    data = {"email": "test@example.com", "password": "password", "full_name": "Test User"}
    response = client.post(
        f"{settings.API_V1_STR}/users/", json=data,
    )
    assert response.status_code == 201
    content = response.json()
    assert content["email"] == data["email"]
    assert content["full_name"] == data["full_name"]
    assert "id" in content

def test_read_user_by_id(client: TestClient) -> None:
    # First create a user
    data = {"email": "test2@example.com", "password": "password", "full_name": "Test User 2"}
    response = client.post(
        f"{settings.API_V1_STR}/users/", json=data,
    )
    user_id = response.json()["id"]

    # Now read it
    response = client.get(
        f"{settings.API_V1_STR}/users/{user_id}",
    )
    assert response.status_code == 200
    content = response.json()
    assert content["email"] == data["email"]
    assert content["id"] == user_id

def test_read_users(client: TestClient) -> None:
    response = client.get(
        f"{settings.API_V1_STR}/users/",
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_user(client: TestClient) -> None:
    # Create user
    data = {"email": "test3@example.com", "password": "password", "full_name": "Original Name"}
    response = client.post(
        f"{settings.API_V1_STR}/users/", json=data,
    )
    user_id = response.json()["id"]

    # Update user
    update_data = {"full_name": "Updated Name"}
    response = client.put(
        f"{settings.API_V1_STR}/users/{user_id}", json=update_data,
    )
    assert response.status_code == 200
    assert response.json()["full_name"] == update_data["full_name"]

def test_delete_user(client: TestClient) -> None:
    # Create user
    data = {"email": "test4@example.com", "password": "password", "full_name": "To Be Deleted"}
    response = client.post(
        f"{settings.API_V1_STR}/users/", json=data,
    )
    user_id = response.json()["id"]

    # Delete user
    response = client.delete(
        f"{settings.API_V1_STR}/users/{user_id}",
    )
    assert response.status_code == 200

    # Verify deleted
    response = client.get(
        f"{settings.API_V1_STR}/users/{user_id}",
    )
    assert response.status_code == 404
