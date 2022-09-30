from project.infrastructure.data_layer.data_access_adapter import MongoDataLayer
import pytest
from bson.objectid import ObjectId
from project.domain.person.business_rules.manage_address import ManageAddress
from project.domain.person.repository.address import Address

manage_address = ManageAddress()

_person_id = str(ObjectId())

base_data = {
    "status": "active",
    "person_id": _person_id,
    "country": "str",
    "state": "str",
    "city": "str",
    "street": "str",
    "district": "str",
    "zip_code": "str",
    "number": "str",
    "type": "billing"
}


address = Address(**base_data)

output_data = {}


@pytest.mark.asyncio
async def test_save_address():
    save_result = await manage_address.save_address(address)
    if not save_result.id:
        raise AssertionError
    output_data["id"] = str(save_result.id)


def test_compose_response():
    data = base_data.copy()
    data["_id"] = output_data["id"]
    save_result = manage_address.compose_response_address(data)
    if not save_result.id:
        raise AssertionError


def test_compose_response_whithout_id():
    data = base_data.copy()
    save_result = manage_address.compose_response_address(data)
    if not save_result:
        raise AssertionError


@pytest.mark.asyncio
async def test_save_address_has_exist():
    with pytest.raises(Exception):
        same_address = Address(**base_data)
        await manage_address.save_address(same_address)


@pytest.mark.asyncio
async def test_update_address():
    await manage_address.update_address(output_data["id"], {"status": "active"})


@pytest.mark.asyncio
async def test_update_address_type_error():
    with pytest.raises(Exception):
        await manage_address.update_address("0", {"person_id": ""})


@pytest.mark.asyncio
@pytest.mark.asyncio
async def test_get_by_id_address():
    get_result = await manage_address.get_address_by_id(output_data["id"])
    if output_data["id"] != str(get_result.id):
        raise AssertionError


@pytest.mark.asyncio
async def test_get_by_id_address_type_error():
    with pytest.raises(Exception):
        await manage_address.get_address_by_id("0")


@pytest.mark.asyncio
@pytest.mark.asyncio
async def test_get_by_query_address():
    get_result = await manage_address.get_address_by_query({"person_id": base_data["person_id"]})
    if len(get_result) != 1:
        raise AssertionError


@pytest.mark.asyncio
async def test_get_by_query_address_type_error():
    get_result = await manage_address.get_address_by_query({"color": (1, 2, 3)})
    if len(get_result) != 0:
        raise AssertionError


@pytest.mark.asyncio
@pytest.mark.asyncio
async def test_get_by_query_address_error():
    with pytest.raises(Exception):
        manage_address_error = ManageAddress()
        manage_address_error.dao = MongoDataLayer("")
        await manage_address_error.get_address_by_query({"color": (1, 2, 3)})


@pytest.mark.asyncio
@pytest.mark.asyncio
async def test_delete_address():
    delete_result = await manage_address.delete_address(output_data["id"])
    if not delete_result:
        raise AssertionError


@pytest.mark.asyncio
@pytest.mark.asyncio
async def test_delete_address_error():
    with pytest.raises(Exception):
        await manage_address.delete_address("0")
