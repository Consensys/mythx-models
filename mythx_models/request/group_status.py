"""This module contains the GroupRequest domain model."""

from pydantic import BaseModel, Field


class GroupStatusRequest(BaseModel):
    group_id: str = Field(alias="groupId")

    class Config:
        allow_population_by_field_name = True
        use_enum_values = True

    @property
    def endpoint(self):
        return "v1/analysis-groups/{}".format(self.group_id)

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
        return {}
