from project.helpers.pydantic_typo import MongoId
from typing import Optional
from pydantic import BaseModel


class BillingDataQueryString(BaseModel):
    status: Optional[str]
    person_id: Optional[str]


class BillingDataUpdateData(BaseModel):
    status: Optional[str]
    person_id: Optional[str]
    payment_method_codes: Optional[list[str]]


class BillingDataResponse(BaseModel):
    id: Optional[MongoId]
    status: str
    person_id: str
    payment_method_codes: list[str]


class BillingDataInput(BaseModel):
    status: str
    person_id: str
    payment_method_codes: list[str]


class BillingDataModified(BaseModel):
    itens_affected: int
    itens_modified: int
