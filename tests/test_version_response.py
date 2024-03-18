from hypothesis import given

from mythx_models.response import VersionResponse

from .strategies.version import version_response


@given(version_response())
def test_serde(response):
    resp = VersionResponse(**response)
    assert resp.model_dump(by_alias=True) == response
