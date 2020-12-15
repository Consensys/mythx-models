from hypothesis import given

from mythx_models.request import GroupOperationRequest

from .strategies.group import group_operation_request


@given(group_operation_request())
def test_serde(response):
    obj = GroupOperationRequest(**response)
    assert obj.dict(by_alias=True) == response


@given(group_operation_request())
def test_attributes(request):
    parsed = GroupOperationRequest(**request)

    assert parsed.dict(by_alias=True) == request
    assert parsed.headers == {}
    assert parsed.payload == {"type": parsed.type_}
    assert parsed.method == "POST"
    assert parsed.endpoint == f"v1/analysis-groups/{parsed.group_id}"
    assert parsed.parameters == {}
