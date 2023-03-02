import pytest
from project.helpers.pydantic_typo import ObjectId
from project.infrastructure.drivers.elasticsearch.adapter import ElkAdapter
import time


@pytest.mark.asyncio
def test_get_buildinfo():
    elk = ElkAdapter("mstemplate")
    if elk.get_buildinfo() is not True:
        raise AssertionError


@pytest.mark.asyncio
async def test_get_one_success():
    elk = ElkAdapter("mstemplate")
    data: dict = {"key": "value", "key2": "value2"}
    id = await elk.insert_one(data)
    result = await elk.get_one(id=str(id))
    if result != data:
        raise AssertionError


@pytest.mark.asyncio
async def test_get_one_error():
    with pytest.raises(Exception):
        elk = ElkAdapter("mstemplate123")
        id = 123456 + True
        await elk.get_one(id=id)


@pytest.mark.asyncio
async def test_get_many_success():
    elk = ElkAdapter("mstemplate")
    data: dict = {"key": "value", "key2": "value2"}
    queryble_ids = [str(await elk.insert_one(data)) for i in range(10)]
    new_filter = {"query": {"ids": {"values": queryble_ids}}}
    result = await elk.get_many(filter=new_filter)
    if len(result) == 1:
        raise AssertionError


@pytest.mark.asyncio
async def test_get_many_error():
    with pytest.raises(Exception):
        elk = ElkAdapter("mstemplate")
        await elk.get_many(filter={"key": "pineapple"})


@pytest.mark.asyncio
async def test_insert_one_success():
    elk = ElkAdapter("mstemplate")
    result = await elk.insert_one({"key": "value"})
    if type(result) != ObjectId:
        raise AssertionError


@pytest.mark.asyncio
async def test_insert_one_error():
    with pytest.raises(Exception):
        elk = ElkAdapter("mstemplate")
        result = await elk.insert_one({"key": Exception("")})


@pytest.mark.asyncio
async def test_insert_many_success():
    list_of_itens = [{"key": "value"}] * 100
    elk = ElkAdapter("mstemplate")
    result = await elk.insert_many(list_of_itens)
    if type(result) != list:
        raise AssertionError
    if len(result) != 100:
        raise AssertionError


@pytest.mark.asyncio
async def test_insert_many_error():
    with pytest.raises(Exception):
        elk = ElkAdapter("mstemplate")
        await elk.insert_many({"key": Exception("")})


@pytest.mark.asyncio
async def test_update_one_success():
    elk = ElkAdapter("mstemplate")
    data: dict = {"person": "jhon", "age": 32}
    id = await elk.insert_one(data)
    acknowledged, modified_count = await elk.update_one(id, {"age": 45})
    if acknowledged is not True:
        raise AssertionError
    if modified_count != 1:
        raise AssertionError


@pytest.mark.asyncio
async def test_update_one_error():
    with pytest.raises(Exception):
        elk = ElkAdapter("mstemplate")
        await elk.update_one({"key": Exception("")}, {})


@pytest.mark.asyncio
async def test_update_many_success():
    elk = ElkAdapter("mstemplate")
    data: dict = [
        {"person": "jhon", "age": 57},
        {"person": "carl", "age": 57},
        {"person": "jake", "age": 57},
        {"person": "samy", "age": 57},
        {"person": "moes", "age": 57},
        {"person": "jean", "age": 57},
        {"person": "Cler", "age": 57},
        {"person": "Nast", "age": 57},
    ]
    await elk.insert_many(data)
    acknowledged, modified_count = await elk.update_many(
        {"query": {"range": {"age": {"gte": 57}}}},
        {"age": 29},
    )
    if acknowledged is not True:
        raise AssertionError
    if modified_count == 0:
        raise AssertionError


@pytest.mark.asyncio
async def test_update_many_error():
    with pytest.raises(Exception):
        elk = ElkAdapter("mstemplate")
        await elk.update_many({"age": {"$gt": Exception()}}, {"age": 29})


@pytest.mark.asyncio
async def test_delete_success():
    elk = ElkAdapter("mstemplate")
    data: dict = {"person": "jhon", "age": 32}
    id = await elk.insert_one(data)
    new_id = str(id)
    time.sleep(1.1)
    criteria = {"query": {"terms": {"_id": [new_id]}}}
    acknowledged, deleted_count = await elk.delete(criteria)

    if acknowledged is not True or deleted_count == 0:
        raise AssertionError(acknowledged, deleted_count)


@pytest.mark.asyncio
async def test_delete_error():
    with pytest.raises(Exception):
        elk = ElkAdapter("mstemplate")
        await elk.delete({"key": Exception()})
