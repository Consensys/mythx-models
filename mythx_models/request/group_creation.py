"""This module contains the AuthLogoutRequest domain model."""

from typing import Optional

from pydantic import BaseModel, Field


class GroupCreationRequest(BaseModel):
    group_name: Optional[str] = Field(alias="groupName")

    class Config:
        allow_population_by_field_name = True
        use_enum_values = True

    @property
    def endpoint(self):
        return "v1/analysis-groups"

    @property
    def method(self):
        return "POST"

    @property
    def payload(self):
        return {"groupName": self.group_name}

    @property
    def headers(self):
        return {}

    @property
    def parameters(self):
        return {}
