from binascii import hexlify

from hypothesis.strategies import (
    binary,
    booleans,
    characters,
    composite,
    dictionaries,
    fixed_dictionaries,
    integers,
    lists,
    none,
    one_of,
    sampled_from,
    shared,
    text,
    tuples,
    uuids,
)


@composite
def file_source_lists(draw, min_size=0, max_size=10):
    return draw(
        lists(
            sampled_from(
                [
                    "main.sol",
                    "some_file.sol",
                    "a_third_contract.sol",
                    "four.sol",
                    "more_contracts.sol",
                ]
            ),
            max_size=max_size,
            min_size=min_size,
        )
    )


@composite
def source_locations(draw):
    file_names = file_source_lists(min_size=1)

    bytecode_hashes = lists(
        sampled_from(
            [
                "0x0000000000000000000000000000000000000000",
                "0x0000000000000000000000000000a00003000100",
                "0x00000000000ab000000000000000a00003000100",
            ]
        ),
        max_size=3,
        min_size=1,
    )

    source_format, source_type, source_list = draw(
        sampled_from(
            [
                ("text", "solidity", draw(file_names)),
                ("evm-byzantium-bytecode", "raw-bytecode", draw(bytecode_hashes)),
            ]
        )
    )
    source_map = lists(integers(min_value=0, max_value=1200), min_size=2, max_size=2)
    src_map = draw(source_map)
    max_value = len(source_list) - 1 if source_list else 10
    src_map.append(draw(integers(min_value=-1, max_value=max_value)))

    return {
        "sourceMap": ":".join(map(str, src_map)),
        "sourceList": source_list,
        "sourceFormat": source_format,
        "sourceType": source_type,
    }


@composite
def test_case(draw):
    return {
        "address": "0x901d12ebe1b195e5aa8748e62bd7734ae19b51f",
        "blockCoinbase": "0xcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcb",
        "blockDifficulty": "0xa7d7343662e26",
        "blockGasLimit": "0x7d0000",
        "blockNumber": "0x66e393",
        "blockTime": "0x5bfa4639",
        "gasLimit": "0x7d000",
        "gasPrice": "0x773594000",
        "input": draw(
            sampled_from(
                [
                    "0x6fab5ddf",  # Fal1out
                    "0x8aa96f38",  # collectAllocations()
                    (  # transfer
                        "0xa9059cbb0000000000000000000000000000000000000000000000000000000070a0"
                        "82310000000000000000000000000000000000000000000000000000000000000002"
                    ),
                    (  # transfer
                        "0xa9059cbb080808080808080808080808808020048008080004101000402001200010"
                        "80044080400800080004011002080101010001001040080204080008400210040402"
                    ),
                    "0x00362a95bebebebebebebebebebebebedeadbeefdeadbeefdeadbeefdeadbeefdeadbeef",  # donate
                    "0x2e1a7d4d0000000000000000000000000000000000000000000000000000000000000001",  # withdraw
                ]
            )
        ),
        "name": "unknown",
        "origin": "0xdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef",
        "value": "0x0",
    }


@composite
def decoded_locations(draw):
    return [
        {"line": draw(integers()), "column": draw(integers())},
        {"line": draw(integers()), "column": draw(integers())},
        draw(booleans()),
    ]


@composite
def issues(draw):
    swc_int = draw(integers(min_value=100, max_value=140))
    swc_id = f"SWC-{swc_int}"
    locations = draw(lists(source_locations(), min_size=1, max_size=3))

    decoded_loc = draw(lists(decoded_locations()))

    extra = {
        "testCases": draw(one_of(none(), lists(test_case(), min_size=1, max_size=3))),
        "hidden": draw(booleans()),
    }
    if extra["testCases"] is None:
        del extra["testCases"]

    return {
        "swcID": swc_id,
        "swcTitle": draw(text()),
        "description": {"head": draw(text()), "tail": draw(text())},
        "severity": draw(sampled_from(["High", "Medium", "Low", "Unknown"])),
        "locations": locations,
        "decodedLocations": decoded_loc,
        "extra": extra,
    }


@composite
def issue_reports(draw):
    meta_data = {
        "toolName": draw(
            one_of(
                none(),
                sampled_from(
                    ["maru", "Maru", "harvey", "Harvey", "mythril", "Mythril"]
                ),
            )
        ),
        "logs": draw(
            one_of(
                lists(
                    fixed_dictionaries(
                        {
                            "hidden": booleans(),
                            "level": sampled_from(["error", "warning", "info"]),
                            "msg": characters(),
                        }
                    )
                )
            )
        ),
        "maru": draw(
            one_of(
                none(),
                fixed_dictionaries(
                    {
                        "checks": dictionaries(
                            sampled_from(
                                [
                                    "arithmetic_operation",
                                    "authorization_tx_origin",
                                    "continue_in_do_while",
                                    "datalog",
                                    "default_visibility_function",
                                    "default_visibility_state_variables",
                                    "deprecated_functions",
                                    "gas_dos",
                                    "hardcoded_gas_limit",
                                    "incorrect_constructor_name",
                                    "incorrect_erc20_implementation",
                                    "incorrect_function_state_mutability",
                                    "lock_pragma",
                                    "out_of_bounds_array_access",
                                    "outdated_compiler_version",
                                    "public_function_external",
                                    "right_to_left_override",
                                    "shadowing_builtin_symbols",
                                    "shadowing_variables",
                                    "typographical_error",
                                    "unchecked_call_return_value",
                                    "uninitialized_storage_pointer",
                                    "unused_variable",
                                    "weak_randomness_function",
                                ]
                            ),
                            booleans(),
                        )
                    }
                ),
            )
        ),
        "propertyChecking": draw(booleans()),
    }
    if meta_data["toolName"] is None:
        del meta_data["toolName"]
    if meta_data["maru"] is None:
        del meta_data["maru"]
    if meta_data["logs"] is None:
        del meta_data["logs"]

    return {
        "issues": draw(lists(issues(), min_size=1, max_size=2)),
        "sourceType": "solidity-file",
        "sourceFormat": "text",
        "sourceList": draw(lists(characters(), max_size=3)),
        "meta": meta_data,
    }


@composite
def bytecodes(draw, min_size=3, max_size=20):
    byte_code = hexlify(draw(binary(min_size=min_size, max_size=max_size))).decode(
        "utf-8"
    )
    return f"0x{byte_code}"


@composite
def sourcemap_components(draw, fileid_limit=None):
    smap = draw(lists(integers(min_value=0, max_value=1200), min_size=2, max_size=2))
    smap.append(
        draw(integers(min_value=-1, max_value=fileid_limit + 1 if fileid_limit else 10))
    )
    if draw(booleans()):
        smap.append(draw(sampled_from(["-", "i", "o"])))
    return ":".join(map(str, smap))


@composite
def source_maps(draw, fileid_limit=None):
    components = draw(
        lists(sourcemap_components(fileid_limit), min_size=1, max_size=100)
    )
    return ";".join(components)


@composite
def detected_issues_response(draw):
    return draw(
        lists(
            issue_reports(),
            min_size=1,
            max_size=3,
        )
    )


@composite
def submission_request(
    draw,
    bytecode=None,
    deployed_bytecode=None,
    source_map=None,
    deployed_source_map=None,
    source_list=None,
    main_source=None,
):
    bytecode = draw(bytecode or bytecodes())
    deployed_bytecode = draw(deployed_bytecode or bytecodes())
    source_list = draw(source_list or file_source_lists(min_size=2))
    main_source = draw(main_source or sampled_from(source_list))
    source_map = draw(source_map or source_maps(fileid_limit=len(source_list) - 1))
    deployed_source_map = draw(
        deployed_source_map or source_maps(fileid_limit=len(source_list) - 1)
    )
    source = """
        function Fal1out() public payable {}
        function allocate() public payable {}
        function sendAllocation(address payable allocator) public {}
        function collectAllocations() public onlyOwner {}
        function allocatorBalance(address allocator) public view returns (uint) {}
        function transfer(address _to, uint _value) public returns (bool) {}
        function withdraw(uint _amount) public {}
        function donate(address _to) public payable {}
    """
    sources = {draw(sampled_from(source_list)): {"source": source}}

    return {
        "bytecode": bytecode,
        "deployedBytecode": deployed_bytecode,
        "sourceList": source_list,
        "mainSource": main_source,
        "version": draw(sampled_from(["0.4.24", "0.5.0"])),
        "mode": draw(sampled_from(["full", "quick", "deep"])),
        "sourceMap": source_map,
        "sources": sources,
        "deployedSourceMap": deployed_source_map,
    }


@composite
def detected_issues_request(draw):
    return {"uuid": str(draw(uuids()))}
