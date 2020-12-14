from hypothesis import given

from mythx_models.request import AuthLogoutRequest

from .strategies.auth import auth_logout_request


@given(auth_logout_request())
def test_serde(response):
    resp = AuthLogoutRequest(**response)
    assert resp.dict(by_alias=True) == response
