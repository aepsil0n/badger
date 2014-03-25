#! /usr/bin/env python
"""
Converts a series of input files to output files using a Python script

You can convert a single frame, a range of frames or poll from the input
directory as files are appearing.

Usage:
    badger <item> <index>
    badger <item> range <start> <stop> [<step>] [--polling] [--interval=<sec>]
    badger <item> poll [<start> <step>] [--interval=<sec>]

Options:
    -h --help           Show this screen.
    --version           Show version.
    --polling           Makes range command also poll for input files.
    --interval=<sec>    Interval between polls in seconds [default: 1].

"""

from itertools import count
from docopt import docopt

from .loader import load_item
from .commands import Converter


def main():
    """Main entry point for badger script"""
    # Parse arguments
    args = docopt(__doc__, version='alpha')

    item = load_item(args['<item>'])
    converter = Converter(item)

    if args['range']:
        frames = range(
            int(args['<start>']),
            int(args['<stop>']),
            int(args['<step>'] or 1))
        converter.series(frames)
    elif args['poll']:
        poller = count(
            int(args['<start>'] or 0),
            int(args['<step>'] or 1))
        converter.series(poller, polling=float(args['--interval']))
    else:
        index = int(args['<index>'])
        converter.single(index)


# Execute main function if this module is run
if __name__ == '__main__':
    main()
