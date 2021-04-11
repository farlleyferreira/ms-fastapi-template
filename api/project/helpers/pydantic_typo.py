from bson.objectid import ObjectId


class MongoId(ObjectId):
    """
        MongoId class
    Args:
        ObjectId: Mongo Object Id Type
    """

    def __init__(self):
        """
            Implementation for validating the ObjectId type.
        """
        super().__init__()

    @classmethod
    def __get_validators__(cls):
        """
            Binds the validator to standard class validators
        """
        yield cls.validate

    @classmethod
    def validate(cls, v):
        """
            Checks whether the assigned value can be a valid ObjectId or not.
        """
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return v

    @classmethod
    def __modify_schema__(cls, field_schema):
        """
            Modifies the standard ObjectId schema to accept the string type
        """
        field_schema.update(type='string')
