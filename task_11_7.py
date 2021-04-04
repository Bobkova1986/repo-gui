class ComplexNumber:
	def __init__(self, cplx_nums):
		self.cplx_nums = cplx_nums

	def __add__(self, other):
		print("Сумма комплексных чисел:")
		return complex(self.cplx_nums) + complex(other.cplx_nums)

	def __mul__(self, other):
		print("Произведение комплексных чисел:")
		return complex(self.cplx_nums) * complex(other.cplx_nums)


a = ComplexNumber(-5 + 3j)
b = ComplexNumber(-4 + 4j)

print(a.__add__(b))
print(a.__mul__(b))
