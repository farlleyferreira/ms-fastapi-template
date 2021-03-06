from fastapi import FastAPI
from elasticapm.contrib.starlette import ElasticAPM
from project.infrastructure.drivers.apm.adapter import ApmAdapter
from project.resources.lifecheck.controllers.lifecheck_controller import router as lifecheckapi
from project.infrastructure.monitoring_layer.aplication_general_log import Log

log = Log()
app = FastAPI()
apm = ApmAdapter.get_client()

log.record.info("starting up aplication!!!")

app.add_middleware(ElasticAPM, client=apm)
app.include_router(lifecheckapi, prefix="/health",)
