class Reviews:
    def __init__(self):
        self.reviews = {}

    def add_review(self, user_id, product_id, rating, comment=""):
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        self.reviews.setdefault(product_id, {})[user_id] = {
            "rating": rating,
            "comment": comment
        }

    def edit_review(self, user_id, product_id, rating, comment=""):
        self.add_review(user_id, product_id, rating, comment)

    def get_average_rating(self, product_id):
        product_reviews = self.reviews.get(product_id, {})
        if not product_reviews:
            return 0.0
        ratings = [review["rating"] for review in product_reviews.values()]
        return round(sum(ratings) / len(ratings), 1)
