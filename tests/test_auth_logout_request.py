from hypothesis import given

from mythx_models.request import AuthLogoutRequest

from .strategies.auth import auth_logout_request


@given(auth_logout_request())
def test_serde(response):
    resp = AuthLogoutRequest(**response)
    assert resp.dict(by_alias=True) == response


@given(auth_logout_request())
def test_attributes(request):
    parsed = AuthLogoutRequest(**request)

    assert parsed.dict(by_alias=True) == request
    assert parsed.headers == {}
    assert parsed.payload == request
    assert parsed.method == "POST"
    assert parsed.endpoint == f"v1/auth/logout"
    assert parsed.parameters == {}
