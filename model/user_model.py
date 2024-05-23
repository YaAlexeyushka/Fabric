from model.model import model


class user_model(model):
    __name: str = None
    __description: str = None
    __address: str = None
    __phone: str = None
    __email: str = None
    
    def __init__(self, name=None, description=None, address=None, phone=None, email=None):
        self.__name = name
        self.__description = description
        self.__address = address
        self.__phone = phone
        self.__email = email
    
    def create(name="Default", description="Default", address="Default", phone="Default", email="Default"):
        model = user_model(name, description, address, phone, email)

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