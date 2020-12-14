"""This module contains the AnalysisSubmissionResponse domain model."""

from pydantic import Field

from .analysis import AnalysisShort


class AnalysisSubmissionResponse(AnalysisShort):
    pass
