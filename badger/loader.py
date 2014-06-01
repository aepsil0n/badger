"""
Functionality to load an object from a module

"""

from importlib import import_module
from six.moves import configparser
import json
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


def read_init_kwargs(args):
    """Read initialization keyword arguments from docopt args

    This parses the --config option to look for configuration files and to read
    keyword arguments for the item from there. The function returns the keyword
    arguments as a dictionary.

    Note, that all values are passed through ast.literal_eval, so the
    configuration file is expected to contain literal Python expressions as
    values.

    """
    config = configparser.ConfigParser()
    if '--config' in args and args['--config'] is not None:
        config.read(args['--config'])
        config_dict = config.defaults()
        if config.has_section(args['<item>']):
            config_dict.update(config.items(args['<item>']))
        return {k: json.loads(v) for k, v in config_dict.items()}
    else:
        return {}


def load_item(path, init_kwargs=None):
    """Load an item given a path specification

    The specification may be either of:

    module:path
    module

    The optional `init_kwargs` argument is a dictionary of keyword arguments to
    be provided to the object in case it is not a module.

    """
    match = re.match('^(.*):(.*)$', path)
    if match:
        return load_object(match.group(1), match.group(2))(
            **(init_kwargs or {}))
    return load_module(path)
