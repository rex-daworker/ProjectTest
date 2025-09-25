class AddressBook:
    def __init__(self):
        self.addresses = []

    def add_address(self, label, address_line, city, postal_code, country, tel_number, default=False):
        if default:
            for addr in self.addresses:
                addr["default"] = False
        if len(self.addresses) >= 5:
            self.addresses.pop(0)
        self.addresses.append({
            "label": label,
            "address_line": address_line,
            "city": city,
            "postal_code": postal_code,
            "country": country,
            "tel_number": tel_number,
            "default": default
        })

    def get_all_addresses(self):
        return list(self.addresses)

    def delete_address(self, label):
        removed_default = False
        self.addresses = [
            addr for addr in self.addresses
            if not (addr["label"] == label and (removed_default := addr["default"]))
        ]
        if removed_default and self.addresses:
            self.addresses[0]["default"] = True

    def get_default_address(self):
        return next((addr for addr in self.addresses if addr.get("default")), None)
