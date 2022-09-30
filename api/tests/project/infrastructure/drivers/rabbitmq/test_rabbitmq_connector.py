import pytest
import asyncio
from project.infrastructure.drivers.rabbitmq.connector import RabbitMq


@pytest.mark.asyncio
async def test_rabbitmq_connection_success():
    """
    when: Crio uma conexão com o Rabbit MQ
    Then: Obtenho sucesso
    """
    rabbitmq = RabbitMq()
    if not await rabbitmq.connection():
        raise AssertionError


@pytest.mark.asyncio
async def test_rabbitmq_connection_error():
    with pytest.raises(Exception):
        rabbitmq = RabbitMq()
        rabbitmq.host = ""
        await rabbitmq.connection()
