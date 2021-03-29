from project.infrastructure.drivers.apm.adapter import ApmAdapter


class Monitor:

    @staticmethod
    def send_kpi_message(message: str) -> None:
        """
            Envia mensagem para o elastic APM

        Args:
            message: str
            body (str, optional): Caso desejar poderá ser enviado
            um objeto baseado no contexto da aplicação

        """
        client = ApmAdapter().client()
        client.capture_exception()
        client.capture_message(message)

    @ staticmethod
    def begin_transaction(name: str) -> None:
        """
            Inicia captura de transação

        Args:
            name (str): nome da transação
        """
        ApmAdapter().client().begin_transaction(name)

    @ staticmethod
    def end_transaction(name: str, status: str) -> None:
        """
            Finaliza captura de transação

        Args:
            name (str): nome da transação
            status (str): status da transação
        """
        ApmAdapter().client().end_transaction(name, status)
