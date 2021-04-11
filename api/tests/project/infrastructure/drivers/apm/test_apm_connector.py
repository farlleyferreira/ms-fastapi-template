
import pytest
from project.infrastructure.drivers.apm.adapter import Apm


def test_apm_connection_success():
    apm = Apm()
    assert apm.client()


def test_apm_connection_error():
    apm = Apm()
    apm.apm_config = {}

    assert pytest.raises(Exception, apm.client)
