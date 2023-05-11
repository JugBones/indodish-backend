import pytest
from fastapi import status

from src.auth.constants import ErrorCode
from async_asgi_testclient import TestClient


@pytest.mark.asyncio
async def test_register(client: TestClient) -> None:
    response = await client.post(
        "/auth/register",
        json={
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@example.com",
            "password": "password123",
            "password_confirmation": "password123",
        },
    )

    response_json = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert response_json == {"email": "johndoe@example.com"}


@pytest.mark.asyncio
async def test_register_email_taken(
    client: TestClient, monkeypatch: pytest.MonkeyPatch
) -> None:
    from src.auth import services

    async def fake_getter(*args, **kwargs):
        return True

    monkeypatch.setattr(services, "get_user_by_email", fake_getter)

    response = await client.post(
        "/auth/register",
        json={
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@example.com",
            "password": "password123",
            "password_confirmation": "password123",
        },
    )

    response_json = response.json()

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response_json["detail"] == ErrorCode.EMAIL_TAKEN
