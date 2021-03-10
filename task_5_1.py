def odd_nums(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


for i in odd_nums(15):
    print(i)

print(type(odd_nums(15)))