percent_to_generate = 20
user_percent = int(input("ВВЕДИТЕ ЧИСЛО ОТ 1 до 20"))
while user_percent > percent_to_generate or user_percent < 1:
    print("ВАШЕ ЧИСЛО ВНЕ ДИАПЗОНА ОТ 1 ДО ", percent_to_generate)
    user_percent = int(input("ВВЕДИТЕ ЧИСЛО ОТ 1 до 20"))
else:
    if user_percent % 10 == 1 and user_percent % 100 != 11:
        print("Вы ввели ",user_percent, " процент")
    elif 1 < user_percent % 10 < 5 and not 11 < user_percent % 100 < 15:
        print("Вы ввели ",user_percent, " процента")
    else:
        print("Вы ввели ", user_percent, " процентов")
print("Список для проверки: ")
for percent in range(percent_to_generate + 1):
    if percent % 10 == 1 and percent % 100 != 11:
        print(percent, " процент")
    elif 1 < percent % 10 < 5 and not 11 < percent % 100 < 15:
        print(percent, " процента")
    else:
        print(percent, " процентов")