from functools import wraps


def _logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = [el for el in (*args, *kwargs.values())]
        a = [f'{func.__name__}({el}: {type(el)})' for el in result]
        print(*a, *func(*args, *kwargs), sep=",")

    return wrapper


@_logger
def calc_cube(*x, **y):
    result = [el for el in (*x, *y.values()) if isinstance(el, int) or isinstance(el, float)]
    return [n ** 3 for n in result]


b = calc_cube(5, 8, 8.88)