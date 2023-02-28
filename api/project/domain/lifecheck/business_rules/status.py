from datetime import datetime
from project.infrastructure.drivers.redis.adapter import RedisAdapter
from project.infrastructure.drivers.rabbitmq.adapter import RabbitMqAdapter
from project.infrastructure.drivers.elasticsearch.adapter import ElkAdapter

from project.domain.lifecheck.repositories.model_status import LifeStatus, Details
from project.domain.lifecheck.validations.status import ValidateHelth


from project.infrastructure.data_layer.concrete_datalayer import DataLayer


class Lifecheck(object):
    def __init__(self, request_headers):
        self.request_headers = request_headers

    async def get_life_status(self) -> LifeStatus:

        validate = ValidateHelth()

        mongo_result = await self.get_mongo_database_status()
        queue_status = await self.get_queue_status()
        mdb_result = await self.get_redis_database_status()
        elk_result = await self.get_elk_database_status()

        mongo_status = validate.specific_status(mongo_result)
        queue_status = validate.specific_status(queue_status)
        redis_status = validate.specific_status(mdb_result)
        elk_status = validate.specific_status(elk_result)

        api_status, api_message = validate.general_status(
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

    async def get_redis_database_status(self) -> bool:
        is_ok_database = RedisAdapter().get_buildinfo()
        return is_ok_database

    async def get_elk_database_status(self) -> bool:
        is_ok_database = ElkAdapter(resource_name="teste").get_buildinfo()
        return is_ok_database

    async def get_mongo_database_status(self) -> bool:
        is_ok_database = await DataLayer(technology="mongo").get_buildinfo()
        return is_ok_database

    async def get_queue_status(self) -> bool:
        is_ok_queue = await RabbitMqAdapter().get_buildinfo()
        return is_ok_queue
