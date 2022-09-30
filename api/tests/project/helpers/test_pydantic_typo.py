import pytest
from project.helpers.pydantic_typo import MongoId

from dotenv import load_dotenv

load_dotenv()


def test_mongo_id_instance():
    mongo_id = MongoId()
    if not MongoId().validate(str(mongo_id)):
        raise AssertionError


def test_mongo_id_instance_error():
    with pytest.raises(ValueError):
        MongoId().validate(True)
