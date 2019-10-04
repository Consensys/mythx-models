import json
from copy import deepcopy

from mythx_models.response import (
    Issue,
    Severity,
    SourceFormat,
    SourceLocation,
    SourceType,
)

from . import common as testdata


def assert_issue(issue: Issue, skip_decoded=False):
    assert issue.swc_id == testdata.SWC_ID
    assert issue.swc_title == testdata.SWC_TITLE
    assert issue.description_short == testdata.DESCRIPTION_HEAD
    assert issue.description_long == testdata.DESCRIPTION_TAIL
    assert issue.severity == Severity(testdata.SEVERITY)
    if not skip_decoded:
        assert issue.decoded_locations == testdata.DECODED_LOCATIONS_OBJ
    assert len(issue.locations) == 1
    location = issue.locations[0]
    assert location.source_map.to_sourcemap() == testdata.SOURCE_MAP
    assert location.source_format == SourceFormat.EVM_BYZANTIUM_BYTECODE
    assert location.source_type == SourceType.RAW_BYTECODE
    assert location.source_list == testdata.SOURCE_LIST


def test_issue_from_valid_json():
    issue = Issue.from_json(json.dumps(testdata.ISSUE_DICT))
    assert_issue(issue)


def test_issue_from_dict():
    issue = Issue.from_dict(testdata.ISSUE_DICT)
    assert_issue(issue)


def test_issue_to_json():
    assert json.loads(testdata.ISSUE_OBJECT.to_json()) == testdata.ISSUE_DICT


def test_issue_to_dict():
    assert testdata.ISSUE_OBJECT.to_dict() == testdata.ISSUE_DICT


def test_source_location_from_dict():
    sl = SourceLocation.from_dict(testdata.SOURCE_LOCATION)
    assert sl.source_format == testdata.SOURCE_FORMAT
    assert sl.source_list == testdata.SOURCE_LIST
    assert sl.source_map.to_sourcemap() == testdata.SOURCE_MAP
    assert sl.source_type == testdata.SOURCE_TYPE


def test_decoded_locations_removed():
    issue_data = deepcopy(testdata.ISSUE_DICT)
    del issue_data["decodedLocations"]
    issue = Issue.from_dict(issue_data)
    assert_issue(issue, skip_decoded=True)
    assert "decodedLocations" not in issue.to_dict()


def test_decoded_locations_empty_removed():
    issue_data = deepcopy(testdata.ISSUE_DICT)
    issue_data["decodedLocations"] = []
    issue = Issue.from_dict(issue_data)
    assert_issue(issue, skip_decoded=True)
    assert "decodedLocations" not in issue.to_dict()


def test_decoded_locations_only_removed():
    issue_data = deepcopy(testdata.ISSUE_DICT)
    issue_data["decodedLocations"] = [[]]
    issue = Issue.from_dict(issue_data)
    assert_issue(issue, skip_decoded=True)
    assert "decodedLocations" not in issue.to_dict()


def test_decoded_locations_empty_skip():
    issue_data = deepcopy(testdata.ISSUE_DICT)
    issue_data["decodedLocations"].append([])
    issue = Issue.from_dict(issue_data)
    assert_issue(issue, skip_decoded=True)
    assert "decodedLocations" in issue.to_dict()
