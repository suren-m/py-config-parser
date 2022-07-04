from config_loader_app import config_rules

_token = config_rules.Token()
_section_bool = config_rules.SectionBoolenVal()


def parse(value):       
    '''Takes the given value (string) and converts it to correct type based on config_rules

    Args:
        value: section value string from config 

    Returns:
        parsed_value: can be of type int or array or bool or string or None depending on input
    '''

    parsed_value = None
    
    # arrays
    if _token.string_marker not in value and _token.array_sep in value:
        parsed_value = value.split(',')
        return parsed_value        

    # bools
    if value in _section_bool.accepted:
        if value in _section_bool.falsy:
            parsed_value = False
        if value in _section_bool.truthy:
            parsed_value = True
        return parsed_value        

    # numbers or string
    try:
        parsed_value = int(value)
    except:
        parsed_value = value
    finally:
        if _token.string_marker in value:
            parsed_value = value.replace(_token.string_marker, '')
        return parsed_value   
    