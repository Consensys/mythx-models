from typing import List

from pydantic import BaseModel

from .project import ShortProject


class ProjectListResponse(BaseModel):
    projects: List[ShortProject]
    total: int
