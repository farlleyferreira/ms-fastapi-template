
from bson.objectid import ObjectId
from pymongo.results import UpdateResult
from project.infrastructure.drivers.mongo.adapter import MongoAdapter


class DataLayer(MongoAdapter):

    def __init__(self, collection: str) -> None:
        super().__init__()
        self.collection = collection

    def get_collection(self):
        database = self.client()
        collection = database[self.collection]
        return collection

    async def get_by_id(self, _id: ObjectId):
        collection = self.get_collection()
        object_result = await collection.find_one({"_id": _id})
        return object_result

    async def get_by_filter(self, _filter: dict):
        collection = self.get_collection()
        cursor = collection.find(_filter)
        object_result = await cursor.to_list(None)
        await cursor.close()
        return object_result

    async def save(self, _object: dict):
        collection = self.get_collection()
        save_result = await collection.insert_one(_object)
        object_result = await self.get_by_id(save_result.inserted_id)
        return object_result

    async def update(self, criteria: dict, _object: dict) -> UpdateResult:
        collection = self.get_collection()
        object_result = await collection.update_one(criteria, {'$set': _object})
        return object_result

    async def delete(self, criteria: dict):
        collection = self.get_collection()
        object_result = await collection.delete_many(criteria)
        return object_result
