"""
Wrapper around a subset of the builtin itertools module

NOTE: so far only count is required.

"""

import itertools


class count(object):
    """
    A counting iterator that starts at some point and steps forward

    This is essentially a wrapper to the functionally equivalent built-in
    `itertools.count`. The difference is that this object does not track its
    own state but rather returns a new built-in count object when iterated
    over.

    Furthermore, equality of two of these count objects is defined by equality
    of starting point and step size.

    """
    
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step

    def __eq__(self, other):
        return self.start == other.start and self.step == other.step

    def __iter__(self):
        return itertools.count(self.start, self.step)

    def __repr__(self):
        return repr(iter(self))
