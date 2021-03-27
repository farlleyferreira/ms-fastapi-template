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

    input_data = {
        "status": "active",
        "person_id": str(ObjectId()),
        "payment_method_codes": [
            str(ObjectId()),
        ]
    }
    physical_person = BillingData(**input_data)
    assert input_data["status"] == physical_person.dict()["status"]
