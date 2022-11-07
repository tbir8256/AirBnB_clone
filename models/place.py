#!/usr/bin/python3
"""Defines Place class"""
<<<<<<< HEAD

from models.base_model import BaseModel

class Place(BaseModel):
    """Represent a place

    Attributes:
        city_id (str): city id
        user_id (str): user id 
        name (str): The name of the city
        description (str): The descrip of the place
        name (str): The name of the city
=======
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.

    Attributes:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms of the place.
        number_bathrooms (int): The number of bathrooms of the place.
        max_guest (int): The maximum number of guests of the place.
        price_by_night (int): The price by night of the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of Amenity ids.
>>>>>>> 29c2a13a5df82f693a41fdb5b9358430d935c4e9
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
