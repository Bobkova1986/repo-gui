duration = int(input("ВВЕДИТЕ ЧИСЛО"))
d = duration // 86400
h = duration % 86400 // 3600
m = duration // 60 % 60
s = duration % 60

print(d, " дн.", h, " час.", m, " мин.", s, "сек.")
