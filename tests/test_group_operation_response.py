from hypothesis import given

from mythx_models.response import GroupOperationResponse

from .strategies.group import group_operation_response


@given(group_operation_response())
def test_serde(response):
    obj = GroupOperationResponse(**response)
    assert obj.dict(by_alias=True) == response
