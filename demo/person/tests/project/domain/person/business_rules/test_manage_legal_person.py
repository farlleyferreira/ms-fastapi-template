from project.infrastructure.data_layer.data_access_adapter import MongoDataLayer
import pytest
from project.domain.person.business_rules.manage_legal_person import ManageLegalPerson
from project.domain.person.repository.legal_person import LegalPerson

manage_legal_person = ManageLegalPerson()


base_data = {
    "status": "active",
    "business_name": "teste corp",
    "fantasy_name": "teste dos testes corporate",
    "sponsor_business_document_id": "11122233344",
    "business_document_id": "55566677000188",
    "email": "teste.corp@teste.com",
    "phone": "+5534988882222",
}

legal_person = LegalPerson(**base_data)

output_data = {}


@pytest.mark.asyncio
async def test_save_legal_person():
    save_result = await manage_legal_person.save_legal_person(legal_person)
    if not save_result.id:
        raise AssertionError
    output_data["id"] = str(save_result.id)


def test_compose_response():
    data = base_data.copy()
    data["_id"] = output_data["id"]
    save_result = manage_legal_person.compose_response_legal_person(data)
    if not save_result.id:
        raise AssertionError


def test_compose_response_whithout_id():
    data = base_data.copy()
    save_result = manage_legal_person.compose_response_legal_person(data)
    if not save_result:
        raise AssertionError


@pytest.mark.asyncio
async def test_save_legal_person_has_exist():
    with pytest.raises(Exception):
        same_legal_person = LegalPerson(**base_data)
        await manage_legal_person.save_legal_person(same_legal_person)


@pytest.mark.asyncio
async def test_save_legal_person_email_has_exist():
    with pytest.raises(Exception):
        another_base_data = base_data.copy()
        another_base_data["business_name"] = "januario"
        another_base_data["business_document_id"] = "55566377000188"
        another_legal_person = LegalPerson(**another_base_data)
        await manage_legal_person.save_legal_person(another_legal_person)


@pytest.mark.asyncio
async def test_save_legal_person_document_has_exist():
    with pytest.raises(Exception):
        another_base_data = base_data.copy()
        another_base_data["business_name"] = "januario"
        another_base_data["email"] = "antonio.neto@teste.com"
        another_legal_person = LegalPerson(**another_base_data)
        await manage_legal_person.save_legal_person(another_legal_person)


@pytest.mark.asyncio
async def test_update_legal_person():
    await manage_legal_person.update_legal_person(output_data["id"], {"email": "joao.silva@teste.com"})


@pytest.mark.asyncio
async def test_update_legal_person_type_error():
    with pytest.raises(Exception):
        await manage_legal_person.update_legal_person("0", {"email": "joao.silva2@teste.com"})


@pytest.mark.asyncio
@pytest.mark.asyncio
async def test_get_by_id_legal_person():
    get_result = await manage_legal_person.get_legal_person_by_id(output_data["id"])
    if output_data["id"] != str(get_result.id):
        raise AssertionError


@pytest.mark.asyncio
async def test_get_by_id_legal_person_type_error():
    with pytest.raises(Exception):
        await manage_legal_person.get_legal_person_by_id("0")


@pytest.mark.asyncio
@pytest.mark.asyncio
async def test_get_by_query_legal_person():
    get_result = await manage_legal_person.get_legal_person_by_query({"email": "joao.silva@teste.com"})
    if len(get_result) != 1:
        raise AssertionError


@pytest.mark.asyncio
async def test_get_by_query_legal_person_type_error():
    get_result = await manage_legal_person.get_legal_person_by_query({"color": (1, 2, 3)})
    if len(get_result) != 0:
        raise AssertionError


@pytest.mark.asyncio
async def test_get_by_query_legal_person_error():
    with pytest.raises(Exception):
        manage_legal_person_error = ManageLegalPerson()
        manage_legal_person_error.dao = MongoDataLayer("")
        await manage_legal_person_error.get_legal_person_by_query({})


@pytest.mark.asyncio
@pytest.mark.asyncio
async def test_delete_legal_person():
    delete_result = await manage_legal_person.delete_legal_person(output_data["id"])
    if not delete_result:
        raise AssertionError


@pytest.mark.asyncio
@pytest.mark.asyncio
async def test_delete_legal_person_error():
    with pytest.raises(Exception):
        await manage_legal_person.delete_legal_person("0")
