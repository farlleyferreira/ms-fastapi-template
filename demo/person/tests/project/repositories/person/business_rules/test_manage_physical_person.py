import pytest
from datetime import datetime
from project.domain.person.business_rules.manage_physical_person import ManagePhysicalPerson
from project.domain.person.repository.physical_person import PhysicalPerson

manage_physical_person = ManagePhysicalPerson()


base_data = {
    "status": "active",
    "name": "Anestesio",
    "last_name": "Da Silva Neto",
    "birthdate": datetime.strptime("1985-08-01", "%Y-%m-%d"),
    "gender": "",
    "personal_document_id": "66399855071",
    "email": "joao4neto@teste.com",
    "phone": "+5534288887777",
}

physical_person = PhysicalPerson(**base_data)

output_data = {}


@pytest.mark.asyncio
async def test_save_physical_person():
    save_result = await manage_physical_person.save_physical_person(physical_person)
    assert save_result.id
    output_data["id"] = str(save_result.id)


def test_compose_response():
    data = base_data.copy()
    data["_id"] = output_data["id"]
    save_result = ManagePhysicalPerson.compose_response_physical_person(data)
    assert save_result.id


def test_compose_response_whithout_id():
    data = base_data.copy()
    save_result = ManagePhysicalPerson.compose_response_physical_person(data)
    assert save_result


@pytest.mark.asyncio
async def test_save_physical_person_has_exist():
    with pytest.raises(Exception):
        same_physical_person = PhysicalPerson(**base_data)
        await manage_physical_person.save_physical_person(same_physical_person)


@pytest.mark.asyncio
async def test_save_physical_person_email_has_exist():
    with pytest.raises(Exception):
        another_base_data = base_data.copy()
        another_base_data["name"] = "antonio"
        another_base_data["personal_document_id"] = "22299777773"
        another_physical_person = PhysicalPerson(**another_base_data)
        await manage_physical_person.save_physical_person(another_physical_person)


@pytest.mark.asyncio
async def test_save_physical_person_document_has_exist():
    with pytest.raises(Exception):
        another_base_data = base_data.copy()
        another_base_data["name"] = "antonio"
        another_base_data["email"] = "antonio.neto@teste.com"
        another_physical_person = PhysicalPerson(**another_base_data)
        await manage_physical_person.save_physical_person(another_physical_person)


@pytest.mark.asyncio
async def test_update_physical_person():
    await manage_physical_person.update_physical_person(output_data["id"], {"email": "joao.silva@teste.com"})


@pytest.mark.asyncio
async def test_update_physical_person_type_error():
    with pytest.raises(Exception):
        await manage_physical_person.update_physical_person("0", {"email": "joao.silva2@teste.com"})


@pytest.mark.asyncio
@pytest.mark.asyncio
async def test_get_by_id_physical_person():
    get_result = await manage_physical_person.get_physical_person_by_id(output_data["id"])
    assert output_data["id"] == str(get_result.id)


@pytest.mark.asyncio
async def test_get_by_id_physical_person_type_error():
    with pytest.raises(Exception):
        await manage_physical_person.get_physical_person_by_id("0")


@pytest.mark.asyncio
@pytest.mark.asyncio
async def test_get_by_query_physical_person():
    get_result = await manage_physical_person.get_physical_person_by_query({"email": "joao.silva@teste.com"})
    assert len(get_result) == 1


@pytest.mark.asyncio
@pytest.mark.asyncio
async def test_get_by_query_physical_person_with_date():
    get_result = await manage_physical_person.get_physical_person_by_query({
        "initial_date": "1988-01-01",
        "end_date": "2001-01-01"
    })
    assert len(get_result) == 0


@pytest.mark.asyncio
async def test_get_by_query_physical_person_type_error():
    get_result = await manage_physical_person.get_physical_person_by_query({"color": (1, 2, 3)})
    assert len(get_result) == 0


@pytest.mark.asyncio
async def test_get_by_query_physical_person_type_error_fetch():
    with pytest.raises(Exception):
        await manage_physical_person.get_physical_person_by_query(
            {
                "initial_date": True,
                "end_date": False
            }
        )


@pytest.mark.asyncio
@pytest.mark.asyncio
async def test_delete_physical_person():
    delete_result = await manage_physical_person.delete_physical_person(output_data["id"])
    assert delete_result


@pytest.mark.asyncio
@pytest.mark.asyncio
async def test_delete_physical_person_error():
    with pytest.raises(Exception):
        await manage_physical_person.delete_physical_person("0")
