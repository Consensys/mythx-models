from hypothesis import given

from mythx_models.response import AuthRefreshResponse

from .strategies.auth import auth_refresh_response


@given(auth_refresh_response())
def test_serde(response):
    obj = AuthRefreshResponse(**response)
    assert obj.dict(by_alias=True) == {
        "access": response["access"],
        "refresh": response["refresh"],
    }
