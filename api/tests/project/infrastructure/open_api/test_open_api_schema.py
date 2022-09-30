from project.routers import app

from project.infrastructure.open_api.open_api_schema import Schema


def test_open_api():

    schema = Schema(app=app, title="teste", version="0.0.0", url_logo="", description="")
    oas = schema.create()
    if 'info' not in oas:
        raise AssertionError
    schema._app.openapi_schema = oas

    new_oas = schema.create()
    if oas != new_oas:
        raise AssertionError
