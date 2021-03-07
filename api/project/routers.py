from fastapi import FastAPI
from elasticapm.contrib.starlette import ElasticAPM
from project.infrastructure.drivers.apm.adapter import ApmAdapter
from project.resources.lifecheck.controllers.lifecheck_controller import router as lifecheckapi


app = FastAPI()
apm = ApmAdapter.get_client()

# app middlewares
app.add_middleware(ElasticAPM, client=apm)

# app routes
app.include_router(lifecheckapi, prefix="/health",)
