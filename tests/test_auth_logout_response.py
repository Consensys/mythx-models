from mythx_models.response import AuthLogoutResponse


def test_auth_login_response_from_valid_json():
    resp = AuthLogoutResponse()
    assert resp.dict() == {}
