from hypothesis import given

from mythx_models.response import AnalysisSubmissionResponse

from .strategies.analysis import analysis_status


@given(analysis_status())
def test_serde(response):
    resp = AnalysisSubmissionResponse(**response)
    assert resp.model_dump(by_alias=True) == response
