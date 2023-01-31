import pytest
import asyncio
from project.infrastructure.drivers.rabbitmq.adapter import RabbitMqAdapter


@pytest.mark.asyncio
async def test_get_buildinfo():
    rabbitmq = RabbitMqAdapter()
    assert await rabbitmq.get_buildinfo() == True

