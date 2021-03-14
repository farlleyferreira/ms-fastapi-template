
import pytest
import asyncio
from project.infrastructure.drivers.rabbitmq.connector import RabbitMq


@pytest.mark.asyncio
async def test_rabbitmq_connection_success():
    """
        when: Crio uma conexão com o Apm
        Then: Obtenho sucesso
    """
    rabbitmq = RabbitMq()
    assert await rabbitmq.connection()


def test_rabbitmq_connection_error():
    """
            when: Crio uma conexão com o Apm
            Then: Obtenho falha
        """
    with pytest.raises(Exception):
        rabbitmq = RabbitMq()
        rabbitmq.rabbit_mq_config = {"port": -5000}
        loop = asyncio.run(rabbitmq.connection())
        loop.close()
