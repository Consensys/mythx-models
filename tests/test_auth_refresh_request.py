from hypothesis import given

from mythx_models.request import AuthRefreshRequest

from .strategies.auth import auth_refresh_request


@given(auth_refresh_request())
def test_serde(response):
    obj = AuthRefreshRequest(**response)
    assert obj.dict(by_alias=True) == {
        "accessToken": response["accessToken"],
        "refreshToken": response["refreshToken"],
    }
