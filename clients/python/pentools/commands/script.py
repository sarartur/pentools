import argparse

from ..settings import Settings
from ..client import Client
from .. import cli
from .. import responses
from ..types.exceptions import PenToolsException

def script(settings):
    client = Client(**settings)
    response = client.get_script_by_id(**settings)
    if response.err:
        raise PenToolsException(response.data)
    return responses.create_script_message(response.data[0], settings.full)

def main(args):
    parser = argparse.ArgumentParser(
        prog="pentools script",
        description="Look up and format script")
    parser.add_argument(
        "-i", "--id",
        type=int,
        dest='script_id',
        help="Script id.",
        required=True)
    parser.add_argument(
        "-p", "--port",
        type=int,
        help="The port the listener will listen on.")
    parser.add_argument(
        "-ho", "--host",
        type=str,
        help="The host name / address.")
    parser.add_argument(
        "-e", "--encoding",
        type=str,
        help="The encoding of the script.")
    parser.add_argument(
        "-s", "--shell",
        type=str,
        help="shell to pipe into.")
    parser.add_argument(
        "-f", "--full",
        action="store_true",
        help="Shows operating systems, name and id of script.")
    to_console = script(settings=Settings(**vars(parser.parse_args(args))))
    cli.display(to_console)


