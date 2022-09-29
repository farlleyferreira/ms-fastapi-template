import os
import motor.motor_asyncio as async_mongo
from project.infrastructure.monitoring_layer.aplication_general_log import Log

log = Log()


class Mongo(object):
    def __init__(self) -> None:
        """
            Na inicialização da classe de conexão com o Mongo,
        as configurações de ambiente são carregadas em tempo de execução,
        e servidas sob o contexto da instancia.
        """

        self.host: str = str(os.getenv("MONGO_HOST"))
        self.port = os.getenv("MONGO_PORT")
        self.username: str = str(os.getenv("MONGO_USERNAME"))
        self.password: str = str(os.getenv("MONGO_PASSWORD"))
        self.database: str = str(os.getenv("MONGO_DATABASE"))

    def client(self):
        """
            Cria uma conexão com o Mongo

        Raises:
            error: Exception

        Returns:
            Mongo.Database
        """
        try:

            uri: str = (
                f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}"
            )

            client = async_mongo.AsyncIOMotorClient(uri)

            return client[self.database]

        except Exception as error:

            log.record.error(
                "MongoDB connection error, check your server and credentials",
                exc_info=error,
            )
            raise error
