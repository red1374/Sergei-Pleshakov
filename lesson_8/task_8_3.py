from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # args_str = list(map(lambda x: f'{x}: {type(x)}', args))
        # if kwargs:
        #     args_str.extend(list(map(lambda x: f'{x}: {type(x)}', kwargs)))
        args_gen = (f'{x}: {type(x)}' for x in args)
        kwargs_gen = (f'{key, kwargs[key]}: {type(kwargs[key])}' for key in kwargs)

        result = func(*args, **kwargs)
        print(f'{func.__name__}({", ".join(args_gen)}, {", ".join(kwargs_gen)}): {type(result)}')
        return result

    return wrapper


@type_logger
def calc_cube_hard(x, y, z, test=1):
    return x ** 3 + y / z * test


print(calc_cube_hard(2, 5, 1, test=2.5))
print(calc_cube_hard.__name__)
