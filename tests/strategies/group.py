from hypothesis.strategies import (
    composite,
    datetimes,
    integers,
    lists,
    sampled_from,
    text,
    uuids,
)


@composite
def group_data(draw):
    return {
        "completedAt": str(draw(datetimes())),
        "createdAt": str(draw(datetimes())),
        "createdBy": str(draw(text())),
        "id": str(draw(uuids())),
        "mainSourceFiles": draw(lists(text(), max_size=3)),
        "name": draw(text()),
        "numAnalyses": {
            "total": draw(integers()),
            "queued": draw(integers()),
            "running": draw(integers()),
            "failed": draw(integers()),
            "finished": draw(integers()),
        },
        "numVulnerabilities": {
            "high": draw(integers()),
            "medium": draw(integers()),
            "low": draw(integers()),
            "none": draw(integers()),
        },
        "progress": draw(integers()),
        "projectId": str(draw(uuids())),
        "status": draw(sampled_from(["opened", "sealed"])),
    }


@composite
def group_status_response(draw):
    return draw(group_data())


@composite
def group_status_request(draw):
    return {"groupId": str(draw(uuids()))}


@composite
def group_operation_response(draw):
    return draw(group_data())


@composite
def group_operation_request(draw):
    return {
        "groupId": str(draw(uuids())),
        "type": draw(
            sampled_from(["seal_group", "add_to_project", "remove_from_project"])
        ),
    }


@composite
def group_list_response(draw):
    groups = draw(lists(group_data(), max_size=3))
    return {"groups": groups, "total": len(groups)}


@composite
def group_list_request(draw):
    return {
        "offset": draw(integers()),
        "createdBy": draw(text()),
        "groupName": draw(text()),
        "dateFrom": draw(datetimes()),
        "dateTo": draw(datetimes()),
    }


@composite
def group_creation_response(draw):
    return draw(group_data())


@composite
def group_creation_request(draw):
    return {"groupName": draw(text())}
