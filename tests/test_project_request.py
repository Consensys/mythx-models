from hypothesis import given

from mythx_models.request import (
    ProjectCreationRequest,
    ProjectDeleteRequest,
    ProjectListRequest,
    ProjectStatusRequest,
    ProjectUpdateRequest,
)
from tests import (
    project_creation_request,
    project_deletion_request,
    project_list_request,
    project_status_request,
    project_update_request,
)


@given(project_list_request())
def test_list(request):
    parsed = ProjectListRequest(**request)

    assert parsed.dict() == request
    assert parsed.headers == {}
    assert parsed.payload == {}
    assert parsed.method == "GET"
    assert parsed.endpoint == "v1/projects"
    assert parsed.parameters == {
        "limit": parsed.limit,
        "offset": parsed.offset,
        "name": parsed.name,
    }


@given(project_status_request())
def test_status(request):
    parsed = ProjectStatusRequest(**request)

    assert parsed.dict() == request
    assert parsed.headers == {}
    assert parsed.payload == {}
    assert parsed.method == "GET"
    assert parsed.endpoint == "v1/projects/" + parsed.project_id
    assert parsed.parameters == {}


@given(project_update_request())
def test_update(request):
    parsed = ProjectUpdateRequest(**request)
    if "name" not in request:
        request["name"] = ""
    if "description" not in request:
        request["description"] = ""

    assert parsed.dict() == request
    assert parsed.headers == {}
    assert parsed.payload == {"name": parsed.name, "description": parsed.description}
    assert parsed.method == "POST"
    assert parsed.endpoint == "v1/projects/" + parsed.project_id
    assert parsed.parameters == {}


@given(project_creation_request())
def test_creation(request):
    parsed = ProjectCreationRequest(**request)
    if "groups" not in request:
        request["groups"] = []

    assert parsed.dict() == request
    assert parsed.headers == {}
    assert parsed.payload == {
        "name": parsed.name,
        "description": parsed.description,
        "groups": parsed.groups,
    }
    assert parsed.method == "POST"
    assert parsed.endpoint == "v1/projects"
    assert parsed.parameters == {}


@given(project_deletion_request())
def test_delete(request):
    parsed = ProjectDeleteRequest(**request)

    assert parsed.dict() == request
    assert parsed.headers == {}
    assert parsed.payload == {}
    assert parsed.method == "DELETE"
    assert parsed.endpoint == "v1/projects/" + parsed.project_id
    assert parsed.parameters == {}
