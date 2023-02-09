class Request:
    quantity = 3
    name = "печеньки"

    def __init__(self, request: str, stocks: dict):
        data = request.lower().split(' ')

        self.quantity = int(data[2])
        self.name = data[3]
        self.departure = data[5]
        self.destination = data[7]
