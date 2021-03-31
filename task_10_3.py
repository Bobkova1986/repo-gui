class Cell:
    def __init__(self, nums):
        self.nums = nums

    def order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + ' * ' * (self.nums % rows)

    def __str__(self):
        return f'{self.nums}'

    def __add__(self, other):
        print("Сумма клеток:")
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print("Разница клеток:")
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 else "В 1 клетке ячеек меньше чем во 2"

    def __mul__(self, other):
        print("Произведение клеток:")
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print("Деление клеток:")
        return Cell(self.nums // other.nums)


cell_1 = Cell(13)
cell_2 = Cell(9)

print(cell_1.order(5))
print(cell_1.__add__(cell_2))
print(cell_1.__sub__(cell_2))
print(cell_1.__mul__(cell_2))
print(cell_1.__floordiv__(cell_2))