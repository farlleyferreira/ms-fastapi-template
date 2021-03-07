from project.infrastructure.drivers.redis.connector import Redis


class RedisAdapter:

    @staticmethod
    def get_database():
        """
            Instancia um client de conexão entre a
        aplicação e o Redis

        Returns:
            Redis
        """
        redis = Redis()
        return redis.client()

    @staticmethod
    def get_buildinfo() -> bool:
        """
            Verifica se a conexão está ou não
        efetuada com sucesso

        Returns:
            bool
        """
        redis = Redis()
        client = redis.client()
        if client.ping():
            return True
        return False
