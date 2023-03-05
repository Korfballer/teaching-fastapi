"""Pydantic models.

References:
    https://docs.pydantic.dev/usage/models/
"""

# Standard library imports
import json
from typing import List, Optional, Union

# Third party imports
from pydantic import BaseModel, validator

# Local application imports
# n/a

class ExpandedModel(BaseModel):

    def to_dict(self):
        """
        Add method to convert class attributes to dictionary.

        References:
            https://stackoverflow.com/questions/61517/python-dictionary-from-an-objects-fields/31770231#31770231
        """
        return vars(self)

    def to_json(self):
        """
        Add method to JSON serialize.

        References:
            https://stackoverflow.com/questions/61517/python-dictionary-from-an-objects-fields/61531302#61531302
        """
        return json.dumps(self, default = lambda x: vars(x))


class Seats(ExpandedModel):
    """Number of seats requested for a table."""

    seats: Union[float, int] = None

    @validator('seats')
    def validate_seats(cls, v):
        """Validate the value of 'seats'."""
        if v < 1:

            raise ValueError("seats must be greater than, or equal to 1")

        if v != int(v):

            raise ValueError("seats must be an integer")

        return int(v)

class Order(ExpandedModel):
    """Restaurant order."""

    food: Optional[Union[List[str], str]] = None
    drinks: Optional[Union[List[str], str]] = None
