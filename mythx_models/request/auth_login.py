"""This module contains the AuthLoginRequest domain model."""

from pydantic import BaseModel


class AuthLoginRequest(BaseModel):
    username: str
    password: str

    @property
    def endpoint(self):
        return "v1/auth/login"

    @property
    def method(self):
        return "POST"

    @property
    def payload(self):
        return {"username": self.username, "password": self.password}

    @property
    def headers(self):
        return {}

    @property
    def parameters(self):
        return {}
