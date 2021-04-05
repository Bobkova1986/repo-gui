from datetime import date, datetime, timedelta, time
import time


class Data:
	def __init__(self, date_str):
		self.date_str = date_str

	@classmethod
	def date_to_numbers(cls, date_str):
		return cls(date_str=[int(i) for i in date_str.split('-')])

	@staticmethod
	def valid_date(date_str):
		try:
			correct_date = datetime.strptime(date_str, "%d-%m-%Y")
		except ValueError:
			print("Дата введена некорректно")
		else:
			print("Дата введена корректно")


d = input("Введите дату в формате dd-mm-yyyy:")
my_date = Data.date_to_numbers(d)
print(*my_date.date_str)
print(type(my_date.date_str[0]))
Data.valid_date(d)

