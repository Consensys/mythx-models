"""This module contains domain models regarding analysis jobs."""

import logging
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field

LOGGER = logging.getLogger(__name__)


class GroupStatistics(BaseModel):
    total: int
    queued: int
    running: int
    failed: int
    finished: int


class VulnerabilityStatistics(BaseModel):
    high: int
    medium: int
    low: int
    none: int


class GroupState(str, Enum):
    """An Enum describing the status of an analysis group."""

    OPENED = "opened"
    SEALED = "sealed"


class Group(BaseModel):
    """An object describing an analysis group.

    Such a model was built, because many other API responses deliver the
    same data when it comes to analysis groups. This makes the code more
    DRY, validation easier, and allows for recursive SerDe (e.g. mapping
    :code:`from_dict` to a deserialized JSON list of job objects.
    """

    identifier: str = Field(alias="id")
    name: str
    created_at: str = Field(alias="createdAt")
    created_by: str = Field(alias="createdBy")
    completed_at: str = Field(alias="completedAt")
    progress: int
    status: GroupState
    main_source_files: List[str] = Field(alias="mainSourceFiles")
    analysis_statistics: GroupStatistics = Field(alias="numAnalyses")
    vulnerability_statistics: VulnerabilityStatistics = Field(
        alias="numVulnerabilities"
    )
    project_id: Optional[str] = Field(alias="projectId")

    class Config:
        allow_population_by_field_name = True
        use_enum_values = True
