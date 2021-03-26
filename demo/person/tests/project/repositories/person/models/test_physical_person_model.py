from datetime import datetime
from bson.objectid import ObjectId
from project.repositories.person.models.physical_person import PhysicalPerson


def test_instance_physical_person():

    input_data = {
        "_id": ObjectId(),
        "status": "active",
        "name": "teste",
        "last_name": "teste",
        "age": 12,
        "birthdate": datetime.now(),
        "gender": "",
        "personal_document_id": "11122233344",
        "email": "teste@teste.com",
        "phone": "+5534988887777",
    }
    physical_person = PhysicalPerson(**input_data)
    assert input_data["_id"] == physical_person.dict()["id"]


def test_instance_physical_person_without_id():

    input_data = {
        "status": "active",
        "name": "teste",
        "last_name": "teste",
        "age": 12,
        "birthdate": datetime.now(),
        "gender": "",
        "personal_document_id": "22233344455",
        "email": "teste@teste.com",
        "phone": "+5534988887777",
    }
    physical_person = PhysicalPerson(**input_data)
    assert input_data["status"] == physical_person.dict()["status"]
