from mythx_models.request import VersionRequest


def test_serde():
    resp = VersionRequest()
    assert resp.dict() == {}
