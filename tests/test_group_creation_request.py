from hypothesis import given

from mythx_models.request import GroupCreationRequest

from .strategies.group import group_creation_request


@given(group_creation_request())
def test_serde(response):
    obj = GroupCreationRequest(**response)
    assert obj.dict(by_alias=True) == response
