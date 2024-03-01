#!/usr/bin/python3

"""
Module for handling JSON serialization/deserialization
"""

from datetime import datetime
import uuid
import json


class FileStorage():
    """ Class for handling JSON files """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[type(obj).__name__ + obj.id] = obj
    
    def save(self):
        t = {(FilStorage.__objects[k], v.to_dict()) for k, v in
             FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(t))
    
    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.loads(f.read())
                for key, value in FileStorage.__objects.items():
                    FileStorage.__objects[key] = 
        except:
            pass
