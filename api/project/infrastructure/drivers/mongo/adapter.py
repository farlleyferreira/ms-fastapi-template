from project.helpers.pydantic_typo import ObjectId
from project.infrastructure.drivers.mongo.connector import Mongo
from project.infrastructure.data_layer.abstract_datalayer import AbstractDataLayer


class MongoAdapter(AbstractDataLayer):
    """
    Mongo adapter class
    """

    def __init__(self, resource_name: str) -> None:
        self.resource_name = resource_name
        super().__init__(resource_name=resource_name)

    async def get_buildinfo(self) -> bool:
        client = Mongo().client()
        buildinfo = await client.command("buildinfo")
        return bool(buildinfo["ok"])

    async def get_one(self, id: ObjectId) -> dict:

        client = Mongo().client()
        result = await client[self.resource_name].find_one({"_id": id})
        if not result:
            raise Exception("document not found!")
        return result

    async def get_many(self, filter, *args: any, **kwargs: any) -> dict:

        client = Mongo().client()
        cursor = client[self.resource_name].find(filter=filter)
        result = await cursor.to_list(None)
        await cursor.close()

        if not result:
            raise Exception("result not found!")

        return result

    async def insert_one(self, item: dict) -> ObjectId:
        try:
            client = Mongo().client()
            result = await client[self.resource_name].insert_one(item)
            return result.inserted_id
        except Exception as error:
            raise error

    async def insert_many(self, itens: list[dict]) -> list[ObjectId]:
        try:
            client = Mongo().client()
            result = await client[self.resource_name].insert_many(itens)
            return result.inserted_ids
        except Exception as error:
            raise error

    async def update_one(self, id: ObjectId, data: dict) -> tuple:
        try:
            client = Mongo().client()
            result = await client[self.resource_name].update_one(
                {"_id": id}, {"$set": data}
            )
            acknowledged, modified_count = result.acknowledged, result.modified_count
            return acknowledged, modified_count
        except Exception as error:
            raise error

    async def update_many(self, criteria: dict, data: dict) -> tuple:
        try:
            client = Mongo().client()
            result = await client[self.resource_name].update_many(
                criteria, {"$set": data}
            )
            acknowledged, modified_count = result.acknowledged, result.modified_count
            return acknowledged, modified_count
        except Exception as error:
            raise error

    async def delete(self, criteria: dict) -> tuple:
        try:
            client = Mongo().client()
            result = await client[self.resource_name].delete_many(criteria)
            acknowledged, deleted_count = result.acknowledged, result.deleted_count
            return acknowledged, deleted_count
        except Exception as error:
            raise error
