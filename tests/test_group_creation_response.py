from hypothesis import given

from mythx_models.response import GroupCreationResponse

from .strategies.group import group_creation_response


@given(group_creation_response())
def test_serde(response):
    obj = GroupCreationResponse(**response)
    assert obj.dict(by_alias=True) == response
