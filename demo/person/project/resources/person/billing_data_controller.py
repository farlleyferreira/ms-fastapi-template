from project.domain.person.repository.billing_data import BillingData
from typing import List
from fastapi import APIRouter, HTTPException
from fastapi.param_functions import Depends
from starlette.responses import Response, JSONResponse
from project.resources.person.schemas.billing_data import BillingDataQueryString
from project.resources.person.schemas.billing_data import BillingDataUpdateData
from project.resources.person.schemas.billing_data import BillingDataResponse
from project.resources.person.schemas.billing_data import BillingDataModified
from project.resources.person.schemas.billing_data import BillingDataInput
from project.domain.person.business_rules.manage_billing_data import ManageBillingData


router = APIRouter()


@router.get(
    "/by/id/{id}",
    response_model=BillingDataResponse
)
async def get_by_id(id: str):
    """
        ### Recurso que tem por objetivo buscar dados de pagamento de uma pessoa.
        #### Usa como parametro de busca o seu identificador:
            - id [str(ObjectId)] = "605dcc895dbd779d5e66bd90"
    """
    try:
        manage_billing_data = ManageBillingData()
        billing_data = await manage_billing_data.get_billing_data_by_id(id)
        return billing_data.dict()
    except Exception:
        raise HTTPException(status_code=500, detail="error to fetch data")


@router.get(
    "/by/qs",
    response_model=List[BillingDataResponse],
    responses={204: {"model": None}},
)
async def get_by_query(filter: BillingDataQueryString = Depends(BillingDataQueryString)):
    """
        ### Recurso que tem por objetivo buscar uma lista de dados de pagamento de uma pessoa.
        #### A lista poderá ser filtrada por uma, ou pelo agrupamento das seguintes propriedades:
            - status: [str] =
                - active
                - inactive
            - person_id: [str] = "605dcc895dbd779d5e66bd90"
            - payment_method_codes: list[str] = [
                "605dcc895dbd779d5e66bd90"
            ]
    """
    try:
        input_filter = filter.dict(exclude_none=True)

        manage_billing_data = ManageBillingData()
        list_of_billing_data = await manage_billing_data.get_billing_data_by_query(input_filter)

        if len(list_of_billing_data):
            return list_of_billing_data
        return Response(status_code=204)
    except Exception as error:
        errors = list(error.args)
        return JSONResponse(status_code=500, content=errors)


@router.post(
    "/",
    response_model=BillingDataResponse
)
async def save_billing_data(request: BillingDataInput):
    """
        ### Recurso que tem por objetivo salvar dados de pagamento de uma pessoa.
    """
    try:
        manage_billing_data = ManageBillingData()
        billing_data = BillingData(**request.dict())
        billing_data = await manage_billing_data.save_billing_data(billing_data)
        return billing_data.dict()
    except Exception as error:
        errors = list(error.args)
        return JSONResponse(status_code=400, content=errors)


@router.put(
    "/{id}",
    response_model=BillingDataModified
)
async def update_billing_data(id: str, request: BillingDataUpdateData):
    """
        ### Recurso que tem por objetivo modificar os dados de pagamento de uma pessoa.
        #### Os atributos que poderão ser modificados são:
            - status: [str] =
                - active
                - inactive
            - person_id: [str] = "605dcc895dbd779d5e66bd90"
            - payment_method_codes: list[str] = [
                "605dcc895dbd779d5e66bd90"
            ]
    """
    try:
        update_object = request.dict(exclude_none=True)
        manage_billing_data = ManageBillingData()
        itens_modified = await manage_billing_data.update_billing_data(id, update_object)
        return itens_modified
    except Exception as error:
        errors = list(error.args)
        return JSONResponse(status_code=500, content=errors)


@router.delete(
    "/by/{id}",
    response_model=BillingDataModified
)
async def delete(id: str):
    """
        ### Recurso que tem por objetivo deletar os dados de pagamento de uma pessoa.
        #### Usa como parametro de busca o seu identificador:
            - id [str(ObjectId)] = "605dcc895dbd779d5e66bd90"
    """
    try:
        manage_billing_data = ManageBillingData()
        billing_data = await manage_billing_data.delete_billing_data(id)
        return billing_data
    except Exception as error:
        errors = list(error.args)
        return JSONResponse(status_code=500, content=errors)
