
from bson.objectid import ObjectId
from pymongo.results import UpdateResult
from project.infrastructure.drivers.mongo.adapter import MongoAdapter


class DataLayer(MongoAdapter):

    def __init__(self, collection: str) -> None:
        """
            Generic access data layer to MongoDB
        """
        super().__init__()
        self.collection = collection

    def get_collection(self):
        """
        Returns:
            Collection: returns a collection instance
        """
        database = self.client()
        collection = database[self.collection]
        return collection

    async def get_by_id(self, _id: ObjectId):
        """
        Args:
            _id (ObjectId): Id of document

        Returns:
            object_result (Document)
        """
        collection = self.get_collection()
        object_result = await collection.find_one({"_id": _id})
        return object_result

    async def get_by_filter(self, _filter: dict):
        """
        Args:
            _filter (dict): dict of parameters to filter find method

        Returns:
            object_result (List[Document]))
        """
        collection = self.get_collection()
        cursor = collection.find(_filter)
        object_result = await cursor.to_list(None)
        await cursor.close()
        return object_result

    async def save(self, _object: dict):
        """
        Args:
            _object (dict): the object that will be saved

        Returns:
           object_result (Document)
        """
        collection = self.get_collection()
        save_result = await collection.insert_one(_object)
        object_result = await self.get_by_id(save_result.inserted_id)
        return object_result

    async def update(self, criteria: dict, _object: dict) -> UpdateResult:
        """
        Args:
            criteria (dict): criteria by which the object(s) will be updated
            _object (dict): the parameters that will be updated

        Returns:
            object_result (UpdateResult)
        """
        collection = self.get_collection()
        object_result = await collection.update_one(criteria, {'$set': _object})
        return object_result

    async def delete(self, criteria: dict):
        """[summary]

        Args:
            criteria (dict): criteria by which the object(s) will be deleted

        Returns:
            object_result (DeleteResult)
        """
        collection = self.get_collection()
        object_result = await collection.delete_many(criteria)
        return object_result
