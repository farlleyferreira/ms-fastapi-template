from bson.objectid import ObjectId
import pytest
from project.infrastructure.constants.mongo_collections import Collections
from project.domain.person.repository.address import Address
from project.infrastructure.data_layer.data_layer_general import DataLayer
from project.domain.person.valitations.address import ValidateAdress


data_layer = DataLayer(Collections.person_address)

base_data = {
    "_id": ObjectId(),
    "status": "active",
    "person_id": str(ObjectId()),
    "country": "Latvéria",
    "state": "Doomstadt",
    "city": "Doomstadt",
    "street": "42 avenue",
    "district": "Norseheim",
    "zip_code": "42B",
    "number": "42424242",
    "type": "billing"
}


async def create_mongo_object(input_data=base_data):
    adress = Address(**input_data)
    result = await data_layer.save(adress.dict(exclude_unset=True))
    return result


async def delete_mongo_object(_id: ObjectId):
    result = await data_layer.delete({"_id": _id})
    return result


@pytest.mark.asyncio
async def test_this_address_has_exist():

    address = await create_mongo_object()

    result = await ValidateAdress.this_address_has_exist(address)

    if result:
        await delete_mongo_object(address["_id"])

    assert result


@pytest.mark.asyncio
async def test_this_address_has_not_exist():

    result = await ValidateAdress.this_address_has_exist({"country": "abacaxiazul"})

    assert not result


@pytest.mark.asyncio
async def test_this_address_is_active():

    address = await create_mongo_object()

    result = await ValidateAdress.this_address_is_active(address["_id"])
    if result:
        await delete_mongo_object(address["_id"])

    assert result


@pytest.mark.asyncio
async def test_this_address_is_inactive():

    base_data = {
        "status": "inactive",
        "person_id": str(ObjectId()),
        "country": "str",
        "state": "str",
        "city": "str",
        "street": "str",
        "district": "str",
        "zip_code": "str",
        "number": "str",
        "type": "billing"
    }

    address = await create_mongo_object(base_data)

    result = await ValidateAdress.this_address_is_active(address["_id"])

    if result:
        await delete_mongo_object(address["_id"])

    assert not result
