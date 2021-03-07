from project.infrastructure.drivers.mongo.connector import Mongo


class MongoAdapter:

    @staticmethod
    def get_database():
        """
            Instancia um client de conexão entre a
        aplicação e o Mongo

        Returns:
            Mongo.Database
        """
        mongo = Mongo()
        return mongo.client()

    @staticmethod
    async def get_buildinfo() -> bool:
        """
            Verifica se a conexão está ou não
        efetuada com sucesso

        Returns:
            bool
        """
        try:
            mongo = Mongo()
            client = mongo.client()
            buildinfo = await client.command("buildinfo")
            return bool(buildinfo["ok"])
        except Exception:
            return False
