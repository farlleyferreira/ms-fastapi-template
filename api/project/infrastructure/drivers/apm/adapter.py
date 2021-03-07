from project.infrastructure.drivers.apm.connector import Apm


class ApmAdapter:

    @staticmethod
    def get_client():
        apm = Apm()
        client = apm.client()
        return client
