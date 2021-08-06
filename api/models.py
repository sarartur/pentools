from enum import unique
import uuid
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
from uuid import uuid4
from datetime import datetime
from pytz import timezone

from .database import Base

tz_est = timezone('US/Eastern')

class StBase(object):
    id = Column(Integer, primary_key=True, unique=True)
    pid = Column(String(50), default=lambda: str(uuid4()))
    timestamp = Column(DateTime, default=datetime.now(tz_est))

class ScriptType(Base, StBase):
    __tablename__ = "script_type"

    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(10_000), nullable=False)
    scripts = relationship('Script',
        backref="script_type")

class Script(Base, StBase):
    __tablename__ = "script"

    name = Column(String(50), nullable=False)
    code = Column(Text, nullable=False)
    script_type_id = Column(Integer, ForeignKey('script_type.id'))
    operating_systems = relationship('OperatingSystem', 
        secondary="os_script_assoc", backref="scripts")

class OsScriptAssoc(Base, StBase):
    __tablename__ = 'os_script_assoc'

    script_id = Column(Integer, ForeignKey('script.id'))
    os_id = Column(Integer, ForeignKey('operating_system.id'))

class OperatingSystem(Base, StBase):
    __tablename__ = 'operating_system'

    name = Column(String(50), nullable=False)



