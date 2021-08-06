from sqlalchemy.sql.functions import mode
from . import models

def get_scripts(db, all_=False, id_=None, type_=None, script_name=None,
    os=None):
    query = db.query(models.Script)
    if id_:
        query = query.filter(models.Script.id == id_)
    if type_:
        query = query.join(models.ScriptType).filter(models.Script.name == script_name)
    if script_name:
        query = query.filter(models.ScriptType.name == type_)
    if os:
        query = query.join(models.OperatingSystem, models.Script.operating_systems)\
            .filter(models.OperatingSystem.name == os)
    return query.all() if all_ else query.first()

def get_script_types(db, script_type_name = None):
    query = db.query(models.ScriptType)
    if not script_type_name or script_type_name == "all":
        return query.all()
    query = query.filter(models.ScriptType.name == script_type_name)
    return query.all()