from elasticsearch.client import Elasticsearch
from project.infrastructure.drivers.elasticsearch.connector import Elk


class ElkAdapter(Elk):
    """
    Elk adapter class
    """

    def __init__(self) -> None:
        super().__init__()

    def elk_client(self, index: str):
        pass

    def get_buildinfo(self) -> bool:
        """
            Verifica se a conexão está ou não
        efetuada com sucesso

        Returns:
            bool
        """
        client: Elasticsearch = self.client()
        ping_result = client.ping()
        return ping_result
