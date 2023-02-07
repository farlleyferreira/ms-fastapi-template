import pytest
import asyncio
from motor.motor_asyncio import AsyncIOMotorDatabase
from project.infrastructure.drivers.mongo.connector import Mongo


def test_mongo_connection_success():
    mongo = Mongo()
    client = mongo.client()
    assert type(client) == AsyncIOMotorDatabase


def test_mongo_connection_error():
    mongo = Mongo()
    mongo.host = ""
    mongo.username = ""

    assert pytest.raises(Exception, mongo.client)
