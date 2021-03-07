import json
from aio_pika import Message, DeliveryMode, ExchangeType
from project.infrastructure.drivers.rabbitmq.connector import RabbitMq


class RabbitMqAdapter:
    """[summary]

    Returns:
        [type]: [description]
    """

    @staticmethod
    async def post_message(
        exange_name: str,
        message_body: dict,
        routing_key: str,
        headers: dict = None,
        priority: int = None
    ):
        """[summary]

        Args:
            exange_name (str): [description]
            message_body (dict): [description]
            routing_key (str): [description]
            headers (dict, optional): [description]. Defaults to None.
            priority (int, optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """

        rabbit_mq = RabbitMq()
        connection = await rabbit_mq.connection()

        channel = await connection.channel()

        channel_exchange = await channel.declare_exchange(
            exange_name,
            ExchangeType.FANOUT
        )

        binary_message_body = json.dumps(message_body).encode()
        delivery_mode = DeliveryMode.PERSISTENT

        message = Message(
            binary_message_body,
            delivery_mode=delivery_mode,
            headers=headers,
            priority=priority
        )

        await channel_exchange.publish(message, routing_key=routing_key)

        await connection.close()

        return {"message_sent": True}

    @staticmethod
    async def get_buildinfo() -> bool:
        """[summary]

        Returns:
            bool: [description]
        """
        rabbit_mq = RabbitMq()
        connection = await rabbit_mq.connection()
        is_closed = connection.is_closed
        await connection.close()
        if is_closed:
            return False
        return True
