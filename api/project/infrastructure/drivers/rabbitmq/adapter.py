from project.infrastructure.drivers.rabbitmq.connector import RabbitMq


class RabbitMqAdapter(RabbitMq):
    def __init__(self) -> None:
        super().__init__()

    async def get_buildinfo(self) -> bool:
        connection = await self.connection()
        is_closed = connection.is_closed
        await connection.close()
        return not is_closed
