from project.infrastructure.drivers.mongo.connector import Mongo


class MongoAdapter:

    @staticmethod
    def get_database():
        mongo = Mongo()
        return mongo.client()

    @staticmethod
    def get_collection(collection: str):
        mongo = Mongo()
        client = mongo.client()
        return client[collection]

    @staticmethod
    async def get_buildinfo() -> bool:
        try:
            mongo = Mongo()
            client = mongo.client()
            buildinfo = await client.command("buildinfo")
            return bool(buildinfo["ok"])
        except Exception:
            return False
