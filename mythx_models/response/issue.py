"""This module contains domain models regrading found issues."""

from typing import Any, Dict, List, Optional, Tuple, Union

from pydantic import BaseModel, Field

try:
    from typing_extensions import Literal
except ImportError:
    from typing import Literal

Severity = Union[
    Literal["Unknown"],
    Literal["None"],
    Literal["Low"],
    Literal["Medium"],
    Literal["High"],
]

SourceType = Union[
    Literal["raw-bytecode"],
    Literal["ethereum-address"],
    Literal["solidity-contract"],
    Literal["solidity-file"],
]


SourceFormat = Union[
    Literal["text"],
    Literal["solc-ast-legacy-json"],
    Literal["solc-ast-compact-json"],
    Literal["evm-byzantium-bytecode"],
    Literal["ewasm-raw"],
]


class SourceMapLocation(BaseModel):
    offset: int = Field(ge=0)
    length: int = Field(ge=0)
    file_id: int = Field(ge=-1)
    jump_type: Literal["o", "i", "-"]


class SourceMap(BaseModel):
    raw: str

    @property
    def components(self):
        return self.decompress(self.raw)

    @staticmethod
    def sourcemap_reducer(
        accumulator: Tuple[int, int, int, str], component: str
    ) -> List[str]:
        parts = component.split(":")
        full = []

        for i in range(4):
            part_exists = i < len(parts) and parts[i]
            part = parts[i] if part_exists else accumulator[i]
            full.append(part)

        return full

    @staticmethod
    def decompress(source_map: str) -> List[SourceMapLocation]:
        components = source_map.split(";")
        accumulator = (-1, -1, -2, "")
        result = []

        for val in components:
            curr = SourceMap.sourcemap_reducer(accumulator, val)
            accumulator = curr
            result.append(curr)

        return [
            SourceMapLocation(
                offset=c[0] if c[0] else 0,
                length=c[1] if c[1] else 0,
                file_id=c[2] if c[2] else -1,
                jump_type=c[3] if c[3] else "-",
            )
            for c in result
        ]


class LineLocation(BaseModel):
    line: int
    column: int


class SourceLocation(BaseModel):
    source_map: str = Field(alias="sourceMap")
    source_type: str = Field(alias="sourceType")
    source_format: str = Field(alias="sourceFormat")
    source_list: List[str] = Field(alias="sourceList")

    class Config:
        allow_population_by_field_name = True


class IssueDescription(BaseModel):
    head: str
    tail: str


class Issue(BaseModel):
    swc_id: str = Field(alias="swcID")
    swc_title: str = Field(alias="swcTitle")
    description: IssueDescription
    severity: Severity
    locations: List[SourceLocation]
    extra: Dict[str, Any]
    decoded_locations: Optional[List[Tuple[LineLocation, LineLocation, bool]]] = Field(
        alias="decodedLocations"
    )

    class Config:
        allow_population_by_field_name = True
        use_enum_values = True
