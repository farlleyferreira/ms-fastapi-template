
import pytest
from project.infrastructure.drivers.redis.connector import Redis


def test_mongo_connection_success():
    redis = Redis()
    assert redis.client()


def test_mongo_connection_error():
    redis = Redis()
    redis.host = ""
    redis.password = ""

    assert pytest.raises(Exception, redis.client)