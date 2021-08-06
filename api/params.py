from fastapi import Path, Query
from sqlalchemy.sql.expression import desc

from . import enums

script_name = Path(..., 
    title="Script Name",
    description="Name of the script.",
    example="python_1")
script_type = Path(...,
    title="Script Type",
    description="The type of scripts.",
    example="rev"
)

script_id = Query(None,
    title="Script id",
    description="The id of the script.",
    example=1
)
raw = Query(False,
    title="Raw",
    description="Plain text response format.",
    example='1')
shell = Query(enums.Shell.bin_bash, 
    title="Shell",
    description="Shell to pipe into.",
    example="bin/bash")
host = Query('8.8.8.8', 
    title="Host",
    description="Host name of the listener.",
    example="8.8.8.8")
encoding = Query(enums.Encoding.utf_8,
    title="Encoding",
    description="Encoding of the code.",
    example="utf-8")
port = Query(8000,
    title="Port",
    description="The port the listener will listen on.",
    min = 1024, max = 65535,
    example=8000)
os = Query(None,
    title="Operating system",
    description="The name of the operating system.",
    example="linux")
