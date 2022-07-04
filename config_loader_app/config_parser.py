from config_loader_app import config_rules


_token = config_rules.Token()


def generate_config_by_group(items, overrides):      
    '''Takes a list of config items and yields a tuple with group_name and a group dict with its sections            
    '''

    group = {}
    group_name = None

    for item in items:
        if item.startswith(_token.group_start):                        
            if group:
                yield (group_name, group)
                group_name = None
                group = {}      

            group_name = item[1:-1] # group name is a string between []
            group[group_name] = {} 

        if item[1:-1] != group_name:
            if _token.section_sep in item: # ignore comments in new line

                section = item.split(_token.section_sep)                
                section_key = section[0].strip()
                (section_value, _, _) = section[1].partition(_token.comment_start) # ignore comments
                
                if _token.override_start in item:
                    start_index = section_key.find(_token.override_start)+1
                    end_index = section_key.find(_token.override_end)
                    override = section_key[start_index:end_index]

                    if override in overrides:
                        (section_key, _, _) = section[0].partition(_token.override_start)
                    else:
                        continue            
                                
                group[group_name][section_key] = section_value.strip()
 
    yield (group_name, group)