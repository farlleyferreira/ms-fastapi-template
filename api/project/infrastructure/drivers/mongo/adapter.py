from typing import Any
from project.infrastructure.drivers.mongo.connector import Mongo


class MongoAdapter:

    @staticmethod
    def get_database() -> any:
        mongo = Mongo()
        return mongo.client()

    @staticmethod
    def get_collection(collection: str) -> any:
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
