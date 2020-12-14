from hypothesis import given

from mythx_models.response import VersionResponse

from .strategies.version import version_response


@given(version_response())
def test_serde(response):
    resp = VersionResponse(**response)
    assert resp.dict(by_alias=True) == response
