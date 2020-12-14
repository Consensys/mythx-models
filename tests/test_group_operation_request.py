from hypothesis import given

from mythx_models.request import GroupOperationRequest

from .strategies.group import group_operation_request


@given(group_operation_request())
def test_serde(response):
    obj = GroupOperationRequest(**response)
    assert obj.dict(by_alias=True) == response
