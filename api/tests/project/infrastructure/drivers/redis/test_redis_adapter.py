
import pytest
from project.infrastructure.drivers.redis.adapter import RedisAdapter


def test_get_buildinfo():
    redis = RedisAdapter()
    assert redis.get_buildinfo() == True
    assert type(redis.get_buildinfo()) == bool
