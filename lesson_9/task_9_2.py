class Road:
    def __init__(self, length_attr, width_attr):
        self._width = width_attr
        self._length = length_attr

    def calculate_asphalt_mass(self, mass_for_meter, thickness):
        return self._width * self._length * mass_for_meter * thickness

    def show__asphalt_mass(self, mass_for_meter, thickness):
        calc_mass = self.calculate_asphalt_mass(mass_for_meter, thickness)
        print(f'{calc_mass / 1000}т')


r = Road(20, 5000)
r.show__asphalt_mass(25, 5)
