#!/usr/bin/python3
"""Defines the FileStorage class"""

import json
from models.base_model import BaseModel

class FileStorage:
    """Represent an Storage engine

       Attributes:
       __file_path (str): The name of the fiile
       __objects (dict): a dictionary of object
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set __objects obj with obj_class_name.id"""
        objname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objname, obj.id)] = obj

    def save(self):
        
