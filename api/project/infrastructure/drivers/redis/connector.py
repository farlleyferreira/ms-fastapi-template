import redis

from project.infrastructure.environments.loader import Configs
from project.infrastructure.monitoring_layer.aplication_general_log import Log
from project.infrastructure.monitoring_layer.aplication_kpi import Monitor

log = Log()


class Redis(object):
    """[summary]

    Args:
        object ([type]): [description]
    """

    def __init__(self):
        self.redis_config: dict = Configs.get_by_key("redis")

    def client(self):
        """[summary]

        Raises:
            error: [description]

        Returns:
            [type]: [description]
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
            Monitor.send_kpi_message("Redis client error", str(error))

            raise error
