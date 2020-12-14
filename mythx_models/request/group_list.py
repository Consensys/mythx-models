"""This module contains the GroupListRequest domain model."""

from datetime import datetime

from pydantic import BaseModel, Field


class GroupListRequest(BaseModel):
    offset: int
    created_by: str = Field(alias="createdBy")
    group_name: str = Field(alias="groupName")
    date_from: datetime = Field(alias="dateFrom")
    date_to: datetime = Field(alias="dateTo")

    @property
    def endpoint(self):
        return "v1/analysis-groups"

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
            "createdBy": self.created_by,
            "groupName": self.group_name,
            "dateFrom": self.date_from.isoformat() if self.date_from else None,
            "dateTo": self.date_to.isoformat() if self.date_to else None,
        }

