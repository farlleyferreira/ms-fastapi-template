import pytest

from bson.objectid import ObjectId
from project.domain.person.repository.address import Address


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
        "number": "str",
        "type": "billing"
    }
    physical_person = Address(**input_data)
    if input_data["_id"] != physical_person.dict()["id"]:
        raise AssertionError


def test_instance_physical_person_without_id():
    with pytest.raises(ValueError):
        input_data = {
            "status": "",
            "person_id": "",
            "country": "str",
            "state": "str",
            "city": "str",
            "street": "str",
            "district": "str",
            "zip_code": "str",
            "number": "str",
            "type": ""
        }
        Address(**input_data)
