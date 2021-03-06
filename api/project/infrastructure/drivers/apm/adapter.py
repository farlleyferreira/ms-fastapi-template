from elasticsearch.client import Elasticsearch
from project.infrastructure.drivers.apm.connector import Apm


class ApmAdapter:

    @staticmethod
    def get_client() -> object:
        apm = Apm()
        return apm.client()