from hypothesis import given

from mythx_models.request import AuthLoginRequest

from .strategies.auth import auth_login_request


@given(auth_login_request())
def test_serde(response):
    obj = AuthLoginRequest(**response)
    assert obj.dict(by_alias=True) == {
        "password": obj.password,
        "username": obj.username,
    }


@given(auth_login_request())
def test_attributes(request):
    parsed = AuthLoginRequest(**request)
    reduced_payload = {"password": request["password"], "username": request["username"]}

    assert parsed.dict(by_alias=True) == reduced_payload
    assert parsed.headers == {}
    assert parsed.payload == reduced_payload
    assert parsed.method == "POST"
    assert parsed.endpoint == f"v1/auth/login"
    assert parsed.parameters == {}
