
from datetime import datetime

from project.infrastructure.constants.Enumerators import SystemStatus as status
from project.infrastructure.constants.Enumerators import ApiHealth as health

from project.infrastructure.drivers.mongo.adapter import MongoAdapter
from project.infrastructure.drivers.redis.adapter import RedisAdapter
from project.infrastructure.drivers.rabbitmq.adapter import RabbitMqAdapter
from project.infrastructure.drivers.elasticsearch.adapter import ElkAdapter


class Lifecheck:
    """[summary]
    """

    def __init__(self, request_headers):
        self.request_headers = request_headers

    async def get_life_status(self):
        """[summary]

        Returns:
            [type]: [description]
        """

        mongo_status = await self.get_mongo_database_status()
        redis_status = await self.get_redis_database_status()
        queue_status = await self.get_queue_status()
        elk_status = await self.get_elk_database_status()

        api_status, api_message = self.get_api_status([
            mongo_status,
            queue_status,
            redis_status,
            elk_status
        ])

        referer = self.request_headers["Referer"] if 'Referer' in self.request_headers else ""

        return {
            "aplication_message": api_message,
            "aplication_name": "FastApi microservice template",
            "response_at": datetime.now(),
            "api_status": api_status,
            "referer": referer,
            "details": {
                "rabbit_mq_status": queue_status,
                "mongo_status": mongo_status,
                "redis_status": redis_status,
                "elk_status": elk_status,
            }
        }

    def get_api_status(self, aplication_status: list):
        """[summary]

        Args:
            aplication_status (list): [description]

        Returns:
            [type]: [description]
        """

        is_ok = all(
            _status == status.GREEN for _status in aplication_status
        )

        its_danger = all(
            _status == status.RED for _status in aplication_status[0:2]
        )

        if is_ok:
            return health.success.value
        elif not is_ok and not its_danger:
            return health.warning.value
        else:
            return health.danger.value

    async def get_mongo_database_status(self):
        """[summary]

        Returns:
            Literal: [description]
        """
        is_ok_database = await MongoAdapter.get_buildinfo()
        return status.GREEN if is_ok_database else status.RED

    async def get_redis_database_status(self):
        """[summary]

        Returns:
            Literal: [description]
        """
        is_ok_database = RedisAdapter.get_buildinfo()
        return status.GREEN if is_ok_database else status.RED

    async def get_elk_database_status(self):
        """[summary]

        Returns:
            Literal: [description]
        """
        is_ok_database = ElkAdapter.get_buildinfo()
        return status.GREEN if is_ok_database else status.RED

    async def get_queue_status(self):
        """[summary]

        Returns:
            Literal: [description]
        """
        is_ok_queue = await RabbitMqAdapter.get_buildinfo()
        return status.GREEN if is_ok_queue else status.RED
