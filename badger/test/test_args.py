from mock import Mock
from nose.tools import raises, assert_equal
from itertools import islice

from badger.itertools_wrapper import count
from badger.args import range_cmd, poll, default


class TestRange(object):

    def setup(self):
        self.converter = Mock()
        self.args = {
            '<start>': None,
            '<stop>': None,
            '<step>': None,
            '--polling': False,
            '--interval': 1,
        }

    def test_simple(self):
        self.args['<start>'] = '0'
        self.args['<stop>'] = '5'
        range_cmd(self.args, self.converter)
        self.converter.series.assert_called_with(range(5), polling=None)

    def test_with_step(self):
        self.args['<start>'] = '5'
        self.args['<stop>'] = '16'
        self.args['<step>'] = '2'
        range_cmd(self.args, self.converter)
        self.converter.series.assert_called_with(range(5, 16, 2), polling=None)

    def test_polling(self):
        self.args['<start>'] = '0'
        self.args['<stop>'] = '5'
        self.args['--polling'] = True
        range_cmd(self.args, self.converter)
        self.converter.series.assert_called_with(range(5), polling=1)

    def test_interval(self):
        self.args['<start>'] = '0'
        self.args['<stop>'] = '5'
        self.args['--polling'] = True
        self.args['--interval'] = '2'
        range_cmd(self.args, self.converter)
        self.converter.series.assert_called_with(range(5), polling=2.0)

    @raises(ValueError)
    def test_faulty_start(self):
        self.args['<start>'] = 'blah'
        self.args['<stop>'] = '5'
        range_cmd(self.args, self.converter)

    @raises(ValueError)
    def test_faulty_stop(self):
        self.args['<start>'] = '0'
        self.args['<stop>'] = 'blah'
        range_cmd(self.args, self.converter)

    @raises(ValueError)
    def test_faulty_step(self):
        self.args['<start>'] = '0'
        self.args['<stop>'] = '5'
        self.args['<step>'] = 'foo'
        range_cmd(self.args, self.converter)

    @raises(ValueError)
    def test_faulty_interval(self):
        self.args['<start>'] = '0'
        self.args['<stop>'] = '5'
        self.args['--polling'] = True
        self.args['--interval'] = 'foo'
        range_cmd(self.args, self.converter)


class TestPoll(object):

    def converter_series(self, *args, **kwargs):
        self.series_calls.append({'args': args, 'kwargs': kwargs})

    def setup(self):
        self.series_calls = []
        self.converter = Mock()
        self.args = {
            '<start>': None,
            '<step>': None,
            '--interval': 1,
        }

    def test_no_args(self):
        poll(self.args, self.converter)
        self.converter.series.assert_called_with(count(), polling=1)

    def test_start(self):
        self.args['<start>'] = '5'
        poll(self.args, self.converter)
        self.converter.series.assert_called_with(count(5), polling=1)

    def test_start_step(self):
        self.args['<start>'] = '6'
        self.args['<step>'] = '2'
        poll(self.args, self.converter)
        self.converter.series.assert_called_with(count(6, 2), polling=1)

    def test_interval(self):
        self.args['--interval'] = '3'
        poll(self.args, self.converter)
        self.converter.series.assert_called_with(count(), polling=3)

    @raises(ValueError)
    def test_faulty_start(self):
        self.args['<start>'] = 'blah'
        poll(self.args, self.converter)

    @raises(ValueError)
    def test_faulty_step(self):
        self.args['<start>'] = '17'
        self.args['<step>'] = 'blah'
        poll(self.args, self.converter)

    @raises(ValueError)
    def test_faulty_interval(self):
        self.args['--interval'] = 'foo'
        poll(self.args, self.converter)


class TestDefault(object):

    def setup(self):
        self.converter = Mock()
        self.args = {
            '<index>': None,
        }

    def test_no_index(self):
        default(self.args, self.converter)
        self.converter.single.assert_called_with(0)

    def test_index(self):
        self.args['<index>'] = '2'
        default(self.args, self.converter)
        self.converter.single.assert_called_with(2)

    @raises(ValueError)
    def test_faulty_index(self):
        self.args['<index>'] = 'foo'
        default(self.args, self.converter)
