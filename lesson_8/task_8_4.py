from functools import wraps


class DivizionByZeroError(Exception):
    def __init__(self, msg=''):
        self.message = msg
        super().__init__(self.message)


def val_checker(callback):
    def type_logger(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if callback(args[2]):
                raise DivizionByZeroError(f'wrong val: {args[2]}')

            args_str = list(map(lambda x: f'{x}: {type(x)}', args))
            if kwargs:
                args_str.extend(list(map(lambda x: f'{x}: {type(x)}', kwargs)))

            result = func(*args, **kwargs)
            print(f'{func.__name__}({", ".join(args_str)}): {type(result)}')
            return result

        return wrapper
    return type_logger


@val_checker(lambda z: z == 0)
def calc_cube_hard(x, y, z, test=1):
    return x ** 3 + test * y / z


print(calc_cube_hard.__name__)
print(calc_cube_hard(2, 5, 0, test=2.5))
