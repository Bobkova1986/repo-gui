from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Евгения'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def join(tutors, klasses):
    return (tuple(x) for x in zip_longest(tutors, klasses))


print(*join(tutors,klasses))
print(type(join(tutors, klasses)))