import pytest
from fastapi import status
from async_asgi_testclient import TestClient


@pytest.mark.asyncio
async def test_signin(client: TestClient):
    response = await client.post(
        "/auth/tokens", json={"email": "johndoe@example.com", "password": "password123"}
    )
    response_json = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert list(response_json.keys()) == ["access_token", "refresh_token"]


@pytest.mark.asyncio
async def test_signin_wrong_credentials(client: TestClient):
    response = await client.post(
        "/auth/tokens",
        json={"email": "johndoe@example.com", "password": "wrong-password"},
    )
    response_json = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert list(response_json.keys()) == ["access_token", "refresh_token"]
