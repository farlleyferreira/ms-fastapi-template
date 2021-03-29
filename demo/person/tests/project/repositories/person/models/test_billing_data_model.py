import pytest
from bson.objectid import ObjectId
from project.repositories.person.models.billing_data import BillingData


def test_instance_physical_person():

    input_data = {
        "_id": ObjectId(),
        "status": "active",
        "person_id": str(ObjectId()),
        "payment_method_codes": [
            str(ObjectId()),
        ]
    }
    physical_person = BillingData(**input_data)
    assert input_data["_id"] == physical_person.dict()["id"]


def test_instance_physical_person_without_id():
    with pytest.raises(ValueError):
        input_data = {
            "status": "",
            "person_id": "",
            "payment_method_codes": []
        }
        BillingData(**input_data)
