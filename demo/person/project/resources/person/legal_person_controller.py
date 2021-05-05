from project.domain.person.repository.legal_person import LegalPerson
from typing import List
from fastapi import APIRouter, HTTPException
from fastapi.param_functions import Depends
from starlette.responses import JSONResponse, Response
from project.resources.person.schemas.legal_person import LegalPersonQueryString
from project.resources.person.schemas.legal_person import LegalPersonResponse
from project.resources.person.schemas.legal_person import LegalPersonModified
from project.resources.person.schemas.legal_person import LegalPersonInput
from project.domain.person.business_rules.manage_legal_person import ManageLegalPerson


router = APIRouter()


@router.get(
    "/by/id/{id}",
    response_model=LegalPersonResponse
)
async def get_by_id(id: str):
    """
        ### Recurso que tem por objetivo buscar uma pessoa.
        #### Usa como parametro de busca o seu identificador:
            - id [str(ObjectId)] = "605dcc895dbd779d5e66bd90"
    """
    try:
        manage_legal_person = ManageLegalPerson()
        legal_person = await manage_legal_person.get_legal_person_by_id(id)
        return legal_person.dict()
    except Exception:
        raise HTTPException(status_code=500, detail="error to fetch data")


@router.get(
    "/by/qs",
    response_model=List[LegalPersonResponse],
    responses={204: {"model": None}},
)
async def get_by_query(filter: LegalPersonQueryString = Depends(LegalPersonQueryString)):
    """
        ### Recurso que tem por objetivo buscar uma lista de pessoas.
        #### A lista poderá ser filtrada por uma, ou pelo agrupamento das seguintes propriedades:
            - business_name: [str] = joao
            - fantasy_name: [str] = da silva
            - status: [str] =
                - active
                - inactive
            - sponsor_business_document_id: [str] = 11122233344 -> CPF
            - business_document_id: [str]  11222333444455 -> CNPJ
            - personal_document_id: [str] = 000.000.000-00
            - email: [str] = email@email.com
            - phone: [str] = +5534911112222
    """
    try:
        input_filter = filter.dict(exclude_none=True)

        manage_legal_person = ManageLegalPerson()
        list_of_legal_person = await manage_legal_person.get_legal_person_by_query(input_filter)

        if len(list_of_legal_person):
            return list_of_legal_person
        return Response(status_code=204)

    except Exception as error:
        errors = list(error.args)
        return JSONResponse(status_code=500, content=errors)


@router.post(
    "/",
    response_model=LegalPersonResponse
)
async def save_legal_person(request: LegalPersonInput):
    """
        ### Recurso que tem por objetivo salvar uma pessoa fisica.
    """
    try:
        manage_legal_person = ManageLegalPerson()
        legal_person = LegalPerson(**request.dict())
        legal_person = await manage_legal_person.save_legal_person(legal_person)
        return legal_person.dict()
    except RuntimeError as error:
        errors = list(error.args)
        return JSONResponse(status_code=400, content=errors)


@router.put(
    "/{id}",
    response_model=LegalPersonModified
)
async def update_legal_person(id: str, request: LegalPersonQueryString):
    """
        ### Recurso que tem por objetivo modificar os dados de uma pessoa.
        #### Os atributos que poderão ser modificados são:
            - business_name: [str] = joao
            - fantasy_name: [str] = da silva
            - status: [str] =
                - active
                - inactive
            - sponsor_business_document_id: [str] = 11122233344 -> CPF
            - business_document_id: [str]  11222333444455 -> CNPJ
            - personal_document_id: [str] = 000.000.000-00
            - email: [str] = email@email.com
            - phone: [str] = +5534911112222
    """
    try:
        update_object = request.dict(exclude_none=True)
        manage_legal_person = ManageLegalPerson()
        itens_modified = await manage_legal_person.update_legal_person(id, update_object)
        return itens_modified
    except Exception as error:
        errors = list(error.args)
        return JSONResponse(status_code=500, content=errors)


@router.delete(
    "/by/{id}",
    response_model=LegalPersonModified
)
async def delete(id: str):
    """
        ### Recurso que tem por objetivo deletar os dados de uma pessoa.
        #### Usa como parametro de busca o seu identificador:
            - id [str(ObjectId)] = "605dcc895dbd779d5e66bd90"
    """
    try:
        manage_legal_person = ManageLegalPerson()
        legal_person = await manage_legal_person.delete_legal_person(id)
        return legal_person
    except Exception as error:
        errors = list(error.args)
        return JSONResponse(status_code=500, content=errors)
