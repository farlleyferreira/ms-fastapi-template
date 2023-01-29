from project.infrastructure.drivers.mongo.adapter import MongoAdapter
from project.infrastructure.drivers.elasticsearch.adapter import ElkAdapter


class DataLayer(object):

    def __init__(self, database_type: str = 'mongo') -> None:
        super().__init__()
        self.database_type: str = database_type
        

    def get_client(self, resource_name: str) -> MongoAdapter | None:
        if self.database_type == 'elasticsearch':
            return None
        return MongoAdapter(resource_name)
