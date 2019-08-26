import pytest

from mythx_models import request as reqmodels
from mythx_models import response as respmodels
from mythx_models.exceptions import ValidationError

from . import common as testdata


@pytest.mark.parametrize(
    "r_dict,model,should_raise,exc",
    [
        (
            testdata.ANALYSIS_LIST_REQUEST_DICT,
            reqmodels.AnalysisListRequest,
            False,
            ValidationError,
        ),
        (
            testdata.DETECTED_ISSUES_REQUEST_DICT,
            reqmodels.DetectedIssuesRequest,
            False,
            ValidationError,
        ),
        (
            testdata.ANALYSIS_STATUS_REQUEST_DICT,
            reqmodels.AnalysisStatusRequest,
            False,
            ValidationError,
        ),
        (
            testdata.ANALYSIS_SUBMISSION_REQUEST_DICT,
            reqmodels.AnalysisSubmissionRequest,
            True,
            ValidationError,
        ),
        (
            testdata.LOGIN_REQUEST_DICT,
            reqmodels.AuthLoginRequest,
            True,
            ValidationError,
        ),
        (
            testdata.LOGOUT_REQUEST_DICT,
            reqmodels.AuthLogoutRequest,
            True,
            ValidationError,
        ),
        (
            testdata.REFRESH_REQUEST_DICT,
            reqmodels.AuthRefreshRequest,
            True,
            ValidationError,
        ),
        (
            testdata.ANALYSIS_LIST_RESPONSE_DICT,
            respmodels.AnalysisListResponse,
            True,
            ValidationError,
        ),
        (
            testdata.DETECTED_ISSUES_RESPONSE_DICT,
            respmodels.DetectedIssuesResponse,
            True,
            ValidationError,
        ),
        (
            testdata.ANALYSIS_STATUS_RESPONSE_DICT,
            respmodels.AnalysisStatusResponse,
            True,
            ValidationError,
        ),
        (
            testdata.ANALYSIS_SUBMISSION_RESPONSE_DICT,
            respmodels.AnalysisSubmissionResponse,
            True,
            ValidationError,
        ),
        (
            testdata.LOGIN_RESPONSE_DICT,
            respmodels.AuthLoginResponse,
            True,
            ValidationError,
        ),
        (
            testdata.LOGOUT_RESPONSE_DICT,
            respmodels.AuthLogoutResponse,
            False,
            ValidationError,
        ),
        (
            testdata.REFRESH_RESPONSE_DICT,
            respmodels.AuthRefreshResponse,
            True,
            ValidationError,
        ),
    ],
)
def test_model_validators(r_dict, model, should_raise, exc):
    if should_raise:
        with pytest.raises(exc):
            model.validate({})
    else:
        model.validate(r_dict)
