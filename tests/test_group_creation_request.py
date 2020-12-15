from hypothesis import given

from mythx_models.request import GroupCreationRequest

from .strategies.group import group_creation_request


@given(group_creation_request())
def test_serde(response):
    obj = GroupCreationRequest(**response)
    assert obj.dict(by_alias=True) == response


@given(group_creation_request())
def test_attributes(request):
    parsed = GroupCreationRequest(**request)

    assert parsed.dict(by_alias=True) == {"groupName": parsed.group_name}
    assert parsed.headers == {}
    assert parsed.payload == {"groupName": parsed.group_name}
    assert parsed.method == "POST"
    assert parsed.endpoint == f"v1/analysis-groups"
    assert parsed.parameters == {}
