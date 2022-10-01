from datetime import datetime
from pydantic import BaseModel
from project.infrastructure.constants.health_check_status import Status


class Details(BaseModel):
    rabbit_mq_status: Status
    mongo_status: Status
    redis_status: Status
    elk_status: Status


class LifeStatus(BaseModel):
    aplication_message: str
    aplication_name: str
    response_at: datetime
    api_status: Status
    referer: str
    details: Details
