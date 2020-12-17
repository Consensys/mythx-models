from hypothesis import given
from hypothesis.strategies import composite, integers, lists, sampled_from, text, uuids

from mythx_models.request import (
    ProjectCreationRequest,
    ProjectDeleteRequest,
    ProjectListRequest,
    ProjectStatusRequest,
    ProjectUpdateRequest,
)


@composite
def project_list_request(draw):
    return {
        "offset": draw(integers(min_value=0)),
        "limit": draw(integers(min_value=1)),
        "name": draw(text()),
    }


@composite
def project_status_request(draw):
    return {"project_id": str(draw(uuids(version=4)))}


@composite
def project_update_request(draw):
    return draw(
        sampled_from(
            [
                {
                    "project_id": str(draw(uuids(version=4))),
                    "name": draw(text()),
                    "description": draw(text()),
                },
                {"project_id": str(draw(uuids(version=4))), "name": draw(text())},
                {
                    "project_id": str(draw(uuids(version=4))),
                    "description": draw(text()),
                },
            ]
        )
    )


@composite
def project_creation_request(draw):
    return draw(
        sampled_from(
            [
                {"name": draw(text()), "description": draw(text())},
                {
                    "name": draw(text()),
                    "description": draw(text()),
                    "groups": [str(x) for x in draw(lists(uuids(version=4)))],
                },
            ]
        )
    )


@composite
def project_deletion_request(draw):
    return {"project_id": str(draw(uuids(version=4)))}


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
        request["name"] = None
    if "description" not in request:
        request["description"] = None

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
