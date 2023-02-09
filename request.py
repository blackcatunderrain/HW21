class Request:

    def __init__(self, request: str, storages: dict):
        data = request.lower().split(' ')

        self.quantity = int(data[1])
        self.name = data[2]
        self.departure = data[4]
        self.destination = data[6]
