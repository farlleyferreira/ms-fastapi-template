from project.repositories.lifecheck.business_rules.health_status import Lifecheck
from project.infrastructure.constants.Enumerators import SystemStatus as status
from project.infrastructure.constants.Enumerators import ApiHealth as health

life_check = Lifecheck({})


def test_get_api_status_danger():
    list_status = [status.RED, status.RED, status.RED, status.RED, ]
    api_status = life_check.get_api_status(list_status)
    assert api_status == health.danger.value


def test_get_api_status_warning():
    list_status = [status.GREEN, status.RED, status.RED, status.RED, ]
    api_status = life_check.get_api_status(list_status)
    assert api_status == health.warning.value
