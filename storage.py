from abc import abstractmethod, ABC


class Storage(ABC):
    def __init__(self, items: dict, capacity: int):
        self._items = items
        self._capacity = capacity

    @abstractmethod
    def add(self, name, quantity):
        pass

    @abstractmethod
    def remove(self, name, quantity):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass
