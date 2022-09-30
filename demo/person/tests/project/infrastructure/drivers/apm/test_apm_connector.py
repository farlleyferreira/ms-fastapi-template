
import pytest
from project.infrastructure.drivers.apm.adapter import Apm


def test_apm_connection_success():
    apm = Apm()
    if not apm.client():
        raise AssertionError


def test_apm_connection_error():
    apm = Apm()
    apm.apm_config = {}

    if not pytest.raises(Exception, apm.client):
        raise AssertionError
