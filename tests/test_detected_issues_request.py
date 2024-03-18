from hypothesis import given

from mythx_models.request import DetectedIssuesRequest

from .strategies.report import detected_issues_request


@given(detected_issues_request())
def test_serde(response):
    obj = DetectedIssuesRequest(**response)
    assert obj.model_dump(by_alias=True) == response


@given(detected_issues_request())
def test_attributes(request):
    parsed = DetectedIssuesRequest(**request)

    assert parsed.model_dump(by_alias=True) == {"uuid": request["uuid"]}
    assert parsed.headers == {}
    assert parsed.payload == {}
    assert parsed.method == "GET"
    assert parsed.endpoint == f"v1/analyses/{parsed.uuid}/issues"
    assert parsed.parameters == {}
