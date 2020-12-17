"""This module contains the GroupOperation domain model."""

from pydantic import BaseModel, Field


class GroupOperationRequest(BaseModel):
    group_id: str = Field(alias="groupId")
    type_: str = Field(alias="type")

    class Config:
        allow_population_by_field_name = True
        use_enum_values = True

    @property
    def endpoint(self):
        return "v1/analysis-groups/{}".format(self.group_id)

    @property
    def method(self):
        return "POST"

    @property
    def payload(self):
        return {"type": self.type_}

    @property
    def headers(self):
        return {}

    @property
    def parameters(self):
        return {}
