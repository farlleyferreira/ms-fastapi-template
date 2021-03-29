import pytest
from bson.objectid import ObjectId
from datetime import datetime
from http import HTTPStatus as status
from httpx import AsyncClient
from tests.configurations.constants import API_URL

from project.routers import app

resource = "/person/address/"

_birthdate = str(datetime.strptime("1985-08-01", "%Y-%m-%d"))
_person_id = str(ObjectId())

base_data = {
    "status": "active",
    "person_id": _person_id,
    "country": "Latvéria",
    "state": "Doomstadt",
    "city": "Doomstadt",
    "street": "42 avenue",
    "district": "Norseheim",
    "zip_code": "42424242",
    "number": "42B",
    "type": "billing"
}


_output_data = {}


@pytest.mark.asyncio
async def test_save_address_200():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.post(resource, json=base_data)
        assert response.status_code == status.OK
        _output_data["id"] = response.json()["id"]


@pytest.mark.asyncio
async def test_save_address_400():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.post(resource, json=base_data)
        assert response.status_code == status.BAD_REQUEST


@pytest.mark.asyncio
async def test_save_address_422():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.post(resource, json={})
        assert response.status_code == status.UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
async def test_update_address_200():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        _id = _output_data["id"]
        response = await client.put(f"{resource}{_id}", json={"number": "42B"})
        assert response.status_code == status.OK


@pytest.mark.asyncio
async def test_update_address_500():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.put(f"{resource}{_birthdate}", json={"email": "carlos.neto@teste.com"})
        assert response.status_code == status.INTERNAL_SERVER_ERROR


@pytest.mark.asyncio
async def test_get_address_by_id_200():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        _id = _output_data["id"]
        response = await client.get(f"{resource}by/id/{_id}")
        assert response.status_code == status.OK


@pytest.mark.asyncio
async def test_get_address_by_id_500():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.get(f"{resource}by/id/{_birthdate}")
        assert response.status_code == status.INTERNAL_SERVER_ERROR


@pytest.mark.asyncio
async def test_get_address_qs_200():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.get(f"{resource}by/qs", params={})
        assert response.status_code == status.OK


@pytest.mark.asyncio
async def test_get_address_qs_204():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.get(f"{resource}by/qs", params={"street": "tony sterco"})
        assert response.status_code == status.NO_CONTENT


@pytest.mark.asyncio
async def test_delete_address_200():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        _id = _output_data["id"]
        response = await client.delete(f"{resource}by/{_id}")
        assert response.status_code == status.OK


@pytest.mark.asyncio
async def test_delete_address_500():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.delete(f"{resource}by/{_birthdate}")
        assert response.status_code == status.INTERNAL_SERVER_ERROR
