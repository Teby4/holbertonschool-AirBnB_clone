#!/usr/bin/python3

"""
Module for handling and serialization of instances
"""

from datetime import datetime
import uuid


class BaseModel():
    """ Base class for all instances """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        print("[{}] ({}) <{}>".format(type(self), self.id, self.__dict__))

    def to_dict(self):
        r = self.__dict__
        r["__class__"] = type(self)
        return r

    def save(self):
        self.updated_at = datetime.now()