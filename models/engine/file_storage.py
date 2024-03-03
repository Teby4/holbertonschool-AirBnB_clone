#!/usr/bin/python3

"""
Module for handling JSON serialization/deserialization
"""

from datetime import datetime
import uuid
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity


class FileStorage():
    """ Class for handling JSON files """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[type(obj).__name__ + "." + obj.id] = obj

    def save(self):
        t = {}
        for k, v in FileStorage.__objects.items():
            t[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(t))

    def reload(self):
        classList = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
                }
        try:
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.loads(f.read())
                for key, value in FileStorage.__objects.items():
                    cls = classList[value["__class__"]]
                    FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
