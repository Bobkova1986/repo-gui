class Road:
    def __init__(self, length, width):
        self._length = 20
        self._width = 5000


class AsphaltAmount(Road):
    def __init__(self, _length, _width, mass, depth):
        self.mass = 25
        self.depth = depth
        super().__init__(_length, _width)


a = AsphaltAmount(20, 5000, 25, 5)
print(a._length * a._width * a.mass * a.depth)