from abc import ABC, abstractmethod

class DataLayer(ABC):

    @abstractmethod
    async def get_buildinfo(self) -> bool:
        '''
            Return ping database 
        '''

    # @abstractmethod
    # async def get_one(self) -> object:
    #     '''
    #         Return one registry of context database by key
    #     '''

    # @abstractmethod
    # async def get_by_filter(self):
    #     '''
    #         Return a list of registrys of context database
    #     '''

    # @abstractmethod
    # async def insert_one(self):
    #     '''
    #         Insert one registry in context database
    #     '''

    # @abstractmethod
    # async def insert_many(self):
    #     '''
    #         Insert a list of registrys in context database by filter
    #     '''

    # @abstractmethod
    # async def update_one(self):
    #     '''
    #         Updade a registry in context database by id
    #     '''

    # @abstractmethod
    # async def update_many(self):
    #     '''
    #         Updade one or more registrys in context database by filter
    #     '''

    # @abstractmethod
    # async def delete_one(self):
    #     '''
    #         Delete a registry in context database by id
    #     '''

    # @abstractmethod
    # async def delete_many(self):
    #     '''
    #          one or more registrys in context database by filter
    #     '''
