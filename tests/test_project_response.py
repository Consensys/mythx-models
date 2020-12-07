from hypothesis import given

from mythx_models.response import (
    ProjectCreationResponse,
    ProjectDeletionResponse,
    ProjectListResponse,
    ProjectStatusResponse,
    ProjectUpdateResponse,
)
from tests import project_dict_response, project_list_response


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
