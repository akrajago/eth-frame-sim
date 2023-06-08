class Mac:
    def __init__(self):
        self.available = {format(i, "04x").upper() for i in range(65536)}
        self.known = {}

    def create_mac(self, name):
        address = self.available.pop()
        self.known[name] = address
        return address

    def get_mac(self, name):
        return self.known[name]
