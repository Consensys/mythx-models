from mythx_models.exceptions import MythXAPIError


def test_base_type():
    exc = MythXAPIError()
    assert isinstance(exc, MythXAPIError)
    assert isinstance(exc, Exception)
    assert issubclass(MythXAPIError, Exception)
