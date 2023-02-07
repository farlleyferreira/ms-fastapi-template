import pytest
from project.infrastructure.drivers.redis.adapter import RedisAdapter


def test_get_buildinfo():
    redis = RedisAdapter()
    if redis.get_buildinfo() != True:
        raise AssertionError
    if type(redis.get_buildinfo()) != bool:
        raise AssertionError
