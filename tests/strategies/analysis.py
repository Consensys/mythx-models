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

from .report import bytecodes, source_maps


@composite
def analysis_status(draw):
    return {
        "apiVersion": draw(text(min_size=1)),
        "harveyVersion": draw(text(min_size=1)),
        "maruVersion": draw(text(min_size=1)),
        "mythrilVersion": draw(text(min_size=1)),
        "queueTime": draw(integers()),
        "status": draw(sampled_from(["Running", "Queued", "Finished"])),
        "submittedAt": draw(datetimes()).isoformat(),
        "submittedBy": draw(text(min_size=1)),
        "uuid": str(draw(uuids(version=4))),
        "runTime": draw(integers()),
        "clientToolName": draw(text()),
        "groupId": draw(text()),
        "groupName": draw(text()),
        "analysisMode": draw(sampled_from(["full", "quick", "standard"])),
    }


@composite
def analysis_submission(draw):
    filename = draw(text(min_size=1))
    return {
        "bytecode": draw(bytecodes()),
        "mainSource": filename,
        "sources": {
            "filename": {
                "source": draw(
                    sampled_from(
                        [
                            "pragma solidity >=0.4.22 <0.6.0;\\n\\ncontract Token {\\n}",
                            draw(text(min_size=1)),
                        ]
                    )
                ),
                "ast": {"absolutePath": "/Users/mirko/Desktop/consensys/sol/Token.sol"},
            }
        },
    }


@composite
def analysis_status_request(draw):
    return {"uuid": str(draw(uuids(version=4)))}


@composite
def analysis_input_request(draw):
    return {"uuid": str(draw(uuids(version=4)))}


@composite
def analysis_list_response(draw):
    analysis_list = draw(lists(analysis_status()))
    return {"total": len(analysis_list), "analyses": analysis_list}


@composite
def analysis_list_request(draw):
    return {
        "offset": draw(integers()),
        "dateFrom": draw(datetimes()),
        "dateTo": draw(datetimes()),
        "createdBy": draw(text()),
        "groupName": draw(text()),
        "groupId": draw(text()),
        "mainSource": draw(text()),
    }
