from project.infrastructure.drivers.rabbitmq.connector import RabbitMq


class RabbitMqAdapter:

    @staticmethod
    async def get_connection():
        """
            Instancia um client de conexão entre a
        aplicação e o RabbitMq

        Returns:
            Coroutine[Any, Any, ConnectionType@connect]
        """

        rabbit_mq = RabbitMq()
        connection = await rabbit_mq.connection()

        return connection

    @staticmethod
    async def get_buildinfo() -> bool:
        """
            Verifica se a conexão está ou não
        efetuada com sucesso

        Returns:
            bool
        """
        rabbit_mq = RabbitMq()
        connection = await rabbit_mq.connection()
        is_closed = connection.is_closed
        await connection.close()
        return not is_closed
