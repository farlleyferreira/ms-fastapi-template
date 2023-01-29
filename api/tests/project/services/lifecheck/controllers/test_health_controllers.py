import pytest
from http import HTTPStatus as status
from httpx import AsyncClient
from tests.configurations.constants import API_URL

from project.routers import app


@pytest.mark.asyncio
async def test_ping():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.get("/health/")
        assert response.status_code == status.OK
        result = response.json()
        assert "api_status" in result
        assert result["api_status"] == "green"
