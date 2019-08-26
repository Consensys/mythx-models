import pytest

from mythx_models.exceptions import ValidationError
from mythx_models.response import AuthLogoutResponse

from . import common as testdata


def test_auth_login_response_from_valid_json():
    resp = AuthLogoutResponse.from_json("{}")
    assert type(resp) == AuthLogoutResponse


def test_auth_login_response_from_invalid_json():
    with pytest.raises(ValidationError):
        AuthLogoutResponse.from_json('{"foo": "bar"}')


def test_auth_login_response_from_valid_dict():
    resp = AuthLogoutResponse.from_dict({})
    assert type(resp) == AuthLogoutResponse


def test_auth_login_response_from_invalid_dict():
    with pytest.raises(ValidationError):
        AuthLogoutResponse.from_dict({"foo": "bar"})


def test_auth_login_response_to_json():
    assert testdata.LOGOUT_RESPONSE_OBJECT.to_json() == "{}"


def test_auth_login_response_to_dict():
    assert testdata.LOGOUT_RESPONSE_OBJECT.to_dict() == {}
