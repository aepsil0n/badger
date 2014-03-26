"""
This module takes care of dispatching to the right batch call

Every function decorated with `@command` in this module translates to a badger
subcommand and defines how a given converter and docopt dictionary are to be
executed.

"""

from .itertools_wrapper import count


_all_commands = {}

def command(name=None):
    """Decorator to register commands"""
    def cmd_deco(fct):
        _all_commands[name or fct.__name__] = fct
        return fct
    return cmd_deco


def determine_command(args):
    """
    Determine the command to be executed from the parsed docopt arguments

    """
    for cmd, fct in _all_commands.iteritems():
        if cmd not in args:
            continue
        if args[cmd]:
            return fct
    return default


@command('range')
def range_cmd(args, converter):
    """
    The range command

    This command will process a range of input files specified exactly like the
    range() function.

    """
    frames = range(
        int(args['<start>']),
        int(args['<stop>']),
        int(args['<step>'] or 1))
    polling = float(args['--interval']) if args['--polling'] else None
    converter.series(frames, polling=polling)


@command()
def poll(args, converter):
    """
    The poll command

    This command polls input files indefinitely from the input folder and
    processes them as they appear.

    """
    poller = count(
        int(args['<start>'] or 0),
        int(args['<step>'] or 1))
    converter.series(poller, polling=float(args['--interval']))


def default(args, converter):
    """
    This is the default action executed

    """
    index = int(args['<index>'] or 0)
    converter.single(index)
