# Определите класс car с двумя атрибутами: color и speed.
# Затем создайте экземпляр и верните speed

"""
class Car:
    color = 'red'
    speed = 20

car_ex = Car()
print(car_ex.speed)
"""


class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def __str__(self):
        return self.color

    def run(self):
        print('RUUUN!')


car_ex = Car('Blue', speed=25)
print(car_ex.speed)

print(car_ex.__dir__())


class Mycar(Car):
    pass


mcar = Mycar('red', 200)
mcar.run()
