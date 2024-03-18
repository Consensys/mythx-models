from hypothesis import given

from mythx_models.response import AnalysisListResponse

from .strategies.analysis import analysis_list_response


@given(analysis_list_response())
def test_serde(response):
    resp = AnalysisListResponse(**response)
    assert resp.model_dump(by_alias=True) == response
