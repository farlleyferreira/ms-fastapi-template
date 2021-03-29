import aio_pika

from project.infrastructure.environments.loader import Configs
from project.infrastructure.monitoring_layer.aplication_general_log import Log
from project.infrastructure.monitoring_layer.aplication_kpi import Monitor

log = Log()


class RabbitMq:

    def __init__(self) -> None:
        """
            Na inicialização da classe de conexão com o RabbitMQ,
        as configurações de ambiente são carregadas em tempo de execução,
        e servidas sob o contexto da instancia.
        """
        self.rabbit_mq_config: dict = Configs.get_by_key("rabbitmq")

    async def connection(self):
        """
            Cria uma conexão com o RabbitMQ

        Raises:
            error: Exception

        Returns:
            Coroutine[Any, Any, ConnectionType@connect]
        """
        try:

            host: str = self.rabbit_mq_config["host"]
            port: int = self.rabbit_mq_config["port"]
            username: str = self.rabbit_mq_config["username"]
            password: str = self.rabbit_mq_config["password"]

            connection = await aio_pika.connect(
                host=host,
                port=port,
                login=username,
                password=password
            )

            return connection

        except Exception as error:

            log.record.error(
                "RabbitMQ connection error, check your server and configurations",
                exc_info=error
            )
            Monitor.send_kpi_message("RabbitMQ client error")

            raise error
