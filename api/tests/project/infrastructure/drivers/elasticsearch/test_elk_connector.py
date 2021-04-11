
import pytest
from project.infrastructure.drivers.elasticsearch.connector import Elk


def test_elk_connection_success():
    elk = Elk()
    assert elk.client()


def test_elk_connection_error():
    elk = Elk()
    elk.elasticsearch_config = {"unknow": ""}

    assert pytest.raises(Exception, elk.client)
