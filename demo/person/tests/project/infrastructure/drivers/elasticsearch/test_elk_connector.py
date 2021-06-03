
import pytest
from project.infrastructure.drivers.elasticsearch.connector import Elk


def test_elk_connection_success():
    elk = Elk()
    if not elk.client():
        raise AssertionError


def test_elk_connection_error():
    elk = Elk()
    elk.elasticsearch_config = {"unknow": ""}

    if not pytest.raises(Exception, elk.client):
        raise AssertionError
