"""This module contains the AnalysisSubmissionResponse domain model."""

from pydantic import Field

from .analysis import AnalysisShort


class AnalysisSubmissionResponse(AnalysisShort):
    uuid: str
    api_version: str = Field(alias="apiVersion")
    harvey_version: str = Field(alias="harveyVersion")
    maru_version: str = Field(alias="maruVersion")
    mythril_version: str = Field(alias="mythrilVersion")
    queue_time: int = Field(alias="queueTime")
    status: str = Field(alias="status")
    submitted_at: str = Field(alias="submittedAt")
    submitted_by: str = Field(alias="submittedBy")


# class AnalysisSubmissionResponse(BaseResponse):
#     """The API response domain model for a successful analysis job
#     submission."""
#
#     with open(resolve_schema(__file__, "analysis-submission.json")) as sf:
#         schema = json.load(sf)
#
#     def __init__(self, analysis: Analysis):
#         self.analysis = analysis
#
#     @classmethod
#     def from_dict(cls, d) -> "AnalysisSubmissionResponse":
#         """Create the response domain model from a dict.
#
#         This also validates the dict's schema and raises a :code:`ValidationError`
#         if any required keys are missing or the data is malformed.
#
#         :param d: The dict to deserialize from
#         :return: The domain model with the data from :code:`d` filled in
#         """
#         cls.validate(d)
#         return cls(analysis=Analysis.from_dict(d))
#
#     def to_dict(self) -> Dict:
#         """Serialize the response model to a Python dict.
#
#         :return: A dict holding the request model data
#         """
#         d = self.analysis.to_dict()
#         self.validate(d)
#         return d
#
#     def __getattr__(self, name) -> Any:
#         """Return an attribute from the internal Analysis model."""
#         return getattr(self.analysis, name)
#
#     def __eq__(self, other: "AnalysisSubmissionResponse") -> bool:
#         return self.analysis == other.analysis
