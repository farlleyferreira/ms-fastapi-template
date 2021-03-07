from project.infrastructure.drivers.redis.connector import Redis


class RedisAdapter:

    @staticmethod
    def get_database():
        redis = Redis()
        return redis.client()

    @staticmethod
    def get_buildinfo() -> bool:
        redis = Redis()
        client = redis.client()
        if client.ping():
            return True
        return False
