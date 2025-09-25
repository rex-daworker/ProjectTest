import unittest
from app.cart import Cart
from app.order_history import OrderHistory
from app.address_book import AddressBook
from app.search_history import SearchHistory
from app.reviews import Reviews

class TestIntegration(unittest.TestCase):

    def test_checkout_adds_to_order_history(self):
        cart = Cart()
        history = OrderHistory()

        cart.add_item("apple", 2)
        order = cart.checkout()
        order_id = history.add_order(order["items"], 5.0)

        self.assertIsNotNone(history.get_order_by_id(order_id))
        self.assertEqual(len(history.get_all_orders()), 1)

    def test_address_book_default_switch(self):
        addresses = AddressBook()
        addresses.add_address("Home", "123 St", "City", "11111", "Country", "123456789", default=True)
        addresses.add_address("Work", "456 St", "City", "22222", "Country", "987654321")

        addresses.delete_address("Home")
        default = addresses.get_default_address()
        self.assertEqual(default["label"], "Work")

    def test_reviews_and_ratings(self):
        reviews = Reviews()
        reviews.add_review("user1", "product1", 5, "Great!")
        reviews.add_review("user2", "product1", 4, "Good")
        avg = reviews.get_average_rating("product1")
        self.assertEqual(avg, 4.5)

    def test_search_history_and_limit(self):
        search = SearchHistory()
        for i in range(12):
            search.add_query(f"query{i}")
        recent = search.get_recent(10)
        self.assertEqual(len(recent), 10)

if __name__ == '__main__':
    unittest.main()
