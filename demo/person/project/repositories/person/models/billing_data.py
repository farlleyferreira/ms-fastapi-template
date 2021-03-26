from bson.objectid import ObjectId
from typing import List, Optional
from pydantic import BaseModel, Field, validator
from project.helpers.pydantic_typo import MongoId


class BillingData(BaseModel):
    id: Optional[MongoId] = Field(default=None, alias='_id')
    status: str
    person_id: str
    payment_method_codes: list[str]

    @validator('status')
    def validate_status(cls, v):
        if v not in ["active", "inactive"]:
            raise ValueError('status must be active or inactive')
        return v

    @validator('person_id')
    def validate_person_id(cls, v):
        if ObjectId.is_valid(v):
            raise ValueError('person id must be an valid id')
        return v

    @validator('payment_method_codes')
    def validate_payment_method_codes(cls, v):
        if len(v) == 0:
            raise ValueError('payment method codes must have at least one payment method')
        return v
