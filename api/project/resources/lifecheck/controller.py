from fastapi import APIRouter, Request
from project.repositories.lifecheck.business_rules.health_status import Lifecheck

router = APIRouter()


@router.get("/")
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
    return await lifecheck.get_life_status()
