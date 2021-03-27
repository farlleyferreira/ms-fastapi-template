from bson.objectid import ObjectId
from project.repositories.person.models.address import Address


def test_instance_physical_person():

    input_data = {
        "_id": ObjectId(),
        "status": "active",
        "person_id": str(ObjectId()),
        "country": "str",
        "state": "str",
        "city": "str",
        "street": "str",
        "district": "str",
        "zip_code": "str",
        "type": "billing"
    }
    physical_person = Address(**input_data)
    assert input_data["_id"] == physical_person.dict()["id"]


def test_instance_physical_person_without_id():

    input_data = {
        "status": "active",
        "person_id": str(ObjectId()),
        "country": "str",
        "state": "str",
        "city": "str",
        "street": "str",
        "district": "str",
        "zip_code": "str",
        "type": "billing"
    }
    physical_person = Address(**input_data)
    assert input_data["status"] == physical_person.dict()["status"]
