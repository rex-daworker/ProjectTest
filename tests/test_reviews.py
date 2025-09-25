import unittest
from app.reviews import Reviews

class TestReviews(unittest.TestCase):
    def setUp(self):
        self.reviews = Reviews()

    def test_add_valid_review(self):
        self.reviews.add_review("u1", "p1", 5, "Great product")
        avg = self.reviews.get_average_rating("p1")
        self.assertEqual(avg, 5.0)

    def test_invalid_rating(self):
        with self.assertRaises(ValueError):
            self.reviews.add_review("u1", "p1", 6, "Too high")

    def test_edit_review(self):
        self.reviews.add_review("u1", "p1", 4, "Ok")
        self.reviews.edit_review("u1", "p1", 5, "Better")
        avg = self.reviews.get_average_rating("p1")
        self.assertEqual(avg, 5.0)

if __name__ == '__main__':
    unittest.main()
