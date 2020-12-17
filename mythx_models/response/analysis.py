"""This module contains domain models regarding analysis jobs."""

import logging
from enum import Enum

from pydantic import BaseModel, Field

from mythx_models.response.group import VulnerabilityStatistics

LOGGER = logging.getLogger(__name__)


class AnalysisStatus(str, Enum):
    """An Enum describing the status an analysis job can be in."""

    QUEUED = "Queued"
    IN_PROGRESS = "In Progress"
    ERROR = "Error"
    FINISHED = "Finished"


class AnalysisShort(BaseModel):
    uuid: str
    api_version: str = Field(alias="apiVersion")
    harvey_version: str = Field(alias="harveyVersion")
    maru_version: str = Field(alias="maruVersion")
    mythril_version: str = Field(alias="mythrilVersion")
    queue_time: int = Field(alias="queueTime")
    run_time: int = Field(alias="runTime")
    status: str = Field(alias="status")
    submitted_at: str = Field(alias="submittedAt")
    submitted_by: str = Field(alias="submittedBy")
    client_tool_name: str = Field(alias="clientToolName")
    group_id: str = Field(alias="groupId")
    group_name: str = Field(alias="groupName")
    analysis_mode: str = Field(alias="analysisMode")

    class Config:
        allow_population_by_field_name = True
        use_enum_values = True


class Analysis(BaseModel):
    uuid: str
    api_version: str = Field(alias="apiVersion")
    mythril_version: str = Field(alias="mythrilVersion")
    harvey_version: str = Field(alias="harveyVersion")
    maru_version: str = Field(alias="maruVersion")
    queue_time: int = Field(alias="queueTime")
    status: str
    submitted_at: str = Field(alias="submittedAt")
    submitted_by: str = Field(alias="submittedBy")
    main_source: str = Field(alias="mainSource")
    num_sources: str = Field(alias="numSources")
    vulnerability_statistics: VulnerabilityStatistics = Field(
        alias="numVulnerabilities"
    )
    run_time: int = Field(alias="runTime")
    client_tool_name: str = Field(alias="clientToolName")
    group_id: str = Field(alias="groupId")
    analysis_mode: str = Field(alias="analysisMode")
    group_name: str = Field(alias="groupName")
    upgraded: bool
    property_checking: bool = Field(alias="propertyChecking")

    error: str = None
    info: str = None

    class Config:
        allow_population_by_field_name = True
        use_enum_values = True
