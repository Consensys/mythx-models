from hypothesis import given

from mythx_models.request import GroupListRequest

from .strategies.group import group_list_request


@given(group_list_request())
def test_serde(response):
    obj = GroupListRequest(**response)
    assert obj.model_dump(by_alias=True) == response


@given(group_list_request())
def test_attributes(request):
    parsed = GroupListRequest(**request)

    assert parsed.model_dump(by_alias=True) == request
    assert parsed.headers == {}
    assert parsed.payload == {}
    assert parsed.method == "GET"
    assert parsed.endpoint == "v1/analysis-groups"
    assert parsed.parameters == {
        "createdBy": parsed.created_by,
        "dateFrom": parsed.date_from.isoformat(),
        "dateTo": parsed.date_to.isoformat(),
        "groupName": parsed.group_name,
        "offset": parsed.offset,
    }
