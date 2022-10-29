#!/usr/bin/python3
"""
Defines BaseModel

Defines common attributes and methods
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Initialising common attributes and methods
    """
    def __init__(self, id, created_at, updated_at):
    """
    Initialize BaseModel
    """

    self.id = str(uuid4())
    self.created_at = datetime.now()
    self.updated_at = datetime.now()

    def __str__(self):
    """
    Returns string representation of Basemodel
    """
    print("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
    """
    Updates the var: updated_at
    """
    self.updated_at = datetime.now()

    def to_dict(self):
    """
    Returns dict with all keys and values of __dict__
    of the instance
    """
    dict_1 = self.__dict__.copy()
    dict_1["__class__"] = self.__class__.__name__
    for i, j in self.__dict__.items():
        if i in ("created_at", "updated_at"):
            j = self.__dict__[k].isoformat()
            dict_1[i] = j
    return (dict_1)
