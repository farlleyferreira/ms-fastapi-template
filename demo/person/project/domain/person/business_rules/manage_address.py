
import traceback

from bson.objectid import ObjectId

from project.infrastructure.constants.mongo_collections import Collections
from project.infrastructure.data_layer.data_access_adapter import MongoDataLayer

from project.domain.person.repository.address import Address
from project.domain.person.valitations.address import ValidateAdress

from project.infrastructure.monitoring_layer.aplication_general_log import Log
from project.infrastructure.monitoring_layer.aplication_kpi import Monitor

log = Log()


class ManageAddress:

    def __init__(self) -> None:
        self.dao = MongoDataLayer(Collections.person_address)

    async def get_address_by_id(self, id: str) -> Address:
        try:
            _id: ObjectId = ObjectId(id)

            search_result: dict = await self.dao.get_by_id(_id)

            return self.compose_response_address(search_result)

        except Exception as error:

            _error = traceback.format_exc()
            _message = "error to fetching address"
            log.record.error(_message, exc_info=_error)
            Monitor.send_kpi_message(_message)

            raise error

    async def get_address_by_query(self, query: dict):
        try:

            search_result: dict = await self.dao.get_by_filter(query)

            if not len(search_result):
                return []

            list_of_address = [
                self.compose_response_address(address).dict()
                for address in search_result
            ]

            return list_of_address

        except Exception as error:

            _error = traceback.format_exc()
            _message = "error to fetching list of address"
            log.record.error(_message, exc_info=_error)
            Monitor.send_kpi_message(_message)

            raise error

    async def save_address(self, address: Address):
        try:
            _transaction = "save_address"
            Monitor.begin_transaction(_transaction)
            _address = address.dict(exclude_unset=True)

            validate = ValidateAdress
            if await validate.this_address_has_exist(_address):
                cause = "address has exist"
                raise await self.raise_error_address(_transaction, cause)

            save_result: dict = await self.dao.save(_address)

            Monitor.end_transaction(_transaction, "address saved")
            return self.compose_response_address(save_result)

        except Exception as error:

            _error = traceback.format_exc()
            _message = "error to save address"
            log.record.error(_message, exc_info=_error)
            Monitor.send_kpi_message(_message)

            raise error

    async def update_address(self, id: str, address: dict):
        try:
            _id: ObjectId = ObjectId(id)

            update_result: dict = await self.dao.update({"_id": _id}, address)

            matched_count = update_result.matched_count
            modified_count = update_result.modified_count

            return {
                "itens_affected": matched_count,
                "itens_modified": modified_count
            }

        except Exception as error:

            _error = traceback.format_exc()
            _message = "error to update address"
            log.record.error(_message, exc_info=_error)
            Monitor.send_kpi_message(_message)

            raise error

    async def delete_address(self, id: str):
        try:
            _id: ObjectId = ObjectId(id)

            delete_result: dict = await self.dao.delete({"_id": _id})

            deleted_count = delete_result.deleted_count

            return {
                "itens_affected": deleted_count,
                "itens_modified": deleted_count
            }

        except Exception as error:

            _error = traceback.format_exc()
            _message = "error to delete address"
            log.record.error(_message, exc_info=_error)
            Monitor.send_kpi_message(_message)

            raise error

    @staticmethod
    def compose_response_address(object: dict):

        if "_id" in object or "id" in object:
            object["_id"] = str(object["_id"])

        return Address(**object)

    @staticmethod
    async def raise_error_address(tag, cause):
        log.record.error(cause)
        Monitor.end_transaction(tag, cause)
        return RuntimeError(cause)
