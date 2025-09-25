import uuid
from datetime import datetime

class OrderHistory:
    def __init__(self):
        self.history = []

    def get_all_orders(self):
        return self.history

    def add_order(self, items, amount):
        order_id = str(uuid.uuid4())
        order = {
            "id": order_id,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "items": items,
            "amount": amount
        }
        self.history.append(order)
        self.history = self.history[-50:]  # keep last 50
        return order_id

    def get_order_by_id(self, order_id):
        return next((order for order in self.history if order["id"] == order_id), None)
