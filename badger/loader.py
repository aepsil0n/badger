"""
Functionality to load an object from a module

"""

from importlib import import_module
import re


def load_module(module):
    """Loads module given its Python path specification"""
    return import_module(module)


def load_object(module, name):
    """
    Dynamically load an object given a path that consists of a module and name.
    Both of these are provided as strings.

    """
    module_obj = load_module(module)
    return getattr(module_obj, name)


def load_item(path):
    """
    Loads an item given a path specification, which may be either of:

    module:path
    module

    """
    match = re.match('^(.*):(.*)$', path)
    if match:
        return load_object(match.group(1), match.group(2))
    return load_module(path)
