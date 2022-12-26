from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


class Schema(object):
    def __init__(self, app: FastAPI, title: str) -> None:
        """[summary]

        Args:
            app (FastAPI): app instance
            title (str): titulo da documentação
            version (str): versão da aplicação
            url_logo (str): url da logo
            description (str): descrição
        """

        self._app = app
        self._title = title

    def create(self):
        """
            Cria schema de documentação no formato OAS3
        Returns:
            openapi_schema
        """

        if self._app.openapi_schema:
            return self._app.openapi_schema

        version = "0.0.6"
        url_logo = ""
        description = """

        Template base para criação de projetos de microsserviços, o projeto foi criado
        tendo como base a linguagem python 3.9.x, utilizando o framework FastApi

        Neste projeto, existem integrações prontas para consumo, sendo estas:

        - Redis
        - Mongo
        - Rabbit MQ
        - Elasticsearc

        Como framework de testes utilizamos o Pytest bem como, os seguintes pluggins:

        - pytest-cov
        - pytest-bdd
        - pytest-mock
        - pytest-asyncio

        """

        openapi_schema = get_openapi(
            title=self._title,
            version=version,
            routes=self._app.routes,
            description=description,
        )

        openapi_schema["info"]["x-logo"] = {"url": url_logo}

        self._app.openapi_schema = openapi_schema

        return self._app.openapi_schema
