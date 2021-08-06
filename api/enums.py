from enum import Enum

from pydantic.errors import ListError

from . import models as m
from .database import SessionLocal
from .utils import underscore_to_camelcase

class StringEnum(str, Enum):
    def __str__(self):
        return str(self.value)

def create_script_name_enum(script_type_name):
    db = SessionLocal()
    script_type = db.query(m.ScriptType).filter(m.ScriptType.name == script_type_name).first()
    enum =  StringEnum(
        f'Script{underscore_to_camelcase(script_type_name)}', 
        {script.name: script.name for script in script_type.scripts})
    db.close()
    return enum

def create_script_types_enum():
    db = SessionLocal()
    script_types = db.query(m.ScriptType).all()
    load_dict = {script_type.name: script_type.name for script_type in script_types}
    load_dict['all'] = 'all'
    enum = StringEnum("ScriptType", load_dict)
    db.close()
    return enum

def create_os_enum():
    db = SessionLocal()
    operating_systems = db.query(m.OperatingSystem).all()
    load_dict = {os.name: os.name for os in operating_systems}
    enum = StringEnum("OperatingSystem", load_dict)
    db.close()
    return enum

class Shell(StringEnum):
    sh = "sh"
    bin_sh = "bin/sh"
    bash = "bash"
    bin_bash = "bin/bash"
    cmd = "cmd"
    powershell = "powershell"
    ash = "ash"
    bsh = "bsh"
    csh = "csh"
    ksh = "ksh"
    zsh = "zsh"
    pdksh = "pdksh"
    tcsh = "tcsh"

class Encoding(StringEnum):
    utf_8 = 'utf-8'
    url = "url"
    base64 = "base64"
