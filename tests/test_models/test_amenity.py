#!/usr/bin/python3
""""""


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_amenity_attributes(self):
        amenity = Amenity()

        # Check if Amenity instance is created successfully
        self.assertIsInstance(amenity, Amenity)

        # Check if Amenity inherits from BaseModel
        self.assertIsInstance(amenity, BaseModel)

        # Check if 'name' attribute is present
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
