import pytest
from project.helpers.pydantic_typo import MongoId

from dotenv import load_dotenv

load_dotenv()


def test_mongo_id_instance():
    mongo_id = MongoId()
    assert MongoId().validate(str(mongo_id))


def test_mongo_id_instance_error():
    with pytest.raises(ValueError):
        MongoId().validate(True)
