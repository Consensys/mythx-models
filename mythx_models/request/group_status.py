"""This module contains the GroupRequest domain model."""

from mythx_models.exceptions import ValidationError
from mythx_models.request.base import BaseRequest


class GroupStatusRequest(BaseRequest):
    """Perform an API request that gets data for the specified group ID."""

    def __init__(self, group_id: str):
        self.group_id = group_id

    @property
    def method(self):
        """The HTTP method to perform.

        :return: The uppercase HTTP method, e.g. "POST"
        """
        return "GET"

    @property
    def endpoint(self):
        """The API's group status endpoint.

        :return: A string denoting the status endpoint without the host prefix
        """
        return "v1/analysis-groups/{}".format(self.group_id)

    @property
    def headers(self):
        """Additional request headers.

        :return: A dict (str -> str) instance mapping header name to header content
        """
        return {}

    @property
    def parameters(self):
        """Additional URL parameters

        :return: A dict (str -> str) instance mapping parameter name to parameter content
        """
        return {}

    @property
    def payload(self):
        """The request's payload data.

        :return: A Python dict to be serialized into JSON format and submitted to the endpoint.
        """
        return {}

    @classmethod
    def from_dict(cls, d):
        """Create the request domain model from a dict.

        This also validates the dict's schema and raises a :code:`ValidationError`
        if any required keys are missing or the data is malformed.

        :param d: The dict to deserialize from
        :return: The domain model with the data from :code:`d` filled in
        """
        group_id = d.get("group_id")
        if group_id is None:
            raise ValidationError("Missing group_id field in data {}".format(d))
        # TODO: Validate whether UUID
        return cls(group_id=group_id)

    def to_dict(self):
        """Serialize the request model to a Python dict.

        :return: A dict holding the request model data
        """
        return {"group_id": self.group_id}
