from fastapi import APIRouter, Request
from project.domain.lifecheck.business_rules.business_rule import Lifecheck
from project.services.lifecheck.schema import ResponseLifeStatus

router = APIRouter()


@router.get(
    "/",
    response_model=ResponseLifeStatus
)
async def health_check(request: Request):
    """
    ### Recurso que tem por objetivo verificar a saude da aplicação.
    #### Verificando os status dos seguintes drivers:
        - Elasticsearch
        - Mongo
        - Redis
        - Rabit MQ
    """
    lifecheck = Lifecheck(request.headers)
    life_status = await lifecheck.get_life_status()
    return life_status
