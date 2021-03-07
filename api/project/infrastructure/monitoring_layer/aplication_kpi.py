from project.infrastructure.drivers.apm.adapter import ApmAdapter


class Monitor:
    """[summary]
    """

    @staticmethod
    def send_kpi_message(message: str, body: str = None) -> None:
        """[summary]

        Args:
            message (str): [description]
            body (str, optional): [description]. Defaults to None.
        """
        client = ApmAdapter.get_client()
        client.capture_message(
            param_message={
                'message': message,
                'params': body,
            }
        )

    @staticmethod
    def begin_transaction(name: str) -> None:
        """[summary]

        Args:
            name (str): [description]
        """
        ApmAdapter.get_client().begin_transaction(name)

    @staticmethod
    def end_transaction(name: str, status: str) -> None:
        """[summary]

        Args:
            name (str): [description]
            status (str): [description]
        """
        ApmAdapter.get_client().end_transaction(name, status)
