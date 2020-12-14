from hypothesis import given

from mythx_models.request import AnalysisListRequest

from .strategies.analysis import analysis_list_request


@given(analysis_list_request())
def test_serde(response):
    resp = AnalysisListRequest(**response)
    assert resp.dict(by_alias=True) == response
