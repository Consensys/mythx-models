"""This module contains the AnalysisListResponse domain model."""


from typing import List

from pydantic import BaseModel

from .analysis import AnalysisShort


class AnalysisListResponse(BaseModel):
    analyses: List[AnalysisShort]
    total: int
