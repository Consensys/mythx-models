from hypothesis import given

from mythx_models.request import AnalysisSubmissionRequest

from .strategies.analysis import analysis_submission


@given(analysis_submission())
def test_serde(request):
    parsed = AnalysisSubmissionRequest(**request)
    assert {
        k: v for k, v in parsed.dict(by_alias=True).items() if v is not None
    } == request


@given(analysis_submission())
def test_attributes(request):
    parsed = AnalysisSubmissionRequest(**request)

    assert {
        k: v for k, v in parsed.dict(by_alias=True).items() if v is not None
    } == request
    assert parsed.headers == {}
    assert parsed.payload == {"data": request}
    assert parsed.method == "POST"
    assert parsed.endpoint == f"v1/analyses"
    assert parsed.parameters == {}
