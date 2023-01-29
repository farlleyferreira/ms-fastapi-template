from project.domain.lifecheck.validations.validation import ValidateHelth
from project.infrastructure.constants.health_check_status import Status
from project.infrastructure.constants.health_check_status import Health


def test_get_api_status_danger():
    list_status = [Status.RED, Status.RED, Status.RED, Status.RED, ]
    api_status = ValidateHelth().general_status(list_status)

    result_status, result_message = api_status
    expected_result_status, expected_result_message = Health.danger.value
    assert result_status == expected_result_status and result_message == expected_result_message    


def test_get_api_status_warning():
    list_status = [Status.GREEN, Status.RED, Status.RED, Status.RED, ]
    api_status = ValidateHelth().general_status(list_status)
    
    result_status, result_message = api_status
    expected_result_status, expected_result_message = Health.warning.value
    assert result_status == expected_result_status and result_message == expected_result_message
