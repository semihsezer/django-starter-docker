from ballpark import ballpark

def get_friendly_count(count):
    '''
    Args:
        count: @str or @int
    Returns:
        str: @str Human friendly count string (1K, 1.5K etc.)
    '''
    c = int(count)
    if c > 999:
        return ballpark(c)
    else:
        return str(c)

def parse_str_bool(str_bool, default=None):
    '''Helper methood to parse bool from str. ie 'false' => False, 'true' => True.
    default is the default that will be set if parse is unsuccessful.
    '''
    if type(str_bool) == bool:
        return str_bool

    if str_bool.lower() == 'false':
        return False
    elif str_bool.lower() == 'true':
        return True
    else:
        return default


