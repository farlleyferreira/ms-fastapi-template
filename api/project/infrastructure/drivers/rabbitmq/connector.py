import aio_pika

from project.infrastructure.environments.loader import Configs
from project.infrastructure.monitoring_layer.aplication_general_log import Log
from project.infrastructure.monitoring_layer.aplication_kpi import Monitor

log = Log()


class RabbitMq:

    def __init__(self) -> None:
        self.mongo_config: dict = Configs.get_by_key("rabbitmq")

    async def connection(self):
        try:

            host: str = self.mongo_config["host"]
            port: int = self.mongo_config["port"]
            username: str = self.mongo_config["username"]
            password: str = self.mongo_config["password"]

            uri: str = f'amqp://{username}:{password}@{host}:{port}'
            connection = await aio_pika.connect(uri)

            return connection

        except Exception as error:

            Monitor.send_kpi_message("RabbitMQ client error", str(error))
            log.record.error(
                "RabbitMQ connection error, check your server and credentials",
                exc_info=error
            )

            raise error
