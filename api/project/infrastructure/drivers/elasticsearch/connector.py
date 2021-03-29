from elasticsearch import Elasticsearch
from project.infrastructure.environments.loader import Configs
from project.infrastructure.monitoring_layer.aplication_general_log import Log
from project.infrastructure.monitoring_layer.aplication_kpi import Monitor
import sys


log = Log()


class Elk:

    def __init__(self) -> None:
        """
            Na inicialização da classe de conexão com o elasticsearch,
        as configurações de ambiente são carregadas em tempo de execução,
        e servidas sob o contexto da instancia.
        """
        self.elasticsearch_config = Configs.get_by_key("elk")

    def client(self) -> Elasticsearch:
        """
            Cria uma conexão com o elasticsearch

        Raises:
            error: Exception

        Returns:
            Elasticsearch
        """
        try:

            hosts = self.elasticsearch_config["hosts"]
            username = self.elasticsearch_config["username"]
            password = self.elasticsearch_config["password"]

            client = Elasticsearch(
                hosts=hosts,
                http_auth=(username, password)
            )

            return client

        except Exception as error:

            log.record.error(
                "ELK connection error, check your server and credentials",
                exc_info=sys.exc_info()
            )
            Monitor.send_kpi_message("elk client error")

            raise error
