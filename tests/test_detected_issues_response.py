from typing import List

from hypothesis import HealthCheck, given, settings
from pydantic import TypeAdapter

from mythx_models.response import IssueReport

from .strategies.report import detected_issues_response


@given(detected_issues_response())
@settings(suppress_health_check=[HealthCheck.too_slow])
def test_serde(response):
    adapter = TypeAdapter(List[IssueReport])
    objs = adapter.validate_python(response)
    obj: IssueReport
    for obj in objs:
        for issue in obj.issues:
            issue.decoded_locations = [list(loc) for loc in issue.decoded_locations]
    assert [obj.model_dump(by_alias=True) for obj in objs] == response
