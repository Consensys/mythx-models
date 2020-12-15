from mythx_models.request import VersionRequest


def test_serde():
    resp = VersionRequest()
    assert resp.dict() == {}


def test_attributes():
    parsed = VersionRequest()

    assert parsed.headers == {}
    assert parsed.payload == {}
    assert parsed.method == "GET"
    assert parsed.endpoint == f"v1/version"
    assert parsed.parameters == {}
