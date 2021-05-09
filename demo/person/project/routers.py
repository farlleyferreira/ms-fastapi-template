from fastapi import FastAPI
from elasticapm.contrib.starlette import ElasticAPM
from project.infrastructure.open_api.open_api_schema import Schema
from project.infrastructure.drivers.apm.adapter import ApmAdapter
from project.resources.lifecheck.controller import router as life_check_api
from project.resources.person.physical_person_controller import router as physical_person_api
from project.resources.person.legal_person_controller import router as legal_person_api
from project.resources.person.billing_data_controller import router as billing_data_api
from project.resources.person.address_controller import router as address_api


app = FastAPI()
apm = ApmAdapter().client()

# app middlewares
app.add_middleware(ElasticAPM, client=apm)

# app routes
app.include_router(life_check_api, prefix="/health", tags=["health"])
app.include_router(legal_person_api, prefix="/person/legal", tags=["legal"])
app.include_router(physical_person_api, prefix="/person/physical", tags=["physical"])
app.include_router(billing_data_api, prefix="/person/billing_data", tags=["billing_data"])
app.include_router(address_api, prefix="/person/address", tags=["address"])


schema = Schema(
    app=app,
    title="Microservices template",
    version="0.0.0",
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
