from hypothesis import given

from mythx_models.request import GroupListRequest

from .strategies.group import group_list_request


@given(group_list_request())
def test_serde(response):
    obj = GroupListRequest(**response)
    assert obj.dict(by_alias=True) == response
