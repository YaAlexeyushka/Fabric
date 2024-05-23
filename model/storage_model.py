from model.model import model

class storage_model(model):
    __name: str = None
    __description: str = None
    __address: str = None
    __capacity: int = None
    
    def __init__(self, name=None, description=None, address=None, capacity=None):
        self.__name = name
        self.__description = description
        self.__address = address
        self.__capacity = capacity

    @staticmethod
    def create(name="Default", description="Default", address="Default", capacity=10):
        model = storage_model(name, description, address, capacity)
        
        return model

    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    # Getter and Setter for description
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    # Getter and Setter for address
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    # Getter and Setter for phone
    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        self.__capacity = value