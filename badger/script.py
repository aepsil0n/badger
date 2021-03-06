#! /usr/bin/env python
"""
Converts a series of input files to output files using a Python script

You can convert a single frame, a range of frames or poll from the input
directory as files are appearing.

Usage:
    badger <item> range <start> <stop> [<step>] [--polling] [--interval=<sec>]
    badger <item> poll [<start> [<step>]] [--interval=<sec>]
    badger <item> <index>

Options:
    -h --help           Show this screen.
    --version           Show version.
    --polling           Makes range command also poll for input files.
    --interval=<sec>    Interval between polls in seconds [default: 1].

"""

from docopt import docopt

from .loader import load_item
from .commands import Converter
from .args import determine_command


def main():
    """Main entry point for badger script"""
    # Parse arguments
    args = docopt(__doc__, version='alpha')
    # Create converter
    item = load_item(args['<item>'])
    converter = Converter(item)
    # Determine and execute subcommand function
    cmd = determine_command(args)
    cmd(args, converter)


# Execute main function if this module is run
if __name__ == '__main__':
    main()
