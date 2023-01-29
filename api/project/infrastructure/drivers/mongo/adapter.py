from project.helpers.pydantic_typo import ObjectId
from project.infrastructure.drivers.mongo.connector import Mongo


class MongoAdapter(Mongo):
    """
    Mongo adapter class
    """

    def __init__(self, collection: str) -> None:
        super().__init__()
        self.collection = collection

    async def get_buildinfo(self) -> bool:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        client = self.client()
        buildinfo = await client.command("buildinfo")
        return bool(buildinfo["ok"])

    async def get_one(self, _id: ObjectId) -> object:
        """
        Args:
            _id (ObjectId): Id of document

        Returns:
            object_result (Document)
        """
        object_result = await self.client()[self.collection].find_one({"_id": _id})
        return object_result

    async def get_by_filter(self, filter: dict):
        """
        Args:
            filter (dict): dict of parameters to filter find method

        Returns:
            object_result (List[Document]))
        """
        cursor = self.client()[self.collection].find(_filter)
        result = await cursor.to_list(None)
        await cursor.close()
        return result

    async def insert_one(self, item: dict) -> str:
        """
        Args:
            item (dict): the object that will be saved

        Returns:
           object_result (Document)
        """
        result = await self.client()[self.collection].insert_one(item)
        return result.inserted_id

    async def insert_many(self, items: list[dict]) -> list[str]:
        """
        Args:
            items (dict): the object that will be saved

        Returns:
           object_result (Document)
        """
        result = await self.client()[self.collection].insert_many(items)
        return result.inserted_ids

    async def update_one(self, criteria: dict, data: dict):
        """
        Args:
            criteria (dict): the condition to update
            data (dict): the data that will be updated

        Returns:
           object_result (Document)
        """
        object_result = await self.client()[self.collection].update_one(
            criteria, {"$set": _object}
        )
        return object_result

    async def update_many(self, criteria: dict, data: dict):
        """
        Args:
            criteria (dict): the condition to update
            data (dict): the object that will be updated

        Returns:
           object_result (Document)
        """
        object_result = await self.client()[self.collection].update_many(
            criteria, {"$set": _object}
        )
        return object_result

    async def delete(self, criteria: dict):
        """[summary]

        Args:
            criteria (dict): criteria by which the object(s) will be deleted

        Returns:
            object_result (DeleteResult)
        """
        object_result = await self.client()[self.collection].delete_many(criteria)
        return object_result
