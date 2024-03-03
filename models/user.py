#!/usr/bin/python3
"""
Write a class User that inherits from BaseModel
"""

from models.base_model import BaseModel

class User(BaseModel):
    """user class"""

    def __init__(self):
        """"""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
