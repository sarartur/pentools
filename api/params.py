from fastapi import Path, Query
from sqlalchemy.sql.expression import desc

from . import enums

script_name = Path(..., 
    title="Script Name",
    description="Name of the script.")
script_type = Path(...,
    title="Script Type",
    description="The type of scripts."
)

script_id = Query(None,
    title="Script id",
    description="The id of the script."
)
raw = Query(False,
    title="Raw",
    description="Plain text response format.")
shell = Query(enums.Shell.bin_bash, 
    title="Shell",
    description="Shell to pipe into.")
host = Query('8.8.8.8', 
    title="Host",
    description="Host name of the listener.")
encoding = Query(enums.Encoding.utf_8,
    title="Encoding",
    description="Encoding of the code.")
port = Query(8000,
    title="Port",
    description="The port the listener will listen on.",
    min = 1024, max = 65535 )
os = Query(None,
    title="Operating system",
    description="The name of the operating system.")
