
import pytest
from project.infrastructure.drivers.mongo.connector import Mongo


def test_mongo_connection_success():
    """
        when: Crio uma conexão com o Apm
        Then: Obtenho sucesso
    """
    mongo = Mongo()
    assert mongo.client()


def test_mongo_connection_error():
    """
        when: Crio uma conexão com o Apm
        Then: Obtenho falha
    """
    mongo = Mongo()
    mongo.mongo_config = {"unknow": ""}

    assert pytest.raises(Exception, mongo.client)
