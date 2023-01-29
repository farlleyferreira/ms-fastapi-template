from project.infrastructure.constants.health_check_status import Status, Health


class ValidateHelth(object):
    def __init__(self):
        super().__init__()

    def specific_status(self, is_ok_status: bool) -> Status:
        return Status.GREEN if is_ok_status else Status.RED

    def general_status(self, status_list: list[Status]) -> Status:

        is_ok = all(_status == Status.GREEN for _status in status_list)

        its_danger = all(_status == Status.RED for _status in status_list)

        if is_ok:
            return Health.success.value
        elif its_danger:
            return Health.danger.value
        else:
            return Health.warning.value
