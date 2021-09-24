class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self):
        mass = self._length * self._width * 25 * 5 / 1000
        return f'Масса асфальта составляет {mass} тонн (-ы)'


road = Road(2, 5)
print(road.calc_mass())