from typing import List

from hypothesis import HealthCheck, given, settings
from pydantic import parse_obj_as

from mythx_models.response import IssueReport

from .strategies.report import detected_issues_response


@given(detected_issues_response())
@settings(suppress_health_check=[HealthCheck.too_slow])
def test_serde(response):
    objs = parse_obj_as(List[IssueReport], response)
    obj: IssueReport
    for obj in objs:
        for issue in obj.issues:
            issue.decoded_locations = [list(loc) for loc in issue.decoded_locations]
    assert [obj.dict(by_alias=True) for obj in objs] == response
