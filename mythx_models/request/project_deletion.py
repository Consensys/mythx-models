from pydantic import BaseModel


class ProjectDeleteRequest(BaseModel):
    project_id: str

    @property
    def endpoint(self):
        return f"v1/projects/{self.project_id}"

    @property
    def method(self):
        return "DELETE"

    @property
    def payload(self):
        return {}

    @property
    def headers(self):
        return {}

    @property
    def parameters(self):
        return {}
