import re
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field, validator
from project.helpers.pydantic_typo import MongoId


class PhysicalPerson(BaseModel):
    id: Optional[MongoId] = Field(default=None, alias='_id')
    name: str
    last_name: str
    status: str
    birthdate: datetime
    gender: Optional[str]
    personal_document_id: str
    email: str
    phone: str
    age: Optional[int]

    @validator('name')
    def validate_name(cls, v):
        if len(v) <= 0:
            raise ValueError('name must be valid')
        return v

    @validator('last_name')
    def validate_last_name(cls, v):
        if len(v) <= 0:
            raise ValueError('last_name must be valid')
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

    @validator('personal_document_id')
    def validate_personal_document_id(cls, v):
        if not len(v) == 11:
            raise ValueError('personal document must be a valid document')
        return v

    @validator('birthdate')
    def validate_birthdate(cls, v, values):
        age = datetime.now().year - v.year
        values['birthdate'] = age
        return v

    @validator('age')
    def validate_age(cls, v, values):
        age = datetime.now().year - values['birthdate'].year
        return age
