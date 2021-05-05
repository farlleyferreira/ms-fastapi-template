from bson.objectid import ObjectId
from project.infrastructure.constants.mongo_collections import Collections
from project.infrastructure.data_layer.data_layer_general import DataLayer


class ValidateLegalPerson:

    @staticmethod
    async def this_legal_person_has_exist(criteria: dict) -> bool:

        data_layer = DataLayer(Collections.legal_person)
        result = await data_layer.get_by_filter(criteria)

        if len(result) > 0:
            return True

        return False

    @staticmethod
    async def this_legal_person_is_active(_id: ObjectId) -> bool:

        data_layer = DataLayer(Collections.legal_person)
        result = await data_layer.get_by_id(_id)

        if "status" in result and result["status"] == "active":
            return True
        return False

    @staticmethod
    async def this_email_exist_in_store(email: str) -> bool:

        data_layer = DataLayer(Collections.legal_person)
        result = await data_layer.get_by_filter({"email": email})

        if len(result) > 0:
            return True

        return False

    @staticmethod
    async def this_document_id_exist_in_store(document_id: str) -> bool:

        data_layer = DataLayer(Collections.legal_person)
        result = await data_layer.get_by_filter({"business_document_id": document_id})

        if len(result) > 0:
            return True

        return False
