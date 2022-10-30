#!/usr/bin/python3
"""Defines Review class"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Represent a review

    Attributes:
        place_id (str): Place id
        user_id (str): User id 
        text (str): The text of the review
    """

    place_id = ""
    user_id = ""
    text = ""
