from project.repositories.lifecheck.business_rules.health_status import Lifecheck
from project.infrastructure.constants.health_check_status import Status
from project.infrastructure.constants.health_check_status import Health

life_check = Lifecheck({})


def test_get_api_status_danger():
    list_status = [Status.RED, Status.RED, Status.RED, Status.RED, ]
    api_status = life_check.get_api_status(list_status)
    assert api_status == Health.danger.value


def test_get_api_status_warning():
    list_status = [Status.GREEN, Status.RED, Status.RED, Status.RED, ]
    api_status = life_check.get_api_status(list_status)
    assert api_status == Health.warning.value
