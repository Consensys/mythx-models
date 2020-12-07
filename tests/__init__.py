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
