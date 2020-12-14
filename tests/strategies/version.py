from hypothesis.strategies import (
    binary,
    booleans,
    characters,
    composite,
    datetimes,
    dictionaries,
    fixed_dictionaries,
    integers,
    lists,
    none,
    one_of,
    sampled_from,
    shared,
    text,
    uuids,
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
