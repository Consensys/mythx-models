from typing import List

from pydantic import BaseModel

from .project import Project


class ProjectListResponse(BaseModel):
    projects: List[Project]
    total: int
