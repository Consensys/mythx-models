"""This module contains the AnalysisStatusRequest domain model."""

from pydantic import BaseModel


class AnalysisStatusRequest(BaseModel):
    uuid: str

    @property
    def endpoint(self):
        return "v1/analyses/{}".format(self.uuid)

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
