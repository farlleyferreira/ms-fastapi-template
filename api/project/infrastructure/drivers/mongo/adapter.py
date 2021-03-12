from project.infrastructure.drivers.mongo.connector import Mongo


class MongoAdapter(Mongo):

    def __init__(self) -> None:
        super().__init__()

    async def get_buildinfo(self) -> bool:
        """
            Verifica se a conexão está ou não
        efetuada com sucesso

        Returns:
            bool
        """
        try:
            client = self.client()
            buildinfo = await client.command("buildinfo")
            return bool(buildinfo["ok"])
        except Exception:
            return False
