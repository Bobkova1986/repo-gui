class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Машина: {self.name} цвет: {self.color} скорость: {self.speed} полицейская: {self.is_police}')

    def starting(self):
        print(f'Машина {self.name} заведена')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {"налево" if direction == 0 else "направо"}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed}')


class TownCar(Car):
    def show_speed(self):
        return f'{self.name} скорость: {self.speed}. ПРЕВЫШЕНИЕ!' \
            if self.speed > 40 else f'{self.name} скорость: {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        return f'{self.name} скорость: {self.speed}. ПРЕВЫШЕНИЕ!' \
            if self.speed > 60 else f"{self.name} скорость: {self.speed}"


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


town_car = TownCar("volvo", "красный", 80)
town_car.starting()
town_car.turn(2)
print(town_car.show_speed())
town_car.stop()

print()

sport_car = SportCar("Ferrari", "золотой", 320)
sport_car.starting()
sport_car.turn(8)
print(sport_car.show_speed())
sport_car.stop()

print()

work_car = WorkCar("Газель", "серый", 30)
work_car.starting()
work_car.turn(0)
print(work_car.show_speed())
work_car.stop()

print()

police_car = PoliceCar("Smart", "Красный", 80)
police_car.starting()
police_car.turn(1)
print(police_car.show_speed())
police_car.stop()

print()