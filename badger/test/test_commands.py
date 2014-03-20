from badger.commands import Converter

from nose.tools import assert_equal


class Foo:

    def __init__(self):
        self.data = {}

    def process(self, inp, out):
        self.data[inp] = out


class TestConverter:

    def setup(self):
        self.foo = Foo()
        self.converter = Converter(self.foo)

    def test_single(self):
        self.converter.single('foo', 'bar')
        assert_equal(self.foo.data['foo'], 'bar')

    def test_series(self):
        frames = range(0, 3)
        self.converter.series(frames, 'foo{:d}', 'bar{:d}')
        for i in frames:
            assert_equal(self.foo.data['foo' + str(i)], 'bar' + str(i))
