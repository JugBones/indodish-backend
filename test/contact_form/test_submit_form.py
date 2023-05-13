import pytest
from fastapi import status
from async_asgi_testclient import TestClient


@pytest.mark.asyncio
async def test_submit_form(client: TestClient):
    response = await client.post(
        "/contact-form",
        json={
            "name": "John Doe",
            "email": "johndoe@example.com",
            "phone_number": "1234-1234-1234",
            "message": """Lorem Ipsum is simply dummy text of the printing and
            typesetting industry. Lorem Ipsum has been the industry's standard dummy
            text ever since the 1500s, when an unknown printer took a galley
            of type and scrambled it to make a type specimen book. It has
            survived not only five centuries, but also the leap into electronic
            typesetting, remaining essentially unchanged. It was popularised in
            the 1960s with the release of Letraset sheets containing Lorem
            Ipsum passages, and more recently with desktop publishing
            software like Aldus PageMaker including versions of Lorem Ipsum.""",
        },
    )

    assert response.status_code == status.HTTP_201_CREATED
