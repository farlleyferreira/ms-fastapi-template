from elasticsearch.client import Elasticsearch
from project.infrastructure.drivers.elasticsearch.connector import Elk


class ElkAdapter(Elk):
    """
        Elk adapter class
    """

    def __init__(self) -> None:
        super().__init__()

    def get_buildinfo(self) -> bool:
        """
            Verifica se a conexão está ou não
        efetuada com sucesso

        Returns:
            bool
        """
        client: Elasticsearch = self.client()
        return client.ping()
