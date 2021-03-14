
import pytest
from project.infrastructure.drivers.apm.adapter import Apm


def test_apm_connection_success():
    """
        when: Crio uma conexão com o Apm
        Then: Obtenho sucesso
    """
    apm = Apm()
    assert apm.client()


def test_apm_connection_error():
    """
        when: Crio uma conexão com o Apm
        Then: Obtenho falha
    """
    apm = Apm()
    apm.apm_config = {}

    assert pytest.raises(Exception, apm.client)
