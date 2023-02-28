import pytest
from elasticsearch import Elasticsearch
from project.infrastructure.drivers.elasticsearch.connector import Elk


def test_elk_connection_success():
    elk = Elk()
    client = elk.client()
    if type(client) != Elasticsearch:
        raise AssertionError


def test_elk_connection_error():
    elk = Elk()
    elk.hosts = {"elk": Exception()}
    elk.username = ""

    if not pytest.raises(Exception, elk.client):
        raise AssertionError
