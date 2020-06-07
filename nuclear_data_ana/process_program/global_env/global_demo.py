"""This module's docstring summary line.
datatime is included to extract the time difference between
start time and end time.
"""
GLOBAL_DICT = {}

def _init():
    global GLOBAL_DICT


def set_value(key, value):
    """ define a global variable """
    GLOBAL_DICT[key] = value


def get_value(key, def_value=None):
    """obtain a global variable,Return default value
       if it doesn't exist """
    try:
        return GLOBAL_DICT[key]
    except KeyError:
        return def_value
