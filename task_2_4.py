employees_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАЙ',
                  'директор аэлита']
names = []
for i in employees_list:
    names.append(i.split()[-1])
for m in names:
    print("Привет,", m.title())
