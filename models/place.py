#!/usr/bin/python3
"""Defines Place class"""

from models.base_model import BaseModel

class Place(BaseModel):
    """Represent a place

    Attributes:
        city_id (str): city id
        user_id (str): user id 
        name (str): The name of the city
        description (str): The descrip of the place
        name (str): The name of the city
    """

    state_id = ""
    name = ""
