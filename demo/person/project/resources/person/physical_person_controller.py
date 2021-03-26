from project.repositories.person.models.physical_person import PhysicalPerson
from typing import List
from fastapi import APIRouter
from fastapi.param_functions import Depends
from starlette.responses import Response
from project.resources.person.schemas.physical_person import PhysicalPersonQueryString
from project.resources.person.schemas.physical_person import PhysicalPersonResponse
from project.resources.person.schemas.physical_person import PhysicalPersonModified
from project.resources.person.schemas.physical_person import PhysicalPersonInput
from project.repositories.person.business_rules.manage_physical_person import ManagePhysicalPerson


router = APIRouter()


@router.get(
    "/by/id/{id}",
    response_model=PhysicalPersonResponse
)
async def get_by_id(id: str):
    """
        ### Recurso que tem por objetivo buscar uma pessoa.
        #### Usa como parametro de busca o seu identificador:
            - id [str(ObjectId)] = "605dcc895dbd779d5e66bd90"
    """
    manage_physical_person = ManagePhysicalPerson()
    physical_person = await manage_physical_person.get_physical_person_by_id(id)
    return physical_person.dict()


@router.get(
    "by/qs",
    response_model=List[PhysicalPersonResponse],
    responses={204: {"model": None}},
)
async def get_by_query(filter: PhysicalPersonQueryString = Depends(PhysicalPersonQueryString)):
    """
        ### Recurso que tem por objetivo buscar uma lista de pessoas.
        #### A lista poderá ser filtrada por uma, ou pelo agrupamento das seguintes propriedades:
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
    input_filter = filter.dict(exclude_none=True)

    manage_physical_person = ManagePhysicalPerson()
    list_of_physical_person = await manage_physical_person.get_physical_person_by_query(input_filter)

    if len(list_of_physical_person):
        return list_of_physical_person
    return Response(status_code=204)


@router.post(
    "/",
    response_model=PhysicalPersonResponse
)
async def save_physical_person(request: PhysicalPersonInput):
    """
        ### Recurso que tem por objetivo salvar uma pessoa fisica.
    """
    manage_physical_person = ManagePhysicalPerson()
    physical_person = PhysicalPerson(**request.dict())
    physical_person = await manage_physical_person.save_physical_person(physical_person)
    return physical_person.dict()


@router.put(
    "/{id}",
    response_model=PhysicalPersonModified
)
async def update_physical_person(id: str, request: PhysicalPersonQueryString):
    """
        ### Recurso que tem por objetivo modificar os dados de uma pessoa.
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

    update_object = request.dict(exclude_none=True)
    manage_physical_person = ManagePhysicalPerson()
    itens_modified = await manage_physical_person.update_physical_person(id, update_object)
    return itens_modified


@router.delete(
    "/by/{id}",
    response_model=PhysicalPersonModified
)
async def delete(id: str):
    """
        ### Recurso que tem por objetivo deletar os dados de uma pessoa.
        #### Usa como parametro de busca o seu identificador:
            - id [str(ObjectId)] = "605dcc895dbd779d5e66bd90"
    """
    manage_physical_person = ManagePhysicalPerson()
    physical_person = await manage_physical_person.delete_physical_person(id)
    return physical_person
