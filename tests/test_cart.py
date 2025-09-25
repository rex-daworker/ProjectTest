import unittest
from app.cart import Cart

class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()

    def test_add_item(self):
        self.cart.add_item("apple", 2)
        self.assertEqual(self.cart.items["apple"], 2)

    def test_update_quantity(self):
        self.cart.add_item("apple", 2)
        self.cart.add_item("apple", 3)
        self.assertEqual(self.cart.items["apple"], 5)

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("apple", 0)

    def test_checkout_clears_cart(self):
        self.cart.add_item("apple", 2)
        order = self.cart.checkout()
        self.assertEqual(len(self.cart.items), 0)
        self.assertIn("apple", order["items"])

if __name__ == '__main__':
    unittest.main()
