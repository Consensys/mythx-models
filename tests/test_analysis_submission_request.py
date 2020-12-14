from hypothesis import given

from mythx_models.request import AnalysisSubmissionRequest

from .strategies.analysis import analysis_submission


@given(analysis_submission())
def test_serde(request):
    parsed = AnalysisSubmissionRequest(**request)
    assert {
        k: v for k, v in parsed.dict(by_alias=True).items() if v is not None
    } == request
