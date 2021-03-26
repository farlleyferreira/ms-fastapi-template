from datetime import datetime
from project.repositories.person.models.physical_person import PhysicalPerson
from project.helpers.pydantic_typo import MongoId
from typing import Optional
from pydantic import BaseModel


class PhysicalPersonQueryString(BaseModel):
    name: Optional[str] = None
    last_name: Optional[str] = None
    status: Optional[str] = None
    initial_date: Optional[str] = None
    end_date: Optional[str] = None
    gender: Optional[str] = None
    personal_document_id: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None


class PhysicalPersonResponse(BaseModel):
    id: Optional[MongoId]
    name: str
    last_name: str
    status: str
    birthdate: datetime
    gender: Optional[str]
    personal_document_id: str
    email: str
    phone: str
    age: Optional[int]


class PhysicalPersonInput(BaseModel):
    name: str
    last_name: str
    status: str
    birthdate: datetime
    gender: Optional[str]
    personal_document_id: str
    email: str
    phone: str
    age: Optional[int] = 0


class PhysicalPersonModified(BaseModel):
    itens_affected: int
    itens_modified: int
