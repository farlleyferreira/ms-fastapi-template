from project.infrastructure.drivers.apm.connector import Apm


class ApmAdapter(Apm):

    def __init__(self) -> None:
        super().__init__()
