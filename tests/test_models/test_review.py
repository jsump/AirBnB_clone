import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_attributes(self):
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_string_representaion(self):
        self.review.place_id = "1"
        self.review.user_id = "123"
        self.review.text = "Great"
        expected_string = "Review: Place ID - 1, User ID - 123, Text - Great"
        self.assertEqual(str(self.review), expected_string)


if __name__ == "__main__":
    unittest.main()
