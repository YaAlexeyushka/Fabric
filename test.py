from unittest import TestCase
from models.organisation_model import organisation_model
from models.storage_model import storage_model
from models.user_model import user_model


class Tester(TestCase):
    
    
    def test_check_org_mod(self):
        model = organisation_model.create()
        
        assert model is not None
        
    def test_check_stor_mod(self):
        model = storage_model.create()
        
        assert model is not None
        
    def test_check_us_mod(self):
        model = user_model.create()
        
        assert model is not None
   