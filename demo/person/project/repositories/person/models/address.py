from bson.objectid import ObjectId
from typing import List, Optional
from pydantic import BaseModel, Field, validator
from project.helpers.pydantic_typo import MongoId


class Address(BaseModel):
    id: Optional[MongoId] = Field(default=None, alias='_id')
    status: str
    person_id: str
    country: str
    state: str
    city: str
    street: str
    district: str
    zip_code: str
    type: str

    @validator('status')
    def validate_status(cls, v):
        if v not in ["active", "inactive"]:
            raise ValueError('status must be active or inactive')
        return v

    @validator('person_id')
    def validate_person_id(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('person id must be an valid id')
        return v

    @validator('type')
    def validate_type(cls, v):
        if v not in ["billing", "delivery", "home", "work"]:
            raise ValueError('type must be an valid id')
        return v
