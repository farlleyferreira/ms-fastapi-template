import redis

from project.infrastructure.environments.loader import Configs
from project.infrastructure.monitoring_layer.aplication_general_log import Log
from project.infrastructure.monitoring_layer.aplication_kpi import Monitor

log = Log()


class Redis:

    def __init__(self):
        """
            Na inicialização da classe de conexão com o Redis,
        as configurações de ambiente são carregadas em tempo de execução,
        e servidas sob o contexto da instancia.
        """
        self.redis_config: dict = Configs.get_by_key("redis")

    def client(self):
        """
            Cria uma conexão com o RabbitMQ

        Raises:
            error: Exception

        Returns:
            Redis
        """
        try:

            host: str = self.redis_config["host"]
            port: int = self.redis_config["port"]
            password: str = self.redis_config["password"]

            client = redis.Redis(host=host, port=port, password=password)
            client.ping()

            return client

        except Exception as error:

            log.record.error(
                "Redis connection error, check your server and credentials",
                exc_info=error
            )
            Monitor.send_kpi_message("Redis client error")

            raise error
