from hypothesis import given
from hypothesis.strategies import composite, datetimes, lists, text, uuids

from mythx_models.response import (
    ProjectCreationResponse,
    ProjectDeletionResponse,
    ProjectListResponse,
    ProjectStatusResponse,
    ProjectUpdateResponse,
)


@composite
def project_dict_response(draw):
    return {
        "id": str(draw(uuids(version=4))),
        "name": draw(text()),
        "description": draw(text()),
        "created": draw(datetimes()),
        "modified": draw(datetimes()),
    }


@composite
def project_list_response(draw, min_size, max_size):
    projects = draw(
        lists(project_dict_response(), min_size=min_size, max_size=max_size)
    )
    return {"projects": projects, "total": len(projects)}


@given(project_list_response(min_size=0, max_size=10))
def test_list_serde(response):
    parsed = ProjectListResponse(**response)
    assert parsed.dict() == response


@given(project_dict_response())
def test_status_serde(response):
    parsed = ProjectStatusResponse(**response)
    assert parsed.dict() == response


@given(project_dict_response())
def test_creation_serde(response):
    parsed = ProjectCreationResponse(**response)
    assert parsed.dict() == response


@given(project_dict_response())
def test_creation_serde(response):
    parsed = ProjectUpdateResponse(**response)
    assert parsed.dict() == response


def test_deletion_serde():
    parsed = ProjectDeletionResponse()
    assert parsed.dict() == {}
