from config_loader_app import (config_parser as cp, 
    section_value_parser as svp,
    config_cache as cc)


class Config(dict):     
    '''Represents Config object. Contains attributes of type Group
    '''

    def __init__(self, config_items, overrides):
        '''Iterates over the yielded group from config parser and constructs config object    

            Creates a new group object per group and sets it as a property of config object  
        '''       
        for (group_name, config_group) in cp.generate_config_by_group(config_items, overrides): 
            group_obj = Group()            

            for section_name, section_value in config_group[group_name].items():
                setattr(group_obj, section_name, section_value)  

            setattr(self, group_name, group_obj)     

   
    def __getitem__(self, key):        
        '''Invoked when accessing group by index
        '''
        return dict.get(self, key, None) 

    @cc.cache
    def __getattr__(self, key):
        '''Invoked when a call is made to retrieve group or section. Returns attribute if exists else None           
        '''        
        return dict.get(self, key, None)    


    def __setattr__(self, key, value):
        '''Invoked when setting the value of group
        '''
        self[key] = value


class Group(dict):        
    '''Represents Group object. Contains sections as attributes
    '''        

    def __getitem__(self, key):        
        '''Invoked when accessing section by index
        '''
        return dict.get(self, key, None)

    
    def __getattr__(self, key):
        '''Invoked when a call is made to retrieve a section.  Returns section if exists else None      
        '''
        return dict.get(self, key, None) 
    

    def __setattr__(self, key, value):       
        '''Invoked when setting the value of a section
        '''
        parsed_value = svp.parse(value)
        self[key] = parsed_value

  
    
  
    


    

