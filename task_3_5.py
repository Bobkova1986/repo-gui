from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, repeat=True):
    """
    n: количество формируемых шуток, задается пользователем
    repeat: уникальность шуток
    """
    jokes = []
    while n and len(nouns):
        num = randrange(len(adjectives))
        if repeat:
            jokes.append(f"{nouns.pop(num)} {adverbs.pop(num)} {adjectives.pop(num)}")
        else:
            jokes.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        n -= 1
    return jokes


n = int(input("Сколько шуток сформировать?"))
print(get_jokes(n))