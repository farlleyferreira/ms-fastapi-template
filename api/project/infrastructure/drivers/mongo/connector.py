import motor.motor_asyncio as async_mongo
from project.infrastructure.environments.loader import Configs
from project.infrastructure.monitoring_layer.aplication_general_log import Log
from project.infrastructure.monitoring_layer.aplication_kpi import Monitor

log = Log()


class Mongo:

    def __init__(self) -> None:
        self.mongo_config: dict = Configs.get_by_key("mongo")

    def client(self):
        """[summary]

        Raises:
            error: [description]

        Returns:
            [type]: [description]
        """
        try:

            host: str = self.mongo_config["host"]
            port: int = self.mongo_config["port"]
            username: str = self.mongo_config["username"]
            password: str = self.mongo_config["password"]
            database: str = self.mongo_config["database"]

            uri: str = f'mongodb://{username}:{password}@{host}:{port}'
            client = async_mongo.AsyncIOMotorClient(uri)

            return client[database]

        except Exception as error:

            Monitor.send_kpi_message("MongoDB client error", str(error))
            log.record.error(
                "MongoDB connection error, check your server and credentials",
                exc_info=error
            )

            raise error
