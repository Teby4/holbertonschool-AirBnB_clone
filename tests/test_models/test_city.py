#!/usr/bin/python3
""""""


import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def test_city_attributes(self):
        city = City()

        # Check if City instance is created successfully
        self.assertIsInstance(city, City)

        # Check if City inherits from BaseModel
        self.assertIsInstance(city, BaseModel)

        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
