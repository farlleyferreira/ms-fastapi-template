from project.domain.lifecheck.business_rules.life_check import Lifecheck
from project.infrastructure.constants.health_check_status import Status
from project.infrastructure.constants.health_check_status import Health

life_check = Lifecheck({})


def test_get_api_status_danger():
    list_status = [Status.RED, Status.RED, Status.RED, Status.RED, ]
    api_status = life_check.get_api_status(list_status)
    if api_status != Health.danger.value:
        raise AssertionError


def test_get_api_status_warning():
    list_status = [Status.GREEN, Status.RED, Status.RED, Status.RED, ]
    api_status = life_check.get_api_status(list_status)
    if api_status != Health.warning.value:
        raise AssertionError
