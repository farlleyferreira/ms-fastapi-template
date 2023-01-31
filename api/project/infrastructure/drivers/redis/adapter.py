from project.infrastructure.drivers.redis.connector import Redis


class RedisAdapter(Redis):
    """
    Redis adapter class
    """

    def __init__(self) -> None:
        super().__init__()

    def get_buildinfo(self) -> bool:
        """
            Verifica se a conexão está ou não
        efetuada com sucesso

        Returns:
            bool
        """
        client = self.client()
        ping = client.ping()
        return True if ping else False
