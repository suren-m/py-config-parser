import unittest
from config_loader_app import main
from config_loader_app import config_cache

# Arrange and load it once upfront
CONFIG = main.load_example_config(overrides=['staging'])  

class TestConfigLoader(unittest.TestCase):                

    def test_should_return_integer_correctly(self):
        result = CONFIG.common.paid_users_size_limit        
        expected = 2147483648

        self.assertEqual(result, expected)        
        self.assertEqual(type(result), int)

    def test_should_return_string_correctly(self):
        result = CONFIG.ftp.name        
        expected = 'hello there, ftp uploading'

        self.assertEqual(result, expected)        

    def test_should_return_array_correctly(self):
        result = CONFIG.http.params         
        expected = ['array', 'of', 'values'] 

        self.assertEqual(result, expected)  

    def test_should_return_None_for_missing_section(self):
        result = CONFIG.ftp.lastname 
        expected = None
        
        self.assertEqual(result, expected)
        
    def test_should_return_boolean_correctly(self):
        result = CONFIG.ftp.enabled 
        expected = False

        self.assertEqual(result, expected)

    def test_should_allow_access_by_index(self):
        result = CONFIG.ftp['path']
        expected = '/srv/uploads/'

        self.assertEqual(result, expected)

    def test_should_prvoide_dict_representation(self):
        result = CONFIG.ftp 
        expected = { 
            'name'      : 'hello there, ftp uploading',
            'path'      : '/srv/uploads/',
            'enabled'   : False
        }       
        
        self.assertEqual(result, expected)

    def test_should_respect_env_overrides(self):
        result = CONFIG.ftp.path        
        expected = '/srv/uploads/' # staging

        self.assertEqual(result, expected)

    def test_should_cache_group_query(self):
        cache_obj = config_cache.get_cache_obj()
        cache_obj.clear_cache()

        _first = CONFIG.ftp
        _second = CONFIG.ftp
        _third = CONFIG.ftp

        (total_hits, _) = cache_obj.get_hits_and_misses()
        expected = 2
        self.assertEqual(total_hits, expected)


    
TestConfigLoader().test_should_cache_group_query()
