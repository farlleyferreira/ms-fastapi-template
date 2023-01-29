from project.domain.lifecheck.validations.status import ValidateHelth
from project.infrastructure.constants.health_check_status import Status, Health


def test_check_specific_status():
    result_green = ValidateHelth().specific_status(True)
    result_red = ValidateHelth().specific_status(False)
    assert result_green == Status.GREEN
    assert result_red == Status.RED


def test_check_general_status():
    result_success = ValidateHelth().general_status([Status.GREEN])
    result_warning = ValidateHelth().general_status([Status.GREEN, Status.RED])
    result_danger = ValidateHelth().general_status([Status.RED])

    assert result_success == Health.success.value
    assert result_warning == Health.warning.value
    assert result_danger == Health.danger.value
