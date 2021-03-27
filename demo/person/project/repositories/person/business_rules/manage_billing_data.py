
import traceback

from bson.objectid import ObjectId

from project.infrastructure.constants.mongo_collections import Collections
from project.infrastructure.data_layer.data_layer_general import DataLayer

from project.repositories.person.models.billing_data import BillingData
from project.repositories.person.valitations.billing_data import ValidateBillingData

from project.infrastructure.monitoring_layer.aplication_general_log import Log
from project.infrastructure.monitoring_layer.aplication_kpi import Monitor

log = Log()


class ManageBillingData:

    def __init__(self) -> None:
        self.dao = DataLayer(Collections.person_billing_data)

    async def get_billing_data_by_id(self, id: str) -> BillingData:
        try:
            _id: ObjectId = ObjectId(id)

            search_result: dict = await self.dao.get_by_id(_id)

            return self.compose_response_billing_data(search_result)

        except Exception as error:

            _error = traceback.format_exc()
            _message = "error to fetching billing data"
            log.record.error(_message, exc_info=_error)
            Monitor.send_kpi_message(_message, _error)

            raise error

    async def get_billing_data_by_query(self, query: dict):
        try:

            search_result: dict = await self.dao.get_by_filter(query)

            if not len(search_result):
                return []

            list_of_billing_data = [
                self.compose_response_billing_data(billing_data).dict()
                for billing_data in search_result
            ]

            return list_of_billing_data

        except Exception as error:

            _error = traceback.format_exc()
            _message = "error to fetching list of billing data"
            log.record.error(_message, exc_info=_error)
            Monitor.send_kpi_message(_message, _error)

            raise error

    async def save_billing_data(self, billing_data: BillingData):
        try:
            _transaction = "save_billing_data"
            Monitor.begin_transaction(_transaction)
            _billing_data = billing_data.dict(exclude_unset=True)

            validate = ValidateBillingData
            if await validate.this_billing_data_has_exist(_billing_data):
                cause = "billing data has exist"
                raise await self.raise_error_billing_data(_transaction, cause)

            save_result: dict = await self.dao.save(_billing_data)

            Monitor.end_transaction(_transaction, "billing data saved")
            return self.compose_response_billing_data(save_result)

        except Exception as error:

            _error = traceback.format_exc()
            _message = "error to save billing data"
            log.record.error(_message, exc_info=_error)
            Monitor.send_kpi_message(_message, _error)

            raise error

    async def update_billing_data(self, id: str, billing_data: dict):
        try:
            _id: ObjectId = ObjectId(id)

            update_result: dict = await self.dao.update({"_id": _id}, billing_data)

            matched_count = update_result.matched_count
            modified_count = update_result.modified_count

            return {
                "itens_affected": matched_count,
                "itens_modified": modified_count
            }

        except Exception as error:

            _error = traceback.format_exc()
            _message = "error to update billing data"
            log.record.error(_message, exc_info=_error)
            Monitor.send_kpi_message(_message, _error)

            raise error

    async def delete_billing_data(self, id: str):
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
            _message = "error to delete billing data"
            log.record.error(_message, exc_info=_error)
            Monitor.send_kpi_message(_message, _error)

            raise error

    @staticmethod
    def compose_response_billing_data(object: dict):

        if "_id" in object or "id" in object:
            object["_id"] = str(object["_id"])

        return BillingData(**object)

    @staticmethod
    async def raise_error_billing_data(tag, cause):
        log.record.error(cause)
        Monitor.end_transaction(tag, cause)
        return RuntimeError(cause)
