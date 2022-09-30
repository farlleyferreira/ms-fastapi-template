

from project.infrastructure.constants.health_check_status import Status

class ValidationLifeCheck:

    def __init__(self) -> None:
        raise NotImplementedError()

    @staticmethod
    def validate_status(status: bool) -> Status:
        return Status.GREEN if status else Status.RED
