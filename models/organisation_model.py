from abc import ABC

class organisation_model(ABC):
    __name: str = None
    __description: str = None
    __address: str = None
    __phone: str = None
    __email: str = None
    __website: str = None 
    
    def create(self, name=None, description=None, address=None, phone=None, email=None, website=None):
        model = organisation_model()
        model.__name = name
        model.__description = description
        model.__address = address
        model.__phone = phone
        model.__email = email
        model.__website = website
        
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
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def website(self):
        return self.__website

    @website.setter
    def website(self, value):
        self.__website = value