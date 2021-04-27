from project.routers import app

from project.infrastructure.open_api.open_api_schema import Schema


def test_open_api():

    schema = Schema(app=app, title="teste", version="0.0.0", url_logo="", description="")
    oas = schema.create()
    assert 'info' in oas
    schema._app.openapi_schema = oas

    new_oas = schema.create()
    assert oas == new_oas
