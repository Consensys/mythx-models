from datetime import datetime

from pydantic import BaseModel


class Project(BaseModel):
    id: str
    name: str
    description: str
    created: datetime
    modified: datetime
