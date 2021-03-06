from project.infrastructure.drivers.redis.connector import Redis


class RedisAdapter:

    @staticmethod
    def get_database() -> Redis:
        redis = Redis()
        return redis.client()

    @staticmethod
    def get_buildinfo() -> bool:
        try:
            redis = Redis()
            client: Redis = redis.client()
            return client.ping()
        except Exception:
            return False
