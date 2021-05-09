import pytest
from bson.objectid import ObjectId
from project.domain.person.repository.legal_person import LegalPerson


def test_instance_physical_person():

    input_data = {
        "_id": ObjectId(),
        "status": "active",
        "business_name": "teste",
        "fantasy_name": "teste dos testes",
        "sponsor_business_document_id": "11122233344",
        "business_document_id": "55566677000111",
        "email": "teste@teste.com",
        "phone": "+5534988887777",
    }
    physical_person = LegalPerson(**input_data)
    assert input_data["_id"] == physical_person.dict()["id"]


def test_instance_physical_person_errors():
    with pytest.raises(ValueError):
        input_data = {
            "status": "",
            "business_name": "",
            "fantasy_name": "",
            "sponsor_business_document_id": "",
            "business_document_id": "",
            "email": "teste",
            "phone": "",
        }
        LegalPerson(**input_data)
