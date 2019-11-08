import json
from typing import List

from mythx_models.exceptions import ValidationError
from mythx_models.response.base import BaseResponse
from mythx_models.response.group import Group
from mythx_models.util import resolve_schema

INDEX_ERROR_MSG = "Group at index {} was not fetched"


class GroupListResponse(BaseResponse):
    """The API response domain model for a list of analyses."""

    with open(resolve_schema(__file__, "group-list.json")) as sf:
        schema = json.load(sf)

    def __init__(self, groups: List[Group], total: int) -> None:
        self.groups = groups
        self.total = total

    @classmethod
    def from_dict(cls, d: dict):
        """Create the response domain model from a dict.

        This also validates the dict's schema and raises a :code:`ValidationError`
        if any required keys are missing or the data is malformed.

        :param d: The dict to deserialize from
        :return: The domain model with the data from :code:`d` filled in
        """
        cls.validate(d)
        groups = [Group.from_dict(a) for a in d["groups"]]
        return cls(groups=groups, total=d["total"])

    def to_dict(self):
        """Serialize the response model to a Python dict.

        :return: A dict holding the request model data
        """
        d = {"groups": [a.to_dict() for a in self.groups], "total": len(self.groups)}
        self.validate(d)
        return d

    def __iter__(self):
        for analysis in self.groups:
            yield analysis

    def __getitem__(self, idx):
        try:
            return self.groups[idx]
        except IndexError:
            raise IndexError(INDEX_ERROR_MSG.format(idx))

    def __setitem__(self, idx, value):
        try:
            self.groups[idx] = value
        except IndexError:
            raise IndexError(INDEX_ERROR_MSG.format(idx))

    def __delitem__(self, idx):
        try:
            del self.groups[idx]
            self.total -= 1
        except IndexError:
            raise IndexError(INDEX_ERROR_MSG.format(idx))

    def __len__(self):
        return self.total

    def __reversed__(self):
        return reversed(self.groups)

    def __contains__(self, item: Group):
        if not type(item) in (Group, str):
            raise ValueError(
                "Expected type Group or str but got {}".format(type(item))
            )
        identifier = item.identifier if type(item) == Group else item
        return identifier in map(lambda x: x.identifier, self.groups)

    def __eq__(self, candidate):
        return self.total == candidate.total and self.groups == candidate.groups
