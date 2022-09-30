from datetime import datetime
from bson.objectid import ObjectId
import pytest
from project.domain.person.repository.physical_person import PhysicalPerson


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
    if input_data["_id"] != physical_person.dict()["id"]:
        raise AssertionError


def test_instance_physical_person_errors():
    with pytest.raises(ValueError):
        input_data = {
            "status": "",
            "name": "",
            "last_name": "",
            "age": -1,
            "birthdate": datetime.now(),
            "gender": "",
            "personal_document_id": "",
            "email": "",
            "phone": "",
        }
        PhysicalPerson(**input_data)
