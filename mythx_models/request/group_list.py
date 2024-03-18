"""This module contains the GroupListRequest domain model."""

from datetime import datetime
from typing import Optional

from pydantic import ConfigDict, BaseModel, Field


class GroupListRequest(BaseModel):
    offset: Optional[int] = None
    created_by: Optional[str] = Field(None, alias="createdBy")
    group_name: Optional[str] = Field(None, alias="groupName")
    date_from: Optional[datetime] = Field(None, alias="dateFrom")
    date_to: Optional[datetime] = Field(None, alias="dateTo")
    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)

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
