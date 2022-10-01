from project.domain.lifecheck.validations.validation import ValidateHelth
from project.infrastructure.constants.health_check_status import Status
from project.infrastructure.constants.health_check_status import Health


def test_get_api_status_danger():
    list_status = [Status.RED, Status.RED, Status.RED, Status.RED, ]
    api_status = ValidateHelth().validate_general_status(list_status)
    assert api_status == "danger"


def test_get_api_status_warning():
    list_status = [Status.GREEN, Status.RED, Status.RED, Status.RED, ]
    api_status = ValidateHelth().validate_general_status(list_status)
    assert api_status == "warning"
