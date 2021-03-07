from project.infrastructure.drivers.apm.connector import Apm


class ApmAdapter:

    @staticmethod
    def get_client():
        """
            Instancia um client de conexão entre a
        aplicação e o elasticsearch apm

        Returns:
            [elasticapm.Client]
        """
        apm = Apm()
        client = apm.client()
        return client
