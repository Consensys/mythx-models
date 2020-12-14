"""This module contains the GroupListResponse domain model."""

from typing import List

from pydantic import BaseModel

from .group import Group


class GroupListResponse(BaseModel):
    groups: List[Group]
    total: int
