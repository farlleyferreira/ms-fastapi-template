import pytest
from datetime import datetime
from http import HTTPStatus as status
from httpx import AsyncClient
from tests.configurations.constants import API_URL

from project.routers import app

resource = "/person/physical/"
_birthdate = str(datetime.strptime("1985-08-01", "%Y-%m-%d"))

base_data = {
    "status": "active",
    "name": "Carlos",
    "last_name": "Da Silva Neto",
    "birthdate": _birthdate,
    "gender": "homem cisgênero",
    "personal_document_id": "55777933311",
    "email": "carlin.neto@teste.com",
    "phone": "+5534988887777",
}

_output_data = {}


@pytest.mark.asyncio
async def test_save_physical_person_200():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.post(resource, json=base_data)
        if response.status_code != status.OK:
            raise AssertionError
        _output_data["id"] = response.json()["id"]


@pytest.mark.asyncio
async def test_save_physical_person_400():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.post(resource, json=base_data)
        if response.status_code != status.BAD_REQUEST:
            raise AssertionError


@pytest.mark.asyncio
async def test_save_physical_person_422():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.post(resource, json={})
        if response.status_code != status.UNPROCESSABLE_ENTITY:
            raise AssertionError


@pytest.mark.asyncio
async def test_update_physical_person_200():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        _id = _output_data["id"]
        response = await client.put(f"{resource}{_id}", json={"email": "carlos.neto@teste.com"})
        if response.status_code != status.OK:
            raise AssertionError


@pytest.mark.asyncio
async def test_update_physical_person_500():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.put(f"{resource}{_birthdate}", json={"email": "carlos.neto@teste.com"})
        if response.status_code != status.INTERNAL_SERVER_ERROR:
            raise AssertionError


@pytest.mark.asyncio
async def test_get_physical_person_by_id_200():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        _id = _output_data["id"]
        response = await client.get(f"{resource}by/id/{_id}")
        if response.status_code != status.OK:
            raise AssertionError


@pytest.mark.asyncio
async def test_get_physical_person_by_id_500():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.get(f"{resource}by/id/{_birthdate}")
        if response.status_code != status.INTERNAL_SERVER_ERROR:
            raise AssertionError


@pytest.mark.asyncio
async def test_get_physical_person_qs_200():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.get(f"{resource}by/qs", params={})
        if response.status_code != status.OK:
            raise AssertionError


@pytest.mark.asyncio
async def test_get_physical_person_qs_204():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.get(f"{resource}by/qs", params={"name": "tony sterco"})
        if response.status_code != status.NO_CONTENT:
            raise AssertionError


@pytest.mark.asyncio
async def test_get_physical_person_qs_404():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.get(f"{resource}by/qs", params={"initial_date": -True})
        if response.status_code != status.INTERNAL_SERVER_ERROR:
            raise AssertionError


@pytest.mark.asyncio
async def test_delete_physical_person_200():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        _id = _output_data["id"]
        response = await client.delete(f"{resource}by/{_id}")
        if response.status_code != status.OK:
            raise AssertionError


@pytest.mark.asyncio
async def test_delete_physical_person_500():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.delete(f"{resource}by/{_birthdate}")
        if response.status_code != status.INTERNAL_SERVER_ERROR:
            raise AssertionError
