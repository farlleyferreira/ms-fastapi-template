from datetime import datetime
from project.infrastructure.drivers.mongo.adapter import MongoAdapter
from project.infrastructure.drivers.redis.adapter import RedisAdapter
from project.infrastructure.drivers.rabbitmq.adapter import RabbitMqAdapter
from project.infrastructure.drivers.elasticsearch.adapter import ElkAdapter

from project.domain.lifecheck.repositories.repository import LifeStatus, Details
from project.domain.lifecheck.validations.validation import ValidateHelth


class Lifecheck(object):
    def __init__(self, request_headers):
        """
        Regras de negocio para o processo de verificação de status do projeto
        """
        self.request_headers = request_headers

    async def get_life_status(self) -> LifeStatus:
        validate = ValidateHelth()
        
        mongo_status = validate.validate_specific_status(
            await self.get_mongo_database_status()
        )
        queue_status = validate.validate_specific_status(await self.get_queue_status())
        redis_status = validate.validate_specific_status(
            self.get_redis_database_status()
        )
        elk_status = validate.validate_specific_status(self.get_elk_database_status())

        api_status, api_message = validate.validate_general_status(
            [mongo_status, queue_status, redis_status, elk_status]
        )

        referer = (
            self.request_headers["Referer"] if "Referer" in self.request_headers else ""
        )

        details = Details(
            rabbit_mq_status=queue_status,
            mongo_status=mongo_status,
            redis_status=redis_status,
            elk_status=elk_status,
        )

        life_status = LifeStatus(
            aplication_message=api_message,
            aplication_name="FastApi microservice template",
            response_at=datetime.now(),
            api_status=api_status,
            referer=referer,
            details=details,
        )

        return life_status

    @staticmethod
    def get_redis_database_status() -> bool:
        is_ok_database = RedisAdapter().get_buildinfo()
        return is_ok_database

    @staticmethod
    def get_elk_database_status() -> bool:
        is_ok_database = ElkAdapter().get_buildinfo()
        return is_ok_database

    @staticmethod
    async def get_mongo_database_status() -> bool:
        is_ok_database = await MongoAdapter().get_buildinfo()
        return is_ok_database

    @staticmethod
    async def get_queue_status() -> bool:
        is_ok_queue = await RabbitMqAdapter().get_buildinfo()
        return is_ok_queue
