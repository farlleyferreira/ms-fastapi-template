from bson.objectid import ObjectId
import pytest
from project.infrastructure.constants.mongo_collections import Collections
from project.repositories.person.models.legal_person import LegalPerson
from project.infrastructure.data_layer.data_layer_general import DataLayer
from project.repositories.person.valitations.legal_person import ValidateLegalPerson


data_layer = DataLayer(Collections.legal_person)

base_data = {
    "_id": ObjectId(),
    "status": "active",
    "business_name": "teste",
    "fantasy_name": "teste dos testes",
    "sponsor_business_document_id": "11122233344",
    "business_document_id": "55566677000111",
    "email": "teste@teste.com",
    "phone": "+5534988887777",
}


async def create_mongo_object(input_data=base_data):
    legal_person = LegalPerson(**input_data)
    result = await data_layer.save(legal_person.dict(exclude_unset=True))
    return result


async def delete_mongo_object(_id: ObjectId):
    result = await data_layer.delete({"_id": _id})
    return result


@pytest.mark.asyncio
async def test_this_legal_person_has_exist():

    legal_person = await create_mongo_object()

    result = await ValidateLegalPerson.this_legal_person_has_exist(legal_person)

    if result:
        await delete_mongo_object(legal_person["_id"])

    assert result


@pytest.mark.asyncio
async def test_this_legal_person_has_not_exist():

    result = await ValidateLegalPerson.this_legal_person_has_exist({"name": "abacaxiazul"})

    assert not result


@pytest.mark.asyncio
async def test_this_legal_person_is_active():

    legal_person = await create_mongo_object()

    result = await ValidateLegalPerson.this_legal_person_is_active(legal_person["_id"])
    if result:
        await delete_mongo_object(legal_person["_id"])

    assert result


@pytest.mark.asyncio
async def test_this_legal_person_is_inactive():

    base_data = {
        "_id": ObjectId(),
        "status": "inactive",
        "business_name": "teste",
        "fantasy_name": "teste dos testes",
        "sponsor_business_document_id": "11122233344",
        "business_document_id": "55566677000111",
        "email": "teste@teste.com",
        "phone": "+5534988887777",
    }

    legal_person = await create_mongo_object(base_data)

    result = await ValidateLegalPerson.this_legal_person_is_active(legal_person["_id"])

    if result:
        await delete_mongo_object(legal_person["_id"])

    assert not result


@pytest.mark.asyncio
async def test_this_email_exist_in_store():

    legal_person = await create_mongo_object()

    result = await ValidateLegalPerson.this_email_exist_in_store(base_data["email"])
    if result:
        await delete_mongo_object(legal_person["_id"])

    assert result


@pytest.mark.asyncio
async def test_this_email_not_exist_in_store():

    legal_person = await create_mongo_object()

    result = await ValidateLegalPerson.this_email_exist_in_store("a@a.com")
    if result:
        await delete_mongo_object(legal_person["_id"])

    assert not result


@pytest.mark.asyncio
async def test_this_document_id_exist_in_store():

    legal_person = await create_mongo_object()

    result = await ValidateLegalPerson.this_document_id_exist_in_store(base_data["business_document_id"])
    if result:
        await delete_mongo_object(legal_person["_id"])

    assert result


@pytest.mark.asyncio
async def test_this_document_id_not_exist_in_store():

    legal_person = await create_mongo_object()

    result = await ValidateLegalPerson.this_document_id_exist_in_store("05237147000114")
    if result:
        await delete_mongo_object(legal_person["_id"])

    assert not result
