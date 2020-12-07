from typing import Optional

from pydantic import BaseModel


class ProjectListRequest(BaseModel):
    offset: int = 0
    limit: int = 0
    name: Optional[str] = None

    @property
    def endpoint(self):
        return "v1/projects"

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
        return {"offset": self.offset, "limit": self.limit, "name": self.name}
