from request import Request


class Move:

    def __init__(self, request: Request, stocks: dict):
        self._request = request
        self._from = stocks[self._request.departure]
        self._to = stocks[self._request.destination]

    def go(self):
        self._from.remove(name=self._request.name, quantity=self._request.quantity)
        print(f'Курьер забрал {self._request.quantity} {self._request.name} из {self._request.departure}')

        self._to.add(name=self._request.name, quantity=self._request.quantity)
        print(f'Курьер доставил {self._request.quantity} {self._request.name} в {self._request.destination}')
