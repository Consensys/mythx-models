from hypothesis import given

from mythx_models.response import GroupStatusResponse

from .strategies.group import group_status_response


@given(group_status_response())
def test_serde(response):
    obj = GroupStatusResponse(**response)
    assert obj.dict(by_alias=True) == response
