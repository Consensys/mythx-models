"""This module contains the AnalysisListRequest domain model."""

from datetime import datetime

from pydantic import BaseModel, Field


class AnalysisListRequest(BaseModel):
    offset: int
    date_from: datetime = Field(alias="dateFrom")
    date_to: datetime = Field(alias="dateTo")
    created_by: str = Field(alias="createdBy")
    group_name: str = Field(alias="groupName")
    group_id: str = Field(alias="groupId")
    main_source: str = Field(alias="mainSource")

    @property
    def endpoint(self):
        return "v1/analyses"

    @property
    def method(self):
        return "GET"

    @property
    def payload(self):
        return {}

    @property
    def headers(self):
        return {}

    @property
    def parameters(self):
        return {
            "offset": self.offset,
            "dateFrom": self.date_from.isoformat() if self.date_from else None,
            "dateTo": self.date_from.isoformat() if self.date_from else None,
            "createdBy": self.created_by,
            "groupName": self.group_name,
            "groupId": self.group_id,
            "mainSource": self.main_source,
        }

