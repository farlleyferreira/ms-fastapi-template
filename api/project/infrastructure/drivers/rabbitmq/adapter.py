from project.infrastructure.drivers.rabbitmq.connector import RabbitMq


class RabbitMqAdapter(RabbitMq):
    """
    RabbitMQ adapter class
    """

    def __init__(self) -> None:
        super().__init__()

    async def get_buildinfo(self) -> bool:
        """
            Verifica se a conexão está ou não
        efetuada com sucesso

        Returns:
            bool
        """
        connection = await self.connection()
        is_closed = connection.is_closed
        await connection.close()
        return not is_closed
