#!/usr/bin/python3
""""""


import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def test_review_attributes(self):
        review = Review()

        # Check if Review instance is created successfully
        self.assertIsInstance(review, Review)

        # Check if Review inherits from BaseModel
        self.assertIsInstance(review, BaseModel)

        # Check if attributes are present and initialized correctly
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
