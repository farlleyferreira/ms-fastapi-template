from elasticsearch import Elasticsearch

from project.infrastructure.environments.loader import Configs
from project.infrastructure.monitoring_layer.aplication_general_log import Log
from project.infrastructure.monitoring_layer.aplication_kpi import Monitor

log = Log()


class Elk:

    def __init__(self) -> None:
        self.elasticsearch_config = Configs.get_by_key("elk")

    def client(self) -> Elasticsearch:
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

            Monitor.send_kpi_message("elk client error", str(error))
            log.record.error(
                "ELK connection error, check your server and credentials",
                exc_info=error
            )
            raise error
