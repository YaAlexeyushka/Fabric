from model.model import model


class organisation_model(model):
    __name: str = None
    __description: str = None
    __address: str = None
    __phone: str = None
    __email: str = None
    __website: str = None 
    
    def __init__(self, name=None, description=None, address=None, phone=None, email=None, website=None):
        self.__name = name
        self.__description = description
        self.__address = address
        self.__phone = phone
        self.__email = email
        self.__website = website
        
    @staticmethod
    def create(name="Default", description="Default", address="Default", phone='Default', email='Default', website='Default'):
        model = organisation_model(name, description, address, phone, email, website)
        
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