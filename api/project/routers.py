from fastapi import FastAPI
from elasticapm.contrib.starlette import ElasticAPM
from project.infrastructure.open_api.open_api_schema import Schema
from project.infrastructure.drivers.apm.adapter import ApmAdapter
from project.resources.lifecheck.controllers.main_controller import router as lifecheckapi


app = FastAPI()
apm = ApmAdapter().client()

# app middlewares
app.add_middleware(ElasticAPM, client=apm)

# app routes
app.include_router(lifecheckapi, prefix="/health",)


schema = Schema(
    app=app,
    title="Microservices template",
    version="0.0.1",
    url_logo="",
    description="""

    Template base para criação de projetos de microsserviços, o projeto foi criado
    tendo como base a linguagem python 3.9.x, utilizando o framework FastApi

    Neste projeto, existem integrações prontas para consumo, sendo estas:

    - Redis
    - Mongo
    - Rabbit MQ
    - Elasticsearc
    - Elastic APM

    Como framework de testes utilizamos o Pytest bem como, os seguintes pluggins:

    - pytest-cov
    - pytest-bdd
    - pytest-mock
    - pytest-asyncio

    """
)

app.openapi = schema.create
