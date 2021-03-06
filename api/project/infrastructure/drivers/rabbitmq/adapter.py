import json
import asyncio
import aio_pika
from aio_pika import channel

from project.infrastructure.drivers.rabbitmq.connector import RabbitMq
from aio_pika import Message, DeliveryMode, ExchangeType


class RabbitMqAdapter:

    @staticmethod
    async def post_message(
        exange_name: str,
        message_body: dict,
        routing_key: str,
        headers: dict = None,
        priority: int = None
    ):

        rabbit_mq = RabbitMq()
        connection = await rabbit_mq.connection()

        channel = await connection.channel()

        channel_exchange = await channel.declare_exchange(
            exange_name,
            ExchangeType.FANOUT
        )

        message_body = json.dumps(message_body).encode()
        delivery_mode = DeliveryMode.PERSISTENT

        message = Message(
            message_body,
            delivery_mode=delivery_mode,
            headers=headers,
            priority=priority
        )

        await channel_exchange.publish(message, routing_key=routing_key)

        await connection.close()

        return {"message_sent": True}
    
    
    @staticmethod
    async def get_buildinfo() -> RabbitMq:
        try:
            rabbit_mq = RabbitMq()
            connection = await rabbit_mq.connection()
            is_closed = connection.is_closed
            await connection.close()
            return not is_closed
        except Exception:
            return False

