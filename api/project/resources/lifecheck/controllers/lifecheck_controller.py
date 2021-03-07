from fastapi import APIRouter, Request
from project.resources.lifecheck.business_roles.process import Lifecheck

router = APIRouter()


@router.get("/")
async def ping(request: Request):
    """[summary]

    Args:
        request (Request): [description]

    Returns:
        [type]: [description]
    """
    lifecheck = Lifecheck(request.headers)
    return await lifecheck.get_life_status()
