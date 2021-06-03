from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


class Schema(object):
    def __init__(
        self, app: FastAPI, title: str, version: str, url_logo: str, description: str
    ) -> None:
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
        self._version = version
        self._url_logo = url_logo
        self._description = description

    def create(self):
        """
            Cria schema de documentação no formato OAS3
        Returns:
            openapi_schema
        """

        if self._app.openapi_schema:
            return self._app.openapi_schema

        openapi_schema = get_openapi(
            title=self._title,
            version=self._version,
            routes=self._app.routes,
            description=self._description,
        )

        openapi_schema["info"]["x-logo"] = {"url": self._url_logo}

        self._app.openapi_schema = openapi_schema

        return self._app.openapi_schema
