#!/usr/bin/python3
""""""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        # Create an instance of FileStorage for testing
        self.file_storage = FileStorage()

    def tearDown(self):
        # Delete the test JSON file after each test
        try:
            os.remove("test_file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        # Test the 'all' method when there are no objects
        self.assertEqual(self.file_storage.all(), {})

    def test_new(self):
        # Test the 'new' and 'all' methods
        model1 = BaseModel()
        model2 = BaseModel()
        model3 = BaseModel()

        self.file_storage.new(model1)
        self.file_storage.new(model2)
        self.file_storage.new(model3)

        objects = self.file_storage.all()
        self.assertIn("BaseModel." + model1.id, objects)
        self.assertIn("BaseModel." + model2.id, objects)
        self.assertIn("BaseModel." + model3.id, objects)

    def test_save(self):
        # Test the 'save' and 'reload' methods
        model1 = BaseModel()
        model2 = BaseModel()
        model3 = BaseModel()

        self.file_storage.new(model1)
        self.file_storage.new(model2)
        self.file_storage.new(model3)

        # Save the data to a test file
        self.file_storage.save()

        # Create a new instance of FileStorage
        new_file_storage = FileStorage()

        # Reload the data from the test file
        new_file_storage.reload()

        # Check if the reloaded objects match the original ones
        self.assertEqual(self.file_storage.all(), new_file_storage.all())

    def test_reload(self):
        model1 = BaseModel()
        model2 = BaseModel()
        model3 = BaseModel()

        self.file_storage.new(model1)
        self.file_storage.new(model2)
        self.file_storage.new(model3)

        self.file_storage.save()
        
        new_file_storage = FileStorage()

        new_file_storage.reload()
        
        self.assertEqual(self.file_storage.all(), new_file_storage.all())

if __name__ == '__main__':
    unittest.main()