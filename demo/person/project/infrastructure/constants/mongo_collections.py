import enum


class Collections(str, enum.Enum):
    """
        Mongo collections enum set
        Please add your MongoDb collection to this class
        Obs: dont change snake_type pattern
    """
    general_collection = "general_collection"
    person_billing_data = "person_billing_data"
    physical_person = "physical_person"
    person_address = "person_address"
    legal_person = "legal_person"
