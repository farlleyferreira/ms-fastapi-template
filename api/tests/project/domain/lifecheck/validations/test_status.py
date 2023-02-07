from project.domain.lifecheck.validations.status import ValidateHelth
from project.infrastructure.constants.health_check_status import Status, Health


def test_check_specific_status():
    result_green = ValidateHelth().specific_status(True)
    result_red = ValidateHelth().specific_status(False)
    if result_green != Status.GREEN:
        raise AssertionError
    if result_red != Status.RED:
        raise AssertionError


def test_check_general_status():
    result_success = ValidateHelth().general_status([Status.GREEN])
    result_warning = ValidateHelth().general_status([Status.GREEN, Status.RED])
    result_danger = ValidateHelth().general_status([Status.RED])

    if result_success != Health.success.value:
        raise AssertionError
    if result_warning != Health.warning.value:
        raise AssertionError
    if result_danger != Health.danger.value:
        raise AssertionError
