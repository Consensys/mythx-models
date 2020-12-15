from hypothesis import given

from mythx_models.request import AnalysisInputRequest

from .strategies.analysis import analysis_input_request


@given(analysis_input_request())
def test_serde(request):
    resp = AnalysisInputRequest(**request)
    assert resp.dict(by_alias=True) == request


@given(analysis_input_request())
def test_attributes(request):
    parsed = AnalysisInputRequest(**request)

    assert parsed.dict() == request
    assert parsed.headers == {}
    assert parsed.payload == {}
    assert parsed.method == "GET"
    assert parsed.endpoint == f"v1/analyses/{parsed.uuid}/input"
    assert parsed.parameters == {}
