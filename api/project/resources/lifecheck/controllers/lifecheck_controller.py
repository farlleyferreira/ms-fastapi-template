import os
from fastapi import APIRouter, Request
from project.resources.lifecheck.business_roles.process import Lifecheck

router = APIRouter()


@router.get("/")
async def ping(request: Request):
    lifecheck = Lifecheck(request.headers)
    return await lifecheck.get_life_status()
