

class SectionBoolenVal(object):
    accepted    = [ 'yes', 'no', 'true', 'false', 1, 0]
    truthy      = ['yes', 'true', 1]
    falsy       = ['no', 'false', 0]


class Token(object):
    '''Tokens used to detect specific items in the config file
    '''

    group_start     = '['
    group_end       = ']'
    section_sep     = '='
    comment_start   = ';'
    override_start  = '<'
    override_end    = '>'
    array_sep       = ','
    string_marker   = '"'

