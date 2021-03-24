"""This module contains the GroupOperation domain model."""

from pydantic import BaseModel, Field
from typing import Optional

class GroupOperationRequest(BaseModel):
    group_id: str = Field(alias="groupId")
    type_: str = Field(alias="type")
    project_id: Optional[str] = Field(alias="projectId")

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
        payload = {"type": self.type_}
        if self.type_ == "add_to_project":
            payload["projectId"] = self.project_id
        return payload

    @property
    def headers(self):
        return {}

    @property
    def parameters(self):
        return {}
