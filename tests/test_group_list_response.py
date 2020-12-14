from hypothesis import given

from mythx_models.response import GroupListResponse

from .strategies.group import group_list_response


@given(group_list_response())
def test_serde(response):
    obj = GroupListResponse(**response)
    assert obj.dict(by_alias=True) == response
