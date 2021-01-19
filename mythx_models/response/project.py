from datetime import datetime

from pydantic import BaseModel


class ShortProject(BaseModel):
    id: str
    name: str
    created: datetime
    group_count: int
    modified: datetime


class Project(BaseModel):
    id: str
    name: str
    description: str
    created: datetime
    modified: datetime
