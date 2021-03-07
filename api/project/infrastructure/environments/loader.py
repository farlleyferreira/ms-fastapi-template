import errno
from os import path, strerror
from project.infrastructure.monitoring_layer.aplication_general_log import Log
import yaml


log = Log()


class Configs:

    @staticmethod
    def get_by_key(key) -> dict:

        try:
            config_path = "./project/infrastructure/environments/config.yaml"

            path_exists = path.exists(config_path)

            if not path_exists:

                raise FileNotFoundError(
                    errno.ENOENT,
                    strerror(errno.ENOENT),
                    config_path
                )

            config = open(config_path)
            config_dict = yaml.load(config, Loader=yaml.FullLoader)
            environments = config_dict["environments"]
            return environments[key] if key in environments else {}

        except Exception as error:
            log.record.error(
                "MongoDB connection error, check your server and credentials",
                exc_info=error
            )
            raise error
