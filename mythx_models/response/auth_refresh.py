"""This module contains the AuthRefreshResponse domain model."""

from pydantic import BaseModel, Field


class AuthRefreshResponse(BaseModel):
    access_token: str = Field(alias="access")
    refresh_token: str = Field(alias="refresh")

    class Config:
        allow_population_by_field_name = True
        use_enum_values = True
