"""This module contains the AuthRefreshRequest domain model."""

from pydantic import BaseModel, Field


class AuthRefreshRequest(BaseModel):
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")

    @property
    def endpoint(self):
        return "v1/auth/refresh"

    @property
    def method(self):
        return "POST"

    @property
    def payload(self):
        return {
            "jwtTokens": {"access": self.access_token, "refresh": self.refresh_token}
        }

    @property
    def headers(self):
        return {}

    @property
    def parameters(self):
        return {}
