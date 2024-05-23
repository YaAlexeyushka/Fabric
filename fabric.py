from models.organisation_model import organisation_model
from models.storage_model import storage_model
from models.user_model import user_model

class Fabric():
    __maps: dict = None
    
    def __init__(self):
        self.initialize_maps()
    
    def initialize_maps(self):
        self.__maps[Fabric.organisation_key()] = organisation_model
        self.__maps[Fabric.storage_key()] = storage_model
        self.__maps[Fabric.user_key()] = user_model
        
    def create(self, key):
                
        if key not in self.__maps.keys():
            raise Exception("Ошибка")
        
        model = self.__maps[key]
        
        if model is None:
            raise Exception("Ошибка")
        
        return model
        
