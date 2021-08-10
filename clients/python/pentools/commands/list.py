import argparse

from ..settings import Settings
from ..client import Client
from ..types.exceptions import PenToolsException
from .. import cli
from .. import responses

def list_(settings):
    client = Client(**settings)
    response = client.get_script_types(**settings)
    if response.err:
        raise PenToolsException(response.data)
    return responses.create_types_message(response.data, settings.full)

def main(args):
    parser = argparse.ArgumentParser(
        prog="pentools list",
        description="Lists avaliable script types.",
    )
    group = parser.add_argument_group()
    group.add_argument(
        "script_type",
        nargs='?',
        help=f"The type of scripts to be listed. Leave blank to see options",
    )
    group.add_argument(
        "-f", "--full",
        action="store_true",
        help="Shows description and avaliable scripts."
    )
    to_console = list_(settings=Settings(**vars(parser.parse_args(args))))
    cli.display(to_console)


