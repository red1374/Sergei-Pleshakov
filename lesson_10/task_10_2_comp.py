class Clothes:
    def __init__(self, name=''):
        if not name:
            name = self.__class__.__name__

        self.name = name
        self.material = 0
        self._clothes_items = []

    def __str__(self):
        return f'Total material value for "{self.name}" is {round(self.material, 2)}'

    def add_costume(self, height):
        self._clothes_items.append(Costume(height))

    def add_coat(self, size):
        self._clothes_items.append(Coat(size))

    def get_total_material(self):
        self.material = sum((item.material for item in self._clothes_items))
        return self


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        super().__init__()

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, material):
        self.__material = self.size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, height):
        self.height = height
        super().__init__()

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, material):
        self.__material = 2 * self.height + 0.3


# coat1 = Coat(6.5)
# print(coat1.material)

# costume1 = Costume(2)
# print(costume1.material)

clothes1 = Clothes('Set 1')
clothes1.add_coat(9)
clothes1.add_costume(3)
clothes1.add_costume(5)
clothes1.add_coat(7)

print(clothes1.get_total_material())
