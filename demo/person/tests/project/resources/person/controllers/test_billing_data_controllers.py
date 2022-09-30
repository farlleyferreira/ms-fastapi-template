import pytest
from bson.objectid import ObjectId
from datetime import datetime
from http import HTTPStatus as status
from httpx import AsyncClient
from tests.configurations.constants import API_URL

from project.routers import app

resource = "/person/billing_data/"

_birthdate = str(datetime.strptime("1985-08-01", "%Y-%m-%d"))
_person_id = str(ObjectId())

base_data = {
    "status": "active",
    "person_id": _person_id,
    "payment_method_codes": [
        str(ObjectId()),
    ]
}

_output_data = {}


@pytest.mark.asyncio
async def test_save_billing_data_200():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.post(resource, json=base_data)
        if response.status_code != status.OK:
            raise AssertionError
        _output_data["id"] = response.json()["id"]


@pytest.mark.asyncio
async def test_save_billing_data_400():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.post(resource, json=base_data)
        if response.status_code != status.BAD_REQUEST:
            raise AssertionError


@pytest.mark.asyncio
async def test_save_billing_data_422():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.post(resource, json={})
        if response.status_code != status.UNPROCESSABLE_ENTITY:
            raise AssertionError


@pytest.mark.asyncio
async def test_update_billing_data_200():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        _id = _output_data["id"]
        response = await client.put(f"{resource}{_id}", json={"status": "inactive"})
        if response.status_code != status.OK:
            raise AssertionError


@pytest.mark.asyncio
async def test_update_billing_data_500():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.put(f"{resource}{_birthdate}", json={"email": "carlos.neto@teste.com"})
        if response.status_code != status.INTERNAL_SERVER_ERROR:
            raise AssertionError


@pytest.mark.asyncio
async def test_get_billing_data_by_id_200():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        _id = _output_data["id"]
        response = await client.get(f"{resource}by/id/{_id}")
        if response.status_code != status.OK:
            raise AssertionError


@pytest.mark.asyncio
async def test_get_billing_data_by_id_500():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.get(f"{resource}by/id/{_birthdate}")
        if response.status_code != status.INTERNAL_SERVER_ERROR:
            raise AssertionError


@pytest.mark.asyncio
async def test_get_billing_data_qs_200():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.get(f"{resource}by/qs", params={})
        if response.status_code != status.OK:
            raise AssertionError


@pytest.mark.asyncio
async def test_get_billing_data_qs_204():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.get(f"{resource}by/qs", params={"status": "tony sterco"})
        if response.status_code != status.NO_CONTENT:
            raise AssertionError


@pytest.mark.asyncio
async def test_delete_billing_data_200():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        _id = _output_data["id"]
        response = await client.delete(f"{resource}by/{_id}")
        if response.status_code != status.OK:
            raise AssertionError


@pytest.mark.asyncio
async def test_delete_billing_data_500():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        response = await client.delete(f"{resource}by/{_birthdate}")
        if response.status_code != status.INTERNAL_SERVER_ERROR:
            raise AssertionError
