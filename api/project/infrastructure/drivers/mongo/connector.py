import motor.motor_asyncio as async_mongo
from project.infrastructure.environments.loader import Configs
from project.infrastructure.monitoring_layer.aplication_general_log import Log
from project.infrastructure.monitoring_layer.aplication_kpi import Monitor

log = Log()


class Mongo:

    def __init__(self) -> None:
        """
            Na inicialização da classe de conexão com o Mongo,
        as configurações de ambiente são carregadas em tempo de execução,
        e servidas sob o contexto da instancia.
        """
        self.mongo_config: dict = Configs.get_by_key("mongo")

    def client(self):
        """
            Cria uma conexão com o Mongo

        Raises:
            error: Exception

        Returns:
            Mongo.Database
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

            log.record.error(
                "MongoDB connection error, check your server and credentials",
                exc_info=error
            )
            Monitor.send_kpi_message("MongoDB client error", str(error))

            raise error
