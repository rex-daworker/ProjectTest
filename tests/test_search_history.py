import unittest
from app.search_history import SearchHistory

class TestSearchHistory(unittest.TestCase):
    def setUp(self):
        self.search = SearchHistory()

    def test_empty_search_ignored(self):
        self.search.add_query("   ")
        self.assertEqual(self.search.get_recent(5), [])

    def test_duplicate_moves_to_top(self):
        self.search.add_query("shoes")
        self.search.add_query("hats")
        self.search.add_query("shoes")
        recent = self.search.get_recent(2)
        self.assertEqual(recent[0], "shoes")

    def test_limit_storage(self):
        for i in range(15):
            self.search.add_query(f"q{i}")
        self.assertEqual(len(self.search.get_recent(20)), 10)

if __name__ == '__main__':
    unittest.main()
