import json

from mythx_models.response.base import BaseResponse
from mythx_models.response.group import Group
from mythx_models.util import resolve_schema


class GroupStatusResponse(BaseResponse):
    """The API response domain model for a fetching the status of a group."""

    with open(resolve_schema(__file__, "group-status.json")) as sf:
        schema = json.load(sf)

    def __init__(self, group: Group):
        self.group = group

    @classmethod
    def from_dict(cls, d):
        """Create the response domain model from a dict.

        This also validates the dict's schema and raises a :code:`ValidationError`
        if any required keys are missing or the data is malformed.

        :param d: The dict to deserialize from
        :return: The domain model with the data from :code:`d` filled in
        """
        cls.validate(d)
        return cls(group=Group.from_dict(d))

    def to_dict(self):
        """Serialize the response model to a Python dict.

        :return: A dict holding the request model data
        """
        d = self.group.to_dict()
        self.validate(d)
        return d

    def __getattr__(self, name):
        return getattr(self.group, name)
