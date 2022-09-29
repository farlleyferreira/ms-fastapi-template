import aio_pika
import os
from project.infrastructure.monitoring_layer.aplication_general_log import Log


log = Log()


class RabbitMq(object):
    def __init__(self) -> None:
        """
            Na inicialização da classe de conexão com o RabbitMQ,
        as configurações de ambiente são carregadas em tempo de execução,
        e servidas sob o contexto da instancia.
        """        
        self.host: str = str(os.getenv("RABBITMQ_HOST"))
        self.port = int(str(os.getenv("RABBITMQ_PORT")))
        self.username: str = str(os.getenv("RABBITMQ_USERNAME"))
        self.password: str = str(os.getenv("RABBITMQ_PASSWORD"))        

    async def connection(self):
        """
            Cria uma conexão com o RabbitMQ

        Raises:
            error: Exception

        Returns:
            Coroutine[Any, Any, ConnectionType@connect]
        """
        try:
            
            connection = await aio_pika.connect(
                host=self.host, port=self.port, login=self.username, password=self.password
            )

            return connection

        except Exception as error:

            log.record.error(
                "RabbitMQ connection error, check your server and configurations",
                exc_info=error,
            )
            raise error
