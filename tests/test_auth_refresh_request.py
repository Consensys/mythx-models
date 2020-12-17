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


@given(auth_refresh_request())
def test_attributes(request):
    parsed = AuthRefreshRequest(**request)

    assert parsed.dict(by_alias=True) == {
        "accessToken": request["accessToken"],
        "refreshToken": request["refreshToken"],
    }
    assert parsed.headers == {}
    assert parsed.payload == {
        "jwtTokens": {"access": parsed.access_token, "refresh": parsed.refresh_token}
    }
    assert parsed.method == "POST"
    assert parsed.endpoint == f"v1/auth/refresh"
    assert parsed.parameters == {}
