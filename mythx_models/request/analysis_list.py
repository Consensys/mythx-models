"""This module contains the AnalysisListRequest domain model."""

from datetime import datetime
from typing import Optional

from pydantic import ConfigDict, BaseModel, Field


class AnalysisListRequest(BaseModel):
    offset: Optional[int] = None
    date_from: Optional[datetime] = Field(None, alias="dateFrom")
    date_to: Optional[datetime] = Field(None, alias="dateTo")
    created_by: Optional[str] = Field(None, alias="createdBy")
    group_name: Optional[str] = Field(None, alias="groupName")
    group_id: Optional[str] = Field(None, alias="groupId")
    main_source: Optional[str] = Field(None, alias="mainSource")
    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)

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
