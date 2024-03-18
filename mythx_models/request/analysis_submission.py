"""This module contains the AnalysisSubmissionRequest domain model."""

from typing import Any, Dict, List, Optional

from pydantic import ConfigDict, BaseModel, Field

from mythx_models.util import dict_delete_none_fields


class AnalysisSubmissionRequest(BaseModel):
    contract_name: Optional[str] = Field(None, alias="contractName")
    bytecode: str
    source_map: Optional[str] = Field(None, alias="sourceMap")
    deployed_bytecode: Optional[str] = Field(None, alias="deployedBytecode")
    deployed_source_map: Optional[str] = Field(None, alias="deployedSourceMap")
    main_source: str = Field(alias="mainSource")
    sources: Dict[str, Dict[str, Any]]
    source_list: Optional[List[str]] = Field(None, alias="sourceList")
    solc_version: Optional[str] = Field(None, alias="version")
    analysis_mode: Optional[str] = Field(None, alias="analysisMode")
    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)

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
