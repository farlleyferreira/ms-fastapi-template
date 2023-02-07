from abc import ABC, abstractmethod
from project.helpers.pydantic_typo import ObjectId


class AbstractDataLayer(ABC):  # pragma: no cover
    def __init__(self, resource_name: str):
        self.resource_name: str = resource_name
        super().__init__()

    @abstractmethod
    async def get_buildinfo(self) -> bool:
        pass

    @abstractmethod
    async def get_one(self, id: ObjectId) -> dict:
        pass

    @abstractmethod
    async def get_one(self, filter, *args: any, **kwargs: any) -> dict:
        pass

    @abstractmethod
    async def insert_one(self, item) -> ObjectId:
        pass

    @abstractmethod
    async def insert_one(self, item) -> ObjectId:
        pass

    @abstractmethod
    async def insert_many(self, itens: list[dict]) -> list[ObjectId]:
        pass

    @abstractmethod
    async def update_one(self, criteria: dict, data: dict) -> tuple:
        pass

    @abstractmethod
    async def update_many(self, criteria: dict, data: dict) -> tuple:
        pass

    @abstractmethod
    async def delete(self, criteria: dict) -> tuple:
        pass
