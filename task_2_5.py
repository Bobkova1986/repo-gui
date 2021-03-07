price_list = [57.5, 46.51, 97, 115, 98.25, 12.87, 61, 48.33, 47.01, 12]
price_list_decreasing = []

for i in price_list:
    print(int(i // 1), "руб", f'{int(round(i % 1,2) * 100):02}', "коп.", end=", ")

print(" ",end="\n")

for i in sorted(price_list):
    print(int(i // 1), "руб", f'{int(round(i % 1,2) * 100):02}', "коп.", end=", ")

print(" ", end="\n")

price_list_decreasing.extend(sorted(price_list, reverse=True))

for i in price_list_decreasing:
    print(int(i // 1), "руб", f'{int(round(i % 1,2) * 100):02}', "коп.", end=", ")

print(" ", end="\n")

top_five = price_list_decreasing[:5]
for i in top_five:
    print(int(i // 1), "руб", f'{int(round(i % 1,2) * 100):02}', "коп.", end=", ")