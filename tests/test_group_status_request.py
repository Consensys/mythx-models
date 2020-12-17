from hypothesis import given

from mythx_models.request import GroupStatusRequest

from .strategies.group import group_status_request


@given(group_status_request())
def test_serde(response):
    obj = GroupStatusRequest(**response)
    assert obj.dict(by_alias=True) == response


@given(group_status_request())
def test_attributes(request):
    parsed = GroupStatusRequest(**request)

    assert parsed.dict(by_alias=True) == request
    assert parsed.headers == {}
    assert parsed.payload == {}
    assert parsed.method == "GET"
    assert parsed.endpoint == f"v1/analysis-groups/{parsed.group_id}"
    assert parsed.parameters == {}
