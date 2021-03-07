my_dict = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}
def num_translate():
    user_word = str(input("Могу перевести числа от 0 до 10 с английского на русский. Какое число перевести?"))
    print(my_dict.get(user_word.lower()))


num_translate()