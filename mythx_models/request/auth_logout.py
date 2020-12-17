"""This module contains the AuthLogoutRequest domain model."""

from pydantic import BaseModel, Field


class AuthLogoutRequest(BaseModel):
    global_: bool = Field(alias="global")

    @property
    def endpoint(self):
        return "v1/auth/logout"

    @property
    def method(self):
        return "POST"

    @property
    def payload(self):
        return {"global": self.global_}

    @property
    def headers(self):
        return {}

    @property
    def parameters(self):
        return {}
