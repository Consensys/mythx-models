from hypothesis.strategies import (
    composite,
    text,
)


@composite
def version_response(draw):
    return {
        "api": draw(text(min_size=1)),
        "hash": draw(text(min_size=1)),
        "harvey": draw(text(min_size=1)),
        "maru": draw(text(min_size=1)),
        "mythril": draw(text(min_size=1)),
    }
