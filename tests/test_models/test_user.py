#!/usr/bin/python3
""""""


import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def test_user_attributes(self):
        user = User()

        # Check if User instance is created successfully
        self.assertIsInstance(user, User)

        # Check if User inherits from BaseModel
        self.assertIsInstance(user, BaseModel)

        # Check if attributes are present and initialized correctly
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
