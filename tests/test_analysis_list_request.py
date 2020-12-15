from hypothesis import given

from mythx_models.request import AnalysisListRequest

from .strategies.analysis import analysis_list_request


@given(analysis_list_request())
def test_serde(response):
    resp = AnalysisListRequest(**response)
    assert resp.dict(by_alias=True) == response


@given(analysis_list_request())
def test_attributes(request):
    parsed = AnalysisListRequest(**request)

    assert parsed.dict(by_alias=True) == request
    assert parsed.headers == {}
    assert parsed.payload == {}
    assert parsed.method == "GET"
    assert parsed.endpoint == "v1/analyses"
    assert parsed.parameters["createdBy"] == request["createdBy"]
    assert parsed.parameters["groupId"] == request["groupId"]
    assert parsed.parameters["groupName"] == request["groupName"]
    assert parsed.parameters["mainSource"] == request["mainSource"]
    assert parsed.parameters["offset"] == request["offset"]
