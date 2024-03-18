"""This module contains the AuthLoginResponse domain model."""

from pydantic import ConfigDict, BaseModel, Field


class AuthLoginResponse(BaseModel):
    access_token: str = Field(alias="access")
    refresh_token: str = Field(alias="refresh")
    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)
