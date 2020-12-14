from hypothesis import given

from mythx_models.request import AnalysisStatusRequest

from .strategies.analysis import analysis_status_request


@given(analysis_status_request())
def test_serde(response):
    resp = AnalysisStatusRequest(**response)
    assert resp.dict(by_alias=True) == response
