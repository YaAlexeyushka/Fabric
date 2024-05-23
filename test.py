from unittest import TestCase
from fabric import Fabric
from keys import keys


class Tester(TestCase):
    
    def check_organisation_model_create():
        key = keys.organisation_key()
        
        fabric = Fabric()
        
        model = fabric.create(key)
        
        organisation_model = model.create("name", "desc", "address", "phone", "email", "website")
        
        assert organisation_model is not None
        
    def check_storage_model_create():
        key = keys.storage_key()
        
        fabric = Fabric()
        
        model = fabric.create(key)
        
        storage_model = model.create("name", "desc", "address", 10)
        
        assert storage_model is not None
        
        
    def check_user_model_create():
        key = keys.storage_key()
        
        fabric = Fabric()
        
        model = fabric.create(key)
        
        user_model = model.create("name", "desc", "address", "phone", "mail")
        
        assert user_model is not None