import pytest
from unittest.mock import patch
from project.domain.lifecheck.business_rules.status import Lifecheck
from project.infrastructure.constants.health_check_status import Status


path_patch = "project.domain.lifecheck.business_rules.status.Lifecheck"


@pytest.mark.asyncio
@patch(f"{path_patch}.get_elk_database_status")
@patch(f"{path_patch}.get_mongo_database_status")
@patch(f"{path_patch}.get_redis_database_status")
@patch(f"{path_patch}.get_queue_status")
async def test_get_life_status_green(queue, redis, mongo, elk):
    
    _queue = queue
    _redis = redis
    _mongo = mongo
    _elk = elk

    _queue.return_value = True
    _redis.return_value = True
    _mongo.return_value = True
    _elk.return_value = True

    result = await Lifecheck({}).get_life_status()

    assert Status.GREEN == result.api_status
    assert "It's all fine! Shine On You Crazy Diamond!!" == result.aplication_message


@pytest.mark.asyncio
@patch(f"{path_patch}.get_elk_database_status")
@patch(f"{path_patch}.get_mongo_database_status")
@patch(f"{path_patch}.get_redis_database_status")
@patch(f"{path_patch}.get_queue_status")
async def test_get_life_status_yellow(queue, redis, mongo, elk):
    
    _queue = queue
    _redis = redis
    _mongo = mongo
    _elk = elk

    _queue.return_value = True
    _redis.return_value = False
    _mongo.return_value = True
    _elk.return_value = True

    result = await Lifecheck({}).get_life_status()

    assert Status.YELLOW == result.api_status
    assert (
        "WARNING: We have one or more problem, check logfiles please!!!"
        == result.aplication_message
    )


@pytest.mark.asyncio
@patch(f"{path_patch}.get_elk_database_status")
@patch(f"{path_patch}.get_mongo_database_status")
@patch(f"{path_patch}.get_redis_database_status")
@patch(f"{path_patch}.get_queue_status")
async def test_get_life_status_red(queue, redis, mongo, elk):
    
    _queue = queue
    _redis = redis
    _mongo = mongo
    _elk = elk

    _queue.return_value = False
    _redis.return_value = False
    _mongo.return_value = False
    _elk.return_value = False

    result = await Lifecheck({}).get_life_status()

    assert Status.RED == result.api_status
    assert (
        "Ops!!! houston we have a problem!!! A huge problem!!! check all drivers connection!!!"
        == result.aplication_message
    )
