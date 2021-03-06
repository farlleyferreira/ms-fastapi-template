from project.infrastructure.drivers.apm.adapter import ApmAdapter


class Monitor:

    @staticmethod
    def send_kpi_message(message: str, body: any = {}) -> None:
        client = ApmAdapter.get_client()
        client.capture_message(
            param_message={
                'message': message,
                'params': body,
            }
        )

    @staticmethod
    def begin_transaction(name: str) -> None:
        ApmAdapter.get_client().begin_transaction(name)

    @staticmethod
    def end_transaction(name: str, status: str) -> None:
        ApmAdapter.get_client().end_transaction(name, status)
