"""This module contains the AuthLogoutRequest domain model."""

from pydantic import BaseModel, Field


class GroupCreationRequest(BaseModel):
    group_name: str = Field(alias="groupName")

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
