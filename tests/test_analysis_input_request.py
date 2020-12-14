from hypothesis import given

from mythx_models.request import AnalysisInputRequest

from .strategies.analysis import analysis_input_request


@given(analysis_input_request())
def test_serde(response):
    resp = AnalysisInputRequest(**response)
    assert resp.dict(by_alias=True) == response
