from project.infrastructure.drivers.mongo.adapter import MongoAdapter
from project.infrastructure.drivers.elasticsearch.adapter import ElkAdapter


class DataLayer:
    def __init__(self, technology: str = "mongo", resource_name="healthcheck") -> None:

        if technology == "elasticsearch":
            self.instance = object
        elif technology == "mongo":
            self.instance = MongoAdapter(resource_name)
        else:
            self.instance = object

    def __getattr__(self, name):
        return self.instance.__getattribute__(name)
