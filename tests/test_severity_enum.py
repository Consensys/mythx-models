try:
    from mythx_models.response.issue import SEVERITY
except ImportError:
    SEVERITY = None


def test_severity_enum():
    assert SEVERITY is not None
    SEVERITY_ORDER = [SEVERITY.HIGH, SEVERITY.MEDIUM, SEVERITY.LOW, SEVERITY.NONE, SEVERITY.UNKNOWN]
    assert SEVERITY_ORDER.index("High") == 0
    assert SEVERITY_ORDER.index("Medium") == 1
    assert SEVERITY_ORDER.index("Low") == 2
    assert SEVERITY_ORDER.index("None") == 3
    assert SEVERITY_ORDER.index("Unknown") == 4
