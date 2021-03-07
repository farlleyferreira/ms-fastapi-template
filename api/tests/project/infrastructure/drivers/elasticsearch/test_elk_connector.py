
import pytest
from project.infrastructure.drivers.elasticsearch.connector import Elk


def test_elk_connection_success():
    """
        when: Crio uma conexão com o Apm
        Then: Obtenho sucesso
    """
    elk = Elk()
    assert elk.client()


def test_elk_connection_error():
    """
        when: Crio uma conexão com o Apm
        Then: Obtenho falha
    """
    elk = Elk()
    elk.elasticsearch_config = {"unknow": ""}

    assert pytest.raises(Exception, elk.client)
