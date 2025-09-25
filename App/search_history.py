class SearchHistory:
    def __init__(self):
        self.history = []

    def add_query(self, query):
        query = query.strip()
        if not query:
            return
        if query in self.history:
            self.history.remove(query)
        self.history.insert(0, query)
        self.history = self.history[:10]  # keep last 10

    def get_recent(self, count):
        return self.history[:count]
