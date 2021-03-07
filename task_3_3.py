name_list = []
letters = []
sorted_names = {}


def thesaurus():
    name_list.extend(filter(str.isalpha, sorted(user_names.title().split(" "))))
    for i in name_list:
        if i[:1] in letters:
            continue
        else:
            letters.append(i[:1])

    for n in letters:
        sorted_names[n] = list(filter(lambda x: x.startswith(n), name_list))

    print(sorted_names)

user_names = str(input("Введите имена для сортировки"))
thesaurus()
