from nose.tools import assert_equal
from itertools import islice

from badger.itertools_wrapper import count


class TestCount(object):

    def test_plain(self):
        for a, b in zip(islice(count(), 10), range(10)):
            assert_equal(a, b)
    
    def test_start(self):
        for a, b in zip(islice(count(3), 10), range(3, 13)):
            assert_equal(a, b)

    def test_step(self):
        for a, b in zip(islice(count(3, 2), 10), range(3, 23, 2)):
            assert_equal(a, b)

    def test_eq(self):
        assert_equal(count(), count(0))
        assert_equal(count(), count(0, 1))
        assert_equal(count(3), count(3))
        assert_equal(count(3), count(3, 1))
        assert_equal(count(3, 2), count(3, 2))

    def test_repr(self):
        assert_equal(repr(count(3, 2)), 'count(3, 2)')
