from project.repositories.person.models.address import Address
from typing import List
from fastapi import APIRouter, HTTPException
from fastapi.param_functions import Depends
from starlette.responses import Response, JSONResponse
from project.resources.person.schemas.address import AddressQueryString
from project.resources.person.schemas.address import AddressResponse
from project.resources.person.schemas.address import AddressModified
from project.resources.person.schemas.address import AddressInput
from project.repositories.person.business_rules.manage_address import ManageAddress


router = APIRouter()


@router.get(
    "/by/id/{id}",
    response_model=AddressResponse
)
async def get_by_id(id: str):
    """
        ### Recurso que tem por objetivo buscar um endereço.
        #### Usa como parametro de busca o seu identificador:
            - id [str(ObjectId)] = "605dcc895dbd779d5e66bd90"
    """
    try:
        manage_address = ManageAddress()
        address = await manage_address.get_address_by_id(id)
        return address.dict()
    except Exception:
        raise HTTPException(status_code=500, detail="error to fetch data")


@router.get(
    "/by/qs",
    response_model=List[AddressResponse],
    responses={204: {"model": None}},
)
async def get_by_query(filter: AddressQueryString = Depends(AddressQueryString)):
    """
        ### Recurso que tem por objetivo buscar uma lista de endereços.
        #### A lista poderá ser filtrada por uma, ou pelo agrupamento das seguintes propriedades:
            - status: [str] =
                - active
                - inactive
            person_id: [str] = "605dcc895dbd779d5e66bd90"
            country: [str] = "Latvéria"
            state: [str] = "Doomstadt"
            city: [str] = "Doomstadt"
            street: [str] = "42 avenue"
            district: [str] = "Norseheim"
            number: [str] = "42"
            zip_code: [str] = "42424242"
            type: [str] = "home"
    """
    try:
        input_filter = filter.dict(exclude_none=True)

        manage_address = ManageAddress()
        list_of_address = await manage_address.get_address_by_query(input_filter)

        if len(list_of_address):
            return list_of_address
        return Response(status_code=204)
    except Exception as error:
        errors = list(error.args)
        return JSONResponse(status_code=500, content=errors)


@router.post(
    "/",
    response_model=AddressResponse
)
async def save_address(request: AddressInput):
    """
        ### Recurso que tem por objetivo salvar o endereço de uma pessoa.
    """
    try:
        manage_address = ManageAddress()
        address = Address(**request.dict())
        address = await manage_address.save_address(address)
        return address.dict()
    except Exception as error:
        errors = list(error.args)
        return JSONResponse(status_code=400, content=errors)


@router.put(
    "/{id}",
    response_model=AddressModified
)
async def update_address(id: str, request: AddressQueryString):
    """
        ### Recurso que tem por objetivo modificar o endereço de uma pessoa.
        #### Os atributos que poderão ser modificados são:
            - name: [str] = joao
            - last_name: [str] = da silva
            - status: [str] =
                - active
                - inactive
            - initial_date: [str] = 1992-08-06
            - end_date: [str] = 2021-08-06
            - gender: [str] =
                - homem cisgênero
                - mulher cisgênero
                - homem transgênero
                - mulher transgênero
                - não binário
                - outros
            - personal_document_id: [str] = 000.000.000-00
            - email: [str] = email@email.com
            - phone: [str] = +5534911112222
    """
    try:
        update_object = request.dict(exclude_none=True)
        manage_address = ManageAddress()
        itens_modified = await manage_address.update_address(id, update_object)
        return itens_modified
    except Exception as error:
        errors = list(error.args)
        return JSONResponse(status_code=500, content=errors)


@router.delete(
    "/by/{id}",
    response_model=AddressModified
)
async def delete(id: str):
    """
        ### Recurso que tem por objetivo deletar o endereço de uma pessoa.
        #### Usa como parametro de busca o seu identificador:
            - id [str(ObjectId)] = "605dcc895dbd779d5e66bd90"
    """
    try:
        manage_address = ManageAddress()
        address = await manage_address.delete_address(id)
        return address
    except Exception as error:
        errors = list(error.args)
        return JSONResponse(status_code=500, content=errors)
