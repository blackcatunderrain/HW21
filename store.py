from storage import Storage


class Store(Storage):
    def __init__(self, items: dict, capacity: int = 100):
        super().__init__(items, capacity)

    def add(self, name, quantity):
        if self.get_free_space() < quantity:
            raise Exception
        self._items[name] += quantity

    def remove(self, name, quantity):
        if name not in self._items or self._items[name] < quantity:
            raise Exception
        self._items[name] -= quantity
        if self._items[name] == 0:
            self._items.pop(name)

    def get_free_space(self):
        current_space = 0
        for value in self._items.values():
            current_space += value
        return self._capacity - current_space

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self._items)

