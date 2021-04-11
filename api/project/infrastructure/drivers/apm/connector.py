import uuid
from elasticapm.base import Client
from project.infrastructure.environments.loader import Configs
from project.infrastructure.monitoring_layer.aplication_general_log import Log

log = Log()


class Apm(object):

    def __init__(self) -> None:
        """
            Na inicialização da classe de conexão com o apm,
        as configurações de ambiente são carregadas em tempo
        de execução, e servidas sob o contexto da instancia.
        """
        self.apm_config = Configs.get_by_key("apm")

    def client(self):
        """
            Cria uma conexão com o elastic apm

        Raises:
            error: Exception

        Returns:
            elasticapm.Client
        """
        try:
            server_url = self.apm_config["server_url"]
            service_name = self.apm_config["service_name"]
            environment = self.apm_config["environment"]

            settings = {
                'SERVICE_NAME': service_name,
                'SERVER_URL': server_url,
                'ENVIRONMENT': environment,
                'CAPTURE_BODY': 'all',
                'SECRET_TOKEN': str(uuid.uuid4()),
                'CAPTURE_HEADERS': True,
                'DEBUG': True,
                'COLLECT_LOCAL_VARIABLES': 'all',
                'ELASTIC_APM_AUTO_LOG_STACKS': True
            }

            client = Client(settings)
            return client

        except Exception as error:
            log.record.error(
                "Apm connection error, check your server and credentials",
                exc_info=error
            )
            raise error
