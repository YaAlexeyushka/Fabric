from abc import ABC

class storage_model(ABC):
    __name: str = None
    __description: str = None
    __address: str = None
    __capacity: int = None
    
    def create(self, name=None, description=None, address=None, capacity=None):
        model = storage_model()
        model.__name = name
        model.__description = description
        model.__address = address
        model.__capacity = capacity
        
        return model
    
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        self.__capacity = value