class Complex:
    def __init__(self, a=0, b=0):
        self._a = a
        self._b = b

    @property
    def get_a(self):
        return self._a

    @property
    def get_b(self):
        return self._b

    def __add__(self, other):
        return Complex(self._a + other.get_a, self._b + other.get_b)

    def __sub__(self, other):
        return Complex(self._a - other.get_a, self._b - other.get_b)

    def __mul__(self, other):
        a = self._a * other.get_a - self._b * other.get_b
        b = self._a * other.get_b - self._b * other.get_a
        return Complex(a, b)

    def __floordiv__(self, other):
        a = (self._a * other.get_a + self._b * other.get_b) / (other.get_a**2 + other.get_b**2)
        b = (self._a * other.get_b + self._b * other.get_a) / (other.get_a**2 + other.get_b**2)
        return Complex(a, b)

    def __truediv__(self, other):
        return self.__floordiv__(other)

    def __str__(self):
        if not self._b:
            return f'{self._a}'
        else:
            return f'{self._a}+i({self._b})'


complex1 = Complex(5, -2)
complex2 = Complex(2, 5)
complex3 = Complex(2, 0)

print(complex1, '+', complex2, '=', complex1 + complex2)
print(complex2, '-', complex1, '=', complex2 - complex1)
print(complex3, '+', complex1, '=', complex3 - complex1)

print(complex3, '*', complex1, '=', complex3 * complex1)
print(complex2, '*', complex1, '=', complex2 * complex1)

print(complex1, '/', complex2, '=', complex2 / complex1)
print(complex3, '/', complex2, '=', complex3 / complex2)
