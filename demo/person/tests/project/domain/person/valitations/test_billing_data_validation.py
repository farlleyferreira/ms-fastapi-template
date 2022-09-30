from bson.objectid import ObjectId
import pytest
from project.infrastructure.constants.mongo_collections import Collections
from project.domain.person.repository.billing_data import BillingData
from project.infrastructure.data_layer.data_access_adapter import MongoDataLayer
from project.domain.person.valitations.billing_data import ValidateBillingData


data_layer = MongoDataLayer(Collections.person_billing_data)

base_data = {
    "_id": ObjectId(),
    "status": "active",
    "person_id": str(ObjectId()),
    "payment_method_codes": [
        str(ObjectId()),
    ]
}


async def create_mongo_object(input_data=base_data):
    billing_data = BillingData(**input_data)
    result = await data_layer.save(billing_data.dict(exclude_unset=True))
    return result


async def delete_mongo_object(_id: ObjectId):
    result = await data_layer.delete({"_id": _id})
    return result


@pytest.mark.asyncio
async def test_this_billing_data_has_exist():

    billing_data = await create_mongo_object()

    result = await ValidateBillingData.this_billing_data_has_exist(billing_data)

    if result:
        await delete_mongo_object(billing_data["_id"])

    if not result:
        raise AssertionError


@pytest.mark.asyncio
async def test_this_billing_data_has_not_exist():

    result = await ValidateBillingData.this_billing_data_has_exist({"name": "abacaxiazul"})

    if result:
        raise AssertionError


@pytest.mark.asyncio
async def test_this_billing_data_is_active():

    billing_data = await create_mongo_object()

    result = await ValidateBillingData.this_billing_data_is_active(billing_data["_id"])
    if result:
        await delete_mongo_object(billing_data["_id"])

    if not result:
        raise AssertionError


@pytest.mark.asyncio
async def test_this_billing_data_is_inactive():

    base_data = {
        "_id": ObjectId(),
        "status": "inactive",
        "person_id": str(ObjectId()),
        "payment_method_codes": [
            str(ObjectId()),
        ]
    }

    billing_data = await create_mongo_object(base_data)

    result = await ValidateBillingData.this_billing_data_is_active(billing_data["_id"])

    if result:
        await delete_mongo_object(billing_data["_id"])

    if result:
        raise AssertionError
