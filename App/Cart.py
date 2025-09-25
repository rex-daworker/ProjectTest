class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.items[item] = self.items.get(item, 0) + quantity

    def checkout(self):
        order = {"items": dict(self.items)}
        self.items.clear()
        return order
