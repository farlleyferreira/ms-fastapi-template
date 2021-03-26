import re
from typing import List, Optional
from pydantic import BaseModel, Field, validator
from project.helpers.pydantic_typo import MongoId


class LegalPerson(BaseModel):
    id: Optional[MongoId] = Field(default=None, alias='_id')
    status: str
    business_name: str
    fantasy_name: str
    sponsor_business_document_id: str
    business_document_id: str
    mail: str
    phone: str

    @validator('business_name')
    def validate_name(cls, v):
        if len(v) <= 0:
            raise ValueError('business name must be valid')
        return v

    @validator('fantasy_name')
    def validate_last_name(cls, v):
        if len(v) <= 0:
            raise ValueError('fantasy name must be valid')
        return v

    @validator('status')
    def validate_status(cls, v):
        if v not in ["active", "inactive"]:
            raise ValueError('status must be active or inactive')
        return v

    @validator('email')
    def validate_mail(cls, v):
        if(re.search(r"[^@]+@[^@]+\.[^@]+", v)):
            return v
        raise ValueError('email must be valid')

    @validator('phone')
    def validate_phone(cls, v):
        regex = r'[\+\d]?(\d{2,3}[-\.\s]??\d{2,3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
        if(re.search(regex, v)):
            return v
        raise ValueError('phone must be valid')

    @validator('sponsor_business_document_id')
    def validate_sponsor_business_document_id(cls, v):
        if not len(v) == 11:
            raise ValueError('sponsor business document id document must be a valid document')
        return v

    @validator('business_document_id')
    def validate_business_document_id(cls, v):
        if not len(v) == 14:
            raise ValueError('business document id document must be a valid document')
        return v
