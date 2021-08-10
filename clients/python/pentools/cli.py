import argparse
import pkg_resources

def _registered_commands(group):
    registered_commands = pkg_resources.iter_entry_points(group = group)
    return {c.name: c for c in registered_commands}

def dispatch(argv: list):
    registered_commands = _registered_commands(group = "pentools.registered_commands")
    parser = argparse.ArgumentParser(prog='pentools')
    parser.add_argument(
        'command',
        choices = registered_commands,
        help = 'The action pen tools should execute.'
    )
    parser.add_argument(
        "args", help = argparse.SUPPRESS, nargs = argparse.REMAINDER,
    )
    args = parser.parse_args(argv)
    main = registered_commands[args.command].load()
    return main(args = args.args)

def display(msg):
    print(msg)