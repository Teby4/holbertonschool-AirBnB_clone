#!/usr/bin/python3

"""
Module for handling and serialization of instances
"""

from datetime import datetime
import uuid
from models.engine.file_storage import FileStorage
from models import storage

class BaseModel():
    """ Base class for all instances """

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime(value,
                                "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)


    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                self.__dict__)

    def to_dict(self):
        r = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                r[key] = value.isoformat()
            else:
                r[key] = value
            r["__class__"] = type(self).__name__
        return r

    def save(self):
        self.updated_at = datetime.now()
        storage.save()
