def val_checker(lambda_function):
    def _val_checker(func):
        def wrapper(i):
            if lambda_function(i):
                print(func(i))
            else:
                raise ValueError(f'wrong val {i}')

        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x**3


try:
    a = calc_cube(5)
except ValueError as err:
    print(err)