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
