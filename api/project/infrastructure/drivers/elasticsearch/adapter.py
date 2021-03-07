from elasticsearch.client import Elasticsearch
from project.infrastructure.drivers.elasticsearch.connector import Elk


class ElkAdapter:

    @staticmethod
    def get_client() -> Elasticsearch:
        elk = Elk()
        return elk.client()

    @staticmethod
    def get_buildinfo() -> bool:
        elk = Elk()
        client: Elasticsearch = elk.client()
        return client.ping()
