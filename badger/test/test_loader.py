from tempfile import NamedTemporaryFile
from nose.tools import assert_equal

from badger.loader import load_module, load_item, load_object, read_init_kwargs


def test_load_module():
    import math
    assert load_module('math') is math


def test_load_object():
    from math import sin
    assert load_object('math', 'sin') is sin


def test_load_item():
    import collections
    assert load_item('collections') is collections
    assert type(load_item('collections:deque')) is collections.deque


def test_read_init_kwargs():
    with NamedTemporaryFile(delete=False) as tmp:
        tmp.write('[foo]\nparam = 3')
        cfgname = tmp.name
    args = {'<item>': 'foo', '--config': cfgname}
    init_kwargs = read_init_kwargs(args)
    assert_equal(init_kwargs, {'param': 3})


def test_read_init_kwargs_no_kwargs():
    init_kwargs = read_init_kwargs({})
    assert_equal(init_kwargs, {})
