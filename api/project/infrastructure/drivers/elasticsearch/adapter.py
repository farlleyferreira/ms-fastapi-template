import secrets
from elasticsearch.client import Elasticsearch
from bson.objectid import ObjectId
from project.infrastructure.drivers.elasticsearch.connector import Elk
from project.infrastructure.data_layer.abstract_datalayer import AbstractDataLayer


class ElkAdapter(AbstractDataLayer):
    """
    Elk adapter class
    """

    def __init__(self, resource_name: str) -> None:
        self.resource_name: str = resource_name
        super().__init__(resource_name=resource_name)

    def get_buildinfo(self) -> bool:
        client: Elasticsearch = Elk().client()
        ping_result = client.ping()
        return ping_result

    async def get_one(self, id: str) -> dict:
        try:
            client: Elasticsearch = Elk().client()
            result = client.get(index=self.resource_name, id=id)

            if "_source" in result and result["_source"]:
                return result["_source"]

            raise Exception("Item not found")

        except Exception as error:
            raise error

    async def get_many(self, filter) -> list[dict]:
        try:
            client: Elasticsearch = Elk().client()
            result = client.search(index=self.resource_name, body=filter)

            if result["_shards"]["failed"] > 0:
                raise Exception("Item not found")

            hits = result["hits"]["hits"]
            list_of_results = [hit["_source"] for hit in hits]
            return list_of_results

        except Exception as error:
            raise error

    async def insert_one(self, item) -> str:
        try:
            client: Elasticsearch = Elk().client()
            new_id = ObjectId(secrets.token_hex(12))
            result = client.index(index=self.resource_name, id=new_id, body=item)
            if result["_shards"]["failed"] > 0:
                raise Exception("Document cannot be indexed")
            result_id = ObjectId(result["_id"])
            return result_id
        except Exception as error:
            raise error

    async def insert_many(self, itens: list[dict]) -> list[str]:
        try:
            actions: list = []
            ids: list = []
            for item in itens:
                new_id = ObjectId(secrets.token_hex(12))
                action = {"index": {"_index": self.resource_name, "_id": str(new_id)}}

                actions.append(action)
                actions.append(item)
                ids.append(new_id)

            client: Elasticsearch = Elk().client()
            result = client.bulk(index=self.resource_name, body=actions)

            if result["errors"]:
                raise Exception("Document cannot be indexed")

            return ids
        except Exception as error:
            raise error

    async def update_one(self, id: ObjectId, data: dict) -> tuple:
        try:
            client: Elasticsearch = Elk().client()
            new_id = str(id)
            result = client.update(
                index=self.resource_name, id=new_id, body={"doc": data}
            )

            if result["_shards"]["failed"] > 0:
                raise Exception("Document cannot be indexed")
            acknowledged, modified_count = True, result["_shards"]["successful"]
            return acknowledged, modified_count
        except Exception as error:
            raise error

    async def update_many(self, criteria: dict, data: dict) -> tuple:
        try:
            actions: list = []

            client: Elasticsearch = Elk().client()
            result_search = client.search(index=self.resource_name, body=criteria)

            if result_search["_shards"]["failed"] > 0:
                raise Exception("Item not found")

            hits = result_search["hits"]["hits"]

            for item in hits:
                action = {"update": {"_index": self.resource_name, "_id": item["_id"]}}

                actions.append(action)
                actions.append({"doc": data})

            result = client.bulk(index=self.resource_name, body=actions)

            if result["errors"]:
                raise Exception("Document cannot be indexed")

            acknowledged, modified_count = True, len(result["items"])
            return acknowledged, modified_count

        except Exception as error:
            raise error

    async def delete(self, criteria: dict) -> tuple:
        client: Elasticsearch = Elk().client()
        pass
