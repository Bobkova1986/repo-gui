list_of_cubes = []
list_of_cubes_add = []
sum_cubes = 0

for n in range(1, 1001, 2):
    list_of_cubes.append(n ** 3)

for ind, val in enumerate(list_of_cubes):
    sum_of_digits = 0
    while val > 0:
        sum_of_digits += val % 10
        val //= 10
    if sum_of_digits % 7 ==0:
        sum_cubes += list_of_cubes[ind]

print(sum_cubes)

for m in list_of_cubes:
    list_of_cubes_add.append(m+17)

sum_cubes = 0

for ind, val in enumerate(list_of_cubes_add):
    sum_of_digits = 0
    while val > 0:
        sum_of_digits += val % 10
        val //= 10
    if sum_of_digits % 7 ==0:
        sum_cubes += list_of_cubes_add[ind]
print(sum_cubes)


