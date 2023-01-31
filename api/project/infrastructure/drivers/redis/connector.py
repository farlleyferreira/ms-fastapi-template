import redis
import os

from project.infrastructure.monitoring_layer.aplication_general_log import Log

log = Log()


class Redis(object):
    def __init__(self):
        self.host: str = str(os.getenv("REDIS_HOST"))
        self.port = int(str(os.getenv("REDIS_PORT")))
        self.password: str = str(os.getenv("REDIS_PASSWORD"))

    def client(self):
        """
            Cria uma conexão com o RabbitMQ

        Raises:
            error: Exception

        Returns:
            Redis
        """
        try:

            client = redis.Redis(host=self.host, port=self.port, password=self.password)
            client.ping()

            return client

        except Exception as error:

            log.record.error(
                "Redis connection error, check your server and credentials",
                exc_info=error,
            )

            raise error
