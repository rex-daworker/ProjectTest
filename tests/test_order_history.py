import unittest
from app.order_history import OrderHistory

class TestOrderHistory(unittest.TestCase):
    def setUp(self):
        self.history = OrderHistory()

    def test_empty_history(self):
        self.assertEqual(self.history.get_all_orders(), [])

    def test_add_order_and_retrieve(self):
        order_id = self.history.add_order(["item1", "item2"], 25.5)
        self.assertEqual(len(self.history.get_all_orders()), 1)
        self.assertIsNotNone(self.history.get_order_by_id(order_id))

    def test_history_limit(self):
        for i in range(60):
            self.history.add_order([f"item{i}"], i)
        self.assertEqual(len(self.history.get_all_orders()), 50)

if __name__ == '__main__':
    unittest.main()
