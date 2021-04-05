class ZeroError:
	def __init__(self):
		pass


a = int(input("Введите число а:"))
b = int(input("Введите число b:"))

try:
	res = a / b
except ZeroDivisionError:
	print("На ноль делить нельзя")
except ZeroError as err:
	print(err)
else:
	print(f"Результат - {res}")

ZeroError()