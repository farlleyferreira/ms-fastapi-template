from project.helpers.pydantic_typo import MongoId
from typing import Optional
from pydantic import BaseModel


class LegalPersonQueryString(BaseModel):
    business_name: Optional[str]
    fantasy_name: Optional[str]
    status: Optional[str]
    sponsor_business_document_id: Optional[str]
    business_document_id: Optional[str]
    email: Optional[str]
    phone: Optional[str]


class LegalPersonResponse(BaseModel):
    id: Optional[MongoId]
    business_name: str
    fantasy_name: str
    status: str
    sponsor_business_document_id: str
    business_document_id: str
    email: str
    phone: str


class LegalPersonInput(BaseModel):
    business_name: str
    fantasy_name: str
    status: str
    sponsor_business_document_id: str
    business_document_id: str
    email: str
    phone: str


class LegalPersonModified(BaseModel):
    itens_affected: int
    itens_modified: int
