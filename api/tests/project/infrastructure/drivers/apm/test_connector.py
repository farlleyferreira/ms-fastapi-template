
import pytest

from elasticapm.base import Client
from project.infrastructure.drivers.apm.adapter import Apm


def test_apm_connection_success():
    """
        when: Crio uma conexão com o Apm
        Then: Obtenho sucesso
    """
    apm = Apm()
    client = apm.client
    assert type(client()) == type(Client())


def test_apm_connection_error():
    """
        when: Crio uma conexão com o Apm
        Then: Obtenho falha
    """
    apm = Apm()
    apm.apm_config = ""
    client = apm.client

    assert type(client) != type(Client())
    assert pytest.raises(Exception, client)
