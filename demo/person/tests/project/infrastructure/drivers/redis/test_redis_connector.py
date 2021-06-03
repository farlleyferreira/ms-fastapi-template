
import pytest
from project.infrastructure.drivers.redis.connector import Redis


def test_mongo_connection_success():
    redis = Redis()
    if not redis.client():
        raise AssertionError


def test_mongo_connection_error():
    redis = Redis()
    redis.redis_config = {"unknow": ""}

    if not pytest.raises(Exception, redis.client):
        raise AssertionError
