from json import dump
from itertools import zip_longest


with open("users.csv", "r", encoding="utf-8") as users:
    with open("hobby.csv", "r", encoding="utf-8")as hobby:

        if len(users.readlines()) < len(hobby.readlines()):
            with open('my_list.json', 'w', encoding='utf-8') as f:
                zipped_list = zip_longest(users, hobby, fillvalue=None)
                dictionary = {str(el[0]).strip(): (el[1].strip()) for el in zipped_list}

                dump(dictionary, f, ensure_ascii=False, indent=4)
            print(dictionary)
        else:
            exit(1)