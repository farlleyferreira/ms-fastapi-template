from elasticsearch.client import Elasticsearch
from project.infrastructure.drivers.elasticsearch.connector import Elk


class ElkAdapter:

    @staticmethod
    def get_client() -> Elasticsearch:
        """
            Instancia um client de conexão entre a
        aplicação e o elasticsearch

        Returns:
            Elasticsearch
        """
        elk = Elk()
        return elk.client()

    @staticmethod
    def get_buildinfo() -> bool:
        """
            Verifica se a conexão está ou não
        efetuada com sucesso

        Returns:
            bool
        """
        elk = Elk()
        client: Elasticsearch = elk.client()
        return client.ping()
