from msilib.schema import Class


from project.infrastructure.constants.health_check_status import Status

class ValidationLifeCheck:
    
    def __init__(self) -> None:
        pass

    def validate_status(self, status: bool) -> Status:
        return Status.GREEN if status else Status.RED