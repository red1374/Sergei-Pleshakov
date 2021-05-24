class Car:
    def __init__(self, speed, color, is_police, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Car starts moving')

    def stop(self):
        print('Car stops')

    def turn(self, direction):
        print(f'Car turns to the {direction}')

    def show_speed(self):
        print(f'{self.speed} km/h')

    def is_police_car(self):
        if self.is_police:
            print('This is a police car!')
        else:
            print('This is not a police car!')


class TownCar(Car):
    speed_limit = 60

    def show_speed(self):
        if self.speed > TownCar.speed_limit:
            print(f'Attention! Exceeding the speed limit by {self.speed - TownCar.speed_limit} km/h')
        else:
            print(self.speed)


class SportCar(Car):
    speed_limit = 150

    def show_speed(self):
        if self.speed < SportCar.speed_limit:
            print(f'Attention! This is too slow for a Sport car! The minimal speed is {SportCar.speed_limit} km/h')
        else:
            print(self.speed)


class WorkCar(Car):
    speed_limit = 40

    def show_speed(self):
        if self.speed > WorkCar.speed_limit:
            print(f'Attention! Exceeding the speed limit by {self.speed - WorkCar.speed_limit} km/h')
        else:
            print(self.speed)


class PoliceCar(Car):
    pass


print('-- Car 1 ---------------------------')
car1 = Car(50, 'green', False, 'Mazda RX6')
print(car1.name, car1.speed)
car1.go()
car1.turn('Right')
car1.stop()
car1.show_speed()

print('-- Car 2 ---------------------------')
car2 = TownCar(85, 'blue', False, 'Skoda Fabia II')
print(car2.name, car2.speed)
car2.go()
car2.turn('Right')
car2.stop()
car2.go()
car2.is_police_car()
car2.show_speed()

print('-- Car 3 ---------------------------')
car3 = WorkCar(80, 'red', False, 'Ferrari X1')
print(car3.name, car3.speed)
car3.go()
car3.turn('Right')
car3.stop()
car3.show_speed()
print(car2.name, car3.name)

print('-- Car 4 ---------------------------')
car4 = PoliceCar(120, 'special', True, 'Skoda Octavia')
print(car4.name, car4.speed)
car4.go()
car4.turn('Left')
car4.stop()
car4.is_police_car()
car4.show_speed()

print('-- Car 5 ---------------------------')
car5 = SportCar(320, 'white', False, 'McLaren S40')
print(car5.name, car5.speed)
car5.go()
car5.turn('Left')
car5.stop()
car5.is_police_car()
car5.show_speed()

print(car1.speed, car2.speed, car3.speed, car4.speed, car5.speed)
