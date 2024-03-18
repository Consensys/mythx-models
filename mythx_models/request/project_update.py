from typing import Optional

from pydantic import BaseModel


class ProjectUpdateRequest(BaseModel):
    project_id: str
    name: Optional[str] = None
    description: Optional[str] = None

    @property
    def endpoint(self):
        return f"v1/projects/{self.project_id}"

    @property
    def method(self):
        return "POST"

    @property
    def payload(self):
        return {"name": self.name, "description": self.description}

    @property
    def headers(self):
        return {}

    @property
    def parameters(self):
        return {}
