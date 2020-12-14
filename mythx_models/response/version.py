"""This module contains the VersionResponse domain model."""

from pydantic import BaseModel


class VersionResponse(BaseModel):
    api: str
    hash: str
    harvey: str
    maru: str
    mythril: str
