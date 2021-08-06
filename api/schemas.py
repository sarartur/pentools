from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel

class OperatingSystem(BaseModel):
    name: str

    class Config:
        orm_mode = True

class Script(BaseModel):
    id: int
    timestamp: datetime
    name: str
    code: str
    operating_systems: Optional[List[OperatingSystem]] = []

    class Config:
        orm_mode = True

class ScriptType(BaseModel):
    id: int
    timestamp: datetime
    name: str
    description: str
    scripts: Optional[List[Script]] = []

    class Config:
        orm_mode = True

