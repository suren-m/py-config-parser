import os
import sys

from config_loader_app import config_builder, config_validator


def load_config(file_path, overrides=[]): 
    '''Parses config data from file and returns a config object

    Args:
        file_path: full path of the config file
        overrides: array of env specific overrides
        
    Returns:
        config object: contains group and section data (config.groupname.sectionname)
    '''

    config_items = None      
    with open(file_path, "r") as file:        
        config_items = file.read().split('\n')                            
    
    result = config_validator.validate(config_items)
    
    if not result.is_success:
        raise ','.join(result.errors)
        
    config = config_builder.Config(config_items, overrides)             

    return config


def load_example_config(test_file_path = os.path.join(sys.path[0], 'config_file_example'), overrides = []):       
    print(f'loading config from {test_file_path}')
    print(f'using overrides {overrides}')

    return load_config(test_file_path, overrides)    
    

if __name__ == '__main__':   
    test_file_path = os.path.join(sys.path[0], 'tests', 'config_file_example')      
    config = load_example_config(test_file_path, overrides=['staging'])  
    
    print('done')