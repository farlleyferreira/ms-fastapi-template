
import traceback

from datetime import datetime
from bson.objectid import ObjectId
from project.infrastructure.constants.mongo_collections import Collections
from project.infrastructure.data_layer.data_layer_general import DataLayer
from project.repositories.person.models.legal_person import LegalPerson
from project.repositories.person.valitations.legal_person import ValidateLegalPerson

from project.infrastructure.monitoring_layer.aplication_general_log import Log
from project.infrastructure.monitoring_layer.aplication_kpi import Monitor

log = Log()


class ManageLegalPerson:

    def __init__(self) -> None:
        self.dao = DataLayer(Collections.legal_person)

    async def get_legal_person_by_id(self, id: str) -> LegalPerson:
        try:
            _id: ObjectId = ObjectId(id)

            search_result: dict = await self.dao.get_by_id(_id)

            return self.compose_response_legal_person(search_result)

        except Exception as error:

            _error = traceback.format_exc()
            _message = "error to fetching legal person"
            log.record.error(_message, exc_info=_error)
            Monitor.send_kpi_message(_message, _error)

            raise error

    async def get_legal_person_by_query(self, query: dict):
        try:

            date_filter = {}
            if "initial_date" in query:
                initial_date = query["initial_date"]
                date_filter["$gte"] = datetime.strptime(initial_date, "%Y-%m-%d")
                del query["initial_date"]

            if "end_date" in query:
                end_date = query["end_date"]
                date_filter["$lte"] = datetime.strptime(end_date, "%Y-%m-%d")
                del query["end_date"]

            custom_filter = {}
            if date_filter:
                custom_filter["birthdate"] = date_filter

            custom_filter.update(query)
            search_result: dict = await self.dao.get_by_filter(custom_filter)

            if not len(search_result):
                return []

            list_of_legal_person = [
                self.compose_response_legal_person(legal_person).dict()
                for legal_person in search_result
            ]

            return list_of_legal_person

        except Exception as error:

            _error = traceback.format_exc()
            _message = "error to fetching list of legal person"
            log.record.error(_message, exc_info=_error)
            Monitor.send_kpi_message(_message, _error)

            raise error

    async def save_legal_person(self, legal_person: LegalPerson):
        try:
            _transaction = "save_legal_person"
            Monitor.begin_transaction(_transaction)
            _legal_person = legal_person.dict(exclude_unset=True)

            validate = ValidateLegalPerson
            if await validate.this_legal_person_has_exist(_legal_person):
                cause = "legal person has exist"
                raise await self.raise_error_legal_person(_transaction, cause)

            personal_document_id = _legal_person["business_document_id"]
            if await validate.this_document_id_exist_in_store(personal_document_id):
                cause = "personal document id has exist in store"
                raise await self.raise_error_legal_person(_transaction, cause)

            email = _legal_person["email"]
            if await validate.this_email_exist_in_store(email):
                cause = "email has exist in store"
                raise await self.raise_error_legal_person(_transaction, cause)

            save_result: dict = await self.dao.save(_legal_person)

            Monitor.end_transaction(_transaction, "legal person saved")
            return self.compose_response_legal_person(save_result)

        except Exception as error:

            _error = traceback.format_exc()
            _message = "error to save legal person"
            log.record.error(_message, exc_info=_error)
            Monitor.send_kpi_message(_message, _error)

            raise error

    async def update_legal_person(self, id: str, legal_person: dict):
        try:
            _id: ObjectId = ObjectId(id)

            update_result: dict = await self.dao.update({"_id": _id}, legal_person)

            matched_count = update_result.matched_count
            modified_count = update_result.modified_count

            return {
                "itens_affected": matched_count,
                "itens_modified": modified_count
            }

        except Exception as error:

            _error = traceback.format_exc()
            _message = "error to update legal person"
            log.record.error(_message, exc_info=_error)
            Monitor.send_kpi_message(_message, _error)

            raise error

    async def delete_legal_person(self, id: str):
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
            _message = "error to delete legal person"
            log.record.error(_message, exc_info=_error)
            Monitor.send_kpi_message(_message, _error)

            raise error

    @staticmethod
    def compose_response_legal_person(object: dict):

        if "_id" in object or "id" in object:
            object["_id"] = str(object["_id"])

        return LegalPerson(**object)

    @staticmethod
    async def raise_error_legal_person(tag, cause):
        log.record.error(cause)
        Monitor.end_transaction(tag, cause)
        return RuntimeError(cause)
