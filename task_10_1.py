class Matrix:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.a)):
            for j in range(len(self.a[0])):
                sum = other.a[i][j] + self.a[i][j]
                numbers.append(sum)
                if len(numbers) == len(self.a):
                    result.append(numbers)
                    numbers = []
        for i in range(len(result)):
            print(*result[i])


a = [[13, 28, 73], [40, 56, 61], [78, 8, 0]]
b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

matrix_1 = Matrix(a)
matrix_2 = Matrix(b)

print(matrix_1.__add__(matrix_2))