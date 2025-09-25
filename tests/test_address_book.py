import unittest
from app.address_book import AddressBook

class TestAddressBook(unittest.TestCase):
    def setUp(self):
        self.addresses = AddressBook()

    def test_add_address(self):
        self.addresses.add_address("Home", "123 St", "City", "12345", "Country", "123456789")
        self.assertEqual(len(self.addresses.get_all_addresses()), 1)

    def test_limit_five_addresses(self):
        for i in range(6):
            self.addresses.add_address(f"Label{i}", "Addr", "City", "12345", "Country", "123456789")
        self.assertEqual(len(self.addresses.get_all_addresses()), 5)

    def test_delete_default_assigns_new(self):
        self.addresses.add_address("Home", "123 St", "City", "12345", "Country", "123456789", default=True)
        self.addresses.add_address("Work", "456 St", "City", "54321", "Country", "987654321")
        self.addresses.delete_address("Home")
        default = self.addresses.get_default_address()
        self.assertEqual(default["label"], "Work")

if __name__ == '__main__':
    unittest.main()
