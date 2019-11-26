import pytest

from mythx_models import request as reqmodels
from mythx_models import response as respmodels
from mythx_models.exceptions import ValidationError

from . import common as testdata


@pytest.mark.parametrize(
    "r_dict,model,should_raise",
    [
        (testdata.ANALYSIS_LIST_REQUEST_DICT, reqmodels.AnalysisListRequest, False),
        (testdata.DETECTED_ISSUES_REQUEST_DICT, reqmodels.DetectedIssuesRequest, False),
        (testdata.ANALYSIS_STATUS_REQUEST_DICT, reqmodels.AnalysisStatusRequest, False),
        (
            testdata.ANALYSIS_SUBMISSION_REQUEST_DICT,
            reqmodels.AnalysisSubmissionRequest,
            True,
        ),
        (testdata.LOGIN_REQUEST_DICT, reqmodels.AuthLoginRequest, True),
        (testdata.LOGOUT_REQUEST_DICT, reqmodels.AuthLogoutRequest, True),
        (testdata.REFRESH_REQUEST_DICT, reqmodels.AuthRefreshRequest, True),
        (testdata.ANALYSIS_LIST_RESPONSE_DICT, respmodels.AnalysisListResponse, True),
        (
            testdata.DETECTED_ISSUES_RESPONSE_DICT,
            respmodels.DetectedIssuesResponse,
            True,
        ),
        (
            testdata.ANALYSIS_STATUS_RESPONSE_DICT,
            respmodels.AnalysisStatusResponse,
            True,
        ),
        (
            testdata.ANALYSIS_SUBMISSION_RESPONSE_DICT,
            respmodels.AnalysisSubmissionResponse,
            True,
        ),
        (testdata.LOGIN_RESPONSE_DICT, respmodels.AuthLoginResponse, True),
        (testdata.LOGOUT_RESPONSE_DICT, respmodels.AuthLogoutResponse, False),
        (testdata.REFRESH_RESPONSE_DICT, respmodels.AuthRefreshResponse, True),
    ],
)
def test_model_validators(r_dict, model, should_raise):
    if should_raise:
        with pytest.raises(ValidationError):
            model.validate({})
    else:
        model.validate(r_dict)
