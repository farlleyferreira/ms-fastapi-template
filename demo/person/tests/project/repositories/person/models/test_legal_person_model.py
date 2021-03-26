from datetime import datetime
from bson.objectid import ObjectId
from project.repositories.person.models.legal_person import LegalPerson


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


def test_instance_physical_person_without_id():

    input_data = {
        "status": "active",
        "business_name": "teste",
        "fantasy_name": "teste dos testes",
        "sponsor_business_document_id": "11122233344",
        "business_document_id": "55566677000111",
        "email": "teste@teste.com",
        "phone": "+5534988887777",
    }
    physical_person = LegalPerson(**input_data)
    assert input_data["status"] == physical_person.dict()["status"]
