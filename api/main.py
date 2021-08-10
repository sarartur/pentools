from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import PlainTextResponse
from typing import List

from . import (
    models, schemas, crud, enums, 
    params, formating
)
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Pen Tools API", 
    description="Pen Tools API delivers fast and reliable tools for every day pen testing.", 
    version="0.0.4",
    docs_url=None, redoc_url="/docs",
    contact={
        "name": "Artur Saradzhyan",
        "url": "https://github.com/sarartur",
        "email": "sarartur.ruk@gmail.com",
    },
    license_info={
        'name': 'MIT License',
        'url': 'https://github.com/sarartur/pentools/blob/master/LICENSE.txt'
    }
)

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@app.get('/types/{script_type}', response_model=List[schemas.ScriptType],
    description="Look up scripts by script type.")
async def script_types(
    script_type: enums.create_script_types_enum() = params.script_type,
    db: Session=Depends(get_db)
):
    script_types=crud.get_script_types(db, script_type)
    if not script_types:
        raise HTTPException(status_code=404, detail="No scripts of the specified type found.")
    return script_types

@app.get('/rev/{script_name}', response_model=schemas.Script,
    description="Look up and format reverse shell scripts by name.")
async def rev_scripts(
    script_name: enums.create_script_name_enum('rev')=params.script_name,
    host: str=params.host,
    port: int=params.port,
    shell: enums.Shell=params.shell,
    encoding: enums.Encoding=params.encoding,
    raw: bool=params.raw,
    db: Session=Depends(get_db)
):
    script = crud.get_scripts(db, type_='rev', script_name=script_name)
    if not script:
        raise HTTPException(status_code=404, detail="Script not found.")
    formating.format_code(script, encoding=encoding,
        host=host, port=port, shell=shell)
    if raw:
        return PlainTextResponse(content=script.code, status_code=200)
    return script

@app.get('/bind/{script_name}', response_model=schemas.Script,
    description="Look up and format bind shell scripts by name.")
async def bind_scripts(
    script_name: enums.create_script_name_enum('bind')=params.script_name,
    port: int=params.port,
    shell: enums.Shell=params.shell,
    encoding: enums.Encoding=params.encoding,
    raw: bool=params.raw,
    db: Session=Depends(get_db)
):
    script = crud.get_scripts(db, type_='bind', script_name=script_name)
    if not script:
        raise HTTPException(status_code=404, detail="Script not found")
    formating.format_code(script, encoding=encoding,
        port=port, shell=shell)
    if raw:
        return PlainTextResponse(content=script.code, status_code=200)
    return script

@app.get('/msf-venom/{script_name}', response_model=schemas.Script,
    description="Look up and format msf venom shell scripts by name.")
async def msf_scripts(
    script_name: enums.create_script_name_enum('msf_venom')=params.script_name,
    host: str=params.host,
    port: int=params.port,
    shell: enums.Shell=params.shell,
    encoding: enums.Encoding=params.encoding,
    raw: bool=params.raw,
    db: Session=Depends(get_db)
):
    script = crud.get_scripts(db, type_='msf_venom', script_name=script_name)
    if not script:
        raise HTTPException(status_code=404, detail="Script not found.")
    formating.format_code(script, encoding=encoding,
        host=host, port=port, shell=shell)
    if raw:
        return PlainTextResponse(content=script.code, status_code=200)
    return script

@app.get('/listener/{script_name}', response_model=schemas.Script,
    description="Look up and format listener scripts by name.")
async def listener_scripts(
    script_name: enums.create_script_name_enum('listener')=params.script_name,
    port: int=params.port,
    encoding: enums.Encoding=params.encoding,
    raw: bool=params.raw,
    db: Session=Depends(get_db),
):
    script = crud.get_scripts(db, type_='listener', script_name=script_name)
    if not script:
        raise HTTPException(status_code=404, detail="Script not found.")
    formating.format_code(script, encoding=encoding,
        port=port)
    if raw:
        return PlainTextResponse(content=script.code, status_code=200)
    return script


@app.get('/scripts', response_model=List[schemas.Script], 
    description="Filter scripts by operating system or id")
async def scripts(
    id: int=params.script_id,
    host: str=params.host,
    port: int=params.port,
    shell: enums.Shell=params.shell,
    encoding: enums.Encoding=params.encoding,
    os: enums.create_os_enum()=params.os,
    db: Session=Depends(get_db),
):
    scripts = crud.get_scripts(db, all_=True, id_=id, os=os)
    if not scripts:
        raise HTTPException(status_code=404, detail="Scripts not found.")
    for script in scripts:
        formating.format_code(script, encoding=encoding,
            host=host, port=port, shell=shell)
    return scripts



