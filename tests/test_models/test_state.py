#!/usr/bin/python3
""""""


import unittest
from models.state import State


class TestState(unittest.TestCase):

    def test_state_attributes(self):
        state = State()

        # Check if State instance is created successfully
        self.assertIsInstance(state, State)

        # Check if State inherits from BaseModel
        self.assertIsInstance(state, BaseModel)

        # Check if 'name' attribute is present
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
