from config_loader_app import config_rules

token = config_rules.Token()

def validate(config_items):
    '''checks for most common malformed syntax and returns a ValidationResult object
    '''

    class ValidatonResult:
        def __init__(self, result, exception_obj):
            self.is_success = result
            self.errors = []            

    errors = []
    try:
        for i in config_items:
            if i.startswith(token.group_start) and not i.endswith(token.group_end):
                errors.append(f'syntax error in group name {i}')
            elif token.section_sep in i:
                (left, _, right) = i.partition(token.section_sep)

                if not right:
                    errors.append(f'section {left} has no value specified')
                       
                left = left.strip()
                if token.override_start in left and not left.endswith(token.override_end):
                    errors.append(f'syntax error in override for section {i}')

        is_success = False if errors else True
        return ValidatonResult(is_success, errors)

    except Exception as ex:
        return ValidatonResult( False, errors.append( str(ex) ) )


