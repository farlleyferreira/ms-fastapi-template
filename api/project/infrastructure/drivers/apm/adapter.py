from project.infrastructure.drivers.apm.connector import Apm


class ApmAdapter(Apm):
    """
    Apm adapter class
    """

    def __init__(self) -> None:
        super().__init__()
