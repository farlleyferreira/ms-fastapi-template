
import pytest
from project.infrastructure.drivers.redis.connector import Redis


def test_mongo_connection_success():
    """
        when: Crio uma conexão com o Apm
        Then: Obtenho sucesso
    """
    redis = Redis()
    assert redis.client()


def test_mongo_connection_error():
    """
        when: Crio uma conexão com o Apm
        Then: Obtenho falha
    """
    redis = Redis()
    redis.redis_config = {"unknow": ""}

    assert pytest.raises(Exception, redis.client)
