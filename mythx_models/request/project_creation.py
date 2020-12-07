from typing import List

from pydantic import BaseModel, Field


class ProjectCreationRequest(BaseModel):
    name: str
    description: str
    groups: List[str] = Field(default_factory=list)

    @property
    def endpoint(self):
        return "v1/projects"

    @property
    def method(self):
        return "POST"

    @property
    def payload(self):
        return {
            "name": self.name,
            "description": self.description,
            "groups": self.groups,
        }

    @property
    def headers(self):
        return {}

    @property
    def parameters(self):
        return {}
