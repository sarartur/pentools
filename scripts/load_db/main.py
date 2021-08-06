from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import sys
sys.path.append('../')

import api.models as models
from . import code

DB_PATH = "../app.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
models.Base.metadata.create_all(bind=engine)
db = SessionLocal()

description_mapping = {
    'rev': 'Shell session established on a connection that is initiated from a remote machine.',
    'bind': 'Shell session set up on the target host and binds to a specific port to listens for an incoming connection from the attack box.',
    'msf_venom': 'Used to generate and output all of the various types of shell code that are available in Metasploit.',
    'listener': 'Used to catch the incoming connect from a reverse shell'
}

def create_scripts(script_type_name):
    if not description_mapping.get(script_type_name):
        raise Exception('Invalid script_type_name')
    script_type = db.query(models.ScriptType).filter(models.ScriptType.name == script_type_name).first()
    if not script_type:
        script_type = models.ScriptType(
            name = script_type_name,
            description = description_mapping[script_type_name])
        db.add(script_type)
        db.commit()
    for c in getattr(code, script_type_name):
        if db.query(models.Script).filter(models.Script.name == c['name']).first():
            continue
        script = models.Script(name = c['name'], code = c['command'], script_type_id = script_type.id)
        db.add(script)
        db.commit()
        meta = c.get('meta')
        if meta:
            os_ids = []
            for m in meta:
                os = db.query(models.OperatingSystem).filter(models.OperatingSystem.name == m).first()
                if not os:
                    os = models.OperatingSystem(name = m)
                    db.add(os)
                    db.commit()
                os_ids.append(os.id)
            for id_ in os_ids:
                db.add(models.OsScriptAssoc(script_id = script.id, os_id = id_))
            db.commit()

def create_all():
    create_scripts('rev')
    create_scripts('bind')
    create_scripts('msf_venom')
    create_scripts('listener')

def delete_db():
    os.remove(DB_PATH)
