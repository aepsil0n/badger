from badger.loader import load_module, load_item, load_object


def test_load_module():
    import math
    assert load_module('math') is math


def test_load_object():
    from math import sin
    assert load_object('math', 'sin') is sin


def test_load_item():
    import math
    assert load_item('math') is math
    assert load_item('math:sin') is math.sin
