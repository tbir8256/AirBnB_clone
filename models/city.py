#!/usr/bin/python3
"""Defines city class."""

from models.base_model import BaseModel

class City(BaseModel):
    """Represent a city

    Attributes:
        state_id (str): Stae id
        name (str): The name of the city
    """

    state_id = ""
    name = ""
