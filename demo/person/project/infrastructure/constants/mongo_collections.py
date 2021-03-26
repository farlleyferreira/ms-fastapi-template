import enum


class Collections(str, enum.Enum):
    person_billing_data = "person_billing_data"
    physical_person = "physical_person"
    person_address = "person_address"
    legal_person = "legal_person"
