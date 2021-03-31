from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def calculation(self):
        pass

    def __add__(self, other):
        return self.calculation + other.calculation


class Coat(Clothes):
    def __init__(self, v):
        super().__init__()
        self.v = v

    @property
    def size(self):
        return self.__v

    @size.setter
    def v(self, v):
        self.__v = v

    @property
    def calculation(self):
        return self.__v / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, h):
        super().__init__()
        self.h = h

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        self.__h = h

    @property
    def calculation(self):
        return 2 * (self.__h / 100) + 0.3


coat = Coat(42)
costume = Costume(170)

print(coat.calculation)
print(costume.calculation)
print(coat.calculation + costume.calculation)