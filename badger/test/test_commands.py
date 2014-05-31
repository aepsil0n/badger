from badger.commands import Converter

from nose.tools import assert_equal


class Foo:

    def __init__(self):
        self.data = {}

    def process(self, index):
        self.data[self.input_file(index)] = self.output_file(index)

    def input_file(self, index):
        return 'foo{:d}'.format(index)

    def output_file(self, index):
        return 'bar{:d}'.format(index)


class TestConverter:

    def setup(self):
        self.foo = Foo()
        self.converter = Converter(self.foo)

    def test_single(self):
        self.converter.single(0)
        assert_equal(self.foo.data['foo0'], 'bar0')

    def test_series(self):
        frames = range(0, 3)
        self.converter.series(frames)
        for i in frames:
            assert_equal(self.foo.data['foo' + str(i)], 'bar' + str(i))
