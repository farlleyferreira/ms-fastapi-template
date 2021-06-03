
import pytest
from project.infrastructure.drivers.mongo.connector import Mongo


def test_mongo_connection_success():
    """
        when: Crio uma conexão com o Apm
        Then: Obtenho sucesso
    """
    mongo = Mongo()
    if not mongo.client():
        raise AssertionError


def test_mongo_connection_error():
    mongo = Mongo()
    mongo.mongo_config = {"unknow": ""}

    if not pytest.raises(Exception, mongo.client):
        raise AssertionError
