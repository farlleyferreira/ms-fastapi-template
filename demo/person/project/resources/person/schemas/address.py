from project.helpers.pydantic_typo import MongoId
from typing import Optional
from pydantic import BaseModel


class AddressQueryString(BaseModel):
    status: Optional[str]
    person_id: Optional[str]
    country: Optional[str]
    state: Optional[str]
    city: Optional[str]
    street: Optional[str]
    district: Optional[str]
    zip_code: Optional[str]
    number: Optional[str]
    type: Optional[str]


class AddressResponse(BaseModel):
    id: Optional[MongoId]
    status: str
    person_id: str
    country: str
    state: str
    city: str
    street: str
    district: str
    zip_code: str
    number: str
    type: str


class AddressInput(BaseModel):
    status: str
    person_id: str
    country: str
    state: str
    city: str
    street: str
    district: str
    zip_code: str
    number: str
    type: str


class AddressModified(BaseModel):
    itens_affected: int
    itens_modified: int
