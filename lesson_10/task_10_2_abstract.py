from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name=''):
        if not name:
            name = self.__class__.__name__

        self.name = name
        self._material = 0

    @abstractmethod
    def calculate_material(self):
        pass

    @staticmethod
    def calculate_clothes_material(*args):
        if not args:
            return None

        return round(sum(item.material for item in args), 2)


class Coat(Clothes):
    def __init__(self, name):
        self.size = 0
        super(Coat, self).__init__(name)

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, size):
        self.size = size
        self._material = self.calculate_material(size)

    def calculate_material(self, size):
        return size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, name):
        self.height = 0
        super(Coat, self).__init__(name)

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, height):
        self.height = height
        self._material = self.calculate_material(height)

    def calculate_material(self, height):
        return 2 * height + 0.3


coat1 = Coat('Coat 1')
print(coat1.material)
coat1.material = 20
print(coat1.material)

costume1 = Coat('Costume 1')
print(costume1.material)
costume1.material = 10
print(costume1.material)

print(Clothes.calculate_clothes_material(coat1, costume1))
