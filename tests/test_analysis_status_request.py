from hypothesis import given

from mythx_models.request import AnalysisStatusRequest

from .strategies.analysis import analysis_status_request


@given(analysis_status_request())
def test_serde(response):
    resp = AnalysisStatusRequest(**response)
    assert resp.dict(by_alias=True) == response


@given(analysis_status_request())
def test_attributes(request):
    parsed = AnalysisStatusRequest(**request)

    assert parsed.dict(by_alias=True) == request
    assert parsed.headers == {}
    assert parsed.payload == {}
    assert parsed.method == "GET"
    assert parsed.endpoint == f"v1/analyses/{parsed.uuid}"
    assert parsed.parameters == {}
