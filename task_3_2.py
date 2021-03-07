my_dict = dict(zero='ноль', one='один', two='два', three='три', four='четыре', five='пять', six='шесть', seven='семь',
               eight='восемь', nine='девять', ten='десять')
def num_translate_adv():
    if user_word.istitle() == True:
        print(my_dict.get(user_word.lower()).capitalize())
    elif user_word.isupper() == True:
        print(my_dict.get(user_word.lower()).upper())
    else:
        print(my_dict.get(user_word.lower()))


user_word = str(input("Могу перевести числа от 0 до 10 с английского на русский. Какое число перевести?"))
num_translate_adv()