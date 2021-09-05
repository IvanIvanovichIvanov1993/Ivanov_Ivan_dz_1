def type_logger(func):
    def wrapper(x):
        func(x)
        return f'{x}: {type(x)}'

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(6)

print(a)