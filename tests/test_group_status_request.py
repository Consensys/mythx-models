from hypothesis import given

from mythx_models.request import GroupStatusRequest

from .strategies.group import group_status_request


@given(group_status_request())
def test_serde(response):
    obj = GroupStatusRequest(**response)
    assert obj.dict(by_alias=True) == response
