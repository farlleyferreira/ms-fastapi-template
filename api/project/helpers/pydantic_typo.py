from bson.objectid import ObjectId


class MongoId(ObjectId):  # pragma: no cover
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return v

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')
