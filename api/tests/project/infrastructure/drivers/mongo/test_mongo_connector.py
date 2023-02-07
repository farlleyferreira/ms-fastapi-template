import pytest
from motor.motor_asyncio import AsyncIOMotorDatabase
from project.infrastructure.drivers.mongo.connector import Mongo


def test_mongo_connection_success():
    mongo = Mongo()
    client = mongo.client()
    if type(client) != AsyncIOMotorDatabase:
        raise AssertionError


def test_mongo_connection_error():
    mongo = Mongo()
    mongo.host = ""
    mongo.username = ""

    if not pytest.raises(Exception, mongo.client):
        raise AssertionError
