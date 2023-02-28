from elasticsearch import Elasticsearch

from project.infrastructure.monitoring_layer.aplication_general_log import Log
import sys
import os
import json

log = Log()


class Elk(object):
    def __init__(self) -> None:
        self.hosts = os.getenv("ELK_HOSTS")
        self.username = os.getenv("ELK_USERNAME")
        self.password = os.getenv("ELK_PASSWORD")

    def client(self) -> Elasticsearch:
        try:

            hosts = json.loads(str(self.hosts))
            username = self.username
            password = self.password

            client = Elasticsearch(hosts=hosts, http_auth=(username, password))

            return client

        except Exception as error:

            log.record.error(
                "ELK connection error, check your server and credentials",
                exc_info=sys.exc_info(),
            )
            raise error
