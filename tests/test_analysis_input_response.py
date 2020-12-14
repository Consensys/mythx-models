from hypothesis import given

from mythx_models.response import AnalysisInputResponse

from .strategies.analysis import analysis_submission


@given(analysis_submission())
def test_serde(request):
    parsed = AnalysisInputResponse(**request)
    assert {
        k: v for k, v in parsed.dict(by_alias=True).items() if v is not None
    } == request
