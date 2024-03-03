#!/usr/bin/python3
""""""


from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

        dic = model.to_dict()
        self.assertEqual(BaseModel(dic), model)

    def test_str(self):
        model = BaseModel()
        out = "[{}] ({}) <{}>".format(type(model).__name__, model.id,
                                      model.__dict__)
        self.assertEqual(str(model), out)

    def test_to_dict(self):
        model = BaseModel()
        dict = model.to_dict()
        self.assertIsInstance(dict["created_at"], str)
        self.assertIsInstance(dict["updated_at"], str)

    def test_save(self):
        m = BaseModel()
        date = m.updated_at
        m.save()
        self.assertNotEqual(date, m.updated_at)


if __name__ == '__main__':
    unittest.main()
