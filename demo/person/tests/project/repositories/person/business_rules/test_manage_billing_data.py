import pytest
from bson.objectid import ObjectId
from project.repositories.person.business_rules.manage_billing_data import ManageBillingData
from project.repositories.person.models.billing_data import BillingData

manage_billing_data = ManageBillingData()

_person_id = str(ObjectId())

base_data = {
    "status": "active",
    "person_id": _person_id,
    "payment_method_codes": [
        str(ObjectId()),
    ]
}


legal_person = BillingData(**base_data)

output_data = {}


@pytest.mark.asyncio
async def test_save_legal_person():
    save_result = await manage_billing_data.save_billing_data(legal_person)
    assert save_result.id
    output_data["id"] = str(save_result.id)


def test_compose_response():
    data = base_data.copy()
    data["_id"] = output_data["id"]
    save_result = manage_billing_data.compose_response_billing_data(data)
    assert save_result.id


def test_compose_response_whithout_id():
    data = base_data.copy()
    save_result = manage_billing_data.compose_response_billing_data(data)
    assert save_result


@pytest.mark.asyncio
async def test_save_legal_person_has_exist():
    with pytest.raises(Exception):
        same_legal_person = BillingData(**base_data)
        await manage_billing_data.save_billing_data(same_legal_person)


@pytest.mark.asyncio
async def test_update_legal_person():
    await manage_billing_data.update_billing_data(output_data["id"], {"status": "active"})


@pytest.mark.asyncio
async def test_update_legal_person_type_error():
    with pytest.raises(TypeError):
        await manage_billing_data.update_billing_data("0", {"person_id": ""})


@pytest.mark.asyncio
@pytest.mark.asyncio
async def test_get_by_id_legal_person():
    get_result = await manage_billing_data.get_billing_data_by_id(output_data["id"])
    assert output_data["id"] == str(get_result.id)


@pytest.mark.asyncio
async def test_get_by_id_legal_person_type_error():
    with pytest.raises(Exception):
        await manage_billing_data.get_billing_data_by_id("0")


@pytest.mark.asyncio
@pytest.mark.asyncio
async def test_get_by_query_legal_person():
    get_result = await manage_billing_data.get_billing_data_by_query({"person_id": base_data["person_id"]})
    assert len(get_result) == 1


@pytest.mark.asyncio
async def test_get_by_query_legal_person_type_error():
    get_result = await manage_billing_data.get_billing_data_by_query({"color": (1, 2, 3)})
    assert len(get_result) == 0


@pytest.mark.asyncio
@pytest.mark.asyncio
async def test_delete_legal_person():
    delete_result = await manage_billing_data.delete_billing_data(output_data["id"])
    assert delete_result


@pytest.mark.asyncio
@pytest.mark.asyncio
async def test_delete_legal_person_error():
    with pytest.raises(TypeError):
        await manage_billing_data.delete_billing_data("0")
