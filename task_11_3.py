class OwnError(Exception):
	def __init__(self, txt):
		self.txt = txt


my_list = []
inp_data = input("Введите число(для выхода наберите stop):")

while True:
	try:
		inp_data = int(inp_data)
	except ValueError:
		if inp_data.lower() == "stop":
			print(my_list)
			break
		if inp_data.lower() != "stop":
			inp_data = input("Вы ввели не число. Введите число (для выхода наберите stop): ")
	except OwnError as err:
		print(err)
	else:
		my_list.append(inp_data)
		inp_data = input("Введите число (для выхода наберите stop):")


OwnError("ошибка")