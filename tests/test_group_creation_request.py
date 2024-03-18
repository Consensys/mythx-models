from hypothesis import given

from mythx_models.request import GroupCreationRequest

from .strategies.group import group_creation_request


@given(group_creation_request())
def test_serde(response):
    obj = GroupCreationRequest(**response)
    assert obj.model_dump(by_alias=True) == response


@given(group_creation_request())
def test_attributes(request):
    parsed = GroupCreationRequest(**request)

    assert parsed.model_dump(by_alias=True) == {"groupName": parsed.group_name}
    assert parsed.headers == {}
    assert parsed.payload == {"groupName": parsed.group_name}
    assert parsed.method == "POST"
    assert parsed.endpoint == "v1/analysis-groups"
    assert parsed.parameters == {}
