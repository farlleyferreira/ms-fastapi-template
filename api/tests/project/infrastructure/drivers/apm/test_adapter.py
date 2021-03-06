import pytest

from elasticapm.base import Client
from project.infrastructure.drivers.apm.adapter import ApmAdapter


def test_apm_connection_success():
    """
        when: Crio uma conexão com o Apm
        Then: Obtenho um client
    """
    client = ApmAdapter.get_client
    assert type(client()) == type(Client())
