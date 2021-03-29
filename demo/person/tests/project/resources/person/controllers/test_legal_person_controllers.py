import pytest
from datetime import datetime
from http import HTTPStatus as status
from httpx import AsyncClient
from tests.configurations.constants import API_URL

from project.routers import app

resource = "/person/legal/"
_birthdate = str(datetime.strptime("1985-08-01", "%Y-%m-%d"))

base_data = {
    "status": "active",
    "business_name": "teste of the corp",
    "fantasy_name": "teste corporate dev",
    "sponsor_business_document_id": "12132334354",
    "business_document_id": "54556576010287",
    "email": "test2corporate4dev@teste.com",
    "phone": "+5534988882222",
}

_output_data = {}


@pytest.mark.asyncio
async def test_save_legal_person_200():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.post(resource, json=base_data)
        assert response.status_code == status.OK
        _output_data["id"] = response.json()["id"]


@pytest.mark.asyncio
async def test_save_legal_person_400():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.post(resource, json=base_data)
        assert response.status_code == status.BAD_REQUEST


@pytest.mark.asyncio
async def test_save_legal_person_422():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.post(resource, json={})
        assert response.status_code == status.UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
async def test_update_legal_person_200():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        _id = _output_data["id"]
        response = await client.put(f"{resource}{_id}", json={"email": "carlos.neto@teste.com"})
        assert response.status_code == status.OK


@pytest.mark.asyncio
async def test_update_legal_person_500():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.put(f"{resource}{_birthdate}", json={"email": "carlos.neto@teste.com"})
        assert response.status_code == status.INTERNAL_SERVER_ERROR


@pytest.mark.asyncio
async def test_get_legal_person_by_id_200():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        _id = _output_data["id"]
        response = await client.get(f"{resource}by/id/{_id}")
        assert response.status_code == status.OK


@pytest.mark.asyncio
async def test_get_legal_person_by_id_500():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.get(f"{resource}by/id/{_birthdate}")
        assert response.status_code == status.INTERNAL_SERVER_ERROR


@pytest.mark.asyncio
async def test_get_legal_person_qs_200():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.get(f"{resource}by/qs", params={})
        assert response.status_code == status.OK


@pytest.mark.asyncio
async def test_get_legal_person_qs_204():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.get(f"{resource}by/qs", params={"business_name": "tony sterco"})
        assert response.status_code == status.NO_CONTENT


@pytest.mark.asyncio
async def test_delete_legal_person_200():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        _id = _output_data["id"]
        response = await client.delete(f"{resource}by/{_id}")
        assert response.status_code == status.OK


@pytest.mark.asyncio
async def test_delete_legal_person_500():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.delete(f"{resource}by/{_birthdate}")
        assert response.status_code == status.INTERNAL_SERVER_ERROR
