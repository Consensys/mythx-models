from hypothesis import given

from mythx_models.request import DetectedIssuesRequest

from .strategies.report import detected_issues_request


@given(detected_issues_request())
def test_serde(response):
    obj = DetectedIssuesRequest(**response)
    assert obj.dict(by_alias=True) == response
