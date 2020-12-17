"""This module contains the AnalysisSubmissionRequest domain model."""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from mythx_models.util import dict_delete_none_fields


class AnalysisSubmissionRequest(BaseModel):
    contract_name: Optional[str] = Field(alias="contractName")
    bytecode: str
    source_map: Optional[str] = Field(alias="sourceMap")
    deployed_bytecode: Optional[str] = Field(alias="deployedBytecode")
    deployed_source_map: Optional[str] = Field(alias="deployedSourceMap")
    main_source: str = Field(alias="mainSource")
    sources: Dict[str, Dict[str, Any]]
    source_list: Optional[List[str]] = Field(alias="sourceList")
    solc_version: Optional[str] = Field(alias="version")
    analysis_mode: Optional[str] = Field(alias="analysisMode")

    class Config:
        allow_population_by_field_name = True
        use_enum_values = True

    @property
    def endpoint(self):
        return "v1/analyses"

    @property
    def method(self):
        return "POST"

    @property
    def payload(self):
        return {
            "data": dict_delete_none_fields(
                {
                    "contractName": self.contract_name,
                    "bytecode": self.bytecode,
                    "sourceMap": self.source_map,
                    "deployedBytecode": self.deployed_bytecode,
                    "deployedSourceMap": self.deployed_source_map,
                    "mainSource": self.main_source,
                    "sources": self.sources if self.sources else None,
                    "sourceList": self.source_list if self.source_list else None,
                    "version": self.solc_version,
                    "analysisMode": self.analysis_mode,
                }
            )
        }

    @property
    def headers(self):
        return {}

    @property
    def parameters(self):
        return {}
